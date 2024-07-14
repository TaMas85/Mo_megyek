import turtle
import pandas

screen = turtle.Screen()
screen.title("Magyar megyék")
image = "Megye.gif"
screen.addshape(image)
screen.setup(width=980, height=610)
turtle.shape(image)


data = pandas.read_csv("Mo_megyek.csv")

megyek = data.Megye.tolist()

known_megyek = []
miss_megyek = []
no = 0
yes = True
while yes:
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    answer_box = screen.textinput(title=f"Sorold fel a megyéket {no}/50", prompt="(press 'x' to EXIT)\nA megye neve:")
    for i in megyek:
        if i == answer_box:
            known_megyek.append(answer_box)
            no += 1
            right_guess = data[data.Megye == answer_box]
            x = right_guess.x.item()
            y = right_guess.y.item()
            name.goto(x, y)
            name.write(answer_box, font=('Arial', 24, 'normal'))
        elif answer_box == "x":
            yes = False
for i in megyek:
    if i in known_megyek:
        pass
    else:
       miss_megyek.append(i)

miss_data = pandas.DataFrame(miss_megyek)

miss_data.to_csv("learn_megyek.csv")

# hogyan hatarozunk meg koordinatat egy keprol eger kattintassal
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)

screen.mainloop()
