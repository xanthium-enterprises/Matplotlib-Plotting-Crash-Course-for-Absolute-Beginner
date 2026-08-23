#creating 4 plots on the same window

import matplotlib.pyplot as plt

#data for the first plot
x1= [1,2,3,4, 5,6, 7,8, 9,10,11,12,13,14,15]     #list of values on x axis 
y1= [1,0,5,10,11,20,22,32,37,44,43,48,52,60,66]  #list of values on y axis

#data for second plot
x2= [1, 2,3,4, 5,6, 7,8, 9,10,11,12,13,14,15]        #list of values on x axis 
y2= [100,90,85,70,61,50,42,32,37,44,43,48,52,60,66]  #list of values on y axis

#data for third plot
x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # list of values on x axis
y3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # list of values on y axis

#data for Fourth plot
x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


figure,axes = plt.subplots(nrows=2,ncols=2,figsize=(12,5)) # create 4 axes,side by side
                                                           # double row ,double columns
                                                           # figsize specifies the size of the Matplotlib figure.
                                                           # figsize=(width,height) in inches

axes[0,0].plot(x1,y1,'red')   # plot the first graph
axes[0,1].plot(x2,y2,'green') # plot the second graph
axes[1,0].plot(x3,y3,'blue')  # plot the third graph
axes[1,1].plot(x4,y4,'grey')  # plot the fourth graph

axes[0,0].set_title('Plot1')
axes[0,1].set_title('Plot2')
axes[1,0].set_title('Plot3')
axes[1,1].set_title('Plot4')


plt.tight_layout() #automatically adjusts the spacing between subplots so that titles, axis labels, and tick labels don't overlap

figure.canvas.manager.set_window_title('Four Plots in One Figure') # Setting the name of the Window/Figure
plt.show()
