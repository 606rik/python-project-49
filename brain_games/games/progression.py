import random

DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def get_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."  # Скрытое число

    question = " ".join(map(str, progression))
    return question, correct_answer
