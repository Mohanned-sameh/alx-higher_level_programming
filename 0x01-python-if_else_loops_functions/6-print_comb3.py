#!/usr/bin/python3
# Write a program that prints all possible different combinations of two digits.

for i in range(0, 10):
    for j in range(0, 10):
        print("{}{}".format(i, j))
for j in range(0, 10):
    if i != j:
        print("{}{}".format(i, j))
    else:
        continue
