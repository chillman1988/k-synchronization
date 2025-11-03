# src/compute_rotation_curve.py
import numpy as np

def radial_profile(data, center=None):
    y, x = np.indices(data.shape)
    if center is not None:
        x -= center[0]; y -= center[1]
    r = np.sqrt(x**2 + y**2).astype(int)
    tbin = np.bincount(r.ravel(), data.ravel())
    nr = np.bincount(r.ravel())
    radial = tbin / nr
    return np.arange(len(radial)), radial

def newtonian_potential(I_norm):
    return -poisson_inverse_2d(I_norm)

def rotation_curve(Phi_eff, r):
    dPhi_dr = np.gradient(Phi_eff, r, axis=0)
    v_circ = np.sqrt(r * dPhi_dr)
    return np.nan_to_num(v_circ, nan=0.0)
