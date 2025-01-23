from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Запуск игры."""
    run_game(progression)  # Передаем модуль игры целиком
