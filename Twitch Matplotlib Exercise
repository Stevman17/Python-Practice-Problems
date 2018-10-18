import codecademylib3_seaborn  
from matplotlib import pyplot as plt  
import numpy as np  
import pandas as pd  
  
# Now, use the plt.bar() to plot a bar graph using range(len(games)) and viewers as arguments. Feel free to pick a color, too (using color='____'). Then, use plt.show() to visualize it.  
  
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]  
  
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]  
  
plt.bar(range(len(games)), viewers, color='orange')  
#Awesome, let's make the graph more informative by doing the following:  
#Add a title  
plt.title('Gamergaters')  
#Add a legend  
plt.legend('Twitch')  
#Add axis labels  
plt.xlabel('Games')   
plt.ylabel('Number of Viewers')   
#Add ticks  
ax = plt.subplot()  
ax.set_xticks(range(len(games)))  
#Add tick labels (rotate if necessary)  
ax.set_xticklabels(games, rotation=30)  
#makes room for x-label  
plt.tight_layout()  
plt.show()  
#closes the plot to allow for a new one  
plt.close()   
# Pie Chart: League of Legends Viewers' Whereabouts  
  
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]  
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]  
#Because there are 12 countries (including N/A and Others), let's create an array called colors and add 12 color codes   
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']  
#Then, use plt.pie() to plot a pie chart. Don't forget to throw in the countries variable and the colors = colors.  
plt.pie(countries, labels=labels, autopct='%d%%', colors=colors)  
plt.axis('equal')   
plt.title('Twitch Nations')  
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  
plt.savefig('my_pie_chart.png')  
plt.show()  
#closes the plot to allow for a new figure  
plt.close()   
#Jazzed up Pie chart  
##First, let's "explode", or break out, the 1st slice (United States):  
#Then, inside plt.pie(), we are going to: Add the explode, Add shadows, Turn the pie 345 degrees, Add percentages, Configure the percentages' placement  
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  
plt.pie(countries, autopct='%1.0f%%', colors=colors, explode=explode, shadow=True, startangle=345,pctdistance=1.15)  
#also add a title  
plt.title('Twitch Nations')  
#and legends  
plt.legend(labels, loc="right")  
plt.show()  
#closes the plot to allow for a new figure  
plt.close()   
# Line Graph: Time Series Analysis  
  
hour = range(24)  
  
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]  
#Use plt.plot() to plot a line graph.  
plt.plot(hour, viewers_hour)  
#Don't forget to throw in hour and viewers_hour.  
#Then, add the title, the axis labels, legend, and ticks.  
plt.title('Viewers Per Hour')  
plt.xlabel('Hour')   
plt.ylabel('Number of Viewers')   
plt.legend('2015-01-01', markerscale=2)  
ax = plt.subplot()  
ax.set_xticks(hour)  
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])  
  
  
#There is some uncertainty in these numbers because some people leave their browsers open. Let's account for a 15% error in the viewers_hour data.  
  
#First, create a list containing the upper bound of the viewers_hour and call it y_upper.  
y_upper = [i + i*.15 for i in viewers_hour]  
#Then, create a list containing the lower bound of the viewers_hour and call it y_lower.  
y_lower = [i - i*.15 for i in viewers_hour]  
#Lastly, use plt.fill_between() to shade the error, with an alpha of 0.2.  
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)   
#Lastly, use plt.show() to visualize.  
plt.show()  
plt.close()  
