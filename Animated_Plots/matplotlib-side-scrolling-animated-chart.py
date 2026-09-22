#Python code for creating the above a Real Time Side Scrolling Chart using the Matplotlib Library and Python
#(c) www.xanthium.in 2026

import random
import matplotlib.pyplot as plt
import time

from matplotlib.animation import FuncAnimation # needed for animation function
from matplotlib.ticker import MultipleLocator  # import the MultipleLocator

from collections import deque                  # import double ended queue
 
WINDOW_SIZE = 20 # no of points visible at a time 

x = deque(maxlen = WINDOW_SIZE)     # create double ended lists of specific size to hold x cordinates
y = deque(maxlen = WINDOW_SIZE)     # create double ended lists of specific size to hold x cordinates

figure, axes  = plt.subplots(figsize=(10, 5)) # create the figure and axes object,use tuple expansion
                                              # set width =10 and height =5 using figsize

# create a Line2D object by giving empty lists to .plot()
# line, comma means tuple expansion
(line, ) = axes.plot([],               #empty lists for x data
                     [],			   #empty lists for y data
                     linestyle  = '-', #'-' Straight line ,
                     linewidth  =  1,
                     marker     = 'o', #'o' o marker ,'s' square marker ,'^' traiangle marker
                     markersize = 3,
                     color      = '#f9442b',          #other colours ,blue,green,red etc also hex values color='#FF5733'
                     label      = 'Name of the plot') #used by the Legend 
                                                         
                             
                             
axes.xaxis.set_major_locator(MultipleLocator(1)) # place major ticks at multiples of 1 on X Axis 
axes.yaxis.set_major_locator(MultipleLocator(1)) # place major ticks at multiples of 1 on Y Axis 
axes.minorticks_on()                             # Activate Minor ticks

axes.set_ylim(-1, 10)   # set limits on y axis -1 to 20
axes.set_xlim( 0, 20)   # set limits on x axis  0 to 20

axes.set_title('Time Series Random Data Display') #set the name of the Axes

axes.grid(True,color='blue',alpha =0.20) #Show grid,color = blue,alpha transparency = 0.10
axes.legend() #show legend 

#update function called by FuncAnimation(fig,update,...)
def update(frame):
   
   #print(f'frame = {frame}')
   
   x.append(frame)                # create the x cordinate for the line using frame (0,1,2,.....)
   y.append(random.randint(0 ,8)) # create the y cordinate for the line using random number between 1 and 10
   time.sleep(1)
   line.set_data(x, y)            # draw line between x and y cordinate
   time.sleep(1)
   
   
   # Side-scrolling behavior
   if frame >= WINDOW_SIZE:
       print(f'for frame = {frame} -> axes.set_xlim({frame - WINDOW_SIZE+1}, {frame})')
       axes.set_xlim(frame - WINDOW_SIZE+1, frame)
       time.sleep(1)
       
       
   else:
        print(f'for frame = {frame} -> axes.set_xlim(0, {WINDOW_SIZE})')
        axes.set_xlim(0, WINDOW_SIZE)
   
   
   return (line,) # line returned as tuple,#can omit this since blit = false in FuncAnimation()







ani = FuncAnimation(
                   figure,
                   update,           # name of the update function to draw the line 
                   frames  = None ,   # (infinite iterator),Advance frame till user closes window,0,1,2.....
                   interval= 1000,    # time interval between calling update() in ms 
                   blit    = False,  # Redraw everything 
                   repeat  = False,  # do not repeat the plot 
                   cache_frame_data = False) #do not cache anything in memory 


                   
plt.show() #displays the figure and starts the GUI's event loop.

#ani.save("name_of_your_gif.gif", writer="pillow") # To save the graph to disk as gif