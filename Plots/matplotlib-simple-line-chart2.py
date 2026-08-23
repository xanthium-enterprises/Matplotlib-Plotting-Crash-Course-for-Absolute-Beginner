# Comprehensive Line chart 

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator



x= [1, 2,3,4, 5,6, 7,8, 9,10,11,12,13,14,15]    #list of values on x axis 
y= [-5,0,5,10,0,20,0,12,7,-1,3, 8,2,0,-16]      #list of values on y axis

figure,axes = plt.subplots(nrows=1,ncols=1) # creates a drawing area for your graph
                                            # returns a figure and an axes object
                                            # tuple expansion

#Setting up how the plot should look and feel
axes.plot(x,
          y,
          linestyle  = '-.',  #'--' dashed line , '-' Straight line ,':' Straight line  ,'-.' dash-dot line
          linewidth  = 1,
          marker     = 's',   #'o' o marker ,'s' square marker ,'^' traiangle marker,'D' diamond marker
          markersize = 5,
          color      = 'red', #other colours ,blue,green,red etc also hex values color='#FF5733'
          label      = 'Name of the plot'  #used by the Legend 
          
          ) 

#set the name of the Axes object 
axes.set_title('Name of the Axes') #set the name of the Axes
axes.set_xlabel("X values")
axes.set_ylabel("Y values")

#Controlling the ticks on x any axis
axes.xaxis.set_major_locator(MultipleLocator(1)) #spacing = 1 units 
axes.yaxis.set_major_locator(MultipleLocator(5)) #spacing = 5 units

axes.minorticks_on() #Activate Minor ticks

axes.legend()

#Control how the Grid lines Behave
axes.grid(True)
axes.axhline(0, color="blue", linewidth=1)

figure.canvas.manager.set_window_title('Name of the Window') # Setting the name of the Window/Figure

plt.show()
