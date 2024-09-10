#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.calc import CALC_INSTRUCTION, get_calc_and_result


def main():
    start_game(CALC_INSTRUCTION, get_calc_and_result)


if __name__ == "__main__":
    main()
