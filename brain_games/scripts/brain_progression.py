#!/usr/bin/env python3
import random
#from brain_games.cli import welcome_user


def create_progression():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    progression = [start + step * i for i in range(length)]
    correct_result = progression[hidden_index]
    progression[hidden_index] = ".."
    return correct_result, progression

def game_prog():
    user_name = str('user')
    correct_answers = 0
    while correct_answers < 3:
        correct_result, progression = create_progression()
        print("What number is missing in the progression?")
        print("Question:", *progression)
        user_answer = int(input("Your answer: "))
        if user_answer == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'. ")
            print(
	        f"Let's try again, {user_name}!")
            break


    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")


def main():
    game_prog()


if __name__ == '__main__':
    main()
