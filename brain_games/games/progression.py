import random

PROGRESSION_INSTRUCTION = "What number is missing in " \
                          "the progression?"
PROGRESSION_LENGTH = 10


def generate_progression(start, step, length, hidden_index=None):
    progression = [start + step * i for i in range(length)]
    if hidden_index is not None:
        progression[hidden_index] = '..'
    return ' '.join(map(str, progression))


def get_progression_and_hidden_num():
    start, step = random.randint(1, 20), random.randint(1, 20)
    progression_length = random.randint(5, 10)
    hidden_index = random.randint(0, progression_length - 1)
    progression = generate_progression(start, step, progression_length, hidden_index)
    hidden_num = start + step * hidden_index
    return progression, str(hidden_num)