from graph.graph import Graph
from graph.djikstra.djikstra import Dijkstra

g = Graph()
graph_name = "graph.txt"
with open(graph_name) as f:
    i = 0
    for edge in f:
        vertex1, vertex2, weight = edge.split()
        g.add_edge(vertex1, vertex2, int(weight))

dijkstra = Dijkstra(g)

start_vertex = 'a'
final_vertex = 'g'

distance = dijkstra.shortest_path(start_vertex, final_vertex)
print(f"Минимальное расстояние:, {distance}")