"""
Модуль для порівняння ймовірностей результатів від кидання двох кубиків,
отриманих методом Монте-Карло, з аналітичними значеннями.
"""

import pandas as pd

def compare_with_analytical(probabilities: dict[int, float], analytical_probabilities: dict[int, float]) -> None:
    """
    Порівнює ймовірності, отримані методом Монте-Карло, з аналітичними ймовірностями.

    Створює та виводить DataFrame зі значеннями ймовірностей для кожної можливої суми
    результатів кидання двох кубиків.

    Параметри:
    probabilities (dict[int, float]): Ймовірності для кожної суми, отримані методом Монте-Карло.
    analytical_probabilities (dict[int, float]): Аналітичні ймовірності для кожної суми.

    Повертає:
    None
    """

    # Створює DataFrame з даними для порівняння
    comparison_df = pd.DataFrame({
        'Сума': probabilities.keys(),
        'Ймовірність (Монте-Карло)': probabilities.values(),
        'Аналітична ймовірність': [analytical_probabilities[k] for k in probabilities.keys()]
    })

    # Виводить порівняльну таблицю ймовірностей
    print(comparison_df)
