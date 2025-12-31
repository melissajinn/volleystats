# Volleystats

Volleystats is a lightweight tool for analyzing volleyball statistics using natural language. Users can upload game data and ask questions to quickly understand player and team performance.

## Features
- Upload stats in CSV, TXT, or PDF format
- Ask questions about performance (kills, errors, digs, blocks, etc.)
- Automatic stat interpretation using OpenAI

## Tech Stack
- Python
- Streamlit
- OpenAI API
- PyPDF2
- dotenv

## Getting Started
git clone https://github.com/melissajinn/volleystats.git
cd volleystats
pip install -r requirements.txt

Create a `.env` file:
OPENAI_API_KEY=your_api_key_here

Run the app:
streamlit run app.py

## Author
Melissa Jin
