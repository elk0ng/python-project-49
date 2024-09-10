#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.prime import PRIME_INSTRUCTION, get_num_and_prime_ans


def main():
    start_game(PRIME_INSTRUCTION, get_num_and_prime_ans)


if __name__ == "__main__":
    main()
