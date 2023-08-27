import turtle
from chapter04_recursion.maze_constants import DEAD_END, OBSTACLE, PART_OF_PATH, TRIED


class Maze:
    def __init__(self, maze_file_name):
        self.maze_list = []
        rows_in_maze = 0
        columns_in_maze = 0

        maze_file = open(maze_file_name, 'r')
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1

            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2

        self.turtle = turtle.Turtle(shape='turtle')
        turtle.setup(width=600, height=600)
        turtle.setworldcoordinates(-(columns_in_maze - 1) / 2 - .5,
                                   -(rows_in_maze - 1) / 2 - .5,
                                   (columns_in_maze - 1) / 2 + .5,
                                   (rows_in_maze - 1) / 2 + .5)

    def __getitem__(self, index):
        return self.maze_list[index]

    def draw_maze(self):
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate,
                                           'tan')
        self.turtle.color('black', 'blue')

    def draw_centered_box(self, x, y, color):
        turtle.tracer(0)
        self.turtle.up()
        self.turtle.goto(x - .5, y - .5)
        self.turtle.color('black', color)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(1)
            self.turtle.right(90)
        self.turtle.end_fill()
        turtle.update()
        turtle.tracer(1)

    def move_turtle(self, x, y):
        self.turtle.up()
        self.turtle.setheading(self.turtle.towards(x + self.x_translate,
                                                   -y + self.y_translate))
        self.turtle.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        self.turtle.dot(color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val

        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)
