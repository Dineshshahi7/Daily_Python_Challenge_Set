'''
# Emoji Sentiment Counter 😊😢🔥

i) Create a Python program that:
- Takes a text message from the user
- Detects all emojis in the text

ii) Counts:
- positive emojis
- negative emojis
- celebration emojis

iii) Prints the total count for each category
'''

import demoji

demoji.download_codes()

positive = [
    "😊", "😀", "😁", "😄", "😃", "🙂", "😉", "😌",
    "😍", "🥰", "😘", "😇", "🤗", "😎", "🤩", "😺",
    "👍", "👌", "💯", "✨", "🌟", "❤️", "💖", "💙",
    "💚", "💛", "🧡", "🤍", "🫶", "🎈"
]

negative = [
    "😢", "😭", "😞", "😔", "☹️", "🙁", "😟", "😣",
    "😫", "😩", "😖", "😤", "😠", "😡", "😒", "😕",
    "😓", "😥", "😰", "😨", "😱", "💔", "👎"
]

celebration = [
    "🎉", "🥳", "🎊", "🎂", "🎁", "🏆", "🥇",
    "🎆", "🎇", "🍾", "🥂", "🙌", "👏", "🔥", "⭐"
]

text = input("Enter your message: ")

found_emojis = demoji.findall(text)

positive_count = 0
negative_count = 0
celebration_count = 0

for emoji in found_emojis:
    if emoji in positive:
        positive_count += 1
    elif emoji in negative:
        negative_count += 1
    elif emoji in celebration:
        celebration_count += 1

print("Positive emojis:", positive_count)
print("Negative emojis:", negative_count)
print("Celebration emojis:", celebration_count)