import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ChessBoard import *

# Generate Default Array
ChessBoard = np.zeros((72,72))
Pieces = np.zeros((8,8))
ChessBoard[:,:] = 0.75

# For Animation Function
fig, ax = plt.subplots()
FPS = 10
RUNTIME = 10000    # in seconds
move = 0

# Time Dependent Things
def animate(move):

    # Global (mr. worldwide even)
    global ChessBoard
    global Pieces

    # Generator
    Parts, ChessBoard = Board(Pieces, ChessBoard, move)

    # Plotting
    ax.clear()
    ax.imshow(ChessBoard, 'nipy_spectral')

    # Refresh Rate
    move = move + 1
    time.sleep(1/FPS)

# Display Data
ani = FuncAnimation(
    fig, animate,
    frames=FPS*RUNTIME,
    interval=1,
    repeat=False
)
plt.show()
