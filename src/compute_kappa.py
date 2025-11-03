# src/compute_kappa.py
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.fft import fft2, ifft2, fftfreq

def poisson_inverse_2d(I_norm, pixel_scale=1.0):
    ny, nx = I_norm.shape
    kx = fftfreq(nx, d=pixel_scale)
    ky = fftfreq(ny, d=pixel_scale)
    kx, ky = np.meshgrid(kx, ky)
    k2 = kx**2 + ky**2 + 1e-10
    F = fft2(I_norm)
    inv = -ifft2(F / k2).real
    inv -= inv.mean()
    return inv

def fisher_information(I_norm, eps=1e-6):
    p = I_norm + eps
    p /= p.sum()
    grad_x = np.gradient(p, axis=1)
    grad_y = np.gradient(p, axis=0)
    return p * (grad_x**2 + grad_y**2)

def compute_kappa(I_norm, a=1.0, b=0.5, c=0.3):
    I_smooth = gaussian_filter(I_norm, sigma=1)
    term1 = a * I_smooth
    term2 = b * poisson_inverse_2d(I_smooth)
    term3 = c * fisher_information(I_norm)
    return term1 + term2 + term3
