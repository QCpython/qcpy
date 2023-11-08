import matplotlib.pyplot as plt
import numpy as np

# ScalerMappable is needed for creating the color bar on the State Vector visualization
# that shows what each qubit's phase angle is
from matplotlib.cm import ScalarMappable


def sphere(_background):
    # creates a sphere
    plt.clf()
    plt.close()
    plt.clf()
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    r = 1
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    # surface helps give the sphere a translucent look
    ax.plot_surface(x, y, z, color="linen", alpha=0.1)
    ax.scatter(0, 0, 0, s=5, color="black")
    # plots accent lines around the sphere
    theta = np.linspace(0, 2 * np.pi, 50)
    zs = np.zeros(50)
    xs = r * np.sin(theta)
    ys = r * np.cos(theta)
    ax.plot(xs, ys, zs, color="black", alpha=0.25)  # line around equator
    # line around north & south poles
    ax.plot(zs, xs, ys, color="black", alpha=0.25)
    # accent lines along x, y, and z axes
    zeros = np.zeros(50)
    line = np.linspace(-1, 1, 50)
    ax.plot(line, zeros, zeros, color="black", alpha=0.25)
    ax.plot(zeros, line, zeros, color="black", alpha=0.25)
    ax.plot(zeros, zeros, line, color="black", alpha=0.25)
    # wireframe sets up lines around the sphere
    ax.plot_wireframe(x, y, z, rstride=10, cstride=10, linewidth=0.5, color="lightgray")
    # sets backgorund color
    ax.set_facecolor(_background)
    fig.patch.set_facecolor(_background)
    return ax
