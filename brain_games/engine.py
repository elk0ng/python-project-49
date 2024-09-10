import prompt
import random


NUM_OF_ROUNDS = 3


def start_game(instruction, get_answer_and_question):
    user_name = prompt.string("Welcome to the Brain Games!\n"
                              "May I have your name? ")
    print(f"Hello, {user_name}!\n"
          f"{instruction}")
    for _ in range(NUM_OF_ROUNDS):
        question, right_ans = get_answer_and_question()
        user_ans = prompt.string(f'Question: {question}\n'
                                 f'Your answer: ')
        if user_ans == right_ans:
            print("Correct!")
        else:
            print(f"'{user_ans}' is wrong answer ;(\n"
                  f"Correct answer was '{right_ans}'\n"
                  f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
