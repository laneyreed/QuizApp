questions = [
    {
        "question": "What is the capital of France?",
        "choices": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
        "answer": {"C": "Paris"}
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices":{"A": "Vincent van Gogh", "B": "Leonardo da Vinci", "C": "Pablo Picasso", "D": "Claude Monet"},
        "answer": {"B": "Leonardo da Vinci"}
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
        "answer": {"C": "Jupiter"}
    }
]

def get_user_answer():
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    if user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        return get_user_answer()
    return user_answer

user_answers = []
correct_answers = []
for question_data in questions:
    print(question_data["question"])
    # print index
    print(questions.index(question_data))
    print("Choices:")
    # items will give both key and value,
    # if we just say question_data["choices"], it will give only keys
    for key, value in question_data["choices"].items(): 
        print(f"  {key}: {value}")
    user_answer = get_user_answer()
    print(f"Your answer: {user_answer}")
    for key in question_data["answer"]:
        correct_answer = key
        correct_answers.append(correct_answer)
    print(f"Correct answer: {correct_answer}\n")
    user_answers.append(user_answer)

print("Quiz Completed!")
print("Your Answers:", user_answers)
print("Correct Answers:", correct_answers)
    












    # for key, value in question_data["choices"].items():
    #     print(f"  {key}: {value}")
    # user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    
    # if user_answer in question_data["answer"]:
    #     print("Correct!\n")
    # else:
    #     correct_key = list(question_data["answer"].keys())[0]
    #     correct_value = question_data["answer"][correct_key]
    #     print(f"Wrong! The correct answer is {correct_key}: {correct_value}\n")