import matplotlib.pyplot as plt
import numpy as np

Nx = 500
Ny = 500

Nit = 25

z_r = np.linspace(-2 + 2.5*0.0/500.0, -2 + 2.5*500.0/500.0, Nx)
z_i = np.linspace(-1.5 +3.0*0.0/500.0, -1.5 + 3.0*500.0/500.0, Ny)
z = np.zeros((Nx,Ny), dtype = complex)
for i in range(1,Nx):
    for n in range(1,Ny):
        z[i][n] = z_r[i] + 1j*z_i[n]

def iterate(c, Nit):
    out = 0
    for i in range(0, Nit):
        out = out**2 + c
        if abs(out) >2:
            out = 2
            break
    return out

z_Mandel = np.zeros((Nx, Ny), dtype=float)
for i in range (1,Nx):
    for n in range(1, Ny):
        z_Mandel[i][n] = iterate(z[i][n], Nit)
        if abs(z_Mandel[i][n]) > 2:
            z_Mandel[i][n] = 0
        else:
            z_Mandel[i][n] = abs(z_Mandel[i][n])

plt.imshow(z_Mandel.transpose(), cmap='seismic')
plt.show()
