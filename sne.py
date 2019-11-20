# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:29:08 2018

@author: Administrator
"""

import numpy as np
from sklearn.manifold import TSNE

# Random state.
RS = 20150101

import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import scipy.io as sio

# We import seaborn to make nice plots.
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})


data = sio.loadmat('coil20gae.mat')
X = data['X']
Y = np.transpose(data['Y']-1)
Y = np.int32(np.squeeze(Y))
digits_proj = TSNE(random_state=RS).fit_transform(X)

def scatter(x, colors,num):
    # We choose a color palette with seaborn.
    palette = np.array(sns.color_palette("hls", num))

    # We create a scatter plot.
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40,
                    c=palette[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')

#    # We add the labels for each digit.
#    txts = []
#    for i in range(10):
#        # Position of each label.
#        xtext, ytext = np.median(x[colors == i, :], axis=0)
#        txt = ax.text(xtext, ytext, str(i), fontsize=24)
#        txt.set_path_effects([
#            PathEffects.Stroke(linewidth=5, foreground="w"),
#            PathEffects.Normal()])
#        txts.append(txt)

    return f, ax, sc#, txts

scatter(digits_proj, Y,int(Y.max() + 1))
plt.savefig('orl.png', dpi=300)
plt.show()
