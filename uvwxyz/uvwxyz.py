from math import cos, sin
from astropy.coordinates import SkyCoord
import numpy as np


def uvw(ra, dec, d, pmra, pmde, rv):
    """
    Function to calculate UVW given RA, Dec, Distance, RV, and PMs
    Adapted from http://idlastro.gsfc.nasa.gov/ftp/pro/astro/gal_uvw.pro

    :param ra: Right Ascension in degrees
    :param dec: Declination in degrees
    :param d: Distance in parsecs
    :param pmra: Proper motion in RA in milli-arcseconds/year
    :param pmde: Proper motion in Dec in milli-arcseconds/year
    :param rv: Radial velocity in km/s

    :return: U, V, W in km/s

    """

    k = 4.74047  # Equivalent of 1 A.U/yr in km/s
    A00 = 0.0548755604
    A01 = 0.8734370902
    A02 = 0.4838350155
    A10 = 0.4941094279
    A11 = -0.4448296300
    A12 = 0.7469822445
    A20 = -0.8676661490
    A21 = -0.1980763734
    A22 = 0.4559837762

    # Set as arrays in case ra, dec, etc were lists
    ra = np.array(ra)
    dec = np.array(dec)
    d = np.array(d)
    rv = np.array(rv)
    pmra = np.array(pmra)
    pmde = np.array(pmde)

    radcon = 3.1415926/180  # radian conversion factor

    try:
        cosd = cos(dec * radcon)
        sind = sin(dec * radcon)
        cosa = cos(ra * radcon)
        sina = sin(ra * radcon)
    except TypeError:  # For arrays
        cosd = np.array(map(cos, dec * radcon))
        sind = np.array(map(sin, dec * radcon))
        cosa = np.array(map(cos, ra * radcon))
        sina = np.array(map(sin, ra * radcon))

    vec1 = rv
    plx = 1000./d
    vec2 = k * pmra/plx
    vec3 = k * pmde/plx

    u = (A00*cosa*cosd + A01*sina*cosd + A02*sind) * vec1 + \
        (-A00*sina + A01*cosa) * vec2 + \
        (-A00*cosa*sind - A01*sina*sind + A02*cosd) * vec3
    v = (A10*cosa*cosd + A11*sina*cosd + A12*sind) * vec1 + \
        (-A10*sina + A11*cosa) * vec2 + \
        (-A10*cosa*sind - A11*sina*sind + A12*cosd) * vec3
    w = (A20*cosa*cosd + A21*sina*cosd + A22*sind) * vec1 + \
        (-A20*sina + A21*cosa) * vec2 + \
        (-A20*cosa*sind - A21*sina*sind + A22*cosd) * vec3
    u = -u  # Flipping U to be positive towards Galactic center

    return u, v, w


def xyz(ra, dec, d):
    """
    Function to calculate XYZ given RA, Dec, and Distance

    :param ra: Right Ascension in degrees
    :param dec: Declination in degrees
    :param d: Distance in parsecs

    :return: X, Y, Z in parsecs
    """

    ra = np.array(ra)
    dec = np.array(dec)
    d = np.array(d)

    c = SkyCoord(ra=ra, dec=dec, frame='icrs', unit='deg')
    l, b = c.galactic.l.radian, c.galactic.b.radian

    try:
       xgc = d * cos(b) * cos(l)
       ygc = d * cos(b) * sin(l)
       zgc = d * sin(b)
    except TypeError:  # For arrays
        xgc = d * map(cos, b) * map(cos, l)
        ygc = d * map(cos, b) * map(sin, l)
        zgc = d * map(sin, b)

    return xgc, ygc, zgc

