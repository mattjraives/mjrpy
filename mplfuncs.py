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

def resize(fig,axarr):
  nr,nc = np.atleast_2d(axarr).shape
  Y = np.array([5,9,12,14,15])
  X = 9.0*Y[nc]/5.0
  Y = Y[nr]
  fig.set_size_inches(X,Y)
  for ax in axarr.ravel():
    ax.grid("on")
    ax.minorticks_on()
  B = 0.15*5./Y
  L = 0.15*9./X
  fig.subplots_adjust(left=L,bottom=B)
  return fig,axarr
  
  
