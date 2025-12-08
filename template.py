import sys

# part 1

def part1(data):
    return None


# part 2

def part2(data):
    return None


# input

def load_input(input = None):
    day = sys.argv[0].replace('problems/day','')[:-3]

    if input == 'test':
        input = f'input/day{day}_test.in'
    else:
        input = f'input/day{day}.in'

    with open(input, 'r') as file:
        data = [line.rstrip() for line in file.readlines()]

    return data


# main

if __name__ == '__main__':
   data_test = load_input('test')
   data = load_input()
   print(f'Part 1 test: {part1(data_test)}')
   print(f'Part 1:      {part1(data)}')
   print(f'Part 2 test: {part2(data_test)}')
   print(f'Part 2:      {part2(data)}')
