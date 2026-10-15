import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"]
)

deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]

def answer_question(question, dataset_summary):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a weather-data analysis assistant. "
                    "Answer only from the supplied dataset summary. "
                    "Do not invent statistics. If the information "
                    "is missing, state that it is unavailable. "
                    "Distinguish association from causation."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Dataset summary:\n{dataset_summary}\n\n"
                    f"Question: {question}"
                )
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content