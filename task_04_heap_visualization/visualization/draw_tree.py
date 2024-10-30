"""
Модуль для візуалізації бінарного дерева та збереження малюнка в файл.
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає вузли та ребра до графу для побудови візуалізації дерева.

    :param graph: Граф, до якого додаються вузли та ребра.
    :param node: Поточний вузол дерева.
    :param pos: Позиції вузлів для візуалізації.
    :param x: Координата x для поточного вузла.
    :param y: Координата y для поточного вузла.
    :param layer: Рівень глибини в дереві.
    """
    if node is not None:
        # Додавання вузла з його кольором та значенням
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            # Додавання лівого підвузла
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            # Додавання правого підвузла
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph

def draw_tree(tree_root, save_path="task_04_heap_visualization/results/heap.png"):
    """
    Створює візуалізацію дерева та зберігає її у файл за вказаним шляхом.

    :param tree_root: Корінь бінарного дерева для візуалізації.
    :param save_path: Шлях, за яким буде збережено зображення.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Витяг кольорів та значень для візуалізації
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Налаштування розміру зображення та візуалізація графу
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    # Створення папки за необхідності та збереження малюнка
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()
