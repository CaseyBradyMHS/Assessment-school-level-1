else:
    opstring = what_operatoration
    if 1,2,3
        answer_func = first_number_func + second_number_func
        user_answer = num_check(f"What is {first_number_func} + {second_number_func}", low, high)
        opstring = "+"
    # adds question and answer to history
    history.append(first_number_func)
    history.append(opstring)
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