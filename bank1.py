# SCRIPT FOR COAL MINING COMPARISIONS
import matplotlib.pyplot as plt 
# amount of coal activities in metric values 
x = [2.4, 1,2.5,3,4.5,5,6,5,4] 
# corresponding years 
y = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 

# plotting the points 
plt.plot(y, x) 

# naming the  axis 
plt.ylabel('Zlin Coal mining activities') 
plt.xlabel('Years of the last decade') 
plt.title('Economic trejectory of Zlin in last decade') 
# function to show the coal mining and economic impact 
plt.show() 
