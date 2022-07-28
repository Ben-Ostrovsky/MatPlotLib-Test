import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


#define Annotate Max
def annot_max(x,y, elem, ax=None, ):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.4", fc="w", ec="k", lw=0.2)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(elem[0],elem[1]), **kw)


#Elems for Annotation
Elem1=(0.3,0.7)
Elem2=(0.9,0.85)
Elem3=(0.7,0.989)
# Values of X
x = np.linspace(-10, 40, 1000)

#Figure Size
plt.figure(figsize=(10.25,8))

#Creating the plots
Blue, =plt.plot(x, stats.norm(18.8, 3.66).pdf(x))
Orange=plt.plot(x, stats.norm(14.05, 2.99).pdf(x))
Green=plt.plot(x, stats.norm(9.75, 3.65).pdf(x))

#Set X and Y Label Frequency
plt.xticks(np.arange(-10, 41, 2))

#Annotate the Max (Exporting Data)
annot_max(Blue.get_xdata(), Blue.get_ydata(),Elem2)
annot_max(Green[0].get_xdata(), Green[0].get_ydata(),Elem1)
annot_max(Orange[0].get_xdata(), Orange[0].get_ydata(),Elem3)

# Formating Tings
plt.xlim(-10,40)
plt.title('Bell Curve For Amazon Box Size', fontsize='20')
plt.xlabel('Box Size', fontsize='15')
plt.ylabel('Probability', fontsize='15')
plt.show()


