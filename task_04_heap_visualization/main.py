"""
Цей модуль виконує ініціалізацію мінімальної купи, вставляє значення, 
будує дерево з купи, виводить його у термінал та візуалізує дерево.
"""

from heap.min_heap import MinHeap
from visualization.draw_tree import draw_tree

# Ініціалізація мінімальної купи
heap = MinHeap()

# Вставка значень у купу
heap.insert(3)
heap.insert(1)
heap.insert(6)
heap.insert(5)
heap.insert(2)
heap.insert(4)
heap.insert(15)
heap.insert(7)
heap.insert(9)
heap.insert(8)
heap.insert(10)
heap.insert(12)
heap.insert(11)
heap.insert(13)
heap.insert(14)

# Побудова дерева з купи
root = heap.build_tree()

# Виведення дерева у термінал
heap.print_tree(root)

# Виведення купи у термінал
heap.print_heap()

# Візуалізація дерева
draw_tree(root)
