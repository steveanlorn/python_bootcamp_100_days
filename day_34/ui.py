import tkinter
from quiz import Quiz

WINDOW_BG_COLOR = "#21466C"

CANVAS_BG_COLOR = "#FFFFFF"
QUESTION_COLOR = "#21466C"
QUESTION_FONT = ("Arial", 20, "italic")

SCORE_FG_COLOR = "#FFFFFF"
SCORE_FONT = ("Arial", 16, "normal")

WRONG_BG_COLOR = "#AF1F1F"
WRONG_TEXT_COLOR = "#FFFFFF"

TRUE_BG_COLOR = "#1AA698"
TRUE_TEXT_COLOR = "#FFFFFF"


class UI:
    def __init__(self, quiz: Quiz):

        self.score = 0
        self.quiz = quiz

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=WINDOW_BG_COLOR, pady=20, padx=20)

        self.score_text = tkinter.Label(text=f"Score: {self.score}", bg=WINDOW_BG_COLOR, fg=SCORE_FG_COLOR,
                                        font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(self.window, width=300, height=250, bg=CANVAS_BG_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.question_text = self.canvas.create_text(150, 125,
                                                     text=f"Q{quiz.question_number}. {quiz.current_question.text}",
                                                     fill=QUESTION_COLOR, width=290, font=QUESTION_FONT)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.button_true = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_action)
        self.button_true.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.button_false = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_action)
        self.button_false.grid(row=2, column=1)

        # FOR DEBUG
        print(self.quiz.current_question.answer)

        self.window.mainloop()

    def true_action(self):
        self.answer_question("true")

    def false_action(self):
        self.answer_question("false")

    def end_game(self):
        text = f"""
            Congratulations!
            Your final score is {self.score}/{len(self.quiz.questions)}
        """
        self.canvas.itemconfigure(self.question_text, text=text)
        self.button_true["state"] = "disabled"
        self.button_false["state"] = "disabled"

    def set_question(self):
        if self.quiz.is_still_has_question():
            self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text,
                                      text=f"Q{self.quiz.question_number}. {self.quiz.current_question.text}")
            # FOR DEBUG
            print(self.quiz.current_question.answer)
        else:
            self.end_game()

    def answer_question(self, answer: str):
        if self.quiz.current_question.check_answer(answer):
            self.update_score(1)
            self.flash_canvas_color((TRUE_BG_COLOR, TRUE_TEXT_COLOR))
        else:
            self.flash_canvas_color((WRONG_BG_COLOR, WRONG_TEXT_COLOR))

        self.window.after(501, self.set_question)

    def flash_canvas_color(self, color: tuple[str, str]):
        """Change canvas bg color and font color for 500ms and change back to default color"""
        self.canvas["bg"] = color[0]
        self.canvas.itemconfigure(self.question_text, fill=color[1])
        self.window.after(500, self.reset_canvas_color)

    def reset_canvas_color(self):
        """Change canvas bg color back to CANVAS_BG_COLOR and canvas font color to QUESTION_COLOR"""
        self.canvas["bg"] = CANVAS_BG_COLOR
        self.canvas.itemconfigure(self.question_text, fill=QUESTION_COLOR)

    def update_score(self, score: int):
        """Add current score with new score and update the score text"""
        self.score += score
        self.score_text["text"] = f"Score:{self.score}"
