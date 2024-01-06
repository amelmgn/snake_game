import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkOliveGreen')
screen.title("Snake game")
screen.tracer(0)  # turn off a tracer for further screen updates

# Create a snake body
snake = Snake()
food = Food()
score = Scoreboard()

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

    # Detect collisions with the food and print score
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()

    # Detect collisions with walls
    if ((snake.head.xcor() < -280 or snake.head.xcor() > 280)
            or (snake.head.ycor() < -280 or snake.head.ycor() > 280)):
        is_game_on = False
        score.game_over()


screen.exitonclick()
