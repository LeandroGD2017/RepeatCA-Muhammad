#!/usr/bin/env python3
import sys

current_utility = None
total = 0

for line in sys.stdin:
    utility, count = line.strip().split("\t")

    if utility == current_utility:
        total += int(count)
    else:
        if current_utility:
            print(f"{current_utility}\{total}")
        current_utility = utility
        total = int(count)

if current_utility:
    print(f"{current_utility}\t{total}")
    