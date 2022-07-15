import turtle
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
initial_position = [(0, 0), (-20, 0), (-40, 0)]
snake = []


for i in initial_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(i)
    snake.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    for i in range(1, -1, -1):  # 1, 0
        # print(f"i: {i}")          #snake[2]snake[1]snake[0]  이렇게 자리 하고 있는데
        x_ahead = snake[i].xcor()   #        snake[1] 의  x 좌표값
        y_ahead = snake[i].ycor()   #                    y 좌표값을 구해서
        snake[i+1].goto(x_ahead, y_ahead)  # snake[2]가  snake[1] 자리로 이동 하게 함.
                        # 그리고 다음은 snk[1]이 snk[0]자리로 이동함 이렇게 뒤에꺼 두개 따라오게 하는 loop
    snake[0].forward(20)
    # 여기서 snk[0] 이 움직이면  다음에 for 들어가서 snk2는 snk1 자리로 옮기고
    # snk1은 snk[0]자리로 옮겨서 결국 다 따라오게됨
    time.sleep(0.5)
    snake[0].left(90)
    # snake[0].forward(20)

    # screen.update()
    # for i in range(2, -1, -1):
    #     print(i)
    #     snake[i].forward(20)
    #     screen.update()
    #     time.sleep(0.5)



screen.exitonclick()
