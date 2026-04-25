import json
from pydantic_ai import Agent

from src.groq_setup import MODEL
from src.prompts import PROMPT
from src.model import CandidateEvaluation
from src.file_handler import save_data

agent = Agent(
    model=MODEL,
    system_prompt=PROMPT
)

def process_candidate(resume_text: str):
    result = agent.run_sync(resume_text)

    text = result.output.strip()

    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        json_str = text[start:end]

        data = json.loads(json_str)

        output = CandidateEvaluation(**data)

        save_data(output.model_dump())

        return output

    except Exception as e:
        print(" Error parsing response:", e)
        print("Raw output:", text)
        raise