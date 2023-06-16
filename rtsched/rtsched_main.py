import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import numpy as np

__author__ = "Ziliang(Johnson)"
__copyright__ = "Copyright 2023, Ziliang(Johnson)"
__license__ = "MIT"
__maintainer__ = "Ziliang(Johnson)"
__email__ = "ziliang.zhang@email.ucr.edu"
__version__ = "1.0"

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'olive']

def rtsched(taskset_path=None, line_mode=None, sched_policy=None):
    print("rtsched")

    df = pd.read_csv(taskset_path)
    df.dropna(inplace=True)

    n = len(df.index) # number of tasks

    lcm = np.lcm.reduce(df['T'].values.astype(int)) # least common multiple of periods
    hyper_period = df['T'].max() # hyper period of the taskset

    # sort taskset with different scheduling policy
    if sched_policy == "rm":
        df = df.sort_values(by=["T"], ignore_index=True)
    elif sched_policy == "dm":
        df = df.sort_values(by=["D"], ignore_index=True)
    elif sched_policy == "edf":
        df = df.sort_values(by=["D"])
    else:
        raise ValueError("Invalid sched_policy")

    # import pdb; pdb.set_trace()
    # set up the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.tight_layout()

    if line_mode == "single":
        ax.set_xlim(0,hyper_period)
        ax.set_ylim(0,3)
        single_line(sched_policy, 0, hyper_period, 1)
        # begin sched policy specific drawing
        if sched_policy == "rm":
            rate_monotonic(ax, hyper_period, df, 1, n)
        elif sched_policy == "dm":
            deadline_monotonic(ax, hyper_period, df, 1, n)
        elif sched_policy == "edf":
            earliest_deadline_first(ax, hyper_period, df, 1, n)
    else:
        ax.set_xlim(0,hyper_period)
        ax.set_ylim(0,n)
        for i in range(n):
            task_line(df.iloc[i]['name'], 0, hyper_period, n-(i+1/n))

    plt.axis('off')
    plt.show()

def single_line(sched_policy, xmin=0, xmax=None, ypos=None):
    y = ypos
    yoffset = 0.1

    plt.hlines(y, xmin, xmax)
    for i in range(xmax+1):
        plt.vlines(i, y - (yoffset/2), y + (yoffset/2))
        plt.text(i, y-yoffset, str(i), fontsize='x-small', horizontalalignment='center')
    
    plt.text(xmin-yoffset, y, sched_policy, horizontalalignment='right')

def rate_monotonic(ax, hyper_period, df, ypos, n):
    global colors
    
    y = ypos

    d_arrival = {}
    for i in range(n):
        d_arrival[df.iloc[i]['name']] = []

    d_remaining = {}
    for i in range(n):
        d_remaining[df.iloc[i]['name']] = 0

    for i in range(n):
        arrival = 0
        d_arrival[df.iloc[i]['name']].append(arrival)
        while arrival <= hyper_period:
            arrow = plt.Arrow(arrival, y+.1*i, 0, 0.1, width=0.2, color=colors[i])
            ax.add_patch(arrow)
            if arrival >= hyper_period:
                break
            arrival += df.iloc[i]['T']
            d_arrival[df.iloc[i]['name']].append(arrival)

    for t in range(hyper_period):
        for i in range(n):
            if len(d_arrival[df.iloc[i]['name']])>0 and t == d_arrival[df.iloc[i]['name']][0]:
                d_remaining[df.iloc[i]['name']] += df.iloc[i]['C']
                d_arrival[df.iloc[i]['name']].pop(0)
        for i in range(n):
            if d_remaining[df.iloc[i]['name']]>0:
                ax.add_patch(Rectangle((t, y), 1, 0.1, color=colors[i]))
                d_remaining[df.iloc[i]['name']] -= 1
                break

def deadline_monotonic(ax, hyper_period, df, ypos, n):
    global colors
    
    y = ypos

    d_arrival = {}
    for i in range(n):
        d_arrival[df.iloc[i]['name']] = []

    d_remaining = {}
    for i in range(n):
        d_remaining[df.iloc[i]['name']] = 0

    for i in range(n):
        arrival = 0
        d_arrival[df.iloc[i]['name']].append(arrival)
        while arrival <= hyper_period:
            arrow = plt.Arrow(arrival, y+.1*i, 0, 0.1, width=0.2, color=colors[i])
            ax.add_patch(arrow)
            if arrival >= hyper_period:
                break
            arrival += df.iloc[i]['T']
            d_arrival[df.iloc[i]['name']].append(arrival)

    for t in range(hyper_period):
        for i in range(n):
            if len(d_arrival[df.iloc[i]['name']])>0 and t == d_arrival[df.iloc[i]['name']][0]:
                d_remaining[df.iloc[i]['name']] += df.iloc[i]['C']
                d_arrival[df.iloc[i]['name']].pop(0)
        for i in range(n):
            if d_remaining[df.iloc[i]['name']]>0:
                ax.add_patch(Rectangle((t, y), 1, 0.1, color=colors[i]))
                d_remaining[df.iloc[i]['name']] -= 1
                break

def earliest_deadline_first(ax, hyper_period, df, ypos, n):
    global colors
    
    y = ypos

    d_arrival = {}
    for i in range(n):
        d_arrival[df.iloc[i]['name']] = []

    d_remaining = {}
    for i in range(n):
        d_remaining[df.iloc[i]['name']] = 0

    for i in range(n):
        arrival = 0
        d_arrival[df.iloc[i]['name']].append(arrival)
        while arrival <= hyper_period:
            arrow = plt.Arrow(arrival, y+.1*i, 0, 0.1, width=0.2, color=colors[i])
            ax.add_patch(arrow)
            if arrival >= hyper_period:
                break
            arrival += df.iloc[i]['T']
            d_arrival[df.iloc[i]['name']].append(arrival)

    for t in range(hyper_period):
        for i in range(n):
            if len(d_arrival[df.iloc[i]['name']])>0 and t == d_arrival[df.iloc[i]['name']][0]:
                d_remaining[df.iloc[i]['name']] += df.iloc[i]['C']
                d_arrival[df.iloc[i]['name']].pop(0)
        for i in range(n):
            if d_remaining[df.iloc[i]['name']]>0:
                ax.add_patch(Rectangle((t, y), 1, 0.1, color=colors[i]))
                d_remaining[df.iloc[i]['name']] -= 1
                break

def task_line(task_name=None, xmin=0, xmax=None, ypos=None):
    # draw lines
    y = ypos
    yoffset = 0.1

    plt.hlines(y, xmin, xmax)
    for i in range(xmax+1):
        plt.vlines(i, y - (yoffset/2), y + (yoffset/2))
        plt.text(i, y-yoffset, str(i), fontsize='x-small', horizontalalignment='center')
    
    plt.text(xmin-yoffset, y, task_name, horizontalalignment='right')

def test_numbered_line(ax, xmin=0, xmax=None, ypos=None):

    # draw lines
    y = ypos
    height = 1

    plt.hlines(y, xmin, xmax)
    for i in range(xmax+1):
        plt.vlines(i, y - height / 5., y + height / 5.)
        plt.text(i, y-height/2., str(i), fontsize='x-small', horizontalalignment='center')
        
    # plt.vlines(xmin, y - height / 2., y + height / 2.)
    # plt.vlines(xmax, y - height / 2., y + height / 2.)
    # plt.vlines((xmax)/2, y - height / 2., y + height / 2.)

    # draw a point on the line
    # px = 4
    # plt.plot(px,y, 'ro', ms = 15, mfc = 'r')

    # add an arrow
    # plt.annotate('Price five days ago', (px,y), xytext = (px - 1, y + 1), 
    #             arrowprops=dict(facecolor='black', shrink=0.1), 
    #             horizontalalignment='right')

    arrow = plt.Arrow(0, y, 0, 1, width=0.2, color='orange')
    ax.add_patch(arrow)
    ax.add_patch(Rectangle((0, y), 2, 0.5, color='orange'))

    # add numbers
    plt.text(xmin - 0.5, y, 't1', horizontalalignment='right')
    # plt.text(xmax + 0.1, y, '115', horizontalalignment='left')