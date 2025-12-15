import streamlit as st
import random as ran
import json

#=========================================================
# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = {}

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = []


if 'button_label' not in st.session_state:
    st.session_state.button_label = "Start Quiz"


if 'start_quiz' not in st.session_state:
    st.session_state.start_quiz = False
#=========================================================



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
    # Toggle the button_label state to the opposite value
    st.session_state.start_quiz = not st.session_state.start_quiz

    if st.session_state.start_quiz:
        st.session_state.button_label = "Restart Quiz"
    else:
        st.session_state.button_label = "Start Quiz"
    
    
    questions = read_json_file("questions.json")
    ran.shuffle(questions)
    st.session_state.questions = questions
    return st.session_state.questions

# Format the correct answer for comparison
def format_correct_answer(question_data):
    for key, value in question_data["answer"].items():
        answer = f"{key}. {value}"
    return answer

# Format the choice list for display
def format_choice_list(question_data):
    choices_list = [f"{key}. {value}" for key, value in question_data["choices"].items()]
    # ran.shuffle(choices_list)
    return choices_list

def display_questions(question, choices_list, count):
    answer = st.radio(f"Question {count}.  {question}", choices_list, index=None, key=f"question_{count}")
    return answer

# Function to format and display questions
def format_questions(questions):
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

        st.write(answer)
    # st.write(st.session_state.user_answers)
    # st.write(st.session_state.correct_answers)





#============================================================================================================

if st.session_state.start_quiz:
    with st.form(key="quiz_form"):
        # Call the function to format and display questions
        format_questions(st.session_state.questions)
        submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.write("Form submitted!")
        st.write("User answers:", st.session_state.user_answers)
        st.write("Correct answers:", st.session_state.correct_answers)

st.button(st.session_state.button_label, on_click=shuffle_and_start_quiz)

st.write("Button state:", st.session_state.start_quiz)









# st.title("Quiz App")
# st.write("Welcome to my Streamlit app!")


# if "questions" not in st.session_state:
#     st.session_state.questions = {}

# if "shuffled_questions" not in st.session_state:
#     st.session_state.shuffled_questions = []

# def read_json_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         st.error(f"{file_path} not found. Please ensure the file exists and is in the correct location.")
#         return None



# def start_quiz():
#     count = 0
#     score = 0
#     for question_data in st.session_state.shuffled_questions:
#         count += 1
#         question_index = st.session_state.shuffled_questions.index(question_data)
#         question = question_data["question"]
#         choices = question_data["choices"]
#         correct_answer = question_data["answer"]

#         # Create a list of choices with random order
#         choices_list = list(choices.values())
#         ran.shuffle(choices_list)

#         # Display the question and choices
#         st.write(f"Question {count}: {question}")
#         answer = st.radio("Select your answer:", choices_list, index=None, key=f"question_{count}")

#         # Check if the user's answer is correct
#         if answer == correct_answer:
#             score += 1
#             st.write("Correct!")
#         else:
#             st.write(f"Incorrect! The correct answer is: {correct_answer}")

#     # Display the final score
#     st.write(f"Quiz completed! Your score is: {score}/{count}")



# @st.fragment
# def shuffle_data(data):
#     print("Shuffling data...")
#     if st.button("Start Quiz", on_click=start_quiz, key="start_button"):
#         ran.shuffle(data)
#         st.session_state.shuffled_questions = data
#         print("Data shuffled and stored in session state.")
#         print(st.session_state.shuffled_questions)
    



# data = get_data()
# print("Original Questions:", st.session_state.questions)
# shuffle_data(data)
# print(st.session_state.questions)

# if "shuffled_questions" in st.session_state:
#     with st.form(key="quiz_form"):
        
#         start_quiz()
            
#         submit_button = st.form_submit_button(label="Submit")






# def show_new_quiz():
#     count = 0
#     for question_data in st.session_state.questions:
#         count += 1
#         question_index = st.session_state.questions.index(question_data)
#         question = question_data["question"]
        

        # #=====================================================================================================
        # # list comprehension to create a list of choices
        # choices_list = [f"{key}. {value}" for key, value in question_data["choices"].items()]
        # # print(choices_list)
        # #=====================================================================================================
        # # #for loop through the choices and print them out, does the same as the list comprehension above
        # #     for item in question_data["choices"].items():
        # #         choice = f" {item[0]}. {item[1]}"
        # #         choices_list.append(choice)
        # #         st.write(choice)
        # #======================================================================================================

        # answer = st.radio(f"Question {count}.  {question}", choices_list, index=None, key=f"question_{count}")



# def show_choices(choices):
#     for key, value in choices.items(): 
#         st.markdown(f"<p style='margin-left: 40px;'>{key}: {value}</p>", unsafe_allow_html=True)






# 
# 


# score = 0
# question_list = []
# st.write("Welcome to the Quiz!\n")

# print(st.session_state.questions)




# def get_quiz():
#     count = 0
#     for question_data in st.session_state.questions:
#         count += 1
#         question_index = st.session_state.questions.index(question_data)
#         question = question_data["question"]
        

#         #=====================================================================================================
#         # list comprehension to create a list of choices
#         choices_list = [f"{key}. {value}" for key, value in question_data["choices"].items()]
#         print(choices_list)
#         #=====================================================================================================
#         # #for loop through the choices and print them out, does the same as the list comprehension above
#         #     for item in question_data["choices"].items():
#         #         choice = f" {item[0]}. {item[1]}"
#         #         choices_list.append(choice)
#         #         st.write(choice)
#         #======================================================================================================

#         question_list.append(question)
#     return question_list
#         #======================================================================================================
# questions = get_quiz()

# print(question_list)
# # 
# # st.write(answer)

# my_answer = st.radio("choose your favorite color", ("Blue", "Red", "Green", "Purple"), index=None)
# st.write(my_answer)

















# def start_quiz():
#     count = 0
#     score = 0
#     print("Welcome to the Quiz!\n")
#     ran.shuffle(questions)
#     for question_data in questions:
#         count += 1
#         question_index = questions.index(question_data)
#         question = question_data["question"]




# # Option B: Allowing a user to upload a file
# uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])
# if uploaded_file is not None:
#     # Read the file and convert to JSON
#     input_data = json.load(uploaded_file)
#     st.write("Data from uploaded file:")
#     st.json(input_data)