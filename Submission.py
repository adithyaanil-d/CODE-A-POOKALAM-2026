import turtle
import math

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Onam Pookalam")
screen.bgcolor("white")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

S = 0.72

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

def filled_circle(radius, color):
    radius *= S
    move(0, -radius)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def polygon(points, color):
    points = [(x * S, y * S) for x, y in points]

    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(points[0])
    t.pendown()

    for point in points[1:]:
        t.goto(point)

    t.goto(points[0])
    t.end_fill()

def petal(cx, cy, length, width, angle, color):
    cx *= S
    cy *= S
    length *= S
    width *= S

    rad = math.radians(angle)

    tip_x = cx + length * math.cos(rad)
    tip_y = cy + length * math.sin(rad)

    left_x = cx + width * math.cos(rad + math.pi / 2)
    left_y = cy + width * math.sin(rad + math.pi / 2)

    right_x = cx + width * math.cos(rad - math.pi / 2)
    right_y = cy + width * math.sin(rad - math.pi / 2)

    t.fillcolor(color)

    t.penup()
    t.goto(left_x, left_y)
    t.pendown()

    t.begin_fill()
    t.goto(tip_x, tip_y)
    t.goto(right_x, right_y)
    t.goto(cx, cy)
    t.end_fill()

def petal_ring(count, radius, length, width, color, offset=0):
    for i in range(count):
        angle = offset + i * 360 / count

        cx = radius * math.cos(math.radians(angle))
        cy = radius * math.sin(math.radians(angle))

        petal(cx, cy, length, width, angle, color)

def dot_ring(count, radius, size, color):
    for i in range(count):
        angle = math.radians(i * 360 / count)

        x = radius * math.cos(angle) * S
        y = radius * math.sin(angle) * S

        move(x, y)
        t.dot(size * S, color)

filled_circle(390, "#111111")
filled_circle(365, "#F6B800")
filled_circle(350, "#111111")

petal_ring(24, 285, 100, 32, "#D62828")
petal_ring(24, 245, 92, 30, "#F77F00")
petal_ring(24, 205, 78, 27, "#FCBF49")

petal_ring(24, 172, 62, 23, "#FFF4D6", 7.5)

filled_circle(145, "#176B3A")

for i in range(16):
    angle = i * 360 / 16 + 11.25
    rad = math.radians(angle)

    cx = 125 * math.cos(rad)
    cy = 125 * math.sin(rad)

    points = [
        (cx, cy + 13),
        (cx + 9, cy),
        (cx, cy - 13),
        (cx - 9, cy)
    ]

    polygon(points, "#FFD166")

petal_ring(16, 95, 58, 22, "#C9184A")

petal_ring(16, 72, 43, 17, "#F77F00", 11.25)

petal_ring(12, 48, 35, 14, "#FFF8E7")

filled_circle(38, "#FFD166")

for i in range(8):
    angle = i * 360 / 8
    rad = math.radians(angle)

    cx = 18 * math.cos(rad)
    cy = 18 * math.sin(rad)

    petal(
        cx,
        cy,
        18,
        8,
        angle,
        "#D62828"
    )

filled_circle(11, "#8B1E3F")

dot_ring(24, 330, 8, "#FFF4D6")
dot_ring(24, 310, 6, "#D62828")
dot_ring(16, 105, 6, "#FFF4D6")

t.pensize(4 * S)

for radius, color in [
    (365, "#FFF4D6"),
    (350, "#D62828"),
    (335, "#F77F00"),
    (185, "#FFD166"),
    (155, "#FFF4D6"),
    (75, "#FFD166"),
    (40, "#FFF4D6")
]:
    move(0, -radius * S)
    t.pencolor(color)
    t.circle(radius * S)

filled_circle(7,"#D62828")

screen.update()
turtle.done()
