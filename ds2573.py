""" """

from Measurement import Measurement
from PDGid import PDGPID

def massDs2573():
    """ """
    pcl, par = PDGPID['M148'], 'M148M'
    return [
        Measurement(pcl, par, 2573.2, [(2.7, -2.3), 0.8], r'$MeV/c^{2}$',
            1., 217, r'$e^+e^-\to D^0K^+X$', 'CLEO94'),
        Measurement(pcl, par, 2574.5, [3.3, 1.6], r'$MeV/c^{2}$',
            1., 93, r'$e^+e^-\to D^0K^+X$', 'ARGUS95'),
        Measurement(pcl, par, 2572.2, [0.3, 1.0], r'$MeV/c^{2}$',
            1., 10000, r'$e^+e^-\to DKX$', 'BABAR06'),
        Measurement(pcl, par, 2569.4, [1.6, 0.5], r'$MeV/c^{2}$',
            1., 82, r'$\bar{B}_s^0\to D_s^+KX\mu^-\bar{\nu}$', 'LHCB11'),
        Measurement(pcl, par, 2568.39, [0.29, 0.19, 0.18], r'$MeV/c^{2}$',
            1., 2500, r'$B_s^0\to\bar{D}^0K^-\pi^+$', 'LHCB14'),
        Measurement(pcl, par, 2570.7, [2.0, 1.7], r'$MeV/c^{2}$',
            1., 2500, r'$e^+e^-\to D_s^+\bar{D}^0K^-X$', 'BESIII19')
    ]
