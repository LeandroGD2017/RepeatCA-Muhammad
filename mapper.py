#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader) # Skip header

for row in reader:
    if len(row) >= 15:
        utility = row[15].strip()
        if utility:
            print (f"{utility}\t1")