# src/solve_yukawa_fft.py
import numpy as np
from scipy.fft import fft2, ifft2, fftfreq

def solve_yukawa_fft(kappa, ell, pixel_scale=1.0):
    ny, nx = kappa.shape
    kx = fftfreq(nx, d=pixel_scale)
    ky = fftfreq(ny, d=pixel_scale)
    kx, ky = np.meshgrid(kx, ky)
    k2 = kx**2 + ky**2
    denom = k2 + 1/ell**2
    denom[0, 0] = 1
    F_kappa = fft2(kappa)
    F_K = F_kappa / denom
    K = ifft2(F_K).real
    return K
