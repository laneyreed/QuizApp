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


def get_user_answer(question_index):
    user_answer = input("Enter Your answer (A, B, C, D): ").strip().upper()
    if user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        return get_user_answer(question_index)
    return {question_index: user_answer}

def get_correct_answer(question_data, question_index):
    for key in question_data:
        correct_answer = key
    return {question_index : correct_answer}

def show_choices(choices):
    # items will give both key and value,
    # if we just say question_data["choices"], it will give only keys
    print("Choices:")
    for key, value in choices.items(): 
        print(f"  {key}: {value}")

def start_quiz():
    print("Welcome to the Quiz!\n")
    for question_data in questions:
        question_index = questions.index(question_data)
        print(f"Question {question_index}:")
        question = question_data["question"]
        print(question)
        
        show_choices(question_data["choices"])

        user_answer = get_user_answer(question_index)
        user_answers.append(user_answer)
        
        correct_answer = get_correct_answer(question_data["answer"], question_index)
        correct_answers.append(correct_answer)

def check_answers():
    score = 0
    for i in range(len(user_answers)):
        if user_answers[i] == correct_answers[i]:
            score += 1
    print(f"Your total score is: {score}/{len(questions)}")

def main():
    start_quiz()
    check_answers()
    print("Quiz Completed!")

if __name__ == "__main__":
    main()