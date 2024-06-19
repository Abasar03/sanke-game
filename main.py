from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Eating food
    if snake.snake_head.distance(food) < 15:
        food.new_position()
        snake.extend()
        scoreboard.increase_score()
    #collision with wall
    if snake.snake_head.xcor()>290 or snake.snake_head.xcor()<-300 or snake.snake_head.ycor()>300 or snake.snake_head.ycor()<-290:
        scoreboard.reset_score()
        snake.reset()
    #collision with tail
    for i in snake.snake_list[1:]:
        if snake.snake_head.distance(i)<10:
            scoreboard.reset_score()
            snake.reset()





screen.exitonclick()