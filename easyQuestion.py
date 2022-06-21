def easyQuestoin(questionType, question, min=1, max=20):
    """
    - 'yn' for yes/no questoins.
    - 'num' for digit/number questions.
    - 'tf' for true/false questoins.
    - 'min' and 'max' for defining the maximum and mininum for the numbers both included
    """

    i = 0

    while i < 3:

        # Define answer.
        answer = input(question + ": ")

        # Define answers for yes-no questions.
        if questionType == "yn":

            if any(answer.lower() == j for j in ["yes", "yeah", 'ye', "y", "1"]):
                return True
                # break
            elif any(answer.lower() == j for j in ["no", "nah", "n", "0"]):
                return False
                # break
            else:
                i += 1

                if i < 3:
                    print(f'Please enter yes or no. {3-i}/3 try left.\n')
                else:
                    print("0 try left. Program is terminated.\n")

        # Define answers for number questions. Numbers should be between min and max both included.
        if questionType == "num":

            try:
                answer_int = int(answer)
            except ValueError:
                i += 1

                if i < 3:
                    print(f'Please enter a numeric value. {3-i}/3 try left.\n')
                else:
                    print("0 try left. Program is terminated.\n")
                    break
            else:

                if answer_int >= min and answer_int <= max:
                    return answer_int
                else:
                    i += 1

                    if i < 3:
                        print(
                            f'Please enter a numeric value between {min} and {max} values. {3-i}/3 try left.\n')
                    else:
                        print("0 try left. Program is terminated.\n")
                        break

        # Define answers for true-false questions.
        if questionType == "tf":

            if any(answer.lower() == j for j in ["true", "t", "yes", "yeah", 'ye', "y", "1"]):
                return True
                # break
            elif any(answer.lower() == j for j in ["false", "f", "no", "nah", "n", "0"]):
                return False
                # break
            else:
                i += 1

                if i < 3:
                    print(f'Please enter true or false. {3-i}/3 try left.\n')
                else:
                    print("0 try left. Program is terminated.\n")
