import streamlit as st
import random as ran
import json

st.title("Quiz App")
st.write("Welcome to my Streamlit app!")


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

if "questions" not in st.session_state:
    st.session_state.questions = {}


@st.cache_data
def get_data():
    print("Reading data from file...")
    questions = read_json_file("questions.json")
    return questions

@st.fragment
def shuffle_data(data):
    print("Shuffling data...")
    ran.shuffle(data)
    st.session_state.questions = data
    #====================================================================================
    # because you cannot return a value from a fragment, 
    # session_state is used to store the data in the session, 
    # so when this function is called the the questions are automatically available 
    # for the rest of the app using st.session_state.questions
    #====================================================================================   


data = get_data()
shuffle_data(data)



with st.form(key='my_form'):
    count = 0
    score = 0

    st.write("Welcome to the Quiz!\n")
    for question_data in st.session_state.questions:
        count += 1
        question_index = st.session_state.questions.index(question_data)
        question = question_data["question"]
        choices_list = []

        #=====================================================================================================
        # list comprehension to create a list of choices
        choices_list = [f"{key}. {value}" for key, value in question_data["choices"].items()]
        #=====================================================================================================
        # #for loop through the choices and print them out, does the same as the list comprehension above
        #     for item in question_data["choices"].items():
        #         choice = f" {item[0]}. {item[1]}"
        #         choices_list.append(choice)
        #         st.write(choice)
        #======================================================================================================

        question = st.radio(f"Question {count}.  {question}", options=choices_list, index=None)

    submit_button = st.form_submit_button(label='Submit')



















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