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

if __name__ == "__main__":
    add_to_csv(CSV_FILE, ["prompt", "run", "model", "seconds", "response"], new=True)

    for prompt in PROMPTS:
        for run in range(1, RUNS + 1):
            for model in MODELS:
                start = time.perf_counter()
                response = chat_ollama(model, prompt, timeout_seconds=TIMEOUT_SECONDS)
                seconds = round(time.perf_counter() - start, 2)

                answer = response["message"]["content"]
                print(f"[{model}, run {run}, {seconds}s]\n{answer}\n")
                add_to_csv(CSV_FILE, [prompt, run, model, seconds, answer])
