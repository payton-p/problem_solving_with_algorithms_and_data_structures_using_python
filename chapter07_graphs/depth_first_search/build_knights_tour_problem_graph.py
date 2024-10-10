from chapter07_graphs.graph import Graph


# Another classic problem that we can use to illustrate a second common graph algorithm is called the “knight’s tour.”
# The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle
# is to find a sequence of moves that allow the knight to visit every square on the board exactly once. One such
# sequence is called a 'tour.'
def build_knights_tour_problem_graph(board_size):
    """Build a graph for the Knight's Tour Problem."""

    graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            # This is the vertex id of the given position.
            node_id = position_to_node_id(row, col, board_size)

            # Get the list of legal moves for the given position on the board.
            new_positions = generate_legal_moves(row, col, board_size)

            for position in new_positions:
                position_node_id = position_to_node_id(position[0], position[1], board_size)

                # All legal moves are converted into edges in the graph.
                graph.add_edge(node_id, position_node_id)

    return graph


def position_to_node_id(row, column, board_size):
    """Convert a location on the board in terms of a row and a column into a linear vertex number."""

    return (row * board_size) + column


def generate_legal_moves(x, y, board_size):
    """
    Create list of legal moves for the given position on the board.

    Take the position of the knight on the board and generates each of the eight possible moves.
    """

    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]

        if legal_coordinates(new_x, board_size) and legal_coordinates(new_y, board_size):
            new_moves.append((new_x, new_y))

    return new_moves


def legal_coordinates(x, board_size):
    """Determine if the coordinates are valid for the board size."""

    if 0 <= x < board_size:
        return True
    else:
        return False


def main():
    # Build graph.
    board_size = 5
    graph = build_knights_tour_problem_graph(board_size)
    print(graph.get_vertices())


if __name__ == "__main__":
    main()
