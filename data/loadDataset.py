#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:51:16 2021

@author: marcnol
"""

import numpy as np
import matplotlib.pylab as plt

matrix = np.load("F1/Fig1f.npy")

fig, ax1 = plt.subplots()
fig.set_size_inches((10, 10))

plt.imshow(matrix, cmap="coolwarm",vmin=0,vmax=0.6)
plt.savefig("Fig1f.png")


