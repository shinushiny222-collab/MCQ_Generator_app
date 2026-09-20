import streamlit as st
import json
import re
from google import genai

st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="📝",
    layout="centered"
)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
st.title("AI MCQ Generator")
st.write("Generate multiple-choice questions using AI.")

st.divider()

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Python OOP"
)

number = st.slider(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate MCQs"):

    if not topic.strip():
        st.warning("Please enter a topic.")

    else:

        prompt = f"""
Generate {number} multiple-choice questions about "{topic}".

Difficulty: {difficulty}

Return ONLY valid JSON in this format:

[
    {{
        "question": "Question here",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": "Correct option",
        "explanation": "Short explanation"
    }}
]

Rules:
- Generate exactly {number} questions.
- Each question must have exactly 4 options.
- Only one option must be correct.
- The answer must exactly match one of the options.
- Give a short explanation.
- Do not use Markdown.
- Do not add any text outside the JSON.
"""

        with st.spinner("Generating MCQs..."):

            try:

                interaction = client.interactions.create(
                    model="gemini-3.6-flash",
                    input=prompt
                )

                result = interaction.output_text.strip()

                result = re.sub(
                    r"```json|```",
                    "",
                    result
                ).strip()

                questions = json.loads(result)

                st.session_state["questions"] = questions
                st.session_state["topic"] = topic
                st.session_state["submitted"] = False

            except Exception as e:

                st.error("Unable to generate MCQs.")
                st.code(str(e))

if "questions" in st.session_state:

    st.subheader(
        f"MCQ Quiz: {st.session_state['topic']}"
    )

    questions = st.session_state["questions"]

    for i, q in enumerate(questions):

        st.write(f"### Question {i + 1}")

        st.write(q["question"])

        st.radio(
            "Select your answer:",
            q["options"],
            key=f"answer_{i}"
        )

        st.divider()

    if st.button("Submit Quiz"):

        score = 0

        for i, q in enumerate(questions):

            selected = st.session_state.get(
                f"answer_{i}"
            )

            if selected == q["answer"]:
                score += 1

        st.session_state["score"] = score
        st.session_state["submitted"] = True


if st.session_state.get("submitted", False):

    score = st.session_state["score"]
    total = len(st.session_state["questions"])

    st.success(
        f"Your Score: {score} / {total}"
    )

    st.subheader("Answer Review")

    for i, q in enumerate(
        st.session_state["questions"]
    ):

        selected = st.session_state.get(
            f"answer_{i}"
        )

        if selected == q["answer"]:

            st.write(
                f"Question {i + 1}: Correct"
            )

        else:

            st.write(
                f"Question {i + 1}: Incorrect"
            )

            st.write(
                f"Correct Answer: {q['answer']}"
            )

        st.write(
            f"Explanation: {q['explanation']}"
        )

        st.divider()

if st.button("Create New Quiz"):

    st.session_state.clear()
    st.rerun()