"""
Клас для представлення графа та реалізації алгоритму Дейкстри.
"""

import heapq

class Graph:
    """ 
    Клас, що представляє граф, реалізований як словник сусідства. 
    Може додавати ребра між вершинами та створювати граф з списку ребер.
    """
    def __init__(self):
        """Ініціалізує порожній граф."""
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Додає ребро між вершинами u і v з вказаною вагою."""

        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = weight
        self.graph[v][u] = weight

    @classmethod
    def from_edge_list(cls, edge_list):
        """Створює граф з заданого списку ребер."""

        graph = cls()
        for u, v, weight in edge_list:
            graph.add_edge(u, v, weight)
        return graph

def dijkstra(graph, start_vertex):
    """Обчислює найкоротші шляхи від початкової вершини до всіх інших вершин графа за допомогою алгоритму Дейкстри."""

    # Ініціалізація відстаней до всіх вершин
    shortest_paths = {vertex: float('infinity') for vertex in graph.graph}
    shortest_paths[start_vertex] = 0

    # Пріоритетна черга для обробки вершин
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо, якщо відстань вже не є актуальною
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph.graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths
