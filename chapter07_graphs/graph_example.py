from chapter07_graphs.graph import Graph


def main():
    # Graphs are a more general structure than trees. You can think of a tree as a special kind of graph. There are two
    # wellknown implementations of a graph, the adjacency matrix and the adjacency list.

    # Adjacency Matrix
    # When most of the cells are empty we say that the matrix is “sparse.” A matrix is not a very efficient way to store
    # sparse data.

    # Adjacency List
    # A more space-efficient way to implement a sparsely connected graph is to use an adjacency list. In an adjacency
    # list implementation we keep a master list of all the vertices in the Graph object and then each vertex object in
    # the graph maintains a list of the other vertices that it is connected to. In our implementation of the Vertex
    # class we will use a dictionary rather than a list where the dictionary keys are the vertices, and the values are
    # the weights. The advantage of the adjacency list implementation is that it allows us to compactly represent a
    # sparse graph. The adjacency list also allows us to easily find all the links that are directly connected to a
    # particular vertex.

    graph = Graph()
    for i in range(6):
        graph.add_vertex(i)

    print(graph.get_vertices())

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)
    graph.add_edge(4, 0, 1)
    graph.add_edge(5, 4, 8)
    graph.add_edge(5, 2, 1)

    for v in graph:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))


if __name__ == "__main__":
    main()
