import streamlit as st
import random as ran
import json

# Initialize session state variables
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = {}

if 'button_label' not in st.session_state:
    st.session_state.button_label = "Start Quiz"


if 'start_quiz' not in st.session_state:
    st.session_state.start_quiz = False
#=========================================================

st.title("Quiz App")

# Read JSON file and return data
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        st.error(f"{file_path} not found. Please ensure the file exists and is in the correct location.")
        return None


# Get data from JSON file and store in session state
def shuffle_and_start_quiz():
    
    st.session_state.start_quiz = not st.session_state.start_quiz

    # Toggle the button label based on the start_quiz state
    if st.session_state.start_quiz:
        st.session_state.button_label = "Try Again"
    else:
        st.session_state.button_label = "Start Quiz"
    
    # Read and shuffle the questions from the JSON file
    questions = read_json_file("questions.json")
    ran.shuffle(questions)

    # Store the shuffled questions in session state
    st.session_state.shuffled_questions = questions

    return st.session_state.shuffled_questions

# Format the correct answer for comparison
def format_correct_answer(question_data):
    # Format the correct answer as a string
    for key, value in question_data["answer"].items():
        answer = f"{key}. {value}"
    return answer

# Format the choice list for display
def format_choice_list(question_data):
    # Create a list of choices as strings 
    choices_list = [f"{key}. {value}" for key, value in question_data["choices"].items()]
    # ran.shuffle(choices_list)
    return choices_list

# Display the question and choices using st.radio
def display_questions(question, choices_list, count):
    answer = st.radio(f"Question {count}.  {question}", choices_list, index=None, key=f"question_{count}")
    return answer

# Function to format and display questions
def format_questions(questions):

    # Count is for the question number
    count = 0
    user_answers = []
    correct_answers = []
    for question_data in questions:
        count += 1
        # Get the question text from the question_data dictionary
        question = question_data["question"]

        # Create a list of choices with random order
        choices_list = format_choice_list(question_data)
     
        # Format the correct answer and append to the correct_answers list for comparison
        answer = format_correct_answer(question_data)
        correct_answers.append(answer)

        # Display the question and choices and store the user's answer
        answer = display_questions(question, choices_list, count)
        user_answers.append(answer)

        # Store the user's answers and correct answers in session state
        st.session_state.user_answers = user_answers
        st.session_state.correct_answers = correct_answers

        # st.write(answer)

def score_quiz():
    score = 0
    question_count = len(st.session_state.shuffled_questions)
    for index in range(question_count):
        if st.session_state.user_answers[index] == st.session_state.correct_answers[index]:
            score += 1
    st.write(f"Quiz completed! Your score is: {score}/{question_count}")


def show_results():
    question_count = len(st.session_state.shuffled_questions)
    for index in range(question_count):
        if st.session_state.user_answers[index] == st.session_state.correct_answers[index]:
            st.write(f"Question {index + 1}: Correct!")
            st.write(f"Answer: {st.session_state.user_answers[index]}")
        else:
            st.write(f"Question {index + 1}: Incorrect!")
            st.write(f"Your answer: {st.session_state.user_answers[index]}")
            st.write(f"Correct answer: {st.session_state.correct_answers[index]}")
#============================================================================================================

if st.session_state.start_quiz:
    with st.form(key="quiz_form"):
        st.write("Welcome to the Quiz!"
                 "\n\nPlease select your answers below and click 'Submit' when you are done.")
        st.write("Good luck!")

        # Call the function to format and display questions
        format_questions(st.session_state.shuffled_questions)

        # Display the submit button for the quiz form
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        score_quiz()
        st.button("Show Results", on_click=show_results)


# Display the start/try again button
st.button(st.session_state.button_label, on_click=shuffle_and_start_quiz)

# st.write("Button state:", st.session_state.start_quiz)



