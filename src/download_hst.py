# src/download_hst.py
from astropy.utils.data import download_file
import os

def download_m51():
    url = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:HST/product/icj0a1i8q_flc.fits"
    path = download_file(url, cache=True)
    print(f"M51 FLC downloaded: {path}")
    return path

if __name__ == "__main__":
    download_m51()
