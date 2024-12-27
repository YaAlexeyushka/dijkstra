from graph.graph import Graph
import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        distances = {vertex: float('inf') for vertex in self.graph.get_vertices()}
        distances[start] = 0

        priority_queue = [(0, start)]  
        previous_vertices = {vertex: None for vertex in self.graph.get_vertices()}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex == end:
                break

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.graph.get_accessible_vertices(current_vertex):
                weight = self.graph.get_weight(current_vertex, neighbor)
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_vertices[current]
        path.reverse()

        if path and path[0] == start:
            return path, distances[end]
        return None, float('inf')
