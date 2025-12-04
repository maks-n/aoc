import sys
from pathlib import Path

if len(sys.argv) < 2:
   print("Usage: python lobby.py <path>")
   sys.exit(1)

file_path = Path(sys.argv[1])
total_joltage = 0

with open(file_path, 'r') as file:
    batteries = file.read().strip().split('\n')
    for battery in batteries:
        left = 0
        for i in range(0, len(battery) - 1):
            if battery[i] > battery[left]:
                left = i
        right = left + 1
        for i in range(right, len(battery)):
            if battery[i] > battery[right]:
                right = i
        cur_joltage = int(battery[left]) * 10 + int(battery[right])
        total_joltage += cur_joltage

print(f"Total joltage: {total_joltage}")
