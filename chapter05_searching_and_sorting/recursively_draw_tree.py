import turtle


def tree(branch_length, turtle_cursor):
    if branch_length > 5:
        turtle_cursor.forward(branch_length)
        turtle_cursor.right(20)
        tree(branch_length - 15, turtle_cursor)
        turtle_cursor.left(40)
        tree(branch_length - 15, turtle_cursor)
        turtle_cursor.right(20)
        turtle_cursor.backward(branch_length)


def main():
    turtle_cursor = turtle.Turtle()
    window = turtle.Screen()
    turtle_cursor.left(90)
    turtle_cursor.up()
    turtle_cursor.backward(100)
    turtle_cursor.down()
    turtle_cursor.color("green")
    tree(75, turtle_cursor)

    window.exitonclick()


if __name__ == "__main__":
    main()
