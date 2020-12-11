# SCRIPT FOR COAL MINING COMPARISIONS
import matplotlib.pyplot as plt 
# Recorded Amounts of coal activities in metric values 
x =  [2.4, 4, 7.5, 6, 5.2, 5, 4, 2,4] 
x1 =  [2.1, 4, 7.5, 6, 5.2, 5, 3, 3,3] 

x2 = [1.4, 2, 2.5, 3, 2.2, 4, 5, 5,8] 
x3 = [2.4, 2, 3.5, 3, 4.5, 6, 7, 4,4] 
x4 = [2.4, 4, 7.5, 7, 6.5, 6, 8, 7,6] 
# corresponding years 
y = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 
y1 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 

y2 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 
y3 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019]
y4 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019] 

# plotting the line points  
plt.plot(y4, x4, label = "Zlin activities",color='yellow',) 
plt.plot(y3, x3, label = "Brno activities",color='orange',) 
plt.plot(y2, x2, label = "Praha activities",color='red',) 

plt.plot(y1, x1, label = "Big green",color='green', linestyle='dashed',marker='x') 
plt.plot(y, x, label = "Small green",color='blue', linestyle='dashed',marker='o') 

# naming the  axis and limitations
plt.ylabel('Coal mining activities index') 
plt.ylim(1,9.5) 
plt.xlabel('Years of the last decade') 
plt.xlim(2010,2020) 
plt.title('Trejectories of Zlin/Brno/Praha in last decade') 

# function to show the coal mining and economic impact 
plt.legend()
plt.show() 
