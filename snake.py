from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.body = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        # Create a snake body
        for position in INITIAL_POSITIONS:
            self.add_segment(position=position)
        # First segment of the snake is its head
        self.head = self.body[0]

    def add_segment(self, position):
        new_body_segment = Turtle('circle')
        new_body_segment.penup()
        new_body_segment.color('white')
        new_body_segment.setpos(position)
        self.body.append(new_body_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
