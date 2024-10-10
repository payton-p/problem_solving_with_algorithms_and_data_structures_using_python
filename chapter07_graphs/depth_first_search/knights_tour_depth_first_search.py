from chapter07_graphs.depth_first_search.build_knights_tour_problem_graph import build_knights_tour_problem_graph


# Another classic problem that we can use to illustrate a second common graph algorithm is called the “knight’s tour.”
# The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle
# is to find a sequence of moves that allow the knight to visit every square on the board exactly once. One such
# sequence is called a 'tour.'
def knights_tour(current_depth, path, current_explored_vertex, limit):
    """
    We will use depth first search (DFS) to solve the knight's tour problem. A DFS creates a search tree by exploring
    one branch of the tree as deeply as possible. In this specific problem, we will forbid a node to be visited more
    than once.

    The knight's tour is a special case of a DFS, where the goal is to create the deepest depth first tree, without any
    branches.

    Parameters breakdown:
    current_depth: current depth of the search tree
    path: list of vertices visited up to this point
    current_explored_vertex: the vertex in the graph we wish to explore
    limit: the number of nodes in the path

    DFS uses colors to keep track of which vertices in the graph have been visited. Unvisited vertices are white, and
    visited vertices are colored gray.
    """

    current_explored_vertex.set_color("gray")
    path.append(current_explored_vertex)

    if current_depth < limit:
        neighbor_list = list(order_by_fewest_available_moves(current_explored_vertex))
        i = 0
        done = False

        while i < len(neighbor_list) and not done:
            if neighbor_list[i].get_color() == 'white':
                # When the DFS algorithm finds a dead end, it backs up the tree to the next deepest vertex that allows
                # it to make a legal move. If all neighbors of a particular vertex have been explored, and we have not
                # yet reached our goal length, we have reached a dead end. When we reach a dead end, we must backtrack.
                # Backtracking happens when we return from knights_tour() with a status of False. Since DFS search is
                # recursive, we are implicitly using a stack to help us with our backtracking. When knights_tour()
                # returns False here, we remain inside the while loop and look at the next vertex in the neighbor list.
                done = knights_tour(current_depth + 1, path, neighbor_list[i], limit)

            i = i + 1

        # Prepare to backtrack.
        if not done:
            path.pop()
            current_explored_vertex.set_color('white')

    # Indicates we have found a successful tour.
    else:
        done = True

    if done:
        return path
    else:
        return done


def order_by_fewest_available_moves(current_explored_vertex):
    """
    Order the neighbor list by the fewest available moves.

    The problem with using the vertex with the most available moves as your next vertex on the path is that it tends to
    have the knight visit the middle squares early on in the tour. When this happens it is easy for the knight to get
    stranded on one side of the board where it cannot reach unvisited squares on the other side of the board. On the
    other hand, visiting the squares with the fewest available moves first pushes the knight to visit the squares around
    the edges of the board first. This ensures that the knight will visit the hard-to-reach corners early and can use
    the middle squares to hop across the board only when necessary. Utilizing this kind of knowledge to speed up an
    algorithm is called a heuristic. Humans use heuristics every day to help make decisions, heuristic searches are
    often used in the field of artificial intelligence. This particular heuristic is called Warnsdorff’s algorithm,
    named after H. C. Warnsdorff who published his idea in 1823.
    """

    result_list = []

    for v in current_explored_vertex.get_connections():
        if v.get_color() == "white":
            c = 0

            for w in v.get_connections():
                if w.get_color() == "white":
                    c = c + 1

            result_list.append((c, v))

    # This ensures that we select the vertex to go next that has the fewest available moves.
    result_list.sort(key=lambda x: x[0])

    return [y[1] for y in result_list]


def print_table_of_moves(moves_dictionary, board_size, num_positions):
    """Print a table where the position in the table holds the number of moves it took to get there."""

    print(
        "\n\nTable showing how many moves it took to get to each position. For example, the 0 position on the board is "
        "the 1st move in this example. The 7 position is the 2nd move.")

    position_in_row = 0
    for i in range(num_positions):
        for key in moves_dictionary:
            if i == key:
                if position_in_row < board_size - 1:
                    print(moves_dictionary[i], end=" ")

                    position_in_row += 1
                else:
                    print(moves_dictionary[i])

                    position_in_row = 0


def main():
    # Build graph.
    board_size = 5  # meaning it's a 5x5 board
    graph = build_knights_tour_problem_graph(board_size)
    print(graph.get_vertices())

    # Use DFS to solve the Knight's Tour problem.
    current_depth = 0
    path = []
    start_vertex = graph.get_vertex(0)  # start at (0, 0)
    limit = board_size * board_size - 1  # the number of positions on the board, excluding the starting position
    tour = knights_tour(current_depth, path, start_vertex, limit)

    # Print results.
    moves_dictionary = {}
    if tour is False:
        print("No tour found.")
    else:
        print("\nSuccessful tour (the number indicates the vertex ID, which represents the position on the board):")

        move_num = 1
        for vertex in path:
            print(vertex.get_id(), end=" ")

            moves_dictionary[vertex.get_id()] = move_num
            move_num += 1

    print_table_of_moves(moves_dictionary, board_size, limit + 1)


if __name__ == "__main__":
    main()
