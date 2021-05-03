from turtle import Screen # ,Turtle
from snake import Snake # import Snake class from snake module
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turn animation off

# Create new snake object from Snake class, initialize a snake object
snake = Snake()
# Create food object
food = Food()
# Create scoreboard object
scoreboard = Scoreboard()

# Control snake
screen.listen() # starting listening for keystroke: up, down, left, right
screen.onkey(snake.up, "Up") # bind Up from keyboard to snake object function up
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move Snake: tail will follow head
game_is_on = True
while game_is_on:
    # only update screen when all segments move forward
    # screen is updating every 0.1 sec, delay 0.1 sec and refresh screen
    screen.update()  # animation is updated, we can see snake move to next position.
    time.sleep(0.1)  # sleep by 1 sec, add 1 sec delay after each segment moves.
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15: # if detect collision with food, food size is 10 x 10 pixel, 15 pixel is a number after trying many time
        food.refresh() # food should move to new random position
        snake.extend()
        scoreboard.increase_score() # increase score on scoreboard

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

        # game_is_on = False # end while loop,means end snake movement and food
        # scoreboard.game_over()

    # Detect collision with tail, if head collide with any segment in tail, trigger game_over
    for segment in snake.segments:
        if segment == snake.head: # need to bypass head
            pass
        elif snake.head.distance(segment) < 10: # but will fail because first segment of snake is head, so distance bewteen head & head is <0, game _over
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    # using slicing, slicing works for list & tuple
    # for segment in snake.segments[1:]: # want to loop through every segment in snake.segment except the first one(head)
        # if snake.head.distance(segment) < 10: # but will fail because first segment of snake is head, so distance bewteen head & head is <0, game _over
            # game_is_on = False
            # scoreboard.game_over()

screen.exitonclick()