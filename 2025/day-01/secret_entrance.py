import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python secret_entrance.py <path>")
    sys.exit(1)

file_path = Path(sys.argv[1])
password = 0
dial_number = 50
dial_size = 100


try:
    with open(file_path, 'r') as file:
        for line in file:
            current_line = line.strip()
            rotation = 0
            if current_line[0] == 'L':
                rotation -= int(current_line[1:])
            elif current_line[0] == 'R':
                rotation += int(current_line[1:])
            dial_number = (dial_number + rotation) % dial_size
            if dial_number == 0:
                password += 1
        print(password)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
