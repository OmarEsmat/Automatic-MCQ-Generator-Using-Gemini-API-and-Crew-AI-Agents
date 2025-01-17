from flask import Flask, request, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Supabase
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

# Initialize Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')

# Check if environment variables are loaded correctly
if not supabase_url or not supabase_key or not gemini_api_key:
    raise ValueError("Supabase URL, Key, and Gemini API Key must be set in the .env file.")

supabase = create_client(supabase_url, supabase_key)

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

@app.route('/generate-mcq', methods=['POST'])
def generate_mcq():
    user_text = request.json.get('text')
    mcqs = generate_mcqs_with_gemini(user_text)
    store_data_in_supabase(user_text, mcqs)
    return jsonify({'mcqs': mcqs})

def generate_mcqs_with_gemini(user_text):
    # Initialize the Gemini model
    model = genai.GenerativeModel('gemini-pro')

    # Define the prompt for generating MCQs
    prompt = f"""
    Generate 7 multiple-choice questions (MCQs) based on the following text:
    
    {user_text}
    
    Each MCQ should have:
    - A clear and concise question.
    - 4 options labeled as A, B, C, and D.
    - One correct answer among the options.
    - The options should be plausible and relevant to the question.
    
    Format the output as a JSON-like structure:
    [
        {{
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "correct_answer": "A"
        }},
        {{
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "correct_answer": "B"
        }},
        {{
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
            "correct_answer": "B"
        }}
    ]
    """

    # Generate MCQs using Gemini
    response = model.generate_content(prompt)

    # Parse the response into structured MCQs
    mcqs = parse_mcqs(response.text)
    return mcqs

def parse_mcqs(result):
    # Parse the raw result into structured MCQs
    import json
    try:
        mcqs = json.loads(result)
        return mcqs
    except json.JSONDecodeError:
        # Fallback in case the response is not in JSON format
        mcqs = []
        for line in result.split('\n'):
            if line.strip():
                mcqs.append({'question': line.strip(), 'options': [], 'correct_answer': ''})
        return mcqs

def store_data_in_supabase(user_text, mcqs):
    data = {'user_text': user_text, 'generated_mcqs': mcqs}
    supabase.table('mcqs').insert(data).execute()

if __name__ == '__main__':
    app.run(debug=True)