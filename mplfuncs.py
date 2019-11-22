import numpy as np
from matplotlib.ticker import MaxNLocator

def ax_prune(ax,xy,which):
    if xy=="x":
        prune_x(ax,which)
    elif xy=="y":
        prune_y(ax,which)
    elif xy=="both":
        prune_x(ax,which)
        prune_y(ax,which)
    elif xy==None:
        pass
    else:
        raise ValueError("xy must be one of 'x', 'y', or 'both'.")

def prune_x(ax,which):
    ax.xaxis.set_major_locator(MaxNLocator(nbins=len(ax.get_xticklabels())-1,\
                                           prune=which))

def prune_y(ax,which):
    ax.yaxis.set_major_locator(MaxNLocator(nbins=len(ax.get_yticklabels())-1,\
                                           prune=which))

def resize(fig,axarr,polar=False,square=False):
  nr,nc = np.atleast_2d(axarr).shape
  nr = nr-1
  nc = nc-1
  if square:
    BL_IN = 1.0
    TR_IN = 0.3
    X = BL_IN + (6 * (nc + 1)) + TR_IN
    Y = BL_IN + (6 * (nr + 1)) + TR_IN
    B = BL_IN/Y
    L = BL_IN/X
    T = 1.0 - (TR_IN/Y)
    R = 1.0 - (TR_IN/X)
  else:
    Y = np.array([6,11,15,18,20,21])
    X = 9.0*Y[nc]/6.0
    B = 0.15*6./Y
    L = 0.125*9./X
    if polar:
      Y = X
    else:
      Y = Y[nr]
  fig.set_size_inches(X,Y)
  for ax in np.ravel(axarr):
    ax.grid(True)
    ax.minorticks_on()
    if square:
      ax.set_aspect("equal")
  fig.subplots_adjust(left=L,bottom=B)
  if square:
    fig.subplots_adjust(left=L,bottom=B,top=T,right=R)
  return fig,axarr
