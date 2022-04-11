import turtle
import pandas
from position_of_states import Position

c = ""
d = 0
new_d_s = {}

data = pandas.read_csv("50_states.csv")
data_state = data["state"].to_list()

screen = turtle.Screen()
screen.title("US states game")
shape = "blank_states_img.gif"
# to add any picture but only .gif format
screen.addshape(shape)
turtle.shape(shape)

pos = Position()

b = True
while b:
    user_answer = screen.textinput(title="Guess the name!", prompt=c+"input the correct state name:").title()
    if user_answer == "Exit":
        new_d_s["missing state"] = data_state
        break
    if user_answer in data_state:
        s_data = data[data.state == user_answer]
        pos.writer(int(s_data.x), int(s_data.y), user_answer)
        data_state.remove(user_answer)
        d += 1
        c = f"{d}/50"
        if d == 50:
            b = False

missing_state = pandas.DataFrame(new_d_s)
missing_state.to_csv("missing_state")
