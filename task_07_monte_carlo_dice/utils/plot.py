"""
Цей модуль містить функцію для побудови графіку ймовірностей випадання суми при киданні двох кубиків
та порівняння отриманих результатів із аналітичними значеннями ймовірностей.
"""

import os
import matplotlib.pyplot as plt

def plot_probabilities(probabilities: dict, analytical_probabilities: dict) -> None:
    """
    Побудова графіка для порівняння ймовірностей випадання сум двох кубиків методом Монте-Карло
    з аналітичними ймовірностями.

    Parameters:
    probabilities (dict): Ймовірності сум, отримані методом Монте-Карло.
    analytical_probabilities (dict): Теоретичні (аналітичні) ймовірності для сум.
    """
    # Підготовка даних для графіка
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    analytical_probs = list(analytical_probabilities.values())
    x = range(len(sums))

    # Побудова стовпчастих графіків для отриманих та аналітичних ймовірностей
    plt.bar(x, probs, width=0.4, label='Ймовірність (Монте-Карло)', color='skyblue', align='center')
    plt.bar(
        [p + 0.4 for p in x],
        analytical_probs,
        width=0.4,
        label='Аналітична ймовірність',
        color='orange',
        align='center'
    )

    # Налаштування підписів, заголовків та легенди
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(x, sums)
    plt.legend(fontsize=8)
    plt.grid(axis='y')

    # Створення директорії для збереження графіка, якщо її немає
    os.makedirs('task_07_monte_carlo_dice/results', exist_ok=True)

    # Збереження графіка у файл
    plt.savefig('task_07_monte_carlo_dice/results/dice_probabilities.png')
