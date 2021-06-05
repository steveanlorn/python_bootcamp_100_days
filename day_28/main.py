import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT = "Courier"

WORKING_SESSION = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60

CHECKMARK = "✅"

reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)

    global reps
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    start_button["state"] = "active"
    reset_button["state"] = "disabled"


# -------- TIMER MECHANISM
def start_timer():
    # 1 25 work
    # 2 5 break
    # 3 25 work
    # 4 5 break
    # 5 25 work
    # 6 5 break
    # 7 25 work
    # 8 20 long break

    global reps
    start_button["state"] = "disabled"
    reset_button["state"] = "active"

    reps += 1

    if reps % 2 != 0:
        session = WORKING_SESSION
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        session = LONG_BREAK
        timer_label.config(text="Long Break", fg=RED)
    else:
        session = SHORT_BREAK
        timer_label.config(text="Short Break", fg=PINK)

    countdown(session)


# -------- COUNTDOWN MECHANISM
def countdown(n):
    if n >= 0:
        minute = n // 60
        second = n % 60

        canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(minute, second))
        global timer
        timer = window.after(1000, countdown, n - 1)
    else:
        global reps

        start_button["state"] = "active"

        marks = ""
        for _ in range(math.ceil(reps/2)):
            marks += CHECKMARK
            check_label.config(text=marks)

        if reps == 8:
            reps = 0
            check_label.config(text="")

        window.lift()
        window.attributes("-topmost", True)
        window.after_idle(window.attributes, '-topmost', False)


# -------- UI
window = tkinter.Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, foreground=GREEN, font=(FONT, 36, "bold"))
timer_label.pack()

canvas = tkinter.Canvas(width=256, height=256, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(128, 128, image=tomato_image)
timer_text = canvas.create_text(128, 155, text="00:00", fill="white", font=(FONT, 34, "bold"))
canvas.pack()

button_frame = tkinter.Frame(window, bg=YELLOW)
button_frame.pack(fill=tkinter.BOTH)

start_button = tkinter.Button(button_frame, text="Start", highlightthickness=0, command=start_timer)
start_button.pack(side="left")

reset_button = tkinter.Button(button_frame, text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
reset_button.pack(side="right")

check_label = tkinter.Label(bg=YELLOW, foreground=GREEN, font=(FONT, 18, "bold"))
check_label.pack()

window.mainloop()
