import sys

from chapter06_trees.priority_queue import PriorityQueue
from chapter07_graphs.graph import Graph


def prims_algorithm(graph, start_node):
    """
    Prim's Spanning Tree algorithm.

    Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This
    means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all
    the edges in the tree is minimized.

    Prim's algorithm belongs to a family of algorithms called the “greedy algorithms” because at each step we will
    choose the cheapest next step. In this case the cheapest next step is to follow the edge with the lowest weight.
    """

    # The classic way to implement a priority queue is using a data structure called a binary heap.
    priority_queue = PriorityQueue()

    # Set the default distances. When a vertex is first created distance is set to a very large number. Theoretically,
    # you would set distance to infinity, but in practice we just set it to a number that is larger than any real
    # distance we would have in the problem we are trying to solve.
    for vertex in graph:
        vertex.set_distance(sys.maxsize)
        vertex.set_predecessor(None)

    start_node.set_distance(0)
    priority_queue.build_heap([(vertex.get_distance(), vertex) for vertex in graph])

    distances = {start_node.get_id(): 0}

    while not priority_queue.is_empty():
        current_vertex = priority_queue.delete_min()

        for next_vertex in current_vertex.get_connections():
            new_distance = current_vertex.get_weight(next_vertex)

            # Find an edge that is safe to add to the tree, meaning it is not yet in the tree, and then add it to the
            # tree.
            if next_vertex in priority_queue and new_distance < next_vertex.get_distance():
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

    start_node = graph.get_vertex(0)
    distances = prims_algorithm(graph, start_node)
    print(distances)

    # Get the total weight of the minimum spanning tree.
    total_weight = 0
    for key in distances:
        total_weight += distances[key]

    print("Total weight of the minimum spanning tree:", total_weight)


if __name__ == "__main__":
    main()
