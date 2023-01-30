import numpy as np
from ..QuantumCircuit import QuantumCircuit
import matplotlib.pyplot as plt
# ScalerMappable is needed for creating the color bar on the State Vector visualization
# that shows what each qubit's phase angle is



class BlochSphere:
    """
    Visualizes the quantum state of a single qubit as a sphere
    
    Methods
    --------
    makeSphere():
        returns a Bloch Sphere that plots the quantum state of a single qubit in a 
        3D global view
    """
    
    def __init__(self, circuit = None, blochQubit = None):
        """
        Args:
            circuit: 
                the quantum circuit
            blochQubit:
                the qubit that will be visualized 
        ------
        Variables:
            _amplitudes :
                an array of the amplitude for every state
            _phase_angles :
                an array of the phase angle for every state
        """
        self._amplitutes = circuit.amplitude().flatten()
        self._phase_angles = circuit.phaseAngle().flatten()
        
    def makeSphere(self, path: str = "BlochSphere.png", save: bool = True, show: bool = False, darkmode: bool = True):
        """
            Creates a sphere of the circuit's probabilties
        Args:
            path (str): name of the image to be saved
            save (bool): pass True for the graph to be saved
            show (bool): pass True for the sphere to be shown instead of saved
            darkmode (bool): pass True for darkmode, false for lightmode
        """
        # sets up darkmode or lightmode
        if darkmode:
            _text = 'white'
            _accent = '#39c0ba'
            _background = '#2e3037'
        else:
            _text = 'black'
            _accent = 'black'
            _background = 'white'
        
        # creates a sphere
        plt.clf()
        plt.close()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")     
        u = np.linspace(0,2*np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        r = 1
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        # wireframe sets up lines around the sphere
        ax.plot_wireframe(x, y, z, rstride = 20, cstride = 20, linewidth=.5, color="lightgray")
        # surface helps give the sphere a translucent look 
        ax.plot_surface(x, y, z,  color="linen", alpha=.1)
        ax.scatter(0,0,0, s=5, color="black")
        # plots accent lines around the sphere
        theta = np.linspace(0, 2 * np.pi, 100)
        zs = np.zeros(100)
        xs = r * np.sin(theta)
        ys = r * np.cos(theta)
        ax.plot(xs, ys, zs, color='black', alpha=0.25) # line around equator
        ax.plot(zs, xs, ys, color='black', alpha=0.25) # line around north & south poles
        # accent lines along x, y, and z axes
        zeros = np.zeros(100)
        line = np.linspace(-1,1,100)
        ax.plot(line, zeros, zeros, color='black', alpha=0.25)
        ax.plot(zeros, line, zeros, color='black', alpha=0.25)
        ax.plot(zeros, zeros, line, color='black', alpha=0.25)
        # sets backgorund color
        ax.set_facecolor(_background)
        fig.patch.set_facecolor(_background)
        # x-axis arrow
        ax.quiver(1, 0, 0, .75, 0, 0, color="lightgray")
        ax.text(2, 0, 0, "+x", color="gray")
        # y-axis arrow
        ax.quiver(0, 1, 0, 0, .75, 0, color="lightgray") 
        ax.text(0, 2, 0, "+y", color="gray")
        # +z and |0> arrow
        ax.quiver(0, 0, 1, 0, 0, .75, color="lightgray") 
        ax.text(0, 0, 2, "+z", color="gray")
        ax.text(.1, 0, 1.5, "|0>", color="gray")
        # -z and |1> arrow
        ax.quiver(0, 0, -1, 0, 0, -.75, color="lightgray") 
        ax.text(0, 0, -2, "-z", color="gray")
        ax.text(.1, 0, -1.5, "|1>", color="gray")
        
        ### For testing purposes only now
        zero = np.array([[
            1+0j,
            0+0j
        ]])

        one = np.array([[
            0+0j,
            1+0j
        ]])
        
        final = np.array([])
        
        for i in range(len(self._phase_angles)):
            theta = self._amplitutes[i]
            phi = self._phase_angles[i]
            placement = np.cos(theta / 2) * zero + (np.exp(0+1j * phi) * np.sin(theta / 2) * one)
            final = np.append(final, placement)
        z = final[1::2].flatten()
        y = final[::2].flatten()
        z = z[0]
        y = y[0]

        # gets x, y, z cartesian coords
        x1 = 1 * np.sin(phi) * np.cos(theta)
        y1 = 1 * np.sin(phi) * np.sin(theta)
        z1 = 1 * np.cos(phi)
        # plots a line from center to surface
        xs, ys, zs = [0, x1], [0, y1], [0, z1]
        ax.plot3D(xs, ys, zs, color=_accent)
        ax.scatter(xs[1], ys[1], zs[1], s=5, color=_accent)
        ax.text(xs[1] * 1.15, ys[1] * 1.15, zs[1] * 1.15, "|ψ⟩", color=_text)
        
        plt.axis('off') # removes 3d grid around sphere
        # saves Bloch Sphere as a file and/or shows it as a figure
        if save:
            plt.savefig(path)
        if show:
            plt.show()