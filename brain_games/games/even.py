import random


EVEN_INSTRUCTION = 'Answer "yes" if the number is even, ' \
                   'otherwise answer "no".'
MIN_NUMBER = random.randint(1, 20)
MAX_NUMBER = random.randint(1, 20)


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans():
    num = MIN_NUMBER
    answer = 'yes' if is_even(num) else 'no'
    return num, answer

