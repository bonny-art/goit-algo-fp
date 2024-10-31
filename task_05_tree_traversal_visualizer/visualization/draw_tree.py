"""
Цей модуль реалізує візуалізацію бінарного дерева за допомогою бібліотек NetworkX та Matplotlib.
Він включає функції для побудови графа з бінарного дерева, генерування кольорів для вузлів,
та збереження зображення дерева в файл.
"""

import os
import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, current_node, pos, x=0, y=0, layer=1):
    """
    Додає ребра до графа для візуалізації бінарного дерева.

    :param graph: граф, до якого додаються вузли та ребра.
    :param current_node: поточний вузол дерева.
    :param pos: словник, що зберігає позиції вузлів.
    :param x: координата x поточного вузла.
    :param y: координата y поточного вузла.
    :param layer: поточний рівень дерева.
    """
    if current_node is not None:
        # Додаємо вузол до графа
        graph.add_node(current_node.id, color=current_node.color, label=current_node.val)

        # Додаємо ліве піддерево
        if current_node.left:
            graph.add_edge(current_node.id, current_node.left.id)
            l = x - 1 / 2 ** layer
            pos[current_node.left.id] = (l, y - 1)
            add_edges(graph, current_node.left, pos, x=l, y=y - 1, layer=layer + 1)

        # Додаємо праве піддерево
        if current_node.right:
            graph.add_edge(current_node.id, current_node.right.id)
            r = x + 1 / 2 ** layer
            pos[current_node.right.id] = (r, y - 1)
            add_edges(graph, current_node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph

def generate_color(index):
    """
    Генерує колір на основі індексу для візуалізації вузлів.

    :param index: індекс вузла в порядку обходу.
    :return: рядок кольору у форматі hex.
    """
    r = min(255, 50 + index * 15)
    g = min(255, 150 - index * 10)
    b = 200
    return f'#{r:02X}{g:02X}{b:02X}'

def draw_tree(tree_root, save_path):
    """
    Візуалізує бінарне дерево та зберігає зображення у файл.

    :param tree_root: корінь дерева.
    :param save_path: шлях до файлу для збереження зображення.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    # Візуалізуємо дерево
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Зберігаємо зображення дерева
    plt.savefig(save_path)
    plt.close()
