# functions go here
import random


# loops the questions being asked and displays history.
def questions_history(question_amount_played_func, user_answers_correct_func, difficulty_func):
    while question_amount > question_amount_played_func:
        user_answers_correct_func += questions_for_quiz(difficulty_func)
        question_amount_played_func += 1
        print()
        print(f"You have gotten {user_answers_correct_func} question(s) right ")
        print()

    # this is the end of the loop which asks questions.
    print("All of the questions have been answered! ")
    print()
    print(f"Your final score is {user_answers_correct_func}/{question_amount}! ")
    print()

    # asks if user wants to see history.
    want_history = yes_no("Would you like to see your history? ")
    if want_history == "yes":
        print()

        # prints the history
        for item in history:
            print(item)

    # asks user if they want to play again.
    print()
    print("Thank you very much for playing this quiz! ")
    play_again = input("Press <enter> to play again?")
    if play_again == "":
        return 1
    else:
        return 0


# makes sure that entered numbers are integers.
def num_check(question, num_check_low, num_check_high):
    valid = False
    while not valid:

        num_error = f"Please enter an integer that is higher than {num_check_low} and less than {num_check_high}. "
        error = "Please enter an integer. "

        try:
            # ask for a number.
            response = int(input(question))

            # checks number is more than the minimum and less than the maximum.
            if num_check_low < response < num_check_high:
                return response

            # outputs error if input is invalid
            else:
                print(num_error)
                print()

        except ValueError:
            print(error)
            print()


# displays instructions.
def instructions():
    statement_generator("Instructions", "**")
    print('''
In this quiz, you will get to answer mathematics questions at three different
difficulties. The questions can be addition, subtraction, multiplication or 
division. 
First, you decide which difficulty you would like to play at, with 
the options of easy (1), medium (2), hard (3) and impossible (4) difficulty. Then, you decide how many 
questions you want to answer. Do this by entering an integer (a full number) 
which is below the maximum of fifty, and is one or more. After this, a 
question will display. Answer the question by entering in an integer (as
there are no decimals in the quiz). 

Enjoy!

    ''')
    return ""


# statement/title generator.
def statement_generator(text, decoration):
    # make string with 3 characters
    ends = decoration * 2
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)
    # print statement
    print()
    print(statement)
    print()
    return ""


# yes or no question checker/generator.
def yes_no(question):
    while True:

        # asks the user a yes or no question.
        answer = input(question).lower()
        if answer == "yes" or answer == "y":
            # if they say yes, return yes.
            return "yes"
        elif answer == "no" or answer == "n":
            # if they say no, return no.
            return "no"
        else:
            # Error correction.
            print("Please enter either yes or no.")


# checks that a correct response was entered for the difficulty.
def difficulty_check(question):
    while True:

        # asks the user what difficulty they want.
        answer = input(question).lower()
        # does the user want to play easy mode?
        if answer == "easy" or answer == "e" or answer == "ez":
            return 1

        # does the user want to play medium mode?
        elif answer == "medium" or answer == "m" or answer == "med":
            return 2

        # does the user want to play hard mode?
        elif answer == "hard" or answer == "h" or answer == "hd":
            return 3

        # does the user want to play impossible mode?
        elif answer == "impossible" or answer == "i" or answer == "imp":
            return 4

        # error correction
        else:
            print("Please enter a difficulty. ")


# questions generator. Asks the user a mathematical question for them to answer and adds the question and answer to history.
def questions_for_quiz(difficulty_func):
    # picks a random operator
    what_operation = random.randint(1, 4)

    # defines boundaries for the numbers which are part of the question.
    max_num = 0
    min_num = 1
    max_div_num = 0

    # easy difficulty maximum.
    if difficulty_func == 1:
        max_num = 12
        max_div_num = 10

    # medium difficulty maximum.
    elif difficulty_func == 2:
        max_num = 35
        max_div_num = 18

    # hard difficulty maximum.
    elif difficulty_func == 3:
        max_num = 80
        max_div_num = 45

    # impossible difficulty maximum.
    elif difficulty_func == 4:
        max_num = 9999
        max_div_num = 9999
        min_num = 50

    # gets the random numbers for the questions.
    first_number_func = random.randint(min_num, max_num)
    second_number_func = random.randint(min_num, max_num)

    # division section. Gets a division question by reversing the process of multiplication while including a reduced number for balancing.
    if what_operation == 4:

        # tells history the question is division
        op_string = "/"

        # finds random numbers for division
        first_number_func = random.randint(min_num, max_div_num)
        second_number_func = random.randint(min_num, max_div_num)

        # multiplies the given numbers
        first_number_func_div = first_number_func * second_number_func

        # reverses process for final question
        answer_func = first_number_func_div / first_number_func

        # asks question.
        user_answer = num_check(f"What is {first_number_func_div} divided by {first_number_func} = ", low, high)

        # clarify if the user's answer was correct or not and adds question and answer to history.
        if user_answer == answer_func:
            print("Correct! ")
            history_string = f"{first_number_func_div} {op_string} {first_number_func} = {answer_func}. Your answer was {user_answer}, which was correct! "
            history.append(history_string)
            return 1
        else:
            print("Incorrect... ")
            print(f"The correct answer was {answer_func} ")
            history_string = f"{first_number_func_div} {op_string} {first_number_func} = {answer_func}. Your answer was {user_answer}, which was incorrect... "
            history.append(history_string)
            return 0
    # creates addition, subtraction and multiplication questions.
    else:
        op_string = what_operation
        # addition questions. Gets a pair of random numbers and adds them together before outputting question for user to answer. also remembers the operator.
        if what_operation == 1:

            # finds correct answer
            answer_func = first_number_func + second_number_func

            # asks question
            user_answer = num_check(f"What is {first_number_func} + {second_number_func} = ", low, high)

            # tells history question is addition
            op_string = "+"

        # subtraction questions. Same as addition but uses subtraction.
        elif what_operation == 2:

            # finds correct answer
            answer_func = first_number_func - second_number_func

            # asks question
            user_answer = num_check(f"What is {first_number_func} - {second_number_func} = ", low, high)

            # tells history question is subtraction
            op_string = "-"

        # multiplication questions. Same as addition and subtraction but uses multiplication.
        elif what_operation == 3:

            # finds correct answer
            answer_func = first_number_func * second_number_func

            # asks question
            user_answer = num_check(f"What is {first_number_func} multiplied by {second_number_func} = ", low, high)

            # tells history the question is multiplication
            op_string = "*"

        # error message just in case
        else:

            # error recovery
            print("Something has gone wrong with the program while generating the operator. ")
            answer_func = 0
            user_answer = 0

        # defines if the user's answer is correct or not and adds the question and answer to the history.
        if user_answer == answer_func:
            print("Correct! ")

            # adds question and answer to history
            history_string = f"{first_number_func} {op_string} {second_number_func} = {answer_func}. Your answer was {user_answer}, which was correct! "
            history.append(history_string)
            return 1
        else:
            print("Incorrect... ")
            print(f"The correct answer was {answer_func}")

            # adds question and answer to history
            history_string = f"{first_number_func} {op_string} {second_number_func} = {answer_func}. Your answer was {user_answer}, which was incorrect... "
            history.append(history_string)
            return 0


# main routine goes here.

# Title
statement_generator("Welcome to my mathematics test!", "--*--")

print()
while True:
    # clears amount of users answers being correct and clears history from previous gameplay.
    user_answers_correct = 0
    history = []

    # minimum and maximum number which the user can enter for their answers of questions
    low = -10000000
    high = 10000000

    # asks user if they want to read the instructions.
    want_instructions = yes_no("Would you like to read the instructions?")
    if want_instructions == "yes":
        # prints the instructions.
        instructions()
    else:
        print()

    # asks user how hard they want the questions to be.
    difficulty = difficulty_check('''
What difficulty would you like? 
The options are easy, medium, hard and impossible. ''')
    print()

    # asks the user how many questions they wish to answer.
    question_amount_played = 0
    question_amount = num_check("How many questions would you like to answer? maximum is 50. ", 0, 51)
    print()

    # this asks the questions and displays the history if requested.
    start_again = questions_history(question_amount_played, user_answers_correct, difficulty)

    # asks the user if they want to play again.
    if start_again == 1:
        print()
        continue
    else:
        print("Goodbye!")
        break
