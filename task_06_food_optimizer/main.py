"""
Основний модуль для виконання алгоритмів оптимізації вибору страв 
за обмеженим бюджетом та виведення результатів.
"""

from data.menu import menu
from algorithms.greedy import greedy_algorithm
from algorithms.dynamic import dynamic_programming

def main() -> None:
    """
    Основна функція для виконання алгоритмів оптимізації вибору страв
    за обмеженим бюджетом та виведення результатів.
    """

    # Бюджет для вибору страв
    budget = 100

    # Виконання жадібного алгоритму
    greedy_result, greedy_cost, greedy_calories = greedy_algorithm(menu, budget)

    # Виведення результатів жадібного алгоритму
    print("\nЖадібний алгоритм:")
    print("Обрані страви:", ", ".join(greedy_result))
    print("Витрачена сума:", greedy_cost)
    print("Отримані калорії:", greedy_calories)

    # Виконання алгоритму динамічного програмування
    dp_result, dp_cost, dp_calories = dynamic_programming(menu, budget)

    # Виведення результатів алгоритму динамічного програмування
    print("\nДинамічне програмування:")
    print("Обрані страви:", ", ".join(dp_result))
    print("Витрачена сума:", dp_cost)
    print("Отримані калорії:", dp_calories)

if __name__ == "__main__":
    main()
