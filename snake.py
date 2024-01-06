from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        # Create a snake body
        for i in range(3):
            new_body_segment = Turtle('square')
            new_body_segment.penup()
            new_body_segment.color('white')
            new_body_segment.setpos(x=(-20 * i), y=0)
            self.body.append(new_body_segment)

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(20)
