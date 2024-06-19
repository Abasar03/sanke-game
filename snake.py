from turtle import Turtle


POSITIONS=[(0,0),(-20,0),(20,0)]
MOVE_DISTANCE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270



class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.snake_head=self.snake_list[0]


    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)

    def reset(self):
        for i in self.snake_list:
            i.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.snake_head = self.snake_list[0]



    def add_segment(self,positions):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(positions)
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
        #self.snake_list[0].left(90)


    def up(self):
        if self.snake_head.heading() == DOWN:
            pass
        else:
            self.snake_head.setheading(90)


    def down(self):
        if self.snake_head.heading() == UP:
            pass
        else:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() == RIGHT:
            pass
        else:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() == LEFT:
            pass
        else:
            self.snake_head.setheading(0)

