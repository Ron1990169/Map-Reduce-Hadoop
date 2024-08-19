#!/usr/bin/env python3

import sys

# Initialize the count for ggplot2 downloads
ggplot2_downloads = 0

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into package and count
    package, count = line.split('\t')

    # Convert count (currently a string) to int
    count = int(count)

    # Increment the count for ggplot2 downloads
    ggplot2_downloads += count

# Print the results
print(f'Number of downloads for package ggplot2: {ggplot2_downloads}')



