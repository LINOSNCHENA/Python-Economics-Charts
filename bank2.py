# SCRIPT FOR COAL MINING COMPARISIONS
import matplotlib.pyplot as plt 
# amount of coal activities in metric values 
x1 = [1.4, 2, 2.5, 3, 2.2, 4, 5, 5,8] 
x2 = [2.4, 2, 3.5, 3, 4.5, 6, 7, 4,4] 
x3 = [2.4, 1, 4.5, 4, 5.5, 5, 6, 5,3] 
# corresponding years 
y1 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 
y2 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 
y3 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 

# plotting the line points  
plt.plot(y1, x1, label = "Zlin activities") 
plt.plot(y2, x2, label = "Brno activities") 
plt.plot(y3, x3, label = "Praha activities") 

# naming the  axis 
plt.ylabel('Coal mining activities index') 
plt.xlabel('Years of the last decade') 
plt.title('Economic trejectory of Zlin/Brno/Praha in last decade graph!') 
# function to show the coal mining and economic impact 
plt.legend()
plt.show() 
