class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")

        if question.check_answer(answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def is_still_has_question(self):
        if self.question_number < len(self.questions):
            return True
        return False
