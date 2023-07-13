import csv
import re
import matplotlib.pyplot as plt
from collections import Counter

def count_word_mentions(csv_file, word_list):
    word_counts = Counter()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            paragraph = row['Description']
            paragraph = paragraph.lower() # Convert paragraph to lowercase for case insensitivity
            word_mentions = re.findall(r'\b\w+\b', paragraph) # Extract individual words from the paragraph

            # Count the occurrences of words in the word list
            word_counts.update([word for word in word_mentions if word in word_list])

    return word_counts

# Example data
csv_file = 'Output_file_random_data_generator.csv'
word_list = ['hive', 'impala', 'hadoop', 'resouce','yarn','oozie','server','cm','hdfs','spark']

# Count word mentions in paragraph column
word_counts = count_word_mentions(csv_file, word_list)

# Separate word counts into matched and unmatched words
matched_words = []
matched_counts = []
unmatched_words = []
unmatched_counts = []

for word, count in word_counts.items():
    if word in word_list:
        matched_words.append(word)
        matched_counts.append(count)


# Plot bar chart for matched words
plt.bar(matched_words, matched_counts)
plt.xlabel('Word')
plt.ylabel('Count')
plt.title('Matched Word Mentions')
plt.show()

# Display counts
for word, count in word_counts.items():
    print(f'{word}: {count}')