import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python secret_entrance_star.py <path>")
    sys.exit(1)

file_path = Path(sys.argv[1])
dial_position = 50
dial_size = 100
password = 0

with open(file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        direction = current_line[0]
        distance = int(current_line[1:])
        for _ in range(distance):
            if direction == 'L':
                dial_position = (dial_position - 1 + dial_size) % dial_size
            elif direction == 'R':
                dial_position = (dial_position + 1) % dial_size
            if dial_position == 0:
                password += 1
    print(f"password: {password}")
