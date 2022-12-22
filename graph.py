# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import func as f
from matplotlib.animation import FuncAnimation
from itertools import count
import tkinter as tk
from tkinter import ttk
# Create a graph using the function graphy()
def graphy():
        plt.style.use('seaborn-darkgrid')
        palette = plt.get_cmap('Set1')
        index=count()
        test=True
        def animate(i):
            data = pd.read_csv('data.csv')
            num=0
            plt.cla()
            for j in f.get_dataSSID():
                num+=1
                if( j in data):
                    Test=True
                    print(data[j])
                    plt.plot(data["time"],data[j],marker='', color=palette(num), linewidth=1, alpha=0.9, label=j)
                else:
                    test=False
            plt.xlabel("temps en (s)")
            plt.ylabel("Signal en (%)")
            plt.legend(loc='best',bbox_to_anchor=(0.5,0.,0.5,0.5))
            plt.tight_layout()
        if( test==True):
            ani = FuncAnimation(plt.gcf(), animate, interval=100)
            plt.show()
            # create the root window
