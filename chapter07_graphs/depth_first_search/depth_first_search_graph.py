from chapter07_graphs.graph import Graph


class DfsGraph(Graph):
    """
    Graph that implements the depth first search (DFS).

    This is a subclass of Graph.
    """

    def __init__(self):
        super().__init__()

        self.time = 0  # tracks the number of steps in the algorithm
        self.result_path = []

    def depth_first_search(self):
        """
        The goal is to search as deeply as possible, connecting as many nodes in the graph as possible and branching
        where necessary.

        It is even possible that a DFS will create more than one tree. When the DFS algorithm creates a group of trees,
        we call this a depth first forest.

        This method iterates over all the vertices in the graph, calling depth_first_search_visit on the nodes that are
        white. The reason we iterate over all the nodes, rather than simply searching from a chosen starting node, is to
        make sure that all nodes in the graph are considered and that no vertices are left out of the depth first
        forest.
        """

        for vertex in self:
            vertex.set_color("white")
            vertex.set_predecessor(-1)

        for vertex in self:
            if vertex.get_color() == "white":
                self.depth_first_search_visit(vertex)

    def depth_first_search_visit(self, start_vertex):
        """
        Visit nodes in DFS.

        Call on white nodes.

        The starting/discovery and finishing times for each node display a property called the "parenthesis property."
        This property means that all children of a particular node in the depth first tree have a later discovery
        time and an earlier finish time than their parent.
        """

        # First step in visiting a vertex is to set the color to gray.
        start_vertex.set_color("gray")
        self.time += 1
        start_vertex.set_discovery_time(self.time)

        # Explore all neighboring white vertices as deeply as possible.
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == "white":
                next_vertex.set_predecessor(start_vertex)

                # The use of a stack is implicit because of this recursive call.
                self.depth_first_search_visit(next_vertex)

        self.result_path.append(start_vertex)
        start_vertex.set_color("black")
        self.time += 1
        start_vertex.set_finish_time(self.time)

    def print_result_path(self):
        self.result_path.reverse()

        print("Result path:", end=" ")
        for vertex in self.result_path:
            print(vertex.get_id(), end=" ")
        print()


def main():
    # Build graph.
    graph = DfsGraph()
    for i in ["A", "B", "C", "D", "E", "F"]:
        graph.add_vertex(i)

    print(graph.get_vertices())

    # Add edges.
    graph.add_edge("A", "B", 0)
    graph.add_edge("A", "D", 0)
    graph.add_edge("B", "C", 0)
    graph.add_edge("B", "D", 0)
    graph.add_edge("D", "E", 0)
    graph.add_edge("E", "B", 0)
    graph.add_edge("E", "F", 0)
    graph.add_edge("F", "C", 0)

    for v in graph:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))

    # Result path should be: [A, B, D, E, F, C]
    print("\nApply DFS to graph.")
    graph.depth_first_search()

    print("Total time:", graph.time)
    graph.print_result_path()


if __name__ == "__main__":
    main()
