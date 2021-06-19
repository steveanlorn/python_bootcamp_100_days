from question import Question
from data import question_data
from quiz import Quiz
from ui import UI

question_bank = []
for question in question_data:
    question_bank.append(
        Question(question["question"], question["correct_answer"])
    )

new_quiz = Quiz(question_bank)
quiz_ui = UI(new_quiz)
