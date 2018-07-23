import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 1.25
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True

mpl.rcParams['legend.frameon'] = True
mpl.rcParams['legend.fontsize'] = 15
mpl.rcParams['figure.figsize'] = 9,5
mpl.rcParams['figure.subplot.top'] = 0.95
mpl.rcParams['figure.subplot.right'] = 0.95
mpl.rcParams['figure.subplot.left'] = 0.15
mpl.rcParams['figure.subplot.bottom'] = 0.15
mpl.rcParams['figure.dpi'] = 300
mpl.rcParams['font.size'] = 18

mpl.rcParams['legend.fancybox']=False

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['xtick.top'] = True
mpl.rcParams['ytick.right'] = True

mpl.rcParams['axes.axisbelow'] = False

boxprops = dict(alpha=mpl.rcParams["legend.framealpha"],\
                facecolor=mpl.rcParams["axes.facecolor"],\
                edgecolor=mpl.rcParams["legend.edgecolor"])
