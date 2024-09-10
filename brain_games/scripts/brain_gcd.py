#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.gcd import GCD_INSTRUCTION, get_two_nums_and_gcd


def main():
    start_game(GCD_INSTRUCTION, get_two_nums_and_gcd)


if __name__ == "__main__":
    main()
