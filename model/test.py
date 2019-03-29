class Question:
    def __init__(self, question, points, sub=False):
        self.question = question
        self.points = points
        self.sub = sub

    def get_num_questions(self):
        raise Exception('get_num_questions not implemented')


class ShortQuestion(Question):
    def __init__(self, question, points, choices, sub=False):
        super().__init__(question, points, sub=sub)
        self.choices = choices

    def get_num_questions(self):
        return len(self.choices)


class MediumQuestion(Question):
    def __init__(self, question, points, choices, sub=False):
        super().__init__(question, points, sub=sub)
        self.choices = choices

    def get_num_questions(self):
        return len(self.choices)


class LongQuestion(Question):
    def __init__(self, question, points, choices, translation=False, num_answer_lines=1, sub=False):
        super().__init__(question, points, sub=sub)
        self.choices = choices
        self.translation = translation
        self.num_answer_lines = num_answer_lines

    def get_num_questions(self):
        return len(self.choices)


class FreeFormQuestion(Question):
    def __init__(self, question, points, choices, numbered=True):
        super().__init__(question, points)
        self.choices = choices
        self.numbered = numbered

    def get_num_questions(self):
        return len(self.choices)


class PictureQuestion(Question):
    def __init__(self, question, points, picture, choices):
        super().__init__(question, points)
        self.picture = picture
        self.choices = choices

    def get_num_questions(self):
        return len(self.choices)


class EssayQuestion(Question):
    def __init__(self, question, points, answer_lines, sub=False):
        super().__init__(question, points, sub=sub)
        self.answer_lines = answer_lines

    def get_num_questions(self):
        return 1


class TranslationQuestion(Question):
    def __init__(self, question, points, passage, fill_in_the_blanks):
        super().__init__(question, points)
        self.passage = passage
        self.fill_in_the_blanks = fill_in_the_blanks

    def get_num_questions(self):
        return self.fill_in_the_blanks.count('()')


class DialogueQuestion(Question):
    def __init__(self, question, points, dialogues, sub=False):
        super().__init__(question, points, sub=sub)
        self.dialogues = dialogues

    def get_num_questions(self):
        return len(self.dialogues)


class Dialogue:
    def __init__(self, lines, question):
        self.lines = lines
        self.question = question


class TableQuestion(Question):
    def __init__(self, question, points, x_headers, y_headers, sub=False):
        super().__init__(question, points, sub=sub)
        self.x_headers = x_headers
        self.y_headers = y_headers

    def get_num_questions(self):
        return len(self.x_headers) * len(self.y_headers)


class Test:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
