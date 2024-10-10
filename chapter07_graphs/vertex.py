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

        # Used in breadth first search.
        self.distance = 0
        self.predecessor = None
        self.color = "white"

    def get_id(self):
        """Get the ID of this vertex."""

        return self.id

    def get_distance(self):
        """
        Get the distance of this vertex.

        Used in breadth first search (BFS).
        """

        return self.distance

    def set_distance(self, distance):
        """
        Set the distance of this vertex.

        Used in breadth first search (BFS).
        """

        self.distance = distance

    def get_predecessor(self):
        """
        Get the predecessor of this vertex.

        Used in breadth first search (BFS).
        """

        return self.predecessor

    def set_predecessor(self, predecessor):
        """
        Set the predecessor of this vertex.

        Used in breadth first search (BFS).
        """

        self.predecessor = predecessor

    def get_color(self):
        """
        Get the color of this vertex.

        Used in breadth first search (BFS).
        """

        return self.color

    def set_color(self, color):
        """
        Set the color of this vertex.

        Used in breadth first search (BFS).
        """

        self.color = color

    def add_neighbor(self, neighbor, weight=0):
        """Add a connection from this vertex to another."""

        self.connected_to[neighbor] = weight

    def __str__(self):
        """Define what is returned in print function."""

        return str(self.id) + ' connected_to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        """Get all the vertices in the adjacency list."""

        return self.connected_to.keys()

    def get_weight(self, neighbor):
        """"Get the weight of the edge from this vertex to the vertex passed as a parameter."""

        return self.connected_to[neighbor]
