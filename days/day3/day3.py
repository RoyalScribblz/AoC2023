import os

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

                neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dy, dx in neighbors:
                    new_y = y + dy
                    new_x = x + dx

                    if 0 <= new_y < len(schematic) and 0 <= new_x < len(schematic[new_y]):
                        valid = valid or is_part(schematic[new_y][new_x])

            if value == ".":
                if valid:
                    total_part_numbers += int(number)
                valid = False
                number = ""

        if number != "" and valid:
            total_part_numbers += int(number)

    print(schematic)
    print(total_part_numbers)


def run():
    code()
