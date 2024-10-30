"""
Модуль для реалізації структури даних бінарного дерева з вузлами.
"""

import uuid

class Node:
    """
    Клас Node представляє вузол дерева. Містить значення, колір та унікальний ідентифікатор.
    """

    def __init__(self, key: int, color: str = "skyblue") -> None:
        """
        Ініціалізація вузла з заданим значенням та кольором.

        :param key: Значення, яке буде збережене у вузлі.
        :param color: Колір вузла (за замовчуванням "skyblue").
        """
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла