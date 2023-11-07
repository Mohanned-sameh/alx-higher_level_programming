#!/usr/bin/python3
"""Log parsing script. Reads stdin line by line and computes metrics"""
import sys

total_size = 0
codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

iteration = 0


def print_stats():
    """Function that prints a resume of the stats."""
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v is not 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        line = line.split()
        if len(line) >= 2:
            tmp = iteration
            if line[-2] in codes:
                codes[line[-2]] += 1
                iteration += 1
            try:
                total_size += int(line[-1])
                if tmp == iteration:
                    iteration += 1
            except ValueError:
                if tmp == iteration:
                    continue

        if iteration % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
