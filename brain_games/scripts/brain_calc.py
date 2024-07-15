#!/usr/bin/env python3
import random
from brain_games.cli import welcome_user


def generate_expression():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)


def game_calc():
    user_name = welcome_user()
    print("What is the result of the expression?")
    correct_answers = 0
    while correct_answers < 3:
        expression, correct_result = generate_expression()
        print(f"Question: {expression}")
        answer = input("Your answer: ")
        if answer == str(correct_result):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'."
            )
            print(f"Let's try again, {user_name}!")  # <- Правильный отступ
            break
    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")


def main():
    game_calc()


if __name__ == '__main__':
    main()
