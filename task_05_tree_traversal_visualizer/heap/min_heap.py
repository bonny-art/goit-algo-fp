"""
Модуль для реалізації мін-купки (MinHeap) з можливістю візуалізації дерева та пошуку в глибину і ширину.
"""

import uuid
from visualization.draw_tree import generate_color

class Node:
    """Представляє вузол дерева з відповідними властивостями.

    Атрибути:
    left -- лівий дочірній вузол
    right -- правий дочірній вузол
    val -- значення вузла
    color -- колір вузла (за замовчуванням #87CEEB)
    id -- унікальний ідентифікатор вузла
    """

    def __init__(self, key, color="#87CEEB"):
        """Ініціалізує вузол дерева.

        Аргументи:
        key -- значення вузла
        color -- колір вузла (за замовчуванням #87CEEB)
        """
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

class MinHeap:
    """Представляє мін-купку з операціями вставки, побудови дерева, 
    а також виконання пошуку в глибину і ширину.

    Атрибути:
    nodes -- список вузлів, що складають мін-купку
    """

    def __init__(self):
        """Ініціалізує мін-купку."""
        self.nodes = []

    def insert(self, key):
        """Вставляє новий вузол у мін-купку.

        Аргументи:
        key -- значення, яке потрібно вставити
        """
        new_node = Node(key)
        self.nodes.append(new_node)
        self._heapify_up(new_node)

    def _heapify_up(self, child_node):
        """Виправляє позицію вузла в купці, піднімаючи його вгору.

        Аргументи:
        child_node -- вузол, який потрібно виправити
        """
        index = self.nodes.index(child_node)
        while index > 0:
            parent_index = (index - 1) // 2
            if self.nodes[index].val < self.nodes[parent_index].val:
                self.nodes[index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[index]
                index = parent_index
            else:
                break

    def build_tree(self):
        """Будує дерево з вузлів купки.

        Повертає:
        корінь побудованого дерева або None, якщо купка порожня
        """
        if not self.nodes:
            return None
        for i, current_node in enumerate(self.nodes):
            if 2 * i + 1 < len(self.nodes):
                current_node.left = self.nodes[2 * i + 1]
            if 2 * i + 2 < len(self.nodes):
                current_node.right = self.nodes[2 * i + 2]
        return self.nodes[0]

    def depth_first_search(self, root):
        """Виконує пошук в глибину по дереву.

        Аргументи:
        root -- корінь дерева, з якого починається пошук
        """
        stack = [root]
        visited = set()
        step = 0

        while stack:
            current_node = stack.pop()
            if current_node and current_node.id not in visited:
                visited.add(current_node.id)
                current_node.color = generate_color(step)
                step += 1
                stack.append(current_node.right)
                stack.append(current_node.left)

    def breadth_first_search(self, root):
        """Виконує пошук в ширину по дереву.

        Аргументи:
        root -- корінь дерева, з якого починається пошук
        """
        queue = [root]
        visited = set()
        step = 0

        while queue:
            current_node = queue.pop(0)
            if current_node and current_node.id not in visited:
                visited.add(current_node.id)
                current_node.color = generate_color(step)
                step += 1
                queue.append(current_node.left)
                queue.append(current_node.right)
