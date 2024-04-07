from random import randint

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_symply(number: int):
    if number <= 1:
        return False

    if number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False
        result = True
    return result


def main():
    question = randint(1, 100)
    result = 'yes' if is_symply(question) else 'no'
    return [question, result]
