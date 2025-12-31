import os
import csv
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2
import streamlit as st

# Load OpenAI API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File reading functions
def read_stats(file):
    if file.name.endswith(".csv"):
        return read_csv(file)
    elif file.name.endswith(".txt"):
        return read_txt(file)
    elif file.name.endswith(".pdf"):
        return read_pdf(file)
    else:
        raise ValueError("Unsupported file type. Use CSV, TXT, or PDF.")

def read_csv(file):
    file.seek(0)
    reader = csv.DictReader(file.read().decode("utf-8").splitlines())
    stats_lines = []
    for row in reader:
        line = (f"Player {row['Player']}: Kills: {row['Kills']}, Errors: {row['Errors']}, "
                f"Attempts: {row['Attempts']}, Digs: {row['Digs']}, Aces: {row['Aces']}, "
                f"Blocks: {row['Blocks']}")
        stats_lines.append(line)
