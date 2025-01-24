from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Запуск игры."""
    run_game(even)  # Передаем модуль игры целиком
