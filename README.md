# Rule-Based Chatbot

**Internship:** CodeOrbit Tech – Artificial Intelligence Internship  
**Task:** Task 1 – Rule-Based Chatbot  
**Developer:** Iswariya C  
**Programming Language:** Python 3

## Project Description

This is a beginner-friendly rule-based chatbot developed using Python. It accepts text from a user and responds using predefined rules and keyword matching.

## Features

- Responds to greetings such as `hi`, `hello`, and `hey`
- Answers basic questions about the chatbot
- Responds to questions about Artificial Intelligence and Python
- Handles help and thank-you messages
- Provides a fallback response for unknown questions
- Ends the conversation when the user types `bye`, `goodbye`, `exit`, or `quit`

## Concepts Used

- Python functions
- `if`, `elif`, and `else` conditional statements
- `while` loop
- User input and output
- String methods: `lower()` and `strip()`
- Comments for explaining the chatbot's decision rules

## Requirements

- Python 3
- No external Python packages are required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python chatbot.py
```

On some systems, use:

```bash
python3 chatbot.py
```

## Sample Conversation

```text
========================================
       WELCOME TO AI CHATBOT
========================================
Type 'bye' to end the conversation.

You: Hello
Chatbot: Hello! Welcome. How can I help you?

You: What is AI?
Chatbot: AI stands for Artificial Intelligence. It helps machines perform tasks that normally require human intelligence.

You: Thank you
Chatbot: You are welcome! Happy to help you.

You: Bye
Chatbot: Goodbye! Have a nice day.
```

## Project Structure

```text
CodeOrbit_RuleBasedChatbot/
├── chatbot.py
├── README.md
└── .gitignore
```

## Note

This is a rule-based chatbot. It does not use machine learning or an online AI service. Its responses are selected from the rules written in the Python code.
