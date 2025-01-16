from brain_games.engine import run_game
from brain_games.games.progression import generate_round, GAME_DESCRIPTION


def main():
    """Запуск игры."""
    run_game(GAME_DESCRIPTION, generate_round)

