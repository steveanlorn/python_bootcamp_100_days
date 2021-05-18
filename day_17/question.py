class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, answer):
        if self.answer.lower() == answer.lower():
            return True
        return False
