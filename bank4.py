import matplotlib.pyplot as plt 

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
plt.title('Trejectories of Zlin/Brno/Praha in last decade') 
plt.show() 
