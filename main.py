import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Create a window 600x600 px
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkOliveGreen')
screen.title("Snake game")
screen.tracer(0)  # turn off a tracer for further screen updates
DELAY = 0.1

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

# Listen for controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Move the snake. Prior check if the snake exist
is_game_on = False
if len(snake.body) != 0:
    is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(DELAY)  # A delay between animations
    snake.move()

    # Detect collisions with the food and print score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.refresh_score()

    # Detect collisions with walls
    if ((snake.head.xcor() < -290 or snake.head.xcor() > 290) or
            (snake.head.ycor() < -290 or snake.head.ycor() > 290)):
        is_game_on = False
        score.game_over()

    # Detect collisions with a tail:
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
