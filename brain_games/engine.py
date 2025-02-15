import prompt

MAX_ROUNDS = 3


def run_game(game):
    """Управляет процессом игры."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)  # Используем описание из переданного модуля

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.get_question_and_answer()  
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break  # Выход из цикла при неправильном ответе
    else:
        # Если цикл завершился без break, значит все ответы верные
        print(f"Congratulations, {name}!")

