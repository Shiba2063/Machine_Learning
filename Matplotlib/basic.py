import matplotlib.pyplot as plt
import numpy as np

# # Simple Example
# fig,ax=plt.subplots()
# ax.plot([1,2,3,4],[1,4,2,3])
# plt.show()

# #Figure
## -->Entire canvas/window
# fig = plt.figure()
# fig,ax =plt.subplots()
# fig,axs=plt.subplots(2,2)
# fig,axs = plt.subplot_mosaic([['left','right_top'],['left','right_bottom']])
# plt.show()


##Axes
## -->Area containing the graph

##Axis
## -->The X-axis or Y-axis inside the Axes



##Types of inputs to plotting function

# np.random.seed(19680801) ##seed the random number generator
# data={'a':np.arange(50),
#       'c':np.random.randint(0,50,50),
#       'd':np.random.randn(50)
# }
# data['b']=data['a']+10*np.random.randn(50)
# data['d']=np.abs(data['d'])*100

# fig,ax=plt.subplots(figsize=(5,2.7),layout='constrained')
# ax.scatter('a','b',c='c',s='d',data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()


# ##simple plot
# x = np.linspace(0, 2, 100)  # Sample data.

# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the Axes.
# ax.set_ylabel('y label')  # Add a y-label to the Axes.
# ax.set_title("Simple Plot")  # Add a title to the Axes.
# ax.legend()  # Add a legend.
# plt.show()

# #Helper function
def my_plotter(ax,data1,data2,param_dict):
    """A helper function to make graph."""
    out=ax.plot(data1,data2,**param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
plt.show()



