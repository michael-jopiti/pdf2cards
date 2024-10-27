
class Card:
    ''' Card object:
        - question
        - answer
        - reference to summary point of extraction'''

    def __init__(self, question, answer, references):
        self.question = question
        self.answer = answer
        self.references = references

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_references(self):
        return self.references

    def __str__(self):
        ''' Return a string representation of the Card'''
        return f"Question: {self.question},\nAnswer: {self.answer},\nReferences: {self.references}"
