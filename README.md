# MCQ_Generator_app

## Project Overview

AI MCQ Generator is a Streamlit-based web application that uses Generative AI to automatically create multiple-choice questions from any topic entered by the user.

The application allows users to select the number of questions and difficulty level, generate AI-based MCQs, attend the quiz, and view their score with answer explanations.

## Features

* Generate MCQs automatically using AI
* Enter any topic
* Choose the number of questions
* Select difficulty level
* Four options for each question
* Submit answers and calculate score
* View correct answers
* View explanations for each question
* Create a new quiz

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google Gen AI SDK
* JSON

## Project Structure

```text
AI-MCQ-Generator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd AI-MCQ-Generator
```

### 3. Install Required Packages

```bash
python -m pip install -r requirements.txt
```

## API Key Configuration

Create a folder named `.streamlit` inside the project folder.

Create a file named:

```text
secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Do not upload your API key to GitHub.

Add `.streamlit/secrets.toml` to `.gitignore`.

## Run the Application

Run the following command in the terminal:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## How to Use

1. Enter a topic in the topic field.
2. Select the number of questions.
3. Select the difficulty level.
4. Click `Generate MCQs`.
5. Answer the generated questions.
6. Click `Submit Quiz`.
7. View your score and answer explanations.
8. Click `Create New Quiz` to start another quiz.

## Example

### Topic

```text
AI-Powered Smart Cities
```

### Number of Questions

```text
5
```

### Difficulty

```text
Medium
```

The application automatically generates MCQs based on the selected topic.

## Application Workflow

```text
User Input
    ↓
Topic Selection
    ↓
Number of Questions
    ↓
Difficulty Selection
    ↓
Gemini AI
    ↓
MCQ Generation
    ↓
User Answers
    ↓
Quiz Submission
    ↓
Score and Explanation
```

## Future Enhancements

* Add more difficulty levels
* Add timer-based quizzes
* Add question categories
* Store quiz history
* Add leaderboard
* Add downloadable quiz reports
* Add user login
* Add database integration

## Author

Aseniya Shiny

BSc Computer Science with Artificial Intelligence
