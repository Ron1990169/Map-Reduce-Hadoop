#!/usr/bin/env python3

import sys

# Initialize the country count dictionary
country_count = {}

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into country and count
    country, count = line.split('\t')

    # Convert count (currently a string) to int
    count = int(count)

    # Increment the count for the country
    if country in country_count:
        country_count[country] += count
    else:
        country_count[country] = count

# Find the highest number of downloads by country
highest_country = max(country_count, key=country_count.get)

# Print the results
print(f'Highest number of downloads by a country: {highest_country} with {country_count[highest_country]} downloads')
