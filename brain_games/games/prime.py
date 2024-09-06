from brain_games.engine import start_game, get_random_num


PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_num_and_prime_ans():
    number = get_random_num(1, 20)
    answer = 'yes' if is_prime(number) else 'no'
    return str(num), answer


def start_game_prime():
    start_game(PRIME_INSTRUCTION, get_num_and_prime_ans)
