import matplotlib.pyplot as plt

# Matplotlib is a plotting library for Python. It is not part of the standard library so first needs to be installed.


## first creating an empty figure
fig = plt.figure()

## Add a title to the figure

plt.suptitle(r'iris plots',fontsize = 14)


# Add a label for the X-axis
pl.xlabel('x')
# Add a label for the Y-axis
pl.ylabel("f(x)")

# Also want to add a legend.
pl.legend()

pl.show()


