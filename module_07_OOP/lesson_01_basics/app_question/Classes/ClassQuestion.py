class Question:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return self.correct_answer == user_answer


class Quiz:
    pass
