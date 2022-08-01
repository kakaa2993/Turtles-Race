from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -120
x = -230
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50
    all_turtles.append(new_turtle)
if user_bet:
    is_running = True

while is_running:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_running = False
            the_winner = turtle.pencolor()
            if user_bet.lower() == the_winner:
                print(f"You win! The winner is the '{the_winner}' turtle.")
            else:
                print(f"You lose! The winner is the '{the_winner}' turtle.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()