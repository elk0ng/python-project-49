#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def game_gcd():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ")

        try:
            answer = int(answer)
        except ValueError:
            print(f"'{answer}' is not a number ;(.")
            print(f"Let's try again, {user_name}!")
            break

        correct_answer = gcd(num1, num2)
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")


def main():
    game_gcd()


if __name__ == '__main__':
    main()
