# -*- coding: utf-8 -*-
"""Edaused_car_price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Haz2FvfPNw0N4eFD8voZ2FLosq2noKQy
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("/content/Used Car Dataset.csv")

print("Basic Information:")
print(df.info())


print("\nSummary Statistics:")
print(df.describe())

print("\nShape of the Dataset:")
print(df.shape)

df.info()

df.isnull().sum()

df = df.dropna()

df = df.drop('Unnamed: 0', axis=1)
df.isnull().sum()

df

import pandas as pd

# Assuming your dataframe is 'df' and the registration_year column is in 'df['registration_year']'
# Convert 'Aug-20', 'July-2017', etc., to a consistent format

# Convert 'Aug-20' to '2020-08-01'
df['registration_year'] = pd.to_datetime(df['registration_year'], format='%b-%y', errors='coerce')

# Convert 'July-2017' to '2017-07-01'
df['registration_year'] = pd.to_datetime(df['registration_year'], format='%b-%Y', errors='coerce')

# Convert '2022' to '2022-01-01'
df['registration_year'] = pd.to_datetime(df['registration_year'], format='%Y', errors='coerce')

# Print the resulting dataframe
print(df[['registration_year']])

df.isnull().sum()

df['registration_year'].fillna(df['registration_year'].mean(), inplace=True)

df.isnull().sum()

df.dtypes

# Display summary statistics of numeric columns
print(df.describe())

# Display summary statistics of categorical columns
print(df.describe(include='O'))

# Histograms for numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64'])
for column in numeric_columns.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30, color='skyblue')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Count plots for categorical columns
categorical_columns = df.select_dtypes(include='O')
for column in categorical_columns.columns:
    plt.figure(figsize=(35, 20))
    sns.countplot(x=column, data=df, palette='viridis')
    plt.title(f'Count Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# Correlation heatmap for numeric columns
correlation_matrix = df.corr()
plt.figure(figsize=(30, 15))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Box plots for numeric columns
for column in numeric_columns.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column], color='lightblue')
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

print(df.dtypes)
print(df.shape)

import matplotlib.pyplot as plt
import pandas as pd



# Create a color map for fuel types
color_map = {'Petrol': 'blue', 'Diesel': 'green'}
plt.figure(figsize=(10, 5))
# Plotting
for fuel_type, color in color_map.items():
    fuel_df = df[df['fuel_type'] == fuel_type]
    plt.scatter(fuel_df['engine(cc)'], fuel_df['mileage(kmpl)'], color=color, marker='o', label=fuel_type)

plt.title('Mileage vs Engine Size by Fuel Type')
plt.xlabel('Engine Size (cc)')
plt.ylabel('Mileage (kmpl)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(100, 70))
df['car_name'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Car Names')
plt.xlabel('Car Name')
plt.ylabel('Count')
plt.show()

df['registration_year'] = df['registration_year'].dt.year
plt.figure(figsize=(10, 6))
plt.hist(df['registration_year'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Registration Years')
plt.xlabel('Registration Year')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
df['seats'].value_counts().sort_index().plot(kind='bar', color='lightcoral')
plt.title('Distribution of Number of Seats')
plt.xlabel('Number of Seats')
plt.ylabel('Count')
plt.show()

