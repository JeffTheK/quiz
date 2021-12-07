import pkg_resources
import json
import random
from colorama import Fore, Style

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
    answer_i = i
    print(f"{answer_i}: {question['answer']}")

    inp = int(input(">"))
    if inp == answer_i:
        print(f"{Fore.GREEN}correct!{Style.RESET_ALL}")
    elif inp > 0 and inp <= len(question["options"]) + 1:
        print(f"{Fore.RED}wrong!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}bad number{Style.RESET_ALL}")