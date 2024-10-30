"""
Модуль для реалізації мінімальної купи (MinHeap) з можливістю вставки елементів 
та побудови бінарного дерева. Використовується клас Node для представлення 
вузлів дерева.
"""

from .node import Node

class MinHeap:
    """
    Клас MinHeap реалізує мінімальну купу з можливістю вставки елементів та побудови бінарного дерева.
    """

    def __init__(self):
        """Ініціалізація порожньої купи."""
        self.nodes = []

    def insert(self, key):
        """
        Вставка елемента у купу та упорядкування за допомогою _heapify_up.
        
        :param key: Значення, яке потрібно вставити у купу.
        """
        new_node = Node(key)
        self.nodes.append(new_node)
        self._heapify_up(new_node)

    def _heapify_up(self, node):
        """
        Упорядкування купи шляхом підняття вузла до батьківських елементів, 
        якщо його значення менше, ніж значення батька.
        
        :param node: Вузол, який потрібно упорядкувати.
        """
        index = self.nodes.index(node)
        while index > 0:
            # Обчислення індексу батька
            parent_index = (index - 1) // 2
            # Перевірка та обмін місцями, якщо значення вузла менше за значення батька
            if self.nodes[index].val < self.nodes[parent_index].val:
                self.nodes[index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[index]
                index = parent_index
            else:
                break

    def build_tree(self):
        """
        Побудова дерева з купи. Створює лівий та правий підвузли для кожного вузла.
        
        :return: Корінь побудованого дерева або None, якщо купа порожня.
        """
        if not self.nodes:
            return None
        for i, node in enumerate(self.nodes):
            if 2 * i + 1 < len(self.nodes):
                node.left = self.nodes[2 * i + 1]
            if 2 * i + 2 < len(self.nodes):
                node.right = self.nodes[2 * i + 2]
        return self.nodes[0]

    def print_tree(self, node, level=0):
        """
        Рекурсивне виведення дерева у термінал з відступами для кожного рівня.
        
        :param node: Поточний вузол для виведення.
        :param level: Рівень вузла в дереві, використовується для відступів.
        """
        if node is not None:
            # Виводимо правого нащадка
            self.print_tree(node.right, level + 1)

            # Виводимо поточний вузол з відступом
            print('    ' * level + f'-> {node.val}')

            # Виводимо лівого нащадка
            self.print_tree(node.left, level + 1)

    def print_heap(self):
        """
        Виведення купи у вигляді масиву значень вузлів.
        """
        heap_values = [node.val for node in self.nodes]
        print("Heap as array:", heap_values)
