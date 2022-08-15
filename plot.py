"""
This program is perfom a basic visualisation process, using pandas, numpy, matplotlib & seaborn.
These 2 graphs represents the correlation between nutrition in food & drinks at Starbucks.
"""

# Preparing needed libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the csv file that contains the nutrition information of food and drinks in Starbucks.
drinks = pd.read_csv('starbucks-menu-nutrition-drinks.csv')
food = pd.read_csv('starbucks-menu-nutrition-food.csv', engine='python', encoding='utf-16',
                    names=["Food name", "Calories", "Fat (g)", "Carb. (g)", "Fiber (g)", "Protein (g)"],
                    skiprows=1)


# Extract the needed information, which here is the correlations between nutritions at Starbucks.
drinks_corr = drinks.corr()
food_corr = food.corr()


# Delete the first row & the last column to make the information easier to view
drinks_corr = drinks_corr.iloc[1:, :-1]
food_corr = food_corr.iloc[1:, :-1]


# Create mask for the graph, that only takes the downward triangle from the dataset
drinks_index = np.ones_like(drinks_corr, dtype='bool')
drinks_mask = np.triu(drinks_index, k=1)
food_index = np.ones_like(food_corr, dtype='bool')
food_mask = np.triu(food_index, k=1)


# Visualisation process.
fig, (ax1, ax2) = plt.subplots(1, 2)  # Create a big plot, in which there are 2 graphs

sns.heatmap(data=drinks_corr, mask=drinks_mask, ax=ax1, cmap="YlGnBu", 
            linewidths=.5, vmin=-1, vmax=1, annot=True).set_title('Nutrition in drinks')
sns.heatmap(data=food_corr, mask=food_mask, ax=ax2,
            linewidths=.5, vmin=-1, vmax=1, annot=True).set_title('Nutrition in food')


# Set the figure size.
fig.set_figheight(6.5)
fig.set_figwidth(12)


# Set the figure's title
fig.suptitle('Correlation between nutrition in food & drinks at Starbucks', fontsize=16)
plt.show()
