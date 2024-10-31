"""
Цей скрипт виконує симуляцію кидків двох кубиків, розраховує ймовірності
отриманих сум, будує графік результатів симуляції у порівнянні з аналітичними ймовірностями,
та порівнює обчислені ймовірності з теоретичними.
"""

from utils.simulate import simulate_dice_rolls
from utils.plot import plot_probabilities
from utils.compare import compare_with_analytical
from utils.probabilities import analytical_probabilities


if __name__ == "__main__":
    num_rolls: int = 100000
    seed: int = 42

    # Результати симуляції ймовірностей
    probabilities: dict[int, float] = simulate_dice_rolls(num_rolls, seed)

    # Побудова графіку порівняння ймовірностей
    plot_probabilities(probabilities, analytical_probabilities)

    # Порівняння з аналітичними ймовірностями
    compare_with_analytical(probabilities, analytical_probabilities)
