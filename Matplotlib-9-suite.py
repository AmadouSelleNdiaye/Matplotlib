from matplotlib import pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation
import pandas as pd

"""
First example
x_vals = []
y_vals = []

index=count()
def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    
    plt.cla()
    plt.plot(x_vals, y_vals)
    plt.tight_layout()
    plt.grid(True)
    
ani = FuncAnimation(plt.gcf(),animate,1000)

plt.show()
"""


def animate(i):
    data= pd.read_csv('data_gen.csv')
    x =data['x_value']
    y1=data['total_1']
    y2=data['total_2']
    
    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x,y2, label='channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.grid(True)
    
ani = FuncAnimation(plt.gcf(),animate,1000)

plt.show()
    