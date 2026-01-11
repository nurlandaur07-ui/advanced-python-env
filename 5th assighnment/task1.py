import string

with open('text.txt', 'r') as file:
    lines = file.readlines()

num_lines = len(lines)
words = []
for line in lines:
    line = line.lower()
    for char in string.punctuation:
        line = line.replace(char, ' ')
    words += line.split()

num_words = len(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

with open('analysis.txt', 'w') as out:
    out.write(f"Total number of lines: {num_lines}\n")
    out.write(f"Total number of words: {num_words}\n")
    out.write("Word frequencies:\n")
    for word in sorted(word_count):
        out.write(f"{word}: {word_count[word]}\n")