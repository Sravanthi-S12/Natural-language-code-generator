Natural Language to Code Generator

Project Overview

The Natural Language to Code Generator is a Python-based application that converts plain English instructions into executable Python code using an AI Large Language Model (LLM).

The application accepts a task description from the user, sends it to the Groq API, generates Python code, displays the generated code in the terminal, and automatically saves it into a ".py" file.

Objectives

- Convert natural language instructions into Python code.
- Integrate an AI language model using the Groq API.
- Generate readable and accurate Python programs.
- Display generated code in the terminal.
- Automatically save generated code into a Python file.

Technologies Used

- Python
- Groq API
- Llama 3.3 70B Versatile
- VS Code
- Python-dotenv

Project Structure

Natural_Language_Code_Generator/
│
├── code_generator.py
├── generated_code.py
├── .env
├── .gitignore
└── README.md

Installation and Setup

Step 1: Install Python

Download and install Python from:
https://www.python.org/

Step 2: Install Required Libraries

pip install groq python-dotenv

Step 3: Configure Groq API

1. Visit https://console.groq.com/
2. Create an account.
3. Generate an API key.
4. Create a ".env" file in the project folder.

Add:

GROQ_API_KEY=your_actual_api_key

Step 4: Run the Application

Open the VS Code terminal and execute:

python code_generator.py

Example Usage

Input:

Write a Python function to check whether a number is prime.

Generated Output:

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))

The generated code is displayed in the terminal and saved automatically as "generated_code.py".

Test Cases

The application is intended to handle the following eight task categories:

1. Reverse a string.
2. Check whether a string is a palindrome.
3. Calculate the factorial of a number.
4. Check whether a number is prime.
5. Find the largest element in a list.
6. Remove duplicate elements from a list.
7. Count word frequency using a dictionary.
8. Find the highest scorer from a student dictionary.

Key Features

- Natural language processing through an LLM.
- AI-powered Python code generation.
- Automatic Python file creation.
- Simple command-line interface.
- Error handling.
- Reusable code generation function.

Future Enhancements

- Add a graphical user interface.
- Support multiple programming languages.
- Add code validation and testing.
- Support local LLM models using Ollama.
- Add an option to execute generated code safely.

Conclusion

This project demonstrates how Artificial Intelligence and Natural Language Processing can simplify programming by converting everyday English instructions into Python code. It provides a foundation for developing intelligent coding assistants.



Project Name: Natural Language to Code Generator
Programming Language: Python
