# Name: Yuchen(Olivia) Kuang
# Date: 2025/1/14
# Function: Read and print each row of the Iris dataset

import csv

# Open Iris.csv
with open('data/Iris.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
