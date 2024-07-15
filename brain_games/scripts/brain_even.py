#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if (number % 2 == 0 and answer.lower() == 'yes') or \
           (number % 2 != 0 and answer.lower() == 'no'):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{'yes' if number % 2 == 0 else 'no'}'.")
            print(f"Let's try again, {user_name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
