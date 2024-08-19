#!/usr/bin/env python3

import sys

# Initialize the package count dictionary and the count for Ireland
package_count = {}
ireland_count = 0

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

    # Check if the country is Ireland and increment the count
    if line.startswith('"IE"'):
        ireland_count += count

# Find the most popular package in Ireland
ireland_packages = {k: v for k, v in package_count.items() if k in package_count and k is not None}
most_popular_package = max(ireland_packages, key=ireland_packages.get)

# Print the results
print(f'Most popular package in Ireland: {most_popular_package} with {ireland_packages[most_popular_package]} downloads'
      )
