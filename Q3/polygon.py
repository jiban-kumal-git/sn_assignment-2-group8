import turtle

def draw_edge(length, depth):
    """
    Recursively draw one edge of the fractal polygon.
    - At depth 0: just draw a straight line
    - Otherwise: split into 4 smaller edges with indentation
    """
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3  # divide edge into 3 parts
        draw_edge(length, depth - 1)
        turtle.left(60)       # start indentation
        draw_edge(length, depth - 1)
        turtle.right(120)     # second side of indentation
        draw_edge(length, depth - 1)
        turtle.left(60)       # return to original direction
        draw_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    """
    Draw the full polygon.
    Each side is replaced with a recursive edge pattern.
    """
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)

def main():
    # Get user input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Setup turtle
    turtle.speed("fastest")
    turtle.penup()
    turtle.pendown()

    # Draw fractal polygon
    draw_polygon(sides, length, depth)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
