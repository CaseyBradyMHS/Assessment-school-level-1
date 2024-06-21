# functions go here
import random


# number checker
def num_check(question, low, high):
    valid = False
    while not valid:

        num_error = f"Please enter a number that is higher than {low} and less than {high}. "
        error = "Please enter a number. "

        try:
            # ask for a number
            response = float(input(question))

            # check number is more than 0
            if low < response < high:
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
Placeholder instructions. 
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
    if difficulty_func == 1:
        first_number_func = random.randint(1, 12)
        second_number_func = random.randint(1, 12)
        if what_operation == 1:
            answer_func = first_number_func + second_number_func
            user_answer = num_check(f"What is {first_number_func} + {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 2:
            answer_func = first_number_func - second_number_func
            user_answer = num_check(f"What is {first_number_func} - {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 3:
            answer_func = first_number_func * second_number_func
            user_answer = num_check(f"What is {first_number_func} multiplied by {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 4:
            second_number_func_div = random.randint(2, 10)
            answer_func = first_number_func / second_number_func_div
            user_answer = num_check(f"What is {first_number_func} divided by {second_number_func_div}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
    # medium mode
    elif difficulty_func == 2:
        first_number_func = random.randint(1, 40)
        second_number_func = random.randint(1, 40)
        if what_operation == 1:
            answer_func = first_number_func + second_number_func
            user_answer = num_check(f"What is {first_number_func} + {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 2:
            answer_func = first_number_func - second_number_func
            user_answer = num_check(f"What is {first_number_func} - {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 3:
            answer_func = first_number_func * second_number_func
            user_answer = num_check(f"What is {first_number_func} multiplied by {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 4:
            second_number_func_div = random.randint(2, 10)
            answer_func = first_number_func / second_number_func_div
            user_answer = num_check(f"What is {first_number_func} divided by {second_number_func_div}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
    # hard mode
    elif difficulty_func == 3:
        first_number_func = random.randint(1, 100)
        second_number_func = random.randint(1, 100)
        if what_operation == 1:
            answer_func = first_number_func + second_number_func
            user_answer = num_check(f"What is {first_number_func} + {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 2:
            answer_func = first_number_func - second_number_func
            user_answer = num_check(f"What is {first_number_func} - {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 3:
            answer_func = first_number_func * second_number_func
            user_answer = num_check(f"What is {first_number_func} multiplied by {second_number_func}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
        elif what_operation == 4:
            second_number_func_div = random.randint(2, 10)
            answer_func = first_number_func / second_number_func_div
            user_answer = num_check(f"What is {first_number_func} divided by {second_number_func_div}", -999999, 999999)
            if user_answer == answer_func:
                print("correct")
                return 1
    else:
        print("Something has gone wrong with the program. Please start again. ")
        quit()


# main routine goes here

statement_generator("Welcome to my mathematics test!", "--*--")
user_answers_correct = 0
want_instructions = yes_no("Would you like to read the instructions?")
if want_instructions == "yes":
    instructions()
else:
    pass
difficulty = num_check('''
What difficulty would you like? 
1 is easy, 2 is medium, 3 is hard. ''', 0, 4)
if difficulty == 1:
    user_answers_correct += questions_for_quiz(1)
    print(f"you have gotten {user_answers_correct} question(s) right")