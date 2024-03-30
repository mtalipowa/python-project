import prompt
from brain_games.cli import welcome_user


def core_games(rules, generate_QA):
    name = welcome_user()
    print(rules)

    i = 0
    while i < 3:
        generated_QA = generate_QA()
        question = generated_QA[0]
        result = generated_QA[1]

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
