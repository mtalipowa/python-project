import random
from random import randint

rules = 'What is the result of the expression?'


def calculation(symbol: str, first_number: int, second_number: int) -> int:
    match symbol:
        case '*': return first_number * second_number
        case '+': return first_number + second_number
        case '-': return first_number - second_number


def main():
    symbols = ("+", "-", "*")
    symbol = random.choice(symbols)
    first_number = randint(1, 15)
    second_number = randint(1, 15)
    question = f"{first_number} {symbol} {second_number}"
    result = calculation(symbol, first_number, second_number)
    return [question, str(result)]
