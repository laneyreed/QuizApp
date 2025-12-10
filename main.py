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



user_answers = []
correct_answers = []

def get_user_answer():
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    if user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        return get_user_answer()
    return user_answer

def get_correct_answer(question_data):
    for key in question_data:
        correct_answer = key
    return correct_answer
    print(f"Correct answer: {correct_answer}\n")

def show_choices(choices):
    # items will give both key and value,
    # if we just say question_data["choices"], it will give only keys
    print("Choices:")
    for key, value in choices.items(): 
        print(f"  {key}: {value}")



def start_quiz():
    print("Welcome to the Quiz!\n")
    for question_data in questions:
        question = question_data["question"]
        print(question)
        # print index
        # print(questions.index(question_data))
        
        show_choices(question_data["choices"])

        user_answer = get_user_answer()
        user_answers.append(user_answer)
        
        correct_answer = get_correct_answer(question_data["answer"])
        correct_answers.append(correct_answer)

        print(f"Correct answer: {correct_answer}\n")
        print(f"Your answer: {user_answer}")

start_quiz()
print("Quiz Completed!")
print("Your Answers:", user_answers)
print("Correct Answers:", correct_answers)