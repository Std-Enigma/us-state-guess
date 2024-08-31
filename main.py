import turtle

import pandas

IMAGE = "blank_states_img.gif"
DATA = pandas.read_csv("50_states.csv")
STATES = DATA.state.tolist()
STATES_AMOUNT = len(STATES)
FONT = ("Consolas", 10, "italic")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic(IMAGE)

writer = turtle.Turtle(visible=False)
writer.speed("fastest")
writer.penup()

guessed_states, missing_states = [], []


def correct_the_spelling(word: str) -> str:
    word_to_list = word.split(" ")
    word = ""
    for index in range(len(word_to_list)):
        word += word_to_list[index].capitalize()
        if index == 0 and len(word_to_list) > 1:
            word += " "
    return word


while len(guessed_states) <= 50:
    answer = turtle.textinput(
        title=f"{len(guessed_states)}/{STATES_AMOUNT} States correct.",
        prompt="What's the another state name?",
    )
    if answer != "" or answer is None:
        answer = correct_the_spelling(answer)
    if answer.lower() == "exit":
        missing_states = [state for state in STATES if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states).to_csv("missed_states_data.csv")
        break
    if answer in STATES:
        writer.goto(
            x=int(DATA[DATA.state == answer].x), y=int(DATA[DATA.state == answer].y)
        )
        writer.write(arg=answer, move=False, align="center", font=FONT)
        guessed_states.append(answer)

screen.exitonclick()
