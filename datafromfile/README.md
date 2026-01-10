# Version 2: Data from File

### Location
[datafromfile/](datafromfile/)

### Description
This version improves upon the MVP by reading questions from an external JSON file instead of hardcoding them. It also implements random question selection, making the quiz more dynamic.

### Key Features
- **Dynamic question loading**: Questions are loaded from `questions.json` file
- **Random shuffling**: Questions are presented in random order
- **Command-line interface**: Maintains the text-based interaction style
- **Immediate feedback**: Same as MVP - instant response to answers
- **File-based configuration**: Easy to update quiz questions without modifying code

### Technical Implementation
- **Language**: Python
- **Data Source**: External JSON file
- **Question Shuffling**: Uses `random.shuffle()` to randomize question order
- **File I/O**: JSON parsing for loading questions

### Questions Data Model
Same as MVP - questions.json contains a list of question dictionaries with `question`, `choices`, and `answer` keys.

### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, if I got the question correct I want to know immediately after responding
- As a user, if I got the question wrong I want to see the correct answer immediately after responding
- As a user, I want to see my score after finishing the quiz
- *(Added)* Questions should be picked randomly from the available set

### Files
- `main.py` - Main application file with quiz logic
- `questions.json` - External JSON file containing all quiz questions

### Advantages Over MVP
- **Scalability**: Easily add or modify questions without changing code
- **Variety**: Random question selection provides different quiz experiences
- **Maintainability**: Separation of data (questions.json) from logic (main.py)

---



### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, if I got the question correct I want to know immediately after responding
- As a user, if I got the question wrong I want to see the correct answer immediately after responding
- As a user, I want to see my score after finishing the quiz

### Questions Data Model
- `questions`: a list of question dictionaries
    - questions loaded from JSON file
- **Keys:**
    - `question`: value is the question as a string
    - `choices` : a dictionary, representing the multiple-choice options for the question
    - `answer`: a dictionary, representing the correct answer


- Question picked randomly