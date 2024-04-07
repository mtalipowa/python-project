from brain_games.core import core_games
from brain_games.games import gcd


def main():
    core_games(gcd.rules, gcd.main)


if __name__ == "__main__":
    main
