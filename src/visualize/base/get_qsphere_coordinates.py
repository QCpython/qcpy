import numpy as np


def get_qsphere_coordinates(num_qubits: int, lat_vals):
    coords = []
    phi = []
    theta = []

    for i in range(len(lat_vals)):
        temp_arr = np.linspace(
            2 * (np.pi) / len(lat_vals[i]), 2 * (np.pi), len(lat_vals[i])
        )
        theta.append(temp_arr)

    phi = np.linspace(0, np.pi, num_qubits + 1)

    for i in range(len(phi)):
        for j in range(len(theta[i])):
            x1 = 1 * np.sin(phi[i]) * np.cos(theta[i][j])
            y1 = 1 * np.sin(phi[i]) * np.sin(theta[i][j])
            z1 = 1 * np.cos(phi[i])
            x, y, z = [0, x1], [0, y1], [0, z1]
            coords.append([x, y, z])

    return coords
