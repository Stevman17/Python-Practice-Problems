#Import the modules that you'll be using in this project:
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
#Load WorldCupMatches.csv into a DataFrame called df
df = pd.read_csv('WorldCupMatches.csv')
#Inspect the DataFrame using .head()
print(df.head())
#Create a new column in df named Total Goals, and set it equal to the sum of the columns Home Team Goals and Away Team Goals.
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())
#Set the style of your plot to be whitegrid .
sns.set_style("whitegrid") 
#To make the text in your visualization bigger and easier to read, set the context to be poster. If you would like to further adjust the font size of your plot, you can pass sns.set_context() a second optional argument using the keyword font_scale.
sns.set_context('poster', font_scale=1)
#Inside of plt.subplots(), set the size of the figure to be 12 inches wide and 7 inches tall.
f, ax = plt.subplots((figsize=(12, 7)))
#visualize the columns Year and Total Goals as a bar chart.
ax = sns.barplot(data=df, x="Year", y="Total Goals")
ax.set_title('Goals per Match Over Time')
plot.show()
df_goals=pd.read_csv('goals.csv')
#Now you are going to create a box plot so you can visualize the distribution of the goals data instead of just the average with a bar chart.
#Load goals.csv into a DataFrame called df_goals, and take a quick look at the DataFrame using .head().
print(df_goals.head())
#Try setting the context of the plot to be notebook and the font_scale to be 1.25.
sns.set_context('notebook', font_scale=1.25)
#Create a figure for your second plot. Set the variables f, ax2 and instantiate a figure that is 12 inches wide and 7 inches tall.
f, ax = plt.subplots((figsize=(12, 7)))
#Set ax2 equal to a box plot with the color palette Spectral that visualizes the data in the DataFrame df_goals with the column year on the x-axis and goals on the y-axis.
ax2 = sns.barplot(data=df_goals, x="year", y="goals", palette="Spectral")
#Give your box plot a meaningful and clear title.
ax2.set_title('Goals per Year')
plot.show()
