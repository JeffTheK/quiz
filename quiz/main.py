import pkg_resources
import json

class Question:
    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = options
        self.answer = answer

# returns a list of questions
def load_questions():
    path = pkg_resources.resource_filename('quiz', 'data/questions.json')
    file = open(path)
    text = file.read()
    questions = json.loads(text)
    file.close()
    return questions
    
def run():
    quesstions = load_questions()
    print("hello world")