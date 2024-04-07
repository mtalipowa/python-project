from math import gcd
from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def main():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    question = f"{first_number} {second_number}"
    result = gcd(first_number, second_number)
    return [question, str(result)]
