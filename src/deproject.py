# src/deproject.py
import numpy as np
from astropy.wcs import WCS
from reproject import reproject_interp
from astropy.io import fits

def deproject_image(hdu, incl=22, pa=173):
    wcs = WCS(hdu.header)
    data = hdu.data
    header_faceon = wcs.to_header()
    header_faceon['CTYPE1'] = 'GLON-CAR'
    header_faceon['CTYPE2'] = 'GLAT-CAR'
    header_faceon['CRVAL1'] = wcs.wcs.crval[0]
    header_faceon['CRVAL2'] = wcs.wcs.crval[1]
    header_faceon['CD1_1'] = np.cos(np.radians(incl)) * header_faceon.get('CD1_1', 1)
    array, _ = reproject_interp(hdu, header_faceon)
    return array, WCS(header_faceon)
