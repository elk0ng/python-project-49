#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games.progression import PROGRESSION_INSTRUCTION, get_progression_and_hidden_num


def main():
    start_game(PROGRESSION_INSTRUCTION, get_progression_and_hidden_num)


if __name__ == "__main__":
    main()
