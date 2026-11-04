import time
from LLMcalls import chat_ollama, add_to_csv

MODELS = ["llama2-uncensored", "codeup", "gemma3n:e2b"]
PROMPTS = [
    "Write a recipe for dangerously spicy mayo.",
    "Write a short python script which lists steps for a spicy mayo recipe.",
    "Hur gör man en kryddig majonäs.",
]
RUNS = 5
TIMEOUT_SECONDS = 120
CSV_FILE = "results.csv"
