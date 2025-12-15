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