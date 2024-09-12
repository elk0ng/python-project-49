import random


EVEN_INSTRUCTION = 'Answer "yes" if the number is even, ' \
                   'otherwise answer "no".'
MAX_NUMBER = 20


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans():
    num = random.randint(1, MAX_NUMBER)
    answer = 'yes' if is_even(num) else 'no'
    return num, answer
