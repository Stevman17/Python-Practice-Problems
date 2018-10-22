import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


#Write the command to create the left subplot 
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1, 2, 1) 
x_values = range(len(months))
plt.plot(x_values, visits_per_month, marker='*') 
#Label the x-axis and y-axis with descriptive titles of what they measure.
plt.xlabel('Month')
plt.ylabel('Visitors')
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Visits per Month') 

#Write the command to create the right subplot 
ax2 = plt.subplot(1, 2, 2) 
plt.plot(x_values, key_limes_per_month, marker='o', color='green') 
plt.plot(x_values, persian_limes_per_month, marker='s', color='purple')
plt.plot(x_values, blood_limes_per_month, marker='x', color='orange')
#Add a legend to differentiate the lines, labeling each lime species.
plt.legend(['Key Limes', 'Persian Limes', 'Blood Limes'])
#Label the x-axis and y-axis with descriptive titles of what they measure.
plt.xlabel('Month')
plt.ylabel('Limes sold')
#Set the x-axis ticks to be the x_values, and the tick labels to be the months list.
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
#Add a title to each of the two plots you've created, and adjust the margins to make the text you've added look better.
plt.title('Limes per Month') 
#adjust the margins to make the text you've added look better.
plt.tight_layout()
plt.show()
plt.savefig('Important Graphs.png')

