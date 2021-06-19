import html


class Question:
    def __init__(self, text: str, answer: str):
        self.text = html.unescape(text)
        self.answer = answer

    def check_answer(self, answer: str) -> bool:
        if self.answer.lower() == answer.lower():
            return True
        return False
