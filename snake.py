from turtle import Turtle, Screen
position_direction=[(0,0),(-20,0),(-40,0)]
Up=90
Down=270
Left=180
Right=0
class Snake:
    def __init__(self):
        self.move_dis = 10
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in position_direction:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)

    def move_snake(self):
            for seg in range(len(self.segment) - 1, 0, -1):
                new_x = self.segment[seg - 1].xcor()
                new_y = self.segment[seg - 1].ycor()
                self.segment[seg].goto(new_x, new_y)
            self.head.forward(self.move_dis)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def motion(self):
        self.move_dis += 0.1