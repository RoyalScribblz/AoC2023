import os
import math

with open(os.getcwd() + "/days/day3/input.txt", "r") as f:
    schematic = [list(line.rstrip()) for line in f]


def is_part(value):
    return value not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def code():
    total_part_numbers = 0
    gear_ratios = {}

    for y in range(len(schematic)):
        valid = False
        number = ""
        gear_poss = []
        for x in range(len(schematic[y])):
            value = schematic[y][x]
            if value.isnumeric():
                number += str(value)

                neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dy, dx in neighbors:
                    new_y = y + dy
                    new_x = x + dx

                    if 0 <= new_y < len(schematic) and 0 <= new_x < len(schematic[new_y]):
                        gear = is_part(schematic[new_y][new_x])
                        if gear:
                            gear_poss.append((new_y, new_x))
                        valid = valid or gear

            if not value.isnumeric():
                if valid:
                    total_part_numbers += int(number)
                    for gear_pos in gear_poss:
                        if gear_pos in gear_ratios:
                            gear_ratios[gear_pos].append(int(number))
                        else:
                            gear_ratios[gear_pos] = [int(number)]
                        gear_ratios[gear_pos] = list(dict.fromkeys(gear_ratios[gear_pos]))
                    gear_poss = []
                valid = False
                number = ""

        if number != "" and valid:
            total_part_numbers += int(number)

        print(total_part_numbers)

    print(schematic)
    print(total_part_numbers)

    pair_total = 0
    for gear_pos, values in gear_ratios.items():
        if len(values) == 2:
            pair_total += math.prod(values)
    print(pair_total)


def run():
    code()
