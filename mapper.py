# #!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into fields
    fields = line.split(',')

    # check that the line has the expected number of fields
    if len(fields) == 10:
        # extract the fields
        package = fields[6]
        country = fields[7]
        os = fields[5]

        # Question 1: number of downloads for package ggplot2
        if package == 'ggplot2':
            print('ggplot2\t1')

        # Question 2: highest number of downloads by country
        print('"%s"\t1' % country)

        # Question 3: top 10 most popular packages
        print('"%s"\t1' % package)

        # Question 4: most popular package in Ireland
        if country == 'IE':
            print('"%s"\t1' % package)

        # Question 5: most popular OS among R programmers
        print('"%s"\t1' % os)

# Path: mapper.py
