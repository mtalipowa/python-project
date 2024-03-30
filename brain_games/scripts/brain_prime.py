from brain_games.core import core_games
from brain_games.games import prime


def main():
    core_games(prime.rules, prime.main)


if __name__ == "__main__":
    main
