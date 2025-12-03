question_bank = [
    {
        "question": "What is Photosynthesis?",
        "keywords": {"Photosynthesis": 2, "Light energy": 1, "Chemical energy": 1, "Chloroplasts": 2, "Chlorophyll": 1, "Carbon dioxide": 1, "Water": 1, "Glucose": 1, "Oxygen": 1, "ATP": 1},
    },
    {
        "question": "What is Newton's First Law of Motion?",
        "keywords": {
            "Inertia": 2, 
            "Constant velocity": 1, 
            "External force": 1, 
            "Rest": 1, 
            "Motion": 1, 
            "Net force": 1
        },
    },
    {
        "question": "What is an Operating System?",
        "keywords": {
            "Operating System": 2, 
            "Resource management": 1, 
            "Process management": 1, 
            "Memory management": 1, 
            "File system": 1, 
            "Interface": 1, 
            "Kernel": 1
        },
    },
    {
        "question": "What is Supply and Demand?",
        "keywords": {
            "Supply": 2,
            "Demand": 2,
            "Market equilibrium": 1,
            "Price": 1,
            "Quantity": 1,
            "Consumer behavior": 1,
            "Producer behavior": 1
        },
    },
    {
        "question": "What is DNA Replication?",
        "keywords": {
            "DNA replication": 2,
            "Nucleotides": 1,
            "Double helix": 1,
            "Enzymes": 1,
            "Helicase": 1,
            "DNA polymerase": 1,
            "Semi-conservative": 1
        },
    }
]

total_score = 0

max_score = 0

for question in question_bank:
    print(question["question"])

    response = input("Enter your answer here: ").lower()

    for keyword, weight in question["keywords"].items():
        if keyword.lower() in response:
            total_score += weight
        max_score += weight


print(f"Total Score: {total_score} out of {max_score} points")