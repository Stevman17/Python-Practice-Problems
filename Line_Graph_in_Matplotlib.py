import codecademylib
from matplotlib import pyplot as plt
#Japanese passenger cars sold in the US Thousands of cars (BTS)	
x = [758, 863, 837, 930, 830,	810, 923,	1154, 1183, 1142,	829]
#Murders by blunt object Deaths (US) (CDC)	
y1 = [242,	210,	199,	184,	129,	102,	152,	115,	111,	95,	79]
#	1996	1997	1998	1999	2000	2001	2002	2003	2004	2005	2006	2007	2008	
y2 = [1122,	1123,	1117,	1083,	1050,	1010,	919,	993,	1076,	1205,	1325]
plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker = 'o')
plt.xlabel('Amazing X-axis') 
plt.ylabel('Incredible Y-axis') 
plt.title('Two Lines on One Graph')
plt.legend(['parabola', 'cubic'], loc=4) 

plt.show()
