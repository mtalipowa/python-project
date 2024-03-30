from random import randint

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def main():
    question = randint(1, 500)
    result = parity_check(question)
    return [question, result]
