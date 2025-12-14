
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