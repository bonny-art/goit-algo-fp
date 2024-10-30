"""
Алгоритм сортування злиттям для однозв'язного списку.
Цей модуль реалізує сортування злиттям (merge sort) для однозв'язного списку,
використовуючи допоміжні функції для розбиття списку на частини та об'єднання відсортованих частин.
"""

from .node import Node

def merge_sort_linked_list(head: Node) -> Node:
    """
    Рекурсивна функція сортування злиттям для однозв'язного списку.

    Параметри:
    - head: Node - початок (головний вузол) списку для сортування.

    Повертає:
    - Node - початок відсортованого списку.
    """
    if head is None or head.next is None:
        return head

    # Отримуємо середину списку
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивно сортуємо кожну частину
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    # Об'єднуємо відсортовані частини
    return merge_sorted_lists(left, right)

def get_middle(head: Node) -> Node:
    """
    Функція для знаходження середини списку за допомогою повільного та швидкого вказівників.

    Параметри:
    - head: Node - початок списку.

    Повертає:
    - Node - середній вузол списку.
    """
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(head1: Node, head2: Node) -> Node:
    """
    Функція для об'єднання двох відсортованих частин списку в один.

    Параметри:
    - head1: Node - початок першого відсортованого списку.
    - head2: Node - початок другого відсортованого списку.

    Повертає:
    - Node - початок об'єднаного відсортованого списку.
    """
    if not head1:
        return head2
    if not head2:
        return head1

    # Порівнюємо дані вузлів для злиття у правильному порядку
    if head1.data <= head2.data:
        result = head1
        result.next = merge_sorted_lists(head1.next, head2)
    else:
        result = head2
        result.next = merge_sorted_lists(head1, head2.next)
    return result
