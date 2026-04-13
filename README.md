AutoStream AI Sales Agent
Project Overview

This project implements a Conversational AI Agent for AutoStream, a fictional SaaS platform that provides automated video editing tools for content creators.

The agent simulates a real-world social-to-lead workflow where conversations are converted into qualified business leads.

The system can:

Identify user intent
Answer product questions using a local knowledge base (RAG)
Maintain conversation memory
Detect high-intent users
Capture leads using a mock API tool

Features
1. Intent Detection

The agent classifies user messages into:

Greeting
Product Inquiry
High Intent Lead

This allows the agent to take different actions based on user behaviour.

2. RAG Knowledge Retrieval

Product pricing, features, and company policies are stored in a local JSON knowledge base.

Instead of generating answers blindly, the agent retrieves relevant information and responds accurately.

3. Stateful Conversation Memory

The agent maintains memory across multiple conversation turns using a shared state object.

It remembers:

Lead collection progress
User details
Conversation context
4. Tool Execution – Lead Capture

When high purchase intent is detected, the agent collects:

Name
Email
Creator Platform

After collecting all details, a mock API function is executed:

mock_lead_capture(name, email, platform)

This simulates backend lead automation.

Project Structure
AutoStream_Agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── knowledge_base.json
│
└── agent/
    ├── intent.py
    ├── rag.py
    ├── state.py
    └── tools.py
How to Run Locally
Clone repository
git clone <repo-link>
cd AutoStream_Agent
Create virtual environment
python -m venv venv
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run agent
python app.py
