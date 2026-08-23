#Simple Line chart 

import matplotlib.pyplot as plt


x= [1, 2,3,4, 5,6, 7,8, 9,10,11,12,13,14,15]    #list of values on x axis 
y= [-5,0,5,10,0,20,0,12,7,-1,3, 8,2,0,-16]      #list of values on y axis

figure,axes = plt.subplots() # creates a drawing area for your graph
                             # returns a figure and an axes object
                             # tuple expansion

axes.plot(x,y,'r--^') #plot x,y values on axes object.
axes.set_title('Name of the Axes') #set the name of the Axes
axes.grid(True)

figure.canvas.manager.set_window_title('Name of the Window') # Setting the name of the Window/Figure

plt.show()

