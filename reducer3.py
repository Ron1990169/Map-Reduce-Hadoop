#!/usr/bin/env python3

import sys
from collections import Counter

# Initialize the package count dictionary
package_count = {}

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into package and count
    package, count = line.split('\t')

    # Convert count (currently a string) to int
    count = int(count)

    # Increment the count for the package
    if package in package_count:
        package_count[package] += count
    else:
        package_count[package] = count

# Find the top 10 most popular packages
top_10_packages = Counter(package_count).most_common(10)

# Print the results
print('Top 10 most popular packages:')
for i, (package, count) in enumerate(top_10_packages, start=1):
    print(f'{i}. {package}: {count} downloads')
