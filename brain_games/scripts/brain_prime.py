import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    """Генерирует вопрос и правильный ответ для игры."""
    question = random.randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return str(question), correct_answer
