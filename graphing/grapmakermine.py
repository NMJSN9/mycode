#!/usr/bin/python3
"""Docstrings making a chart"""

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    mcrfanMeans = (25, 30, 15, 40) #mcr length of outage (mins)
    paramorefanMeans = (25, 32, 34, 20) #paramore length of outage (min)
    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, mcrfanMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, paramorefanMeans, width, bottom=mcrfanMeans)

    # Describe the table metadata
    plt.ylabel("Numbers of tickets")
    plt.title("Ticket Purchase to WWWY")
    plt.xticks(ind, ("VIP+", "VIP", "GA+", "GA"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("MCR Fans", "PARAMORE Fans"))

    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/whenwewereyoungfest.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/whenwewereyoung.png")


if __name__ == "__main__":
    main()

