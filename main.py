from src.agent import process_candidate

sample_resume = """
Name: Hari

Skills:
Java, Spring Boot, SQL, REST APIs

Experience:
1 year internship in backend development

Projects:
- Online Banking System
- Library Management System

Strong understanding of OOP and backend development.
"""

def main():
    result = process_candidate(sample_resume)

    print("\n Candidate Evaluation:\n")
    print("Name:", result.candidate_name)
    print("Skills:", result.skills)
    print("Experience:", result.experience_level)
    print("Match Score:", result.match_score)
    print("Strengths:", result.strengths)
    print("Weaknesses:", result.weaknesses)
    print("Summary:", result.summary)
    print("Decision:", result.decision)

if __name__ == "__main__":
    main()