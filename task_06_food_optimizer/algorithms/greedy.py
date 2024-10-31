"""
Грiді алгоритм для вибору предметів із максимальним співвідношенням калорій до вартості.
Повертає список вибраних предметів, загальну вартість і загальну калорійність в рамках бюджету.
"""

from typing import Dict, Tuple, List

def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    """
    Застосовує гріді алгоритм для вибору предметів з максимальним співвідношенням калорій до вартості.
    
    Аргументи:
        items: Словник предметів, де ключ — назва предмета, значення — словник з ключами 'calories' та 'cost'.
        budget: Загальний бюджет для покупки предметів.

    Повертає:
        Кортеж, що містить список вибраних предметів, загальну вартість і загальну калорійність.
    """
    # Сортуємо предмети за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items: List[str] = []
    total_cost: int = 0
    total_calories: int = 0

    # Додаємо предмети поки загальна вартість не перевищує бюджет
    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_cost, total_calories
