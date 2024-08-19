This document is an academic report submitted by Rohin Mehra for Assignment 1 at Griffith College Dublin, as part of the MSc. Big Data Analysis and Management program. 
The assignment focuses on the use of Apache Hadoop to process and analyze a large dataset containing information about package downloads from various sources. 
The report outlines the process of utilizing Hadoop's MapReduce functionality to answer several key questions related to download statistics, including identifying 
the number of downloads for specific packages, determining the top downloading countries, and analyzing the most popular packages and operating systems among R programmers.

Abstract
In this assignment, Apache Hadoop is used to perform operations on a CSV file containing various data points related to package downloads. 
The dataset includes columns for download date, time, package size, R version, processor architecture, operating system, package name, country code, 
and a unique IP identifier. The objective is to apply MapReduce operations to gain insights from the data and answer specific queries related to download patterns, 
such as the number of downloads for the ggplot2 package, the highest number of downloads by country, the top 10 most popular packages, the most popular package in Ireland,
and the most popular operating system among R programmers.

Dataset Columns
date: Date of download
time: Time of download (in UTC)
size: Size of the downloaded package (in bytes)
r_version: Version of R used for the download
r_arch: Processor architecture (i386 = 32-bit, x86_64 = 64-bit)
r_os: Operating System (darwin9.8.0 = macOS, mingw32 = Windows)
package: Name of the downloaded package
country: Two-letter ISO country code
ip_id: Unique daily identifier for each IP address

Objectives and MapReduce Tasks:

Task 1: Number of Downloads for Package ggplot2
To determine the number of downloads for the ggplot2 package, a MapReduce job was executed using the following command:

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/bdm/assignment/input \
-output /user/bdm/assignment/output \
-file /home/bdm/assignment/mapper.py \
-file /home/bdm/assignment/reducer.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer.py’
Output:
Number of downloads for the ggplot2 package: 22,360,632

Task 2: Highest Number of Downloads by Country
This task identified the country with the highest number of package downloads using the following command:

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/bdm/assignment/input \
-output /user/bdm/assignment/output2 \
-file /home/bdm/assignment/mapper.py \
-file /home/bdm/assignment/reducer2.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer2.py’
Output:
Country with the highest number of downloads: "NA" with 3,225,550 downloads

Task 3: Top 10 Most Popular Packages
This task identified the top 10 most popular packages by executing the following command:

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/bdm/assignment/input \
-output /user/bdm/assignment/output3 \
-file /home/bdm/assignment/mapper.py \
-file /home/bdm/assignment/reducer3.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer3.py’
Output:
Top 10 most popular packages:

"NA": 3,225,550 downloads
"mingw32": 3,194,919 downloads
"US": 3,061,236 downloads
"linux-gnu": 778,523 downloads
"darwin17.0": 648,165 downloads
"GB": 569,535 downloads
"darwin20": 328,304 downloads
"CN": 282,214 downloads
"KR": 254,392 downloads
"DE": 236,903 downloads

Task 4: Most Popular Package in Ireland
The fourth task identified the most popular package in Ireland using the following command:

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/bdm/assignment/input \
-output /user/bdm/assignment/output4 \
-file /home/bdm/assignment/mapper.py \
-file /home/bdm/assignment/reducer4.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer4.py’
Output:
Most popular package in Ireland: "mingw32" with 3,194,919 downloads

Task 5: Most Popular Operating System Among R Programmers
The final task determined the most popular operating system among R programmers using the following command:

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/bdm/assignment/input \
-output /user/bdm/assignment/output5 \
-file /home/bdm/assignment/mapper.py \
-file /home/bdm/assignment/reducer5.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer5.py’
Output:
Most popular OS among R programmers: "mingw32" with 3,194,919 downloads

This assignment demonstrates the application of Hadoop's MapReduce to perform large-scale data processing on a CSV dataset, extracting insights related to package 
downloads, geographical distribution, and platform preferences among R users.

