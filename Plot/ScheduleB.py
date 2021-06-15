# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt
fig, planX = plt.subplots()

# Setting XY-axis limits
planX.set_xlim(0, 240)
planX.set_ylim(0, 2)
# Setting labels for xY-axis and y-axis
planX.set_xlabel('Months since start of Project')
planX.set_ylabel('Tasks to be executed')
# Setting ticks on Xy-axis
planX.set_yticks([10, 20, 30, 40])
planX.set_yticklabels(['Reporting', 'Publication','Data-gathering', 'Preparation-works'])

# Setting graph attribute
planX.grid(True)
# Declaring multiple bars in at same level and same width
planX.broken_barh([(1, 60)],(30, 9), facecolors=('tab:green'))
planX.broken_barh([(60, 10), (140, 20)], (20, 9), facecolors=('tab:blue'))
planX.broken_barh([(90, 10), (170, 30)], (10, 9), facecolors=('tab:pink'))
planX.broken_barh([(60, 10), (120, 10), (180, 10), (220, 10)],(0, 9), facecolors=('tab:purple'))

# PDF/PNG file storage
plt.savefig("ScheduleB.png")
plt.show()

print("============================|SecondSchedule-Page-27|====================================")
