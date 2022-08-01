from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
timmy = Turtle("turtle")
timmy.penup()
timmy.goto(x=-230, y=-140)






screen.exitonclick()