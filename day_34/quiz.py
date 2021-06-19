from question import Question


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.question_number = 1
        self.current_question = self.questions[0]

    def next_question(self):
        self.current_question = self.questions[self.question_number]
        self.question_number += 1

    def is_still_has_question(self) -> bool:
        if self.question_number < len(self.questions):
            return True
        return False
