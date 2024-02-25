from random import randint


def main():
    score= 0
    level = get_level()
    for i in range(10):
        number1 = generate_integer(level)
        number2 = generate_integer(level)

        while True:
            user_answer = input(f"{number1} + {number2} = ")
            answer = number1 + number2

            if user_answer.isdigit() and int(user_answer) == answer:
                score += 1
                break
            else:
                for i in range(2):
                    print("EEE")
                    user_answer = input(f"{number1} + {number2} = ")
                    if user_answer.isdigit() and int(user_answer) == answer:
                        score += 1
                        break
                if user_answer.isdigit() and int(user_answer) == answer:
                    break
                else:
                    print(f"{number1} + {number2} = {answer}")
                    break

    print(f"Score: {score}")




def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level
                break



def generate_integer(level):
    level = int(level)
    if level == 1:
        number = randint(0, 9)
        return number
    elif level == 2:
        number = randint(10, 99)
        return number
    else:
        number = randint(100, 999)
        return number




if __name__ == "__main__":
    main()