from collections import Counter

def word_frequency(line):
    words = line.split()
    frequency = Counter(words)
    for word in sorted(frequency):
        print(f"{word}: {frequency[word]}")
line = "which is better python 2 or python 3"
word_frequency(line)
