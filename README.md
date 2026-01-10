# QuizApp

## Overview
This QuizApp project contains three different implementations of a multiple-choice quiz application, each with increasing complexity and user experience enhancements. Each version builds upon lessons learned from the previous one.


## Version Comparison Table

| Feature | MVP | Data from File | Streamlit |
|---------|-----|-----------------|-----------|
| **Interface** | Command-line | Command-line | Web-based |
| **Question Source** | Hardcoded | JSON file | JSON file |
| **Question Order** | Sequential | Random | Random |
| **Immediate Feedback** | ✓ | ✓ | Form-based |
| **Results Review** | ✓ | ✓ | ✓ (detailed) |
| **Retry Quiz** | Manual restart | Manual restart | ✓ (button) |
| **Session Persistence** | None | None | ✓ |
| **Modern UI** | ✗ | ✗ | ✓ |
| **Scalability** | Low | High | High |
| **Deployment** | Local only | Local only | Web-ready |

---

## Version 1: MVP (Minimum Viable Product)
- Python 3.x (standard library only)
### Run MVP Version
```bash
cd mvp
python main.py
```
---

## Version 2: Data from File
- Python 3.x (standard library only)
### MVP → Data from File
**Key Improvements**:
- Separated data from logic
- Enabled question randomization
- Made quiz questions easy to modify

### Run Data from File Version
```bash
cd datafromfile
python main.py
```

---


## Version 3: Streamlit Web Application
- Python 3.x
- Streamlit (see pyproject.toml for specific version)

### Data from File → Streamlit
**Key Improvements**:
- Modernized user interface
- Enhanced user experience
- Added session state management
- Enabled detailed results review
- Simplified retry mechanism
- Made application web-deployable


### Run Streamlit Version
```bash
cd streamlitApp
streamlit run main.py
```

---


## Questions Data Format

All versions use the same JSON structure for questions:

```json
[
    {
        "question": "What is the capital of France?",
        "choices": {
            "A": "London",
            "B": "Berlin",
            "C": "Paris",
            "D": "Madrid"
        },
        "answer": {
            "C": "Paris"
        }
    }
]
```

---

## Future Enhancements

Potential improvements applicable to all versions:
1. User authentication and score tracking
2. Multiple quiz categories
3. Difficulty levels
4. Timed quizzes
5. Question analytics
6. Leaderboard
7. Different question types (true/false, fill-in-the-blank)
8. Question export/import
9. Detailed performance analytics
10. Mobile-responsive design (Streamlit version)

