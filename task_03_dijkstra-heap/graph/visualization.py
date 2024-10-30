"""
Модуль для візуалізації графів з використанням бібліотек Matplotlib та NetworkX.
Забезпечує функції для малювання графа та візуалізації найкоротшого шляху між вузлами.
"""

import os
import matplotlib.pyplot as plt
import networkx as nx
from graph.utils import find_adjusted_positions


def visualize_graph(graph, output_dir='results', filename='transport_network_graph'):
    """Візуалізація зваженого графа."""

    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes,
        node_color='lightblue', font_size=9, font_weight='bold', edge_color='gray'
    )

    edge_labels = nx.get_edge_attributes(graph, 'distance')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    plt.suptitle("Зважений граф", size=20)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()


def visualize_path_on_weighted_graph(graph, path_nodes, output_dir='results', filename='path_graph'):
    """Візуалізація найкоротшого шляху на зваженому графі."""

    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)
    node_sizes = [300 * graph.degree(node) for node in graph.nodes()]

    nx.draw(
        graph, pos, with_labels=True, node_size=node_sizes,
        node_color='lightblue', font_size=9, font_weight='bold', edge_color='gray'
    )

    path_edges = [(path_nodes[i], path_nodes[i + 1]) for i in range(len(path_nodes) - 1)]

    for edge in path_edges:
        start, end = edge
        start_pos = pos[start]
        end_pos = pos[end]

        small = 0.028
        diff = 0.006

        start_size = graph.degree(start) * diff + small
        end_size = graph.degree(end) * diff + small

        adjusted_start_pos, adjusted_end_pos = find_adjusted_positions(start_pos, end_pos, start_size, end_size)

        arrow = plt.Arrow(
            adjusted_start_pos[0], adjusted_start_pos[1],
            adjusted_end_pos[0] - adjusted_start_pos[0],
            adjusted_end_pos[1] - adjusted_start_pos[1],
            width=0.02, color='red'
        )
        plt.gca().add_patch(arrow)

    edge_labels = nx.get_edge_attributes(graph, 'distance')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    plt.suptitle(f"Найкоротший шлях\nвід вузла {path_nodes[0]} до вузла {path_nodes[-1]}", size=20)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()
