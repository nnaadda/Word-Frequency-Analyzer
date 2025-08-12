Word Frequency Analyzer

Option Chosen

Option 3 – Word Frequency Analyzer

This program analyzes a .txt file and reports the most frequent words in the file. It also generates a bar chart visualization of the top words.

Features
Accepts a path to a .txt file.

Ignores punctuation and letter case.

Displays the top 10 most frequent words with their counts and percentages.

Bonus: Generates a bar chart of the top words using Matplotlib.

Handles large files efficiently by reading them in chunks.

How to Run
Install Dependencies
Make sure Python 3 is installed.
Run:
pip install -r requirements.txt

Run the Program
python word_frequency_analyzer.py

Follow Prompts
Enter the path to your .txt file.
View the top 10 most frequent words in the terminal.
The program will also display a bar chart of the top words.

Language and Tools Used
Language: Python 3
Libraries:

re – for regular expressions to clean text

collections.Counter – to count word frequencies

pathlib.Path – for file handling

matplotlib – to generate bar chart visualizations

Example
Input (sample.txt):
In a quiet village, there lived a wise old owl.
The owl had seen many things, and heard many stories.
Each morning, it watched the sun rise over the hills.
Each evening, it listened to the wind whisper through the trees.
The villagers admired the owl for its wisdom and patience.

Terminal Output:
File: sample.txt
Total words: 52
Unique words: 38

the 6 (11.54%)

owl 3 ( 5.77%)

a 2 ( 3.85%)

and 2 ( 3.85%)
...

Generated Chart:
(example_barchart.png)

Project Structure
word_frequency_analyzer.py # Main Python script
requirements.txt # Dependency list
sample.txt # Example text file
example_barchart.png # Sample output chart

Author
Nada Adel – 2025
