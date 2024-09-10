#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.even import EVEN_INSTRUCTION, get_num_and_even_ans


def main():
    start_game(EVEN_INSTRUCTION, get_num_and_even_ans)


if __name__ == "__main__":
    main()
