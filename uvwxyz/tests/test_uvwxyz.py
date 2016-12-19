# Tests

from uvwxyz.uvwxyz import uvw, xyz

# TW Hya from Simbad
ra = 165.46627797
dec = -34.70473119
pmra = -66.19
pmdec = -13.9
dist = 53.7
rv = 13.4


def test_uvw():
    u,v,w = uvw(ra, dec, dist, pmra, pmdec, rv)
    assert round(u, 2) == -10.87
    assert round(v, 2) == -18.35
    assert round(w, 2) == -4.59


def test_xyz():
    x, y, z = xyz(ra, dec, dist)
    assert round(x, 2) == 7.46
    assert round(y, 2) == -48.88
    assert round(z, 2) == 20.94
