from chapter04_recursion.maze import Maze
from chapter04_recursion.maze_constants import DEAD_END, OBSTACLE, PART_OF_PATH, TRIED


def search_from(maze, start_row, start_column):
    # Try each of four directions from this point until we find a way out.

    # Base case return values:
    # 1. We have run into an obstacle, return false.
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False

    # 2. We have found a square that has already been explored.
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False

    # 3. We have found an outside edge not occupied by an obstacle.
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)

    # Otherwise, use logical short-circuiting to try each direction in turn (if needed).
    test1 = search_from(maze, start_row - 1, start_column) or search_from(maze, start_row + 1, start_column)
    test2 = search_from(maze, start_row, start_column - 1) or search_from(maze, start_row, start_column + 1)
    found = test1 or test2

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


def main():
    maze = Maze('maze_test.txt')
    maze.draw_maze()
    maze.update_position(maze.start_row, maze.start_col)

    search_from(maze, maze.start_row, maze.start_col)


if __name__ == "__main__":
    main()
