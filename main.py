from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard  import Scoreboard


# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Kaashish V")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
head = snake.head

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    head = snake.head
    snake.move()

    if head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.add_score()
    score.display()

    # Detect collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        score.reset()
        snake.reset()
        score.game_over()
        game_on = False

    # Detect collision with tail
    for squares in snake.snake_squares[2:]:
        if head.distance(squares) < 10:
            score.reset()
            snake.reset()
            score.game_over()
            game_on = False


screen.exitonclick()







