import random

def generate_progression(start, step, lenght):
    return [start + step * i for i in range(lenght)]

def generate_round():
    """Генерирует данные для одного раунда игры."""
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer

GAME_DESCRIPTION = "What number is missing in the progression?"
