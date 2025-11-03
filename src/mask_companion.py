# src/mask_companion.py
import numpy as np
from photutils.aperture import EllipticalAperture

def mask_ngc5195(data, center=(120, 150), a=40, b=25, theta=45):
    mask = np.zeros(data.shape, dtype=bool)
    aperture = EllipticalAperture(center, a, b, theta=np.radians(theta))
    mask |= aperture.to_mask().to_image(data.shape).astype(bool)
    data[mask] = np.nan
    return data
