#!/usr/bin/env python

import math
import sys

filename = open(sys.argv[1])

def total_fuel(fuel):
    fuels_fuel = math.floor(fuel / 3) - 2
    if fuels_fuel <= 0:
        return 0
    else:
        return fuels_fuel + total_fuel(fuels_fuel)

def part1():
    with filename  as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += math.floor((int(line) / 3)) - 2
        return total

def part2():
    with open("input.txt") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            total += total_fuel(int(line))
        return total

print("Part 1: " + str(part1()) + "\n" + "Part 2: " + str(part2()))