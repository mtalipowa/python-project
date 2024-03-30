from brain_games.core import core_games
from brain_games.games import even


def main():
    core_games(even.rules, even.main)


if __name__ == "__main__":
    main
