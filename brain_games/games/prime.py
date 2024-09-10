import random


PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'
MIN_NUMBER = random.randint(1, 20)
MAX_NUMBER = random.randint(1, 20)

def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_num_and_prime_ans():
    num = get_random_num(1, 20)
    answer = 'yes' if is_prime(num) else 'no'
    return str(num), answer

