import sys

# part 1

def get_num_adj(grid, r, c):
    num_adj = 0

    for dir_row in [-1, 0, 1]:
        for dir_col in [-1, 0, 1]:
            row, col = r+dir_row, c+dir_col
            if row < 0 or row >= len(grid):
                continue
            if col < 0 or col >= len(grid[row]):
                continue
            if dir_row == 0 and dir_col == 0:
                continue
            if grid[row][col] == '@':
                num_adj += 1

    return num_adj


def part1(data):
    total = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '@' and get_num_adj(data, row, col) < 4:
                total += 1

    return total


# part 2

def parse(data):
    return [[val for val in row] for row in data]


def find_removable(grid):
    removable = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and get_num_adj(grid, row, col) < 4:
                removable.add((row, col))

    return removable


def part2(data):
    grid = parse(data)
    removable = find_removable(grid)
    total = 0

    while len(removable) > 0:
        for row, col in removable:
            grid[row][col] = '.'
            total += 1
        removable = find_removable(grid)

    return total


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
