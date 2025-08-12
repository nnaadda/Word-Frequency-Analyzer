"""
Word Frequency Analyzer with Bar Chart

Author: Nada Adel
"""

import re
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

WORD_PATTERN = re.compile(r"[^\w\s]")
WHITESPACE_PATTERN = re.compile(r"\s+")


def read_file(file_path: Path, encoding="utf-8") -> str:
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    text_parts = []
    with file_path.open(encoding=encoding, errors="ignore") as f:
        for line in f:
            text_parts.append(line)
    return "".join(text_parts)


def extract_words(text: str, ignore_case=True, min_length=1) -> list[str]:
    cleaned = WORD_PATTERN.sub(" ", text)
    cleaned = WHITESPACE_PATTERN.sub(" ", cleaned)
    if ignore_case:
        cleaned = cleaned.lower()
    return [w for w in cleaned.split() if len(w) >= min_length]


def count_frequencies(words: list[str]) -> Counter:
    return Counter(words)


def display_top_words(counter: Counter, top_n=10) -> list[tuple[str, int]]:
    total = sum(counter.values())
    top_words = counter.most_common(top_n)
    for rank, (word, count) in enumerate(top_words, start=1):
        pct = (count / total) * 100
        print(f"{rank:>2}. {word:<15} {count:>6} ({pct:5.2f}%)")
    return top_words


def plot_bar_chart(top_words: list[tuple[str, int]]) -> None:
    words, counts = zip(*top_words)
    plt.figure(figsize=(8, 5))
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top Word Frequencies")
    plt.tight_layout()
    plt.show()


def main():
    file_input = input("Enter path to the text file: ").strip()
    file_path = Path(file_input)

    try:
        text = read_file(file_path)
        words = extract_words(text, min_length=1)
        counter = count_frequencies(words)

        print(f"\nFile: {file_path}")
        print(f"Total words: {sum(counter.values())}")
        print(f"Unique words: {len(counter)}\n")

        top_words = display_top_words(counter, top_n=10)

        plot_bar_chart(top_words)

    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
