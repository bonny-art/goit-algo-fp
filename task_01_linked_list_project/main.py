"""
Ця програма створює два однозв'язні списки, демонструє операції реверсування та сортування
методом вставок для одного з них, а також злиття двох відсортованих списків.
"""

from linked_list.linked_list import LinkedList
from linked_list.algorithms import merge_sorted_lists

def main() -> None:
    """
    Основна функція програми для демонстрації операцій над однозв'язними списками.
    """
    # Створюємо два однозв'язні списки та додаємо елементи
    list1 = LinkedList()
    list2 = LinkedList()

    for data in [1, 3, 5]:
        list1.add(data)

    for data in [2, 4, 6]:
        list2.add(data)

    # Виводимо елементи першого списку
    print("\nСписок 1:")
    list1.display()

    # Виводимо елементи другого списку
    print("\nСписок 2:")
    list2.display()

    # Реверсування списку
    list1.reverse()
    print("\nСписок 1 після реверсування:")
    list1.display()

    # Сортування списку методом вставок
    list1.insertion_sort()
    print("\nСписок 1 після сортування методом вставок:")
    list1.display()

    # Злиття двох відсортованих списків
    merged_head = merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("\nЗлитий відсортований список:")
    merged_list.display()

if __name__ == "__main__":
    main()
