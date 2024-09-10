import random


PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'
MAX_NUMBER = 20

def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_num_and_prime_ans():
    num = random.randint(1, MAX_NUMBER)
    answer = 'yes' if is_prime(num) else 'no'
    return str(num), answer

