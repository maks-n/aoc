import sys

# part 1

def part1(data):
    dial_position = 50
    dial_size = 100
    password = 0

    for line in data:
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

    return password


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
