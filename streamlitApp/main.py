import streamlit as st
import random as ran
import json

st.title("Quiz App")
st.write("Welcome to my Streamlit app!")


# Option A: Reading a pre-existing local file
# Replace 'your_file.json' with the path to your JSON file

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        st.error(f"{file_path} not found. Please ensure the file exists and is in the correct location.")
        return None

def show_choices(choices):
    for key, value in choices.items(): 
        st.markdown(f"<p style='margin-left: 40px;'>{key}: {value}</p>", unsafe_allow_html=True)











questions = read_json_file("questions.json")
ran.shuffle(questions)
# st.json(questions)
count = 0
score = 0

st.write("Welcome to the Quiz!\n")
for question_data in questions:
    count += 1
    question_index = questions.index(question_data)
    question = question_data["question"]
    st.text(f"Question {count}.  {question}")
    show_choices(question_data["choices"])




















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