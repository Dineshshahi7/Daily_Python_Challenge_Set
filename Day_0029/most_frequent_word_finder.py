'''
Write a Python program that:

Takes a sentence as input
Removes punctuation (.,!?)
Converts everything to lowercase
Counts how many times each word appears
Prints the most frequent word and its count
'''

text = input("Enter a sentence: ")

# Step 1: remove punctuation
for ch in ".,!?":
    text = text.replace(ch, "")

# Step 2: lowercase
text = text.lower()

# Step 3: split into words
words = text.split()

# Step 4: count words
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: find most frequent word
max_word = ""
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        max_word = word
        max_count = count

# Output
print("Most frequent word:", max_word)
print("Count:", max_count)