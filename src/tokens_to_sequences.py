import pandas as pd
import json
import ast

TOKENS_FILE = "data/processed/genz_tokens.csv"
VOCAB_FILE = "data/processed/vocab.json"
OUTPUT_FILE = "data/processed/genz_sequences.csv"

def main():
    # Load data
    df = pd.read_csv(TOKENS_FILE)

    with open(VOCAB_FILE, "r") as f:
        vocab = json.load(f)

    sequences = []

    for tokens in df["tokens"]:
        token_list = ast.literal_eval(tokens)
        seq = [vocab[token] for token in token_list if token in vocab]
        sequences.append(seq)

    df["sequence"] = sequences

    df[["Sentence", "sequence"]].to_csv(OUTPUT_FILE, index=False)

    print("Sequences created successfully")
    print("Total sequences:", len(sequences))
    print("Saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
