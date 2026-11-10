# Python Matplotlib code for animating Four plots inside the same Window (figure)
# Code will create 4 axes inside a single figure and create an animated side scrolling plot
# (c) www.xanthium.in 2026

import random
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation  # needed for animation function
from matplotlib.ticker import MultipleLocator   # import the MultipleLocator

from collections import deque  # import double ended queue

WINDOW_SIZE = 20  # no of points visible at a time

x0 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold x0 cordinates
y0 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold y0 cordinates

x1 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold x1 cordinates
y1 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold y1 cordinates

x2 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold x2 cordinates
y2 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold y2 cordinates

x3 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold x3 cordinates
y3 = deque(maxlen=WINDOW_SIZE)  # create double ended lists of specific size to hold y3 cordinates

# Create the figure and axes
figure, axes = plt.subplots( nrows = 2,      # two rows
                             ncols = 2,      # two column
                             figsize=(10, 5) # set width = 10 and height = 5 using figsize=()
                           )
figure.canvas.manager.set_window_title('Four Animated Subplots in a Single Figure') # Setting the name of the Window/Figure

# Create Subplot0
# Create a Line2D object by giving empty lists to .plot()
# line0, comma means tuple expansion
(line0,) = axes[0][0].plot(  [],  # empty lists for x0 data
                             [],  # empty lists for y0 data
                             linestyle  = '-',  # '-' Straight line ,
                             linewidth  = 1,
                             marker     = 'o',  # 'o' o marker
                             markersize = 3,
                             color      = 'orange',       # other colours ,blue,green,red etc also hex values color='#FF5733'
                             label      = 'Temperature')  # used by the Legend

# Create Subplot1
# create a Line2D object by giving empty lists to .plot()
# line1, comma means tuple expansion
(line1,) = axes[0][1].plot([],                # empty lists for x data
                           [],                # empty lists for y data
                           linestyle  = '-',  # '-' Straight line ,
                           linewidth  = 1,
                           marker     = 'o',  # 'o' o marker
                           markersize = 3,
                           color      = 'green',  # other colours ,blue,green,red etc also hex values color='#FF5733'
                           label      = 'Pressure')  # used by the Legend

# Create Subplot2
# create a Line2D object by giving empty lists to .plot()
# line2, comma means tuple expansion
(line2,) = axes[1][0].plot([],                # empty lists for x data
                           [],                # empty lists for y data
                           linestyle  = '-',  # '-' Straight line ,
                           linewidth  = 1,
                           marker     = 'o',  # 'o' o marker
                           markersize = 3,
                           color      = 'blue',  # other colours ,blue,green,red etc also hex values color='#FF5733'
                           label      = 'Pressure')  # used by the Legend


# Create Subplot3
# create a Line2D object by giving empty lists to .plot()
# line3, comma means tuple expansion
(line3,) = axes[1][1].plot([],                # empty lists for x data
                           [],                # empty lists for y data
                           linestyle  = '-',  # '-' Straight line ,
                           linewidth  = 1,
                           marker     = 'o',  # 'o' o marker
                           markersize = 3,
                           color      = 'black',  # other colours ,blue,green,red etc also hex values color='#FF5733'
                           label      = 'Pressure')  # used by the Legend

axes[0][0].xaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on X Axis
axes[0][0].yaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on Y Axis
axes[0][0].minorticks_on()  # Activate Minor ticks

axes[0][0].set_ylim(-1, 10)  # set limits on y axis -1 to 20
axes[0][0].set_xlim(0, 20)  # set limits on x axis  0 to 20

axes[0][0].set_title('Temperature',color ='red')  # set the name of the Axes

axes[0][0].grid(True, color = 'blue', alpha =0.25)  # Show grid,color = blue,alpha transparency = 0.10

axes[0][1].xaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on X Axis
axes[0][1].yaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on Y Axis
axes[0][1].minorticks_on()  # Activate Minor ticks

axes[0][1].set_ylim(-1, 10)  # set limits on y axis -1 to 20
axes[0][1].set_xlim(0, 20)  # set limits on x axis  0 to 20

axes[0][1].set_title('Pressure',color = 'green')  # set the name of the Axes

axes[0][1].grid(True, color='blue', alpha=0.25)  # Show grid,color = blue,alpha transparency = 0.10

axes[1][0].xaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on X Axis
axes[1][0].yaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on Y Axis
axes[1][0].minorticks_on()  # Activate Minor ticks

axes[1][0].set_ylim(-1, 10)  # set limits on y axis -1 to 20
axes[1][0].set_xlim(0, 20)  # set limits on x axis  0 to 20

axes[1][0].set_title('Humidity',color = 'blue')  # set the name of the Axes

axes[1][0].grid(True, color='blue', alpha=0.25)  # Show grid,color = blue,alpha transparency = 0.10

axes[1][1].xaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on X Axis
axes[1][1].yaxis.set_major_locator(MultipleLocator(1))  # place major ticks at multiples of 1 on Y Axis
axes[1][1].minorticks_on()  # Activate Minor ticks

axes[1][1].set_ylim(-1, 10)  # set limits on y axis -1 to 20
axes[1][1].set_xlim(0, 20)  # set limits on x axis  0 to 20

axes[1][1].set_title('RPM',color = 'black')  # set the name of the Axes

axes[1][1].grid(True, color='blue', alpha=0.25)  # Show grid,color = blue,alpha transparency = 0.10


plt.tight_layout() #automatically adjusts the spacing between subplots so that titles, axis labels, and tick labels don't overlap

# update function called by FuncAnimation(fig,update,...)
def update(frame):
    print(f'frame = {frame}')

    x0.append(frame)  # create the x cordinate for the line using frame (0,1,2,.....)
    y0.append(random.randint(0, 8))  # create the y cordinate for the line using random number between 1 and 10

    x1.append(frame)  # create the x cordinate for the line using frame (0,1,2,.....)
    y1.append(random.randint(0, 8))  # create the y cordinate for the line using random number between 1 and 10

    x2.append(frame)  # create the x cordinate for the line using frame (0,1,2,.....)
    y2.append(random.randint(0, 8))  # create the y cordinate for the line using random number between 1 and 10

    x3.append(frame)  # create the x cordinate for the line using frame (0,1,2,.....)
    y3.append(random.randint(0, 8))  # create the y cordinate for the line using random number between 1 and 10

    line0.set_data(x0, y0)  # draw line between x and y cordinate
    line1.set_data(x1, y1)  # draw line between x and y cordinate
    line2.set_data(x2, y2)  # draw line between x and y cordinate
    line3.set_data(x3, y3)  # draw line between x and y cordinate

    # Side-scrolling behavior
    if frame >= WINDOW_SIZE:
        print(f'axes.set_xlim({frame - WINDOW_SIZE}, {frame})')
        axes[0][0].set_xlim(frame - WINDOW_SIZE + 1, frame)
        axes[0][1].set_xlim(frame - WINDOW_SIZE + 1, frame)
        axes[1][0].set_xlim(frame - WINDOW_SIZE + 1, frame)
        axes[1][1].set_xlim(frame - WINDOW_SIZE + 1, frame)

    else:
        axes[0][0].set_xlim(0, WINDOW_SIZE)
        axes[0][1].set_xlim(0, WINDOW_SIZE)
        axes[1][0].set_xlim(0, WINDOW_SIZE)
        axes[1][1].set_xlim(0, WINDOW_SIZE)

    return (line0,line1,line2,line3)  # line returned as tuple,#can omit this since blit = false in FuncAnimation()


ani = FuncAnimation(
                     figure,
                     update,          # name of the update function to draw the line
                     frames  = None,  # (infinite iterator),Advance frame till user closes window,0,1,2.....
                     interval= 150,   # time interval between calling update() in ms
                     blit    = False, # Redraw everything
                     repeat  = False, # do not repeat the plot
                     cache_frame_data = False)  # do not cache anything in memory
#ani.save("subplots4.gif", writer="pillow")
plt.show()  # displays the figure and starts the GUI's event loop.
