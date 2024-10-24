# functions go here
import random


def show_history(history_num_max, history_func):
    statement_generator("History", "-")
    history_num = 0
    while history_num < history_num_max:
        print(f'''
{history_func[history_num]} {history_func[history_num + 1]} {history_func[history_num + 2]} = {history_func[history_num + 3]}
you answered {history_func[history_num + 4]} ''')
        history_num += 5


# number checker
def num_check(question, num_check_low, num_check_high):
    valid = False
    while not valid:

        num_error = f"Please enter an integer that is higher than {num_check_low} and less than {num_check_high}. "
        error = "Please enter an integer. "

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than 0
            if num_check_low < response < num_check_high:
                return response

            # outputs error if input is invalid
            else:
                print(num_error)
                print()

        except ValueError:
            print(error)
            print()


# instructions
def instructions():
    statement_generator("Instructions", "**")
    print('''
In this quiz, you will get to answer mathematics questions at three different
difficulties. The questions can be addition, subtraction, multiplication or 
division. 
First, you decide which difficulty you would like to play at, with 
the options of easy (1), medium (2) and hard (3) difficulty. Then, you decide how many 
questions you want to answer. Do this by entering an integer (a full number) 
which is below the maximum of fifty, and is one or more. After this, a 
question will display. Answer the question by entering in an integer (as
there are no decimals in the quiz). 

Enjoy!
    ''')
    return ""


# statement/title generator
def statement_generator(text, decoration):
    # make string with 3 characters
    ends = decoration * 2
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# yes or no question checker/generator
def yes_no(question):
    while True:
        # ask the user if they want to read the instructions.
        answer = input(question).lower()
        if answer == "yes" or answer == "y":
            return "yes"
        elif answer == "no" or answer == "n":
            return "no"
        else:
            print("please enter either yes or no.")


# checks that a correct response was entered for the
def difficulty_check(question):
    while True:
        # ask the user if they want to read the instructions.
        answer = input(question).lower()
        if answer == "easy" or answer == "1" or answer == "ez":
            return 1
        elif answer == "medium" or answer == "2" or answer == "med":
            return 2
        elif answer == "hard" or answer == "3" or answer == "hd":
            return 3
        elif answer == "4":
            return 4
        else:
            print("Please enter a difficulty. ")


# statistics list generator
def get_stats(stats_list):
    stats_list.sort()

    lowest_point = stats_list[0]
    highest_point = stats_list[-1]
    point_average = sum(stats_list) / len(stats_list)
    return [lowest_point, highest_point, point_average]


# questions generator
def questions_for_quiz(difficulty_func):
    # says if it should be a +, -, divide or multiply

    what_operation = random.randint(1, 4)
    # easy mode
    max_num = 0
    min_num = 1
    max_div_num = 0
    if difficulty_func == 1:
        max_num = 12
        max_div_num = 10
    elif difficulty_func == 2:
        max_num = 40
        max_div_num = 20
    elif difficulty_func == 3:
        max_num = 100
        max_div_num = 50
    elif difficulty_func == 4:
        max_num = 9999
        min_num = 50
    first_number_func = random.randint(min_num, max_num)
    second_number_func = random.randint(min_num, max_num)
    # addition
    if what_operation == 1:
        answer_func = first_number_func + second_number_func
        user_answer = num_check(f"What is {first_number_func} + {second_number_func}", low, high)
        # adds question and answer to history
        history.append(first_number_func)
        history.append("+")
        history.append(second_number_func)
        history.append(answer_func)
        history.append(user_answer)

        if user_answer == answer_func:
            print("correct")
            return 1
        else:
            print("incorrect")
            print(f"the correct answer was {answer_func}")
            return 0
    # subtraction
    elif what_operation == 2:
        answer_func = first_number_func - second_number_func
        user_answer = num_check(f"What is {first_number_func} - {second_number_func}", low, high)
        # adds question and answer to history
        history.append(first_number_func)
        history.append("-")
        history.append(second_number_func)
        history.append(answer_func)
        history.append(user_answer)

        if user_answer == answer_func:
            print("correct")
            return 1
        else:
            print("incorrect")
            print(f"the correct answer was {answer_func}")
            return 0
    # multiplication
    elif what_operation == 3:
        answer_func = first_number_func * second_number_func
        user_answer = num_check(f"What is {first_number_func} multiplied by {second_number_func}", low, high)
        # adds question and answer to history
        history.append(first_number_func)
        history.append("*")
        history.append(second_number_func)
        history.append(answer_func)
        history.append(user_answer)

        if user_answer == answer_func:
            print("correct")
            return 1
        else:
            print("incorrect")
            print(f"the correct answer was {answer_func}")
            return 0
    # division
    elif what_operation == 4:
        first_number_func = random.randint(min_num, max_div_num)
        second_number_func = random.randint(min_num, max_div_num)
        first_number_func_div = first_number_func * second_number_func
        answer_func = first_number_func_div / first_number_func
        user_answer = num_check(f"What is {first_number_func_div} divided by {first_number_func}", low, high)
        # adds question and answer to history
        history.append(first_number_func_div)
        history.append("/")
        history.append(first_number_func)
        history.append(answer_func)
        history.append(user_answer)

        if user_answer == answer_func:
            print("correct")
            return 1
        else:
            print("incorrect")
            print(f"the correct answer was {answer_func}")
            return 0

    else:
        print("Something has gone wrong with the program. Please start again. ")
        quit()


# main routine goes here

statement_generator("Welcome to my mathematics test!", "--*--")
while True:
    user_answers_correct = 0
    low = -10000000
    high = 10000000
    history = []
    want_instructions = yes_no("Would you like to read the instructions?")
    if want_instructions == "yes":
        instructions()
    else:
        pass

    # how hard questions are
    difficulty = difficulty_check('''
What difficulty would you like? 
1 is easy, 2 is medium, 3 is hard. ''')

    # how many questions
    question_amount_played = 0
    question_amount = num_check("How many questions would you like to answer? maximum is 50. ", 0, 51)
    # ask questions
    if difficulty == 1:
        while question_amount > question_amount_played:
            user_answers_correct += questions_for_quiz(1)
            question_amount_played += 1
            print(f"you have gotten {user_answers_correct} question(s) right")
        # end loop
        print("All questions have been answered. ")
        print(f"Your final score is {user_answers_correct}/{question_amount}! ")
        want_history = yes_no("Would you like to see your history? ")
        if want_history == "yes":

            show_history(question_amount, history)

            print()
            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
        else:
            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
    if difficulty == 2:
        while question_amount > question_amount_played:
            user_answers_correct += questions_for_quiz(2)
            question_amount_played += 1
            print(f"you have gotten {user_answers_correct} question(s) right")
        # end loop
        print("All questions have been answered. ")
        print(f"Your final score is {user_answers_correct}/{question_amount}! ")
        want_history = yes_no("Would you like to see your history? ")
        if want_history == "yes":

            show_history(question_amount, history)

            print()
            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
        else:
            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
    if difficulty == 3:
        while question_amount > question_amount_played:
            user_answers_correct += questions_for_quiz(3)
            question_amount_played += 1
            print(f"you have gotten {user_answers_correct} question(s) right")
        # end loop
        print("All questions have been answered. ")
        print(f"Your final score is {user_answers_correct}/{question_amount}! ")
        want_history = yes_no("Would you like to see your history? ")
        if want_history == "yes":

            show_history(question_amount, history)

            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
        else:
            print("Thank you very much for playing this quiz! ")
            play_again = input("Press <enter> to play again?")
            if play_again == "":
                continue
            else:
                break
    if difficulty == 4:
        impossible_mode = input("please enter password for secret impossible mode")
        if impossible_mode == "c+k":
            print("Welcome to impossible mode! ")
            while question_amount > question_amount_played:
                user_answers_correct += questions_for_quiz(4)
                question_amount_played += 1
                print(f"you have gotten {user_answers_correct} question(s) right")
            # end loop
            print("All questions have been answered. ")
            print(f"Your final score is {user_answers_correct}/{question_amount}! ")
            want_history = yes_no("Would you like to see your history? ")
            if want_history == "yes":

                show_history(question_amount, history)

                print("Thank you very much for playing this quiz! ")
                play_again = input("Press <enter> to play again?")
                if play_again == "":
                    continue
                else:
                    break
            else:
                print("Thank you very much for playing this quiz! ")
                play_again = input("Press <enter> to play again?")
                if play_again == "":
                    continue
                else:
                    break
        else:
            print("incorrect")
            continue
