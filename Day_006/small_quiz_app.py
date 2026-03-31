import threading
import time

questions = [
    {"q": "Capital of Nepal?", "options": ["Kathmandu", "Delhi", "Beijing"], "ans": "Kathmandu"},
    {"q": "Which language is used for Data Science?", "options": ["Python", "HTML", "CSS"], "ans": "Python"},
    {"q": "2 + 2 = ?", "options": ["3", "4", "5"], "ans": "4"},
    {"q": "Father of computers?", "options": ["Charles Babbage", "Newton", "Einstein"], "ans": "Charles Babbage"},
    {"q": "Keyword to create function?", "options": ["func", "def", "create"], "ans": "def"},
    {"q": "Which loop runs fixed times?", "options": ["for", "while", "if"], "ans": "for"},
    {"q": "Python comment symbol?", "options": ["//", "#", "/*"], "ans": "#"},
    {"q": "10 / 2 = ?", "options": ["2", "5", "10"], "ans": "5"},
    {"q": "Which data type stores multiple items?", "options": ["list", "int", "float"], "ans": "list"},
    {"q": "Function for user input?", "options": ["print()", "input()", "len()"], "ans": "input()"}
]

score = 0
user_answer = None


def take_input():
    global user_answer
    user_answer = input("Enter your answer: ").strip()


for i, question in enumerate(questions, start=1):
    user_answer = None

    print(f"\nQuestion {i}: {question['q']}")
    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")

    input_thread = threading.Thread(target=take_input)
    input_thread.start()

    for remaining in range(10, 0, -1):
        print(f"Time left: {remaining} sec", end="\r")
        time.sleep(1)

        if user_answer is not None:
            break

    print()

    if user_answer is None:
        print("Time's up")
        print("Correct answer:", question["ans"])
        continue

    if user_answer.lower() == question["ans"].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct answer:", question["ans"])

print(f"\nQuiz Finished")
print(f"Your score: {score}/{len(questions)}")