from json import load
import random as ran


# Load questions from JSON file
with open('datafromfile/questions.json', 'r') as file:
    questions = load(file)


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
    print("Choices:")
    for key, value in choices.items(): 
        print(f"  {key}: {value}")

def start_quiz():
    count = 0
    print("Welcome to the Quiz!\n")
    for _ in range(len(questions)):
        count += 1
        question_data = ran.choice(questions)
        question_index = questions.index(question_data)
        question = question_data["question"]

        print(f"Question {count}:")
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