from brain_games.engine import run_game
from brain_games.games import calc


def main():
    run_game(calc)  # Передаем весь модуль вместо отдельных параметров

