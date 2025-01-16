import random
from brain_games.engine import run_game


# Описание игры
GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    """Вычисляет НОД двух чисел."""
    while b:
        a, b = b, a % b
    return a


def generate_round():
    """Генерирует данные для одного раунда игры."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def main():
    """Запуск игры."""
    run_game(GAME_DESCRIPTION, generate_round)
