from brain_games.engine import start_game, get_random_num


GCD_INSTRUCTION = 'Find the greatest common divisor ' \
                  'of given numbers.'


def get_two_nums_and_gcd():
    num1, num2 = get_random_num(), get_random_num()
    nums_pair = f'{num1} {num2}'
    gcd = get_gcd(num1, num2)
    return nums_pair, str(gcd)


def get_gcd(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def start_game_gcd():
    start_game(GCD_INSTRUCTION, get_two_nums_and_gcd)
