# Simple Workflow Engine

A minimal workflow engine built using FastAPI.

## Run the Server

1. Install dependencies:

pip install -r requirements.txt


2. Start FastAPI:

uvicorn app.main:app --reload


📁 Project Structure

workflow-engine/
├── app/
│   ├── main.py
│   ├── engine.py
│   ├── workflows.py
│   ├── models.py
│   └── storage.py
├── requirements.txt
└── README.md
