import sys
from pathlib import Path

if len(sys.argv) < 2:
   print("Usage: python lobby_star.py <path>")
   sys.exit(1)

file_path = Path(sys.argv[1])
total_joltage = 0
num_batteries = 12

with open(file_path, 'r') as file:
    batteries = file.read().strip().split('\n')

    for bank in batteries:
        batteries = [-1]
        for b in range(1, num_batteries+1):
            batteries.append(batteries[b-1]+1)
            for i in range(batteries[b], len(bank) - num_batteries + b):
                if bank[i] > bank[batteries[b]]:
                    batteries[b] = i
        on_batteries = [bank[i] for i in batteries[1:]]
        total_joltage += int(''.join(on_batteries))

print(total_joltage)
