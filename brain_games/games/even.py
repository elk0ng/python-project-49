from brain_games.engine import start_game, get_random_num


EVEN_INSTRUCTION = 'Answer "yes" if the number is even, ' \
                   'otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans():
    num = get_random_num()
    answer = 'yes' if is_even(num) else 'no'
    return num, answer


def start_game_even():
    start_game(EVEN_INSTRUCTION, get_num_and_even_ans)
