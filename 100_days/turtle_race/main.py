from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(
    "Make your bets!", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def set_turtle(turtle, number):
    position = -100 + (35 * int(number))
    turtle.color(colors[int(number)])
    turtle.penup()
    turtle.goto(x=-230, y=position)


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    set_turtle(turtle=new_turtle, number=i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 220:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You won the bet! {winning_color} was the winner!")
            else:
                print(f"You lost! {winning_color} was the winner!")
        random_distance = random.randint(0, 10)
        i.forward(random_distance)


screen.exitonclick()
