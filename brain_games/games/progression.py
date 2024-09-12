import random

PROGRESSION_INSTRUCTION = "What number is missing in " \
                          "the progression?"
PROGRESSION_LENGTH = 10
START = 20
STEP = 20


def generate_progression(start, step, length, hidden_index=None):
    progression = [start + step * i for i in range(length)]
    if hidden_index is not None:
        progression[hidden_index] = '..'
    return ' '.join(map(str, progression))


def get_progression_and_hidden_num():
    start, step = random.randint(1, START), random.randint(1, STEP)
    progress_length = random.randint(5, PROGRESSION_LENGTH)
    hide_index = random.randint(0, progress_length - 1)
    progression = generate_progression(start, step, progress_length, hide_index)
    hidden_num = start + step * hide_index
    return progression, str(hidden_num)
