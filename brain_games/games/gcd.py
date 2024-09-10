import random


GCD_INSTRUCTION = 'Find the greatest common divisor ' \
                  'of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_two_nums_and_gcd():
    num1, num2 = random.randint(MIN_NUMBER, MAX_NUMBER), random.randint(MIN_NUMBER, MAX_NUMBER)
    nums_pair = f'{num1} {num2}'
    gcd = get_gcd(num1, num2)
    return nums_pair, str(gcd)


def get_gcd(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1

