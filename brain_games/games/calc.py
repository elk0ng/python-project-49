import random
from brain_games.engine import start_game, get_random_num

CALC_INSTRUCTION = "What is the result of the expression?"
OPERATIONS = ["+", "-", "*"]

def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def get_calc_and_result():
    num1, num2 = get_random_num(), get_random_num()
    rand_operation = random.choice(OPERATIONS)
    math_expression = f'{num1} ' \
                      f'{rand_operation} {num2}'
    result = calculate(num1, rand_operation, num2)
    return math_expression, str(result)


def start_game_calc():
    start_game(CALC_INSTRUCTION, get_calc_and_result)
