from chapter06_trees.priority_queue import PriorityQueue
from chapter07_graphs.graph import Graph


def dijkstras_algorithm(graph, start_node):
    """
    The algorithm we are going to use to determine the shortest path is called “Dijkstra’s algorithm.” Dijkstra’s
    algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node to all
    other nodes in the graph. Again this is similar to the results of a breadth first search.

    Dijkstra's algorithm is a simple modification to breadth first search.

    The algorithm iterates once for every vertex in the graph; however, the order that we iterate over the vertices is
    controlled by a priority queue. The value that is used to determine the order of the objects in the priority queue
    is distance.

    Dijkstra’s algorithm only works when the edge weights are all positive.
    """

    # The classic way to implement a priority queue is using a data structure called a binary heap.
    priority_queue = PriorityQueue()
    start_node.set_distance(0)
    priority_queue.build_heap([(vertex.get_distance(), vertex) for vertex in graph])

    distances = {0: 0}

    while not priority_queue.is_empty():
        current_vertex = priority_queue.delete_min()

        for next_vertex in current_vertex.get_connections():
            # This comparison has already occurred and doesn't need to occur again.
            if start_node != next_vertex:
                new_distance = current_vertex.get_distance() + current_vertex.get_weight(next_vertex)

                # We always want to explore the vertex that has the smallest distance.
                if new_distance < next_vertex.get_distance():
                    next_vertex.set_distance(new_distance)
                    next_vertex.set_predecessor(current_vertex)
                    priority_queue.decrease_key(next_vertex, new_distance)

                    distances[next_vertex.get_id()] = new_distance

    return distances


def main():
    # Build graph.
    graph = Graph()
    for i in range(9):
        graph.add_vertex(i)

    print("Vertices:", graph.get_vertices())

    # Add the undirected edges for the acyclic graph.
    graph.add_undirected_edge(0, 1, 4)
    graph.add_undirected_edge(1, 2, 8)
    graph.add_undirected_edge(2, 3, 7)
    graph.add_undirected_edge(3, 4, 9)
    graph.add_undirected_edge(4, 5, 10)
    graph.add_undirected_edge(5, 6, 2)
    graph.add_undirected_edge(6, 7, 1)
    graph.add_undirected_edge(7, 0, 8)
    graph.add_undirected_edge(1, 7, 11)
    graph.add_undirected_edge(7, 8, 7)
    graph.add_undirected_edge(2, 8, 2)
    graph.add_undirected_edge(8, 6, 6)
    graph.add_undirected_edge(2, 5, 4)
    graph.add_undirected_edge(3, 5, 14)

    # Set the default distances. When a vertex is first created distance is set to a very large number. Theoretically,
    # you would set distance to infinity, but in practice we just set it to a number that is larger than any real
    # distance we would have in the problem we are trying to solve.
    for vertex in graph:
        vertex.set_distance(100000000000)

    start_node = graph.get_vertex(0)
    distances = dijkstras_algorithm(graph, start_node)

    print("This gives the shortest distances to all vertices. The key is the vertex and the value is the shortest "
          "distance to get there. So, in this example, the fastest way to get to vertex 3 from the start node, 0, is a"
          "distance of 19.")
    print(distances)


if __name__ == "__main__":
    main()
