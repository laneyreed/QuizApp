# Version 1: MVP (Minimum Viable Product)

### Location
[mvp/](mvp/)

### Description
The MVP is a command-line quiz application with questions hardcoded directly in the Python file. This version establishes the foundational structure and core quiz functionality.

### Key Features
- **Command-line interface**: Simple text-based interaction
- **Fixed question set**: Questions are hardcoded in the `main.py` file
- **Sequential questioning**: All questions are presented in order
- **Immediate feedback**: Users get instant feedback on their answers
- **Final score**: Displays total score at the end of the quiz
- **Input validation**: Ensures users enter valid answers (A, B, C, or D)

### Technical Implementation
- **Language**: Python
- **Data Structure**: Questions stored as a list of dictionaries
- **Answer Format**: Hardcoded questions with predefined answer keys

### Questions Data Model
```python
{
    "question": "Question text here",
    "choices": {
        "A": "Option A",
        "B": "Option B", 
        "C": "Option C",
        "D": "Option D"
    },
    "answer": {"C": "Correct option"}
}
```

### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, if I got the question correct I want to know immediately after responding
- As a user, if I got the question wrong I want to see the correct answer immediately after responding
- As a user, I want to see my score after finishing the quiz

### Files
- `main.py` - Main application file with all quiz logic and questions

---


### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, if I got the question correct I want to know immediately after responding
- As a user, if I got the question wrong I want to see the correct answer immediately after responding
- As a user, I want to see my score after finishing the quiz

### Questions Data Model
- `questions`: a list of question dictionaries
- **Keys:**
    - `question`: value is the question as a string
    - `choices` : a dictionary, representing the multiple-choice options for the question
    - `answer`: a dictionary, representing the correct answer