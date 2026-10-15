from pathlib import Path

import streamlit as st


def load_trusted_dataset_summary():
    summary_path = Path(__file__).with_name("dataset_summary.txt")
    return summary_path.read_text(encoding="utf-8").strip()


st.title("Manila Rain Frequency Assistant")
st.write(
    "Ask questions about the cleaned weather dataset "
    "and its predictive model."
)

dataset_summary = load_trusted_dataset_summary()

question = st.text_input(
    "Ask a question about the dataset"
)

if st.button("Ask"):
    if question.strip():
        with st.spinner("Analyzing the dataset..."):
            from rain_controller import answer_question

            response = answer_question(
                question,
                dataset_summary
            )
        st.write(response)