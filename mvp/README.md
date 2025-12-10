
### User Stories
- As a user, I want to answer multiple-choice questions one by one
- As a user, I want to see my score and correct answers immediately after finishing

### Questions Data Model
- `questions`: a list of question dictionaries
- **Keys:**
    - `question`: value is the question as a string
    - `choices` : a dictionary, representing the multiple-choice options for the question
    - `answer`: a dictionary, representing the correct answer