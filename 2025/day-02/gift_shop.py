import sys
from pathlib import Path

if len(sys.argv) < 2:
   print("Usage: python gift_shop.py <path>")
   sys.exit(1)

file_path = Path(sys.argv[1])

invalid_id_sum = 0

with open(file_path, 'r') as file:
    ids = file.read().strip().split(',')
    for id in ids:
        min, max = id.split('-')
        for cur_id in range(int(min), int(max) + 1):
            cur_id_str = str(cur_id)
            cur_id_half_len = len(cur_id_str)//2
            if cur_id_str[:cur_id_half_len] == cur_id_str[cur_id_half_len:]:
                invalid_id_sum += cur_id
print(invalid_id_sum)
