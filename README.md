# AI Job Application Analyzer using Pydantic AI
## Project Overview

This project builds an AI-powered system to analyze candidate resumes and generate structured evaluation reports.

It allows users to input resume text and automatically get insights such as skills, experience level, strengths, weaknesses, and hiring decision.

The system uses a language model to understand unstructured resume data and converts it into structured JSON output using Pydantic validation.

## Tech Stack
- Python
- Pydantic (Data Validation)
- Pydantic AI (Agent Framework)
- Groq API (LLaMA 3 - Response Generation)

## Architecture
```
User Resume Input
        ↓
AI Agent (Pydantic AI)
        ↓
LLM (Groq - LLaMA 3)
        ↓
Structured JSON Output
        ↓
Pydantic Validation
        ↓
Data Storage (applications.json)
        ↓
Final Output Display

```

## Key Functionalities
- Accepts raw resume text as input
- Extracts skills and candidate information
- Estimates experience level (Fresher / Junior / Mid / Senior)
- Assigns a match score (0–100)
- Identifies strengths and weaknesses
- Generates a summary and hiring decision
- Validates output using Pydantic models
- Stores results with timestamp in JSON file
- Handles invalid or malformed AI responses

## Project Structure

```
job_application_analyzer_using_pyndaticAI/
|
|-- src/
|   |-- agent.py              # AI agent logic
|   |-- groq_setup.py         # Groq API configuration
|   |-- model.py              # Pydantic schema
|   |-- prompts.py            # System prompt
|   |-- file_handler.py       # Save results to JSON
|
|-- main.py                   # Entry point
|-- requirements.txt          
|-- .gitignore
|-- README.md
```

## Setup Instructions
```
Clone the Repository
-> git clone https://github.com/Madhumitha212/job-application-analyzer-PydanticAI.git

Move to project directory
-> cd job-application-analyzer-PydanticAI

Create Virtual Environment
-> python -m venv venv
-> venv\Scripts\activate     # Windows
-> source venv/bin/activate  # Mac/Linux

Install Dependencies
-> pip install -r requirements.txt

Configure Environment Variables
-> Create a .env file in root folder

-> Add your Groq API key:
   GROQ_API_KEY=your_api_key_here

Run the Application
-> python main.py
```

## Author
```
R Madhumitha
```