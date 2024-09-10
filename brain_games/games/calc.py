import random


CALC_INSTRUCTION = "What is the result of the expression?"
OPERATIONS = ["+", "-", "*"]
MIN_NUMBER = random.randint(1, 20)
MAX_NUMBER = random.randint(1, 20)


def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def get_calc_and_result():
    num1, num2 = MIN_NUMBER, MAX_NUMBER
    rand_operation = random.choice(OPERATIONS)
    math_expression = f'{num1} ' \
                      f'{rand_operation} {num2}'
    result = calculate(num1, rand_operation, num2)
    return math_expression, str(result)

