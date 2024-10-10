from chapter03_basic_data_structures.queue.queue import Queue
from chapter07_graphs.breath_first_search.build_word_ladder_problem_graph import build_word_ladder_problem_graph


def breadth_first_search(start_vertex):
    """
    Breadth first search (BFS) is one of the easiest algorithms for searching a graph. Given a graph G and a starting
    vertex s, a breadth first search proceeds by exploring edges in the graph to find all the vertices in G for which
    there is a path from s. The remarkable thing about a breadth first search is that it finds all the vertices that are
    a distance k from s before it finds any vertices that are a distance k+1. One good way to visualize what the breadth
    first search algorithm does is to imagine that it is building a tree, one level of the tree at a time. A breadth
    first search adds all children of the starting vertex before it begins to discover any of the grandchildren.
    """

    start_vertex.set_distance(0)
    start_vertex.set_predecessor(None)

    vertex_queue = Queue()
    vertex_queue.enqueue(start_vertex)

    while vertex_queue.size() > 0:
        current_vertex = vertex_queue.dequeue()

        # To keep track of its progress, BFS colors each of the vertices white, gray, or black. All the vertices are
        # initialized to white when they are constructed. A white vertex is an undiscovered vertex. When a vertex is
        # initially discovered it is colored gray, and when BFS has completely explored a vertex it is colored black.
        # This means that once a vertex is colored black, it has no white vertices adjacent to it. A gray node, on the
        # other hand, may have some white vertices adjacent to it, indicating that there are still additional vertices
        # to explore.
        for neighbor in current_vertex.get_connections():
            if neighbor.get_color() == "white":
                # The new, previously unexplored vertex is colored gray.
                neighbor.set_color("gray")

                # The distance to neighbor is set to the distance of current vertex's distance + 1.
                neighbor.set_distance(current_vertex.get_distance() + 1)

                # The predecessor of neighbor is set to the current node (current_vertex).
                neighbor.set_predecessor(current_vertex)

                # The neighbor is added to the end of a queue. Adding neighbor to the end of the queue effectively
                # schedules this node for further exploration, but not until all other vertices on the adjacency list
                # of current_vertex have been explored.
                vertex_queue.enqueue(neighbor)

        current_vertex.set_color("black")


def traverse(y):
    """Traverse a breadth first search graph."""

    x = y
    while x.get_predecessor():
        print(x.get_id())

        x = x.get_predecessor()

    print(x.get_id())


def main():
    # Build graph.
    graph = build_word_ladder_problem_graph("word_file2.txt")
    print(graph.get_vertices())

    # Set the vertex to start on.
    start_vertex = graph.get_vertex("FOOL")

    # Call the breadth first search (BFS).
    breadth_first_search(start_vertex)

    # Traverses graph and prints the shortest path.
    traverse(graph.get_vertex('SAGE'))


if __name__ == "__main__":
    main()
