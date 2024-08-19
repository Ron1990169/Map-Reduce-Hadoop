#!/usr/bin/env python3

import sys

# Initialize the OS count dictionary
os_count = {}

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into OS and count
    os, count = line.split('\t')

    # Convert count (currently a string) to int
    count = int(count)

    # Increment the count for the OS
    if os in os_count:
        os_count[os] += count
    else:
        os_count[os] = count

# Find the most popular OS among R programmers
most_popular_os = max(os_count, key=os_count.get)

# Print the results
print(f'Most popular OS among R programmers: {most_popular_os} with {os_count[most_popular_os]} downloads')
