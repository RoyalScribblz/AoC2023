import os
import re

days = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open(os.getcwd() + "/days/day1/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]


def code(part):
    print(f"Part: {part}")
    total = 0  # running total
    for line in lines:
        print(f"Line: {line}")
        line = line.rstrip()  # remove \n
        if part == 2:
            positions = []  # (value, position)
            for index in range(len(days)):  # find every occurrence of a number and store its location
                for pos in [itr.start() for itr in re.finditer(days[index], line)]:
                    positions.append((str(index), pos))

            positions = sorted(positions, key=lambda p: p[1])
            for pos_index in range(len(positions)):  # insert the values into the position where the word is
                line = line[:positions[pos_index][1]+pos_index] + positions[pos_index][0] + line[positions[pos_index][1]+pos_index:]

        numbers = []
        chars = list(line)
        for char in chars:  # get the numbers from the string
            if char.isnumeric():
                numbers.append(int(char))

        print(f"Numbers in line: {numbers}")
        total += int(str(numbers[0]) + str(numbers[-1]))
        print(f"Running total: {total}")


def run():
    code(1)
    code(2)
