'''
Write a Python program that:

Takes a sentence as input
Removes punctuation (.,!?)
Splits the sentence into words
Groups words based on their length
Prints the result as a dictionary
'''

text = input("Enter a sentence: ")

# Step 1: remove punctuation
for ch in ".,!?":
    text = text.replace(ch, "")

# Step 2: split words
words = text.split()

# Step 3: group by length
grouped = {}

for word in words:
    length = len(word)
    
    if length in grouped:
        grouped[length].append(word)
    else:
        grouped[length] = [word]

# Output
print(grouped)
