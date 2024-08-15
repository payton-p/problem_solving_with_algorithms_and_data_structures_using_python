import turtle


def draw_triangle(points, color, turtle_cursor):
    turtle_cursor.fillcolor(color)
    turtle_cursor.up()
    turtle_cursor.goto(points[0][0], points[0][1])
    turtle_cursor.down()
    turtle_cursor.begin_fill()
    turtle_cursor.goto(points[1][0], points[1][1])
    turtle_cursor.goto(points[2][0], points[2][1])
    turtle_cursor.goto(points[0][0], points[0][1])
    turtle_cursor.end_fill()


def get_midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def draw_sierpinski_triangle(points, degree, turtle_cursor):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, colormap[degree], turtle_cursor)

    if degree > 0:
        draw_sierpinski_triangle([points[0], get_midpoint(points[0], points[1]), get_midpoint(points[0], points[2])],
                                 degree - 1, turtle_cursor)
        draw_sierpinski_triangle([points[1], get_midpoint(points[0], points[1]), get_midpoint(points[1], points[2])],
                                 degree - 1, turtle_cursor)
        draw_sierpinski_triangle([points[2], get_midpoint(points[2], points[1]), get_midpoint(points[0], points[2])],
                                 degree - 1, turtle_cursor)


def main():
    turtle_cursor = turtle.Turtle()
    window = turtle.Screen()
    points = [[-100, -50], [0, 100], [100, -50]]
    draw_sierpinski_triangle(points, 3, turtle_cursor)
    window.exitonclick()


if __name__ == "__main__":
    main()
