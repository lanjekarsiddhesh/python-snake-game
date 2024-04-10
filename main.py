import turtle
from snake import Snake
from snake_food import Food
from score import scoreboard
from turtle import Screen,Turtle
import time

my_screen=Screen()
my_screen.setup(500,500)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)
snake=Snake()
snake.create_snake()
food=Food()
ScoreBoard=scoreboard()

my_screen.listen()
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")

scores=0
game_on=True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food)<15:
        ScoreBoard.increase_score()
        snake.motion()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 235 or  snake.head.xcor() < -235 or snake.head.ycor() > 235 or snake.head.ycor() < -235:
        ScoreBoard.game_over()
        ScoreBoard.reset()
        game_on = False


    for segme in snake.segment[1:]:
        if snake.head.distance(segme) < 10:
            ScoreBoard.game_over()
            ScoreBoard.reset()
            game_on = False

# my_screen.exitonclick()
turtle.done()