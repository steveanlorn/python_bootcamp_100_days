from question import Question
from data import question_data
from quiz import Quiz

question_bank = []
for question in question_data:
    question_bank.append(
        Question(question["question"], question["correct_answer"])
    )

new_quiz = Quiz(question_bank)

while new_quiz.is_still_has_question():
    new_quiz.next_question()

print("You've finished the quiz")
print(f"Total score is: {new_quiz.score}/{new_quiz.question_number}")
