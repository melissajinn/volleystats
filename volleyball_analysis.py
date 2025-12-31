import os
import csv
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_stats(file_path):
    """Detect file type and extract team stats."""
    file_path = file_path.strip('"')  # remove quotes if VS Code adds them
    if file_path.endswith(".csv"):
        return read_csv(file_path)
    elif file_path.endswith(".txt"):
        return read_txt(file_path)
    elif file_path.endswith(".pdf"):
        return read_pdf(file_path)
    else:
        raise ValueError("Unsupported file type. Use CSV, TXT, or PDF.")

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        stats_lines = []
        for row in reader:
            line = (f"Player {row['Player']}: Kills: {row['Kills']}, Errors: {row['Errors']}, "
                    f"Attempts: {row['Attempts']}, Digs: {row['Digs']}, Aces: {row['Aces']}, "
                    f"Blocks: {row['Blocks']}")
            stats_lines.append(line)
    return "\n".join(stats_lines)

def read_txt(file_path):
    with open(file_path, "r") as f:
        return f.read()

def read_pdf(file_path):
    stats = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            stats += page.extract_text() + "\n"
    return stats

def analyze_team_stats(stats: str):
    prompt = f"""
    You are a volleyball coach analyzing team performance.
    Given the stats, write:
    - Overall team strengths
    - Key weaknesses
    - Which players stand out
    - Strategic recommendations for improvement

    Team Stats:
    {stats}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Drag and drop your CSV, TXT, or PDF file here and press Enter:")
    file_path = input().strip()
    file_path = file_path.strip().strip('"').strip("'")

    
    try:
        team_stats = read_stats(file_path)
        analysis = analyze_team_stats(team_stats)
        
        print("\n=== Volleyball Team Analysis ===")
        print(analysis)
        
        with open("analysis.txt", "w") as f:
            f.write(analysis)
        print("\nAnalysis saved to analysis.txt")
    except Exception as e:
        print(f"Error: {e}")
