"""
Цей модуль реалізує алгоритм Дейкстри для знаходження найкоротших шляхів
в графі з використанням списку ребер. Граф візуалізується з допомогою
бібліотеки NetworkX.
"""

from graph.graph import Graph, dijkstra
from graph.visualization import visualize_graph, visualize_path_on_weighted_graph
import networkx as nx

if __name__ == "__main__":

    # Список ребер графа з вагами
    edge_list = [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
        ("D", "E", 3)
    ]

    # Створення графа з списку ребер
    graph = Graph.from_edge_list(edge_list)

    START_VERTEX = "A"

    # Знаходження найкоротших шляхів від початкової вершини
    shortest_paths = dijkstra(graph, START_VERTEX)

    # Виведення найкоротших відстаней до всіх вершин
    for vertex, distance in shortest_paths.items():
        print(f"Найкоротша відстань від {START_VERTEX} до {vertex}: {distance}")

    # Створення графа для візуалізації з NetworkX
    nx_graph = nx.Graph()
    for vertex, neighbors in graph.graph.items():
        for neighbor, weight in neighbors.items():
            nx_graph.add_edge(vertex, neighbor, distance=weight)

    # Візуалізація графа
    visualize_graph(nx_graph, output_dir='task_03_dijkstra-heap/results', filename='weighted_graph')

    # Визначення шляхів для візуалізації
    path_nodes = ["A", "B", "C", "D"]

    # Візуалізація знайденого шляху на графі
    visualize_path_on_weighted_graph(
        nx_graph,
        path_nodes,
        output_dir='task_03_dijkstra-heap/results',
        filename='dijkstra_path_graph'
    )
