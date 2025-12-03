# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.


# Exam Wizard Program

questions = [
    {
        "question": "1. Explain the process of photosynthesis.",
        "keywords": {"sunlight": 2, "chlorophyll": 2, "carbon dioxide": 1, "oxygen": 1, "glucose": 2}
    },
    {
        "question": "2. What are the main functions of the human heart?",
        "keywords": {"pump": 2, "blood": 2, "oxygen": 1, "circulation": 2}
    },
    {
        "question": "3. Describe the water cycle.",
        "keywords": {"evaporation": 2, "condensation": 2, "precipitation": 2, "collection": 1}
    },
    {
        "question": "4. What are the benefits of exercise?",
        "keywords": {"health": 1, "fitness": 2, "strength": 1, "endurance": 1, "mental": 2}
    },
    {
        "question": "5. Explain the importance of education.",
        "keywords": {"knowledge": 2, "skills": 2, "opportunity": 1, "development": 2, "future": 1}
    }
]

def evaluate_answer(answer, keywords):
    score = 0
    answer = answer.lower()
    for word, weight in keywords.items():
        if word in answer:
            score += weight
    return score

def run_exam():
    total_score = 0
    max_score = sum(sum(q["keywords"].values()) for q in questions)

    print("Welcome to the Exam Wizard!\nProvide detailed answers. Keywords matter!\n")

    for q in questions:
        print(q["question"])
        user_answer = input("Your answer: ")
        earned = evaluate_answer(user_answer, q["keywords"])
        total_score += earned
        print(f"Score for this question: {earned}/{sum(q['keywords'].values())}\n")

    print("=== Exam Finished ===")
    print(f"Your total score: {total_score}/{max_score}")


run_exam()
