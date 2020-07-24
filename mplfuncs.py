import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MaxNLocator
from matplotlib import _contour as cntr


def ax_prune(ax, xy, which):
    if xy == "x":
        prune_x(ax, which)
    elif xy == "y":
        prune_y(ax, which)
    elif xy == "both":
        prune_x(ax, which)
        prune_y(ax, which)
    elif xy is None:
        pass
    else:
        raise ValueError("xy must be one of 'x', 'y', or 'both'.")


def prune_x(ax, which):
    ax.xaxis.set_major_locator(MaxNLocator(nbins=len(ax.get_xticklabels())-1,
                                           prune=which))


def prune_y(ax, which):
    ax.yaxis.set_major_locator(MaxNLocator(nbins=len(ax.get_yticklabels())-1,
                                           prune=which))


def resize(fig, axarr, polar=False, square=False):
    nr, nc = np.atleast_2d(axarr).shape
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
        Y = np.array([6, 11, 15, 18, 20, 21])
        X = 9.0*Y[nc]/6.0
    if polar:
        Y = X
    else:
        Y = Y[nr]
        B = 0.15*6./Y
        L = 0.125*9./X
    fig.set_size_inches(X, Y)
    for ax in np.ravel(axarr):
        ax.grid(True)
        ax.minorticks_on()
        if square:
            ax.set_aspect("equal")
    fig.subplots_adjust(left=L, bottom=B)
    if square:
        fig.subplots_adjust(left=L,bottom=B,top=T,right=R)
    return fig,axarr

def get_contourset(X,Y,Z,level):
    contour_generator = cntr.QuadContourGenerator(X,Y,Z,None,
                                                  mpl.rcParams["contour.corner_mask"],0)
    allsegs = [contour_generator.create_contour(level)]
    flatseglist = [s for seg in allsegs for s in seg]
    points = np.concatenate(flatseglist, axis=0)
    x,y = points.T
    return x,y

def eformat(f, prec=2, math=True):
    """Usage : eformat(f, prec=2, math=True)
    Format floats into scientific notation with latex syntax and return as a string.
    Keywords:
    prec = int : This is the number of significant figures - 1
    math = bool : This sets whether to include '$' in the output."""
    d = '$'
    if not math:
        d = ''
    s = "%.*e" % (prec, f)
    m, e = s.split('e')
    e = int(e)
    if prec >= 0:
        return d + r'{0:s} \! \times \! 10^{{{1:d}}}'.format(m, e) + d
    if e != 0:
        return d + r'10^{{{0:d}}}'.format(e) + d
    return d + '1' + d
