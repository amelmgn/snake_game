from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkOliveGreen')
screen.title("Snake game")
screen.tracer(0)  # turn off a tracer for further screen updates

# Create a snake body
snake = Snake()

# Listen for controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Move the snake
is_game_on = False
if len(snake.body) != 0:
    is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)  # A delay between animations
    snake.move()

screen.exitonclick()
