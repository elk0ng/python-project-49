from brain_games.engine import start_game, get_random_num


PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'

def is_prime(num):
    divider = 2
    while num % divider != 0:
        divider += 1
    return divider == num


def get_num_and_prime_ans():
    num = get_random_num(1, 20)
    answer = 'yes' if is_prime(num) else 'no'
    return str(num), answer


def start_game_prime():
    start_game(PRIME_INSTRUCTION, get_num_and_prime_ans)
