import pkg_resources
import json
import random

# returns a list of questions
def load_questions():
    path = pkg_resources.resource_filename('quiz', 'data/questions.json')
    file = open(path)
    text = file.read()
    questions = json.loads(text)
    file.close()
    return questions
    
def run():
    questions = load_questions()
    question = questions[random.randint(0, len(questions) - 1)]
    print(question["question_text"])
    i = 1
    for o in question["options"]:
        print(f"{i}: {o}")
        i += 1
    answer_i = i + 1
    print(f"{answer_i}: {question['answer']}")

    inp = int(input(">"))
    if inp == answer_i:
        print("correct!")
    elif inp < 1 or inp > len(question["options"]) + 1:
        print("wrong!")
    else:
        print("bad number")