import os
import re
from memory_profiler import profile

with open(os.getcwd() + "/days/day3/input.txt", "r") as f:
    schematic = [list(line.rstrip()) for line in f]


def is_part(value):
    return value not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def code():
    total_part_numbers = 0

    for y in range(len(schematic)):
        valid = False
        number = ""
        for x in range(len(schematic[y])):
            value = schematic[y][x]
            if value.isnumeric():
                number += str(value)

                if y - 1 >= 0:
                    valid = valid or is_part(schematic[y - 1][x])  # down
                if y + 1 < len(schematic[y]):
                    valid = valid or is_part(schematic[y + 1][x])  # up
                if x - 1 >= 0:
                    valid = valid or is_part(schematic[y][x - 1])  # left
                if x + 1 < len(schematic[y][x]):
                    valid = valid or is_part(schematic[y][x + 1])  # right

            if value == ".":
                if valid:
                    total_part_numbers += int(number)
                valid = False
                number = ""

        if number != "" and valid:
            total_part_numbers += int(number)

    print(schematic)


def run():
    code()
