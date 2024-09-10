import random

PROGRESSION_INSTRUCTION = "What number is missing in " \
                          "the progression?"
PROGRESSION_LENGTH = 10
MIN_NUMBER = random.randint(1, 50)
MAX_NUMBER = random.randint(50, 100)


def get_progression_and_hidden_num():
    start, step = MIN_NUMBER, MIN_NUMBER
    hidden_index = MAX_NUMBER(0, PROGRESSION_LENGTH - 1)
    progression = generate_progression(start, step, PROGRESSION_LENGTH, hidden_index)
    hidden_num = start + step * hidden_index
    return progression, str(hidden_num)


def generate_progression(start, step, length, hidden_index=None):
    progression = [start + step * i for i in range(length)]
    if hidden_index is not None:
        progression[hidden_index] = '..'
    return ' '.join(map(str, progression))

