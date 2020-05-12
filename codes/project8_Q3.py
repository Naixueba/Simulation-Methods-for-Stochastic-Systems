import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def f(x):
    fx = 418.9829*2 - (x[0]*np.sin(np.sqrt(abs(x[0]))) + x[1]*np.sin(np.sqrt(abs(x[0]))))
    return fx


N_r = 512
x = np.linspace(-N_r, N_r, 100)
y = np.linspace(-N_r, N_r, 100)
X, Y = np.meshgrid(x, y)
Z = 418.9829*2 - (X*np.sin(np.sqrt(abs(X))) + Y*np.sin(np.sqrt(abs(Y))))

# contour plot
plt.figure(num=None, dpi=100)
plt.contourf(X, Y, Z)
plt.title('$f(x1,x2) = 418.9829*2 - (x1*\sin(\sqrt{|x1|} + x2*\sin(\sqrt{|x2|})$')
plt.colorbar()
plt.savefig('Contour_Plot_2D.png')
plt.show()

# 3-D
cplot = plt.figure(num=None, dpi=150)
ax = cplot.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
cbar = cplot.colorbar(surf, shrink=0.5, aspect=5)
cbar.minorticks_on()
plt.title('$f(x1,x2) = 418.9829*2 - (x1*\sin(\sqrt{|x1|} + x2*\sin(\sqrt{|x2|})$')
plt.savefig('Contour_Plot_3D.png')
plt.show()


# find global minimum











