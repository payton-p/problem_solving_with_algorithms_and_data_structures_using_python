from chapter07_graphs.vertex import Vertex


class Graph:
    """
    A graph can be represented by G, where G = (V, E). For the graph G, V is a set of vertices and E is a set of edges.
    Each edge is a tuple (v, w) where w, v is an element of V. We can add a third component to the edge tuple to
    represent a weight. A subgraph s is a set of edges e and vertices v such that e is a subset of E and v is a subset
    of V.

    Path
    A path in a graph is a sequence of vertices that are connected by edges.

    Cycle
    A cycle in a directed graph is a path that starts and ends at the same vertex. A graph with no cycles is called an
    acyclic graph. A directed graph with no cycles is called a directed acyclic graph or a DAG.

    There are two wellknown implementations of a graph, the adjacency matrix and the adjacency list. This class
    implements the adjacency list.
    """

    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Add an instance of Vertex to the graph."""

        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        """Find the vertex in the graph with the given key."""

        if key in self.vertex_list:
            return self.vertex_list[key]
        else:
            return None

    def __contains__(self, key):
        """Determine whether collection contains an item."""

        return key in self.vertex_list

    def add_directed_edge(self, from_vertex, to_vertex, weight=0):
        """
        Adds a new, weighted, directed edge to the graph that connects two vertices.

        An edge (also called an “arc”) is another fundamental part of a graph. An edge connects two vertices to show
        that there is a relationship between them. Edges may be one-way or two-way. If the edges in a graph are all
        one-way, we say that the graph is a directed graph, or a digraph.

        Edges may be weighted to show that there is a cost to go from one vertex to another. For example in a graph of
        roads that connect one city to another, the weight on the edge might represent the distance between the two
        cities.

        When two vertices are connected by an edge, we say that they are adjacent.
        """

        if from_vertex not in self.vertex_list:
            self.add_vertex(from_vertex)

        if to_vertex not in self.vertex_list:
            self.add_vertex(to_vertex)

        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], weight)

    def get_vertices(self):
        """List all vertices in the graph."""

        return self.vertex_list.keys()

    def __iter__(self):
        """Make collection iterable."""

        return iter(self.vertex_list.values())
