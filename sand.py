from matplotlib import rc
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import random
rc('animation', html='jshtml')
plt.rcParams["animation.html"] = "jshtml"
from matplotlib.animation import FuncAnimation

def sand(array, frame): # This is sand falling
    k = 1 # defines ground level
    m = 2 # increase this to reduce angle of repose, but this need to be less than almost 10% of the container width
    rows, cols = array.shape
    options = ["left", "right"]
    for i in range(frame):
      for j in range(cols):
         if ((i < rows-k) and (array[rows-k-(i), j] == 0) and (array[rows-k-(i+1),j] > 0)): # starting from the below, if space is there and above has block
            array[rows-k-(i), j]  = array[rows-k-(i+1),j] # then block falls down
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j+m)] == 0) and (array[rows-k-(i),(j-m)] > 0)): # starting from the below, if space is there below diagonaly opposite
            array[rows-k-(i), (j+m)]  = array[rows-k-(i+1),j] # then block falls down rightwards
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j-m)] == 0) and (array[rows-1-(i),(j+m)] > 0)): # starting from the below, if space is there below diagonaly opposite
            array[rows-k-(i), (j-m)]  = array[rows-k-(i+1),j] # then block falls down leftwards
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j+m)] == 0) and (array[rows-k-(i),(j-m)] == 0)): # starting from the below, if space is there below diagonaly opposite
            chosen_option = random.choice(options)
            if chosen_option == "left":
              array[rows-k-(i), (j-m)]  = array[rows-k-(i+1),j] # then block falls down leftwards
              array[rows-k-(i+1),j] = 0 # leaving space above
            if chosen_option == "right":
              array[rows-k-(i), (j+m)]  = array[rows-k-(i+1),j] # then block falls down rightwards
              array[rows-k-(i+1),j] = 0 # leaving space above
    m = 1
    for i in range(frame):
      for j in range(cols):

         if ((i < rows-k) and (array[rows-k-(i), j] == 0) and (array[rows-k-(i+1),j] > 0)): # starting from the below, if space is there and above has block
            array[rows-k-(i), j]  = array[rows-k-(i+1),j] # then block falls down
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j+m)] == 0) and (array[rows-k-(i),(j-m)] > 0)): # starting from the below, if space is there below diagonaly opposite
            array[rows-k-(i), (j+m)]  = array[rows-k-(i+1),j] # then block falls down rightwards
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j-m)] == 0) and (array[rows-1-(i),(j+m)] > 0)): # starting from the below, if space is there below diagonaly opposite
            array[rows-k-(i), (j-m)]  = array[rows-k-(i+1),j] # then block falls down leftwards
            array[rows-k-(i+1),j] = 0 # leaving space above

         if ((j < cols-m) and (i < rows-k) and (array[rows-k-(i+1), j] > 0) and (array[rows-k-(i),(j+m)] == 0) and (array[rows-k-(i),(j-m)] == 0)): # starting from the below, if space is there below diagonaly opposite
            chosen_option = random.choice(options)
            if chosen_option == "left":
              array[rows-k-(i), (j-m)]  = array[rows-k-(i+1),j] # then block falls down leftwards
              array[rows-k-(i+1),j] = 0 # leaving space above
            if chosen_option == "right":
              array[rows-k-(i), (j+m)]  = array[rows-k-(i+1),j] # then block falls down rightwards
              array[rows-k-(i+1),j] = 0 # leaving space above


# Initialize your initial "Fallen" array
import numpy as np
S = 100
Fallen = np.zeros((S,S)) #np.random.choice([0, 1], size=(S,S), p=[3./5, 2./5])

#for i in range(S//2,S):
#  for j in range(S):
#    Fallen[i,j] =0

for i in range(0, S):
  for j in range(S):
    if (int(0.4*S)<j<int(0.6*S)):
      Fallen[i,j] =1
    else:
      Fallen[i,j] =0

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    #ax.grid()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.imshow(Fallen)
    #plt.pcolormesh(Fallen, edgecolors='k', linewidth=0.1, cmap="viridis")
    #ax.invert_yaxis()
    sand(Fallen, frame)

anim = FuncAnimation(fig, update, frames=range(400), repeat=True, interval=80)

HTML(anim.to_html5_video())
