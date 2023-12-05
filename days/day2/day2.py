import os
import re

with open(os.getcwd() + "/days/day2/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]


def code(red, green, blue):
    total_ids = 0
    total_powers = 0

    for line_index in range(len(lines)):
        game_id = line_index + 1
        picks = lines[line_index].split(": ")[1].split("; ")
        print(f"Picks: {picks}")
        valid_game = True

        least_cubes = {"red": 0, "green": 0, "blue": 0}

        for pick in picks:
            pick = pick.split(" ")
            cubes = {"red": 0, "green": 0, "blue": 0}

            for cube in range(len(pick))[::2]:
                cubes[pick[cube + 1].replace(",", "")] = int(pick[cube])

            if cubes["red"] > red or cubes["green"] > green or cubes["blue"] > blue:
                valid_game = False

            for colour in ("red", "green", "blue"):
                least_cubes[colour] = max(least_cubes[colour], cubes[colour])

        if valid_game:
            total_ids += game_id

        total_powers += max(least_cubes["red"], 1) * max(least_cubes["green"], 1) * max(least_cubes["blue"], 1)

        print(least_cubes)
        print(f"Running id total: {total_ids}")
        print(f"Running total powers: {total_powers}")


def run():
    code(12, 13, 14)
