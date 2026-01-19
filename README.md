# safespace-ai-therapist
AI Mental Health Therapist using FastAPI &amp; Streamlit

SafeSpace is an AI-powered mental health support system designed to assist students in managing exam stress, anxiety, emotional pressure, and feelings of loneliness.
The system provides empathetic, conversational responses similar to a professional therapist, helping users feel heard, supported, and guided.

This project combines Artificial Intelligence, Natural Language Processing, and Web Technologies to create an accessible mental health companion.

Problem Statement:

Students often experience intense stress due to:
-Academic pressure and examinations
-Fear of failure and results
-Lack of emotional support
-Hesitation to seek professional help
Traditional mental health resources may not be available 24/7, and students may feel uncomfortable opening up.
There is a need for a safe, private, and always-available support system.

Proposed Solution

SafeSpace provides:
-An AI-based virtual therapist that responds empathetically
-A chat-based interface for easy interaction
-Emotional validation, normalization, and gentle guidance
-Continuous conversation to explore the root cause of stress
The system acts as a first-level emotional support tool, especially for students.

System Development Approach:

The project follows a modular client-server architecture:
🔹 Frontend
Built using Streamlit
Provides a chat-style user interface
Sends user input to the backend via REST API

🔹 Backend
Developed using FastAPI
Handles request validation and AI processing
Integrates AI logic and tools
Returns structured responses to the frontend

Each component is separated to ensure scalability, maintainability, and clarity.
