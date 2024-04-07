from brain_games.core import core_games
from brain_games.games import progression


def main():
    core_games(progression.rules, progression.main)


if __name__ == "__main__":
    main
