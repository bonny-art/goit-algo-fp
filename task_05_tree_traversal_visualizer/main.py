"""
Програма для візуалізації мін-купки (мінімального бінарного купчастого дерева)
і виконання обходів в глибину та в ширину.
"""

from heap.min_heap import MinHeap
from visualization.draw_tree import draw_tree

def main():
    """Головна функція для вставки елементів у мін-купу 
    та візуалізації дерева після обходів."""

    # Створення об'єкта мін-купки
    heap = MinHeap()

    # Вставка елементів у мін-купу
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

    # Побудова дерева з елементів купи
    heap_root = heap.build_tree()

    # Обхід в глибину та візуалізація
    heap.depth_first_search(heap_root)
    draw_tree(heap_root, save_path="task_05_tree_traversal_visualizer/results/heap_dfs.png")

    # Скидання кольору для обходу в ширину
    for node in heap.nodes:
        node.color = "#87CEEB"

    # Обхід в ширину та візуалізація
    heap.breadth_first_search(heap_root)
    draw_tree(heap_root, save_path="task_05_tree_traversal_visualizer/results/heap_bfs.png")

if __name__ == "__main__":
    main()
