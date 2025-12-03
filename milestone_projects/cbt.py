question_one = """1. What is 2 + 2?
a) 3
b) 4
c) 5
d) 6
"""

question_two = """What color is the sky on a clear day?
a) Red
b) Blue
c) Green
d) Yellow"""


question_three = """How many legs does a spider have?
a) 6
b) 7
c) 8
d) 9
"""


question_four = """What sound does a cow make?
a) Meow
b) Bark
c) Moo
d) Quack"""


question_five = """What is the opposite of 'hot'?
a) Warm
b) Cold
c) Cool
d) Boiling"""


question_bank = [
    {
        "question": question_one,
        "correct_answer": "b"
    },
    {
        "question": question_two,
        "correct_answer": "b"
    },
    {
        "question": question_three,
        "correct_answer": "c"
    },
    {
        "question": question_four,
        "correct_answer": "c"
    },
    {
        "question": question_five,
        "correct_answer": "b"
    },
]


score = 0

for question in question_bank:
    print(question["question"])

    response = input("Enter an option from a to d: ").strip().lower()

    if response == question["correct_answer"]:
        score += 1
    
print(f"At the end of the CBT exam, you scored {score} out of {len(question_bank)} points.")