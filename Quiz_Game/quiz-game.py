questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A: Paris", "B: London", "C: Berlin", "D: Madrid"],
        "answer": "A",
    },
    {
        "prompt": "What is the largest planet in our Solar System?",
        "options": ["A: Earth", "B: Mars", "C: Jupiter", "D: Saturn"],
        "answer": "C",
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": [
            "A: Harper Lee",
            "B: J.K. Rowling",
            "C: Mark Twain",
            "D: Ernest Hemingway",
        ],
        "answer": "A",
    },
    {
        "prompt": "Which element has the chemical symbol 'O'?",
        "options": ["A: Gold", "B: Oxygen", "C: Osmium", "D: Silver"],
        "answer": "B",
    },
    {
        "prompt": "What is the main ingredient in guacamole?",
        "options": ["A: Tomato", "B: Avocado", "C: Pepper", "D: Onion"],
        "answer": "B",
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A: China", "B: South Korea", "C: Japan", "D: Thailand"],
        "answer": "C",
    },
]

def runQuiz(questions):
  score = 0
  questionNumber = 1
  x = " "
  for question in questions:
    qPrompt = question["prompt"]
    print(str(questionNumber) + ". " + qPrompt)
    questionNumber += 1
    for option in question["options"]:
      print(str(3*x) + option)
    answer = input("Enter your answer (A, B, C, or D): ")
    if(answer.upper() == question["answer"]):
      print("Correct!")
      score += 1
    else:
      print("Incorrect. The correct answer was ", question["answer"])
    print()
  print(f"You got {score} out of {len(questions)} questions correct.") 

runQuiz(questions)