class Vertex:
    """
    A vertex (also called a “node”) is a fundamental part of a graph. It can have a name, which we will call the “key.”
    A vertex may also have additional information. We will call this additional information the “payload.”

    There are two wellknown implementations of a graph, the adjacency matrix and the adjacency list. This class
    implements the adjacency list. This class uses a dictionary rather than a list, where the dictionary keys are the
    vertices, and the values are the weights.
    """

    def __init__(self, key):
        self.id = key
        self.connected_to = {}  # keeps track of the vertices to which it is connected and the weight of each edge

    def add_neighbor(self, neighbor, weight=0):
        """Add a connection from this vertex to another."""

        self.connected_to[neighbor] = weight

    def __str__(self):
        """Define what is returned in print function."""

        return str(self.id) + ' connected_to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        """Get all the vertices in the adjacency list."""

        return self.connected_to.keys()

    def get_id(self):
        """Get the ID of this vertex."""

        return self.id

    def get_weight(self, neighbor):
        """"Get the weight of the edge from this vertex to the vertex passed as a parameter."""

        return self.connected_to[neighbor]
