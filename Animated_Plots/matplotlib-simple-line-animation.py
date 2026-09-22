#Simple Line chart Animation using FuncAnimation() Function 

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation #needed for animation function 

x = []     # create empty lists to hold x cordinates
y = []     # create empty lists to hold x cordinates

figure, axes  = plt.subplots() #create the figure and axes object,use tuple expansion

(line, ) = axes.plot([], []) # create a Line2D object by giving empty lists to .plot()
                             # line, comma means tuple expansion

axes.set_ylim(0, 20)   # set limits on y axis 0-20
axes.set_xlim(0, 20)   # set limits on x axis 0-20

axes.grid(True)

#update function called by FuncAnimation(fig,update,...)
def update(frame):
    
    print(f'frame = {frame}')
    
    x.append(frame)                # create the x cordinate for the line using frame (0,1,2,.....)
    y.append(random.randint(1,10)) # create the y cordinate for the line using random number between 1 and 10

    line.set_data(x, y)  # draw line between x and y cordinate 
    
    return (line,) # line returned as tuple 


ani = FuncAnimation(
                    figure,
                    update,           # name of the update function to draw the line 
                    frames  = 20,     # how many times do we need to call the update function(0-19)
                    interval= 100,   # time interval between calling update() in ms 
                    blit    = True,   # Redraw only the parts that have changed
                    repeat  = False)  # Do not repeat,end the animation once the frames reach their last value

#ani.save("line_animation.gif", writer="pillow") To save the graph to disk as gif

plt.show() #displays the figure and starts the GUI's event loop.