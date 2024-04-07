from random import randint

rules = 'What number is missing in the progression?'


def main():
    lenth = randint(5, 10)
    first_number = randint(1, 5)
    step = randint(1, 5)
    last_number: int = first_number + step * (lenth)

    list = [*range(first_number, last_number, step)]

    index = randint(0, lenth - 1)
    result = str(list[index])

    list[index] = ".."
    list = [str(i) for i in list]
    question = " ".join(list)
    return [question, result]
