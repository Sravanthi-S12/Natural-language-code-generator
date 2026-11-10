import os
import re
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: Groq API key not found!")
    exit()

# Connect to Groq
client = Groq(api_key=api_key)

# System prompt
SYSTEM_PROMPT = """
You are an expert Python code generator.

Convert the user's English task into working Python code.

Rules:
1. Return ONLY Python code.
2. Do not provide explanations.
3. Do not use Markdown code fences.
4. Write correct and readable Python code.
5. Include necessary functions and examples.
6. Handle edge cases wherever possible.
"""

def generate_code(task):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": task
            }
        ],
        temperature=0.2
    )

    code = response.choices[0].message.content.strip()

    # Remove Markdown code fences if generated
    code = re.sub(r"^```(?:python)?\s*", "", code)
    code = re.sub(r"\s*```$", "", code)

    return code.strip()


def save_code(code):

    filename = "generated_code.py"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(code)

    print("\nCode saved successfully!")
    print("File name:", filename)


def main():

    print("=" * 45)
    print(" NATURAL LANGUAGE TO CODE GENERATOR")
    print("=" * 45)

    task = input("\nEnter your task: ").strip()

    if not task:
        print("Please enter a valid task.")
        return

    try:
        print("\nGenerating Python code...")

        code = generate_code(task)

        if not code:
            print("No code was generated.")
            return

        print("\nGenerated Python Code:")
        print("-" * 45)
        print(code)
        print("-" * 45)

        save_code(code)

    except Exception as error:
        print("Something went wrong:", error)


if __name__ == "__main__":
    main()