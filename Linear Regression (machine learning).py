# Importing the libraries
#import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Prepare Data

# A. Importing the dataset
data = pd.read_csv("/Users/apple/Documents/PYTHON DOCUMENTS/1000_Companies.csv")
print(data.head())
print(data.shape)
print(data.describe())
print(data.info())
print(data.cumsum)
print(data.max)
print(data.min)
print(data.dropna)


# Extracting the Independent and Dependent Variables
x = data["Profit"]
y = data["State"]
Z = data["Administration"]
print(x)

# Data Visualization
# Create plot
plt.hist(x, y, bins=10, color='blue', edgecolor='black')

# Add labels and title
plt.xlabel("PROFIT")
plt.ylabel("STATE")
plt.title("Simple Line Plot")

# Show plot
plt.show()



