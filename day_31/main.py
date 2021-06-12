import tkinter
import pandas
import pandas.errors
import random
import tkinter.messagebox

SAVE_FILE = "data/save.csv"

try:
    vocabulary_data = pandas.read_csv(SAVE_FILE)
except (FileNotFoundError, pandas.errors.EmptyDataError):
    vocabulary_data = pandas.read_csv("data/sunda-english.csv")


LANG_FRONT = vocabulary_data.columns[0]
LANG_BACK = vocabulary_data.columns[1]

cards = vocabulary_data.to_dict('records')

current_card = None
timer = None


def count_down():
    global timer
    timer = window.after(3000, flip_card, current_card)


def flip_card(card):
    canvas_card.itemconfigure(front_image_canvas, state="hidden")
    canvas_card.itemconfigure(back_image_canvas, state="normal")

    canvas_card.itemconfigure(lang_text, text=LANG_BACK)
    canvas_card.itemconfigure(vocab_text, text=card[LANG_BACK])


def get_new_card():
    global current_card
    current_card = None
    try:
        card = random.choice(cards)
    except IndexError:
        tkinter.messagebox.showinfo("Finish", "All cards have been answered correctly!")
        return
    else:
        current_card = card
        canvas_card.itemconfigure(front_image_canvas, state="normal")
        canvas_card.itemconfigure(back_image_canvas, state="hidden")

        canvas_card.itemconfigure(lang_text, text=LANG_FRONT)
        canvas_card.itemconfigure(vocab_text, text=current_card[LANG_FRONT])

        count_down()


def right_command():
    window.after_cancel(timer)
    if current_card is not None:
        cards.remove(current_card)
    get_new_card()


def wrong_command():
    window.after_cancel(timer)
    if current_card is not None:
        cards.remove(current_card)
        cards.append(current_card)
    get_new_card()


def on_closing():
    save_data = pandas.DataFrame(cards)
    save_data.to_csv(SAVE_FILE, index=False)
    window.destroy()


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

window = tkinter.Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
canvas_card = tkinter.Canvas(window, width=800, height=526)

front_image_canvas = canvas_card.create_image(400, 268, image=card_front)
back_image_canvas = canvas_card.create_image(400, 268, image=card_back, state="hidden")

lang_text = canvas_card.create_text(400, 150, fill="black", font=(FONT, 40, "italic"))
vocab_text = canvas_card.create_text(400, 263, fill="black", font=(FONT, 60, "bold"))

get_new_card()

canvas_card.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(row=0, column=0, columnspan=2)

button_right_image = tkinter.PhotoImage(file="images/right.png")
button_right = tkinter.Button(image=button_right_image, highlightthickness=0, command=right_command)
button_right.grid(row=1, column=0)

button_wrong_image = tkinter.PhotoImage(file="images/wrong.png")
button_wrong = tkinter.Button(image=button_wrong_image, highlightthickness=0, command=wrong_command)
button_wrong.grid(row=1, column=1)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
