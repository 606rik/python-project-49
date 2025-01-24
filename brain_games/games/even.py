import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0


def get_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
