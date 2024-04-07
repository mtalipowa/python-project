import prompt
from brain_games.cli import welcome_user
from typing import Callable

def core_games(rules: str, generate_QA: Callable):
    name = welcome_user()
    print(rules)

    i = 0
    while i < 3:
        question, result = generate_QA()

        print(f"Question: {question}")
        answ = prompt.string('Your answer: ')

        if result != answ:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{result}'")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
        i += 1

    if i == 3:
        print(f"Congratulations, {name}!")
