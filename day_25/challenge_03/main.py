import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=1010, height=461)
screen.bgpic("indonesia.gif")
screen.title("Indonesia Province")
screen.tracer(0)

# Setup code
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

map_data = pandas.read_csv("map.csv")

number_of_province = len(map_data)
correct_answer = []

while len(correct_answer) < number_of_province:
    answer = screen.textinput(f"{len(correct_answer)}/{number_of_province} Jawaban Benar", "Masukan nama provinsi:")

    if answer is None or answer.lower() == "exit":
        break

    data = map_data[map_data.province.str.lower() == answer.lower()]
    if not data.empty:
        x = float(data.x)
        y = float(data.y)
        # province = data.province.to_string(index=False)
        province = data.province.item()
        correct_answer.append(province)

        pin = turtle.Turtle()
        pin.color("black")
        pin.up()
        pin.ht()
        pin.goto(x, y)
        pin.write(province, align="center", font=("Courier", 8, "bold"))
        screen.update()

if len(correct_answer) < number_of_province:
    un_answered_province = []
    for province in map_data.province.tolist():
        if province not in correct_answer:
            un_answered_province.append(province)

    un_answered_data = {
        "province": un_answered_province,
    }

    un_answered_report = pandas.DataFrame(un_answered_data)
    un_answered_report.to_csv("un_answered_report.csv")

screen.exitonclick()
