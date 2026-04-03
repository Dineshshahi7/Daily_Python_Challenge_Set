'''
# Countdown Clock and Timer

i) Create a countdown timer program in Python.

The program should:
- Ask the user to enter time in seconds
- Start counting down from that number
- Show the remaining time every second
- Stop when it reaches 0
- Print "Time's up!"
'''

import time

seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"{mins:02d}:{secs:02d}")
    time.sleep(1)
    seconds -= 1

print("Time's up!")