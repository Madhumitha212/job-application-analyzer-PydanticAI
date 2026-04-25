from pydantic import BaseModel
from typing import List

class CandidateEvaluation(BaseModel):
    candidate_name: str
    skills: List[str]
    experience_level: str
    match_score: int
    strengths: List[str]
    weaknesses: List[str]
    summary: str
    decision: str