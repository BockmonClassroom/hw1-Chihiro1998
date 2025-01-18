# Name: Yuchen(Olivia) Kuang
# Date: 2025/1/14
# Function: Read and print each row of the Iris dataset

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Use pandas to read Iris Data
data = pd.read_csv("data/Iris.csv")

# Print
print(data.to_string())




