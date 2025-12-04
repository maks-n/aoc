import sys
from pathlib import Path

if len(sys.argv) < 2:
   print("Usage: python gift_shop_star.py <path>")
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
            chunks = []
            n = 1
            for _ in range(1, cur_id_half_len + 1):
                chunks = [cur_id_str[i:i+n] for i in range(0, len(cur_id_str), n)]
                if len(set(chunks)) == 1:
                    invalid_id_sum += cur_id
                    break
                n += 1
print(invalid_id_sum)
