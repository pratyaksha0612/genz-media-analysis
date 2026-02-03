import pandas as pd
import json
import ast

INPUT_FILE = "data/processed/genz_tokens.csv"
OUTPUT_FILE = "data/processed/vocab.json"

def main():
    df = pd.read_csv(INPUT_FILE)

    vocab = {}
    index = 1  # start from 1 (0 reserved for padding)

    for tokens in df["tokens"]:
        token_list = ast.literal_eval(tokens)
        for token in token_list:
            if token not in vocab:
                vocab[token] = index
                index += 1

    with open(OUTPUT_FILE, "w") as f:
        json.dump(vocab, f, indent=4)

    print("Vocabulary built successfully")
    print("Total unique words:", len(vocab))
    print("Saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
