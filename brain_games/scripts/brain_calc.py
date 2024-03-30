from brain_games.core import core_games
from brain_games.games import calc


def main():
    core_games(calc.rules, calc.main)


if __name__ == "__main__":
    main
