# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.


# DEFINE a list of questions and answers
#     - Each question has:
#         * The question text
#         * Possible options (if multiple-choice)
#         * The correct answer

# SET score = 0

# FOR each question in the list:
#     DISPLAY the question (and options if any)
#     GET user input (their answer)
#     IF user input matches the correct answer:
#         INCREASE score by 1
#         (optional: display "Correct!")
#     ELSE:
#         (optional: display "Wrong!")

# AFTER all questions are asked:
#     DISPLAY "You scored X out of Y"




questions = [
    {
        "question": "1. What is 2 + 2?",
        "options": {"a": "3", "b": "4", "c": "5", "d": "6"},
        "answer": "b"
    },
    {
        "question": "2. What color is the sky on a clear day?",
        "options": {"a": "Red", "b": "Blue", "c": "Green", "d": "Yellow"},
        "answer": "b"
    },
    {
        "question": "3. How many legs does a spider have?",
        "options": {"a": "6", "b": "7", "c": "8", "d": "9"},
        "answer": "c"
    },
    {
        "question": "4. What sound does a cow make?",
        "options": {"a": "Meow", "b": "Bark", "c": "Moo", "d": "Quack"},
        "answer": "c"
    },
    {
        "question": "5. What is the opposite of 'hot'?",
        "options": {"a": "Warm", "b": "Cold", "c": "Cool", "d": "Boiling"},
        "answer": "b"
    }
    ]



print("Welcome to the CBT!\nSelect the correct option (a, b, c, d).\n")

def ask_questions(q: dict[str, str]):
    print(q["question"])
    for key, text in q["options"].items():
        print(f" {key}) {text}")


    while True:
        response = input("Your answer (a / b / c / d): ").strip().lower()
        if response in ["a", "b", "c", "d"]:
            break
        print("Invalid choice. Please enter a, b, c, or d.")


    if response == q["answer"]:
        return True
    else:
        return False

score = 0
for q in questions:
    if ask_questions(q):
        score += 1


total = len(questions)
percent = (score / total) * 100

print(f"Your score: {score} out of {total} ({(score/total) * 100:.0f}%)")