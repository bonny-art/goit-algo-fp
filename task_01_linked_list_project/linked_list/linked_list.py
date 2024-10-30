"""
Модуль містить клас LinkedList для реалізації однозв'язного списку з можливістю додавання, реверсування,
сортування методом вставок та відображення елементів списку.
"""

from .node import Node

class LinkedList:
    """Клас для представлення однозв'язного списку, що підтримує операції додавання, реверсування, 
    сортування методом вставок та виведення елементів списку.
    """

    def __init__(self) -> None:
        self.head: Node | None = None

    def add(self, data: int) -> None:
        """Додає елемент в кінець списку."""
        new_node = Node(data)

        # Якщо список порожній, додає елемент як голову
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self) -> None:
        """Реверсує однозв'язний список."""
        prev = None
        current = self.head

        # Перестановка зв'язків для кожного елемента
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self) -> None:
        """Сортування однозв'язного списку методом вставок."""
        sorted_list = LinkedList()
        current = self.head

        # Вставка кожного елемента у відсортований список
        while current:
            next_node = current.next
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    def sorted_insert(self, new_node: Node) -> None:
        """Допоміжна функція для вставки вузла в відсортований список."""

        # Вставка нового вузла на початок або в середину списку
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self) -> None:
        """Виводить елементи однозв'язного списку."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
