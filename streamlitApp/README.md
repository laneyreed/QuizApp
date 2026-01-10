# Quiz App Version 3: Streamlit Web Application

### Location
[streamlitApp/](streamlitApp/)

### Description
The most advanced version uses Streamlit to create an interactive web-based quiz application. This provides a modern, user-friendly interface with improved UX/UI and enhanced functionality.

### Key Features
- **Web-based interface**: Modern, interactive web UI using Streamlit
- **Session state management**: Maintains user progress and answers across interactions
- **Question shuffling**: Random question order for variety
- **Interactive buttons**: Intuitive "Start Quiz" and "Try Again" buttons
- **Results display**: Option to view detailed results showing correct/incorrect answers
- **Score calculation**: Automatic score computation and display
- **Radio button selection**: Clean answer selection using radio buttons
- **Form submission**: Quiz answers submitted together rather than one by one

### Technical Implementation
- **Framework**: Streamlit
- **Language**: Python
- **State Management**: Streamlit session state for persistent data
- **Data Source**: External JSON file (questions.json)
- **Frontend**: Automatically generated web interface

### Questions Data Model
Same as previous versions - questions.json contains a list of question dictionaries.

### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, I want to see my score after finishing the quiz
- As a user, I want to have the choice to view the quiz results with correct and incorrect answers
- *(Improved)* I want a modern, visually appealing interface
- *(Improved)* I want to retake the quiz easily with a "Try Again" button

### Key Components

#### Core Functions
- `read_json_file()` - Reads and parses the questions.json file
- `shuffle_and_start_quiz()` - Initializes quiz with shuffled questions and manages session state
- `format_correct_answer()` - Formats answers for comparison
- `format_choice_list()` - Converts choices to displayable format
- `display_questions()` - Renders question with radio button options
- `format_questions()` - Iterates through all questions and captures user responses
- `score_quiz()` - Calculates final score
- `show_results()` - Displays detailed feedback for each question

#### Session State Variables
- `shuffled_questions` - Store shuffled question list
- `button_label` - Track current button text ("Start Quiz" or "Try Again")
- `start_quiz` - Boolean to toggle quiz display state
- `user_answers` - Store all user responses
- `correct_answers` - Store correct answers for comparison

### Files
- `main.py` - Main Streamlit application
- `questions.json` - External JSON file containing all quiz questions
- `pyproject.toml` - Project configuration and dependencies

### How to Run
```bash
streamlit run main.py
```

### Known Issues & Planned Improvements
- **Known Issue**: Results are displayed above the test instead of below
- **Planned Features**:
  - Add a timer for the entire quiz
  - Add options to choose quiz type (e.g., multiple choice, true/false)
  - Add difficulty levels (easy, medium, hard)
  - Add quiz categories (history, science, technology, etc.)

### Advantages Over Data from File
- **Modern UI**: Web-based interface instead of command-line
- **Better UX**: Interactive elements and visual feedback
- **Easier to use**: No command-line knowledge required
- **Scalable**: Can be hosted online for wider access
- **Extended functionality**: Results review, retry capability

---



### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, I want to see my score after finishing the quiz
- As a user, I want to have the choice to view the quiz results with correct and incorrect answers

### Questions Data Model
- `questions`: a list of question dictionaries
    - questions loaded from JSON file
- **Keys:**
    - `question`: value is the question as a string
    - `choices` : a dictionary, representing the multiple-choice options for the question
    - `answer`: a dictionary, representing the correct answer


### App Functionality
- Simple quiz app built using Streamlit
- Reads questions and answers from a JSON file
- Shuffles the questions
- Presents the user with a series of multiple-choice questions
- User can submit their answer
- App will display their score and provide feedback on each question
- User can also try the quiz again by clicking the "Try Again" button

### App Fixes
- when the show results button is clicked, the app displays the correct answer and the user's answer for each question
    - but it is displayed above the test instead of below the test

### 
- add a timer for the entire quiz
- add options to choose quiz type (e.g., multiple choice, true/false)
- add options to choose quiz difficulty (e.g., easy, medium, hard)
- add options to choose quiz category (e.g., history, science, technology)



