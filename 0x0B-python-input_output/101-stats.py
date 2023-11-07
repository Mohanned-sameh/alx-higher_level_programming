#!/usr/bin/python3
"""
Reads from standard input and computes metrics
"""
import sys
import signal

total_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0


def print_statistics():
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 8:
            status_code = int(parts[8])
            total_size += int(parts[10])
            status_code_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
