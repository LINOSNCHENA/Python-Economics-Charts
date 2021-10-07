import matplotlib.pyplot as plt 

# Recorded Amounts of coal activities in metric values 
x =  [2.4, 4, 7.5, 6, 5.2, 5, 4, 2,4,27] 
x1 =  [2.1, 4, 7.5, 6, 5.2, 5, 3, 3,3,38] 

x2 = [1.4, 2, 2.5, 3, 2.2, 4, 5, 5,8,39] 
x3 = [2.4, 2, 3.5, 3, 4.5, 6, 7, 4,4,37] 
x4 = [2.4, 4, 7.5, 7, 6.5, 6, 8, 7,6,37] 

# corresponding years 
y = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2030] 
y1 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2030] 

y2 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2030] 
y3 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2030]
y4 = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2030] 

# ==============================================================================================
# 1. BASIC-Part


plt.plot(y, x) 
# naming the  axis 
plt.ylabel('Zlin Coal mining activities') 
plt.xlabel('Years of the last decade') 
plt.title('Economic trejectory in last decade') 
plt.savefig('../UXviews/A1.png')
plt.show()
# ==============================================================================================
# 2. SECONDAY-PART

# plotting the line points  
plt.plot(y1, x1, label = "Zlin activities") 
plt.plot(y2, x2, label = "Brno activities") 
plt.plot(y3, x3, label = "Praha activities") 
# naming the  axis 
plt.ylabel('Coal mining activities index') 
plt.xlabel('Years of the last decade') 
plt.title('Economic growth trejectories in last decade') 
# function to show the coal mining and economic impact 
plt.legend()
plt.savefig('../UXviews/A2.png')
plt.show()

# ==============================================================================================
# 3. THIRD-PART

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
plt.title('Economic growth trejectories in last decade') 

# function to show the coal mining and economic impact 
plt.legend()
plt.savefig('../UXviews/A3.png')
plt.show()

# ==============================================================================================
# 4. FOURTH-PART

# x-coordinates of left sides of bars 
coal =  [70,73,68,64,56,45,44,43,32,24] 
water =  [70,73,68,64,56,45,44,43,32,24] 
gas =  [70,73,68,64,56,45,44,43,32,24] 
air =  [70,73,67,61,56,47,44,43,32,24] 

# heights of bars 
y = [2010, 2011,2011,2013,2014,2015,2016,2017,2019,2020] 

# labels for bars 
yearIndex = ['y2009','y2010', 'y2011', 'y2012', 'y2013', 'y2014','y2015','y2018','y2019','y2020'] 
plt.bar(y, air, tick_label = yearIndex, width = 0.5, color = ['red', 'green']) 

plt.xlabel('Years') 
plt.ylabel('Coal-Mined') 
# plot title 
plt.title('Economic growth trejectories in last decade') 
plt.savefig('../UXviews/A4.png')
plt.show()

print('============================|FOUR-PARTS|==|PAGE 101|==================================')