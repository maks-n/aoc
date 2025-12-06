import sys

def load_input():
   day = sys.argv[0].replace('problems/day','')[:-3]
   with open(f'{day}.txt', 'r') as file:
      data = [line.rstrip() for line in file.readlines()]
   return data

def load_test_input():
   day = sys.argv[0].replace('problems/day','')[:-3]
   with open(f'{day}_test.txt', 'r') as file:
      data = [line.rstrip() for line in file.readlines()]
   return data


# Parse

def parse(data):
    for i in range(len(data)):
        if data[i] == '':
            break

    ranges = [r.split('-') for r in data[:i]]
    ranges = [(int(l), int(r)) for l, r in ranges]

    ingredients = data[i+1:]
    ingredients = [int(x) for x in ingredients]

    return ranges, ingredients


# Part 1

def part1(data):
    ranges, ingredients = parse(data)

    checked = set()
    total = 0

    for l,r in ranges:
        for i in ingredients:
            if i in checked:
                continue

            if l <= i <= r:
                total += 1
                checked.add(i)

    return total


# Part 2

def part2(data):
    return 0


# main

if __name__ == '__main__':
   data = load_input()
   data_test = load_test_input()
   print(f'Part 1 test: {part1(data_test)}')
   print(f'Part 1:      {part1(data)}')
   print(f'Part 2 test: {part2(data_test)}')
#    print(f'Part 2:      {part2(data)}')
