#! /usr/bin/python3

import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

NUMBER = re.compile('[-+]?\d*\.\d+|\d+')
DATAPATH = '/home/vitaly/work/PDG/DsSpec/data/'
DATAFILE = 'belle_xsection.txt'

def md():
    """ D meson mass """
    return 1.865

def mdst():
    """ D* meson mass """
    return 2.01

def read_table(infile):
    """ Read crossection table """
    table = []
    with open(infile) as file:
        for line in file:
            floats = re.findall(NUMBER, line)
            floats = [float(x) for x in floats]
            if len(floats) == 4:
                table.append(floats + [0., 0., 0.])
            else:
                table.append(floats)
    return np.array(table)

def get_xsec_ddst(table):
    """ Prepare data for plot """
    return (table[:, 0], table[:, 1], np.sqrt(table[:, 2]**2 + table[:, 3]**2))

def get_xsec_dstdst(table, drop=0):
    """ Prepare data for plot """
    return (table[drop:, 0], table[drop:, 4], np.sqrt(table[drop:, 5]**2 + table[drop:, 6]**2))

def plot_xsections(table):
    """ Make plots """
    plt.rc('font', size=24)
    energy, ddst_val, ddst_err = get_xsec_ddst(table)
    energy, dstdst_val, dstdst_err = get_xsec_dstdst(table)
    fig = plt.figure(num=1, figsize=(8, 6), dpi=120, facecolor='w', edgecolor='k')
    plt.errorbar(energy, ddst_val, yerr=ddst_err, fmt='o', markersize=2, linewidth=1, label=r'$DD^{\ast}$')
    plt.errorbar(energy, dstdst_val, yerr=dstdst_err, fmt='D',  markersize=2, linewidth=1, label=r'$D^{\ast}D^{\ast}$')
    plt.grid()
    plt.ylim([0., 5.5])
    plt.xlabel('Energy, GeV/' + r'$c^2$')
    plt.ylabel(r'$\sigma_{e^+e^-\to D^{(\ast)}D^{\ast}}$, nb')
    fig.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def plot_and_fit_ddst(x, y, yerr):
    z = np.poly1d(np.polyfit(x, y, 150, w = 1./yerr))
    # popt, pconv = op.curve_fit(linear, x, y, sigma=yerr)
    fig = plt.figure(num=2, figsize=(8, 6), dpi=120, facecolor='w', edgecolor='k')
    plt.errorbar(x, y, yerr=yerr, fmt='o', markersize=2, linewidth=1)#, label=r'$DD^{\ast}$')
    plt.plot(x, z(x), '-')
    plt.grid()
    plt.ylim([0., 5.5])
    plt.xlabel('Energy, GeV/' + r'$c^2$')
    plt.ylabel(r'$\sigma_{e^+e^-\to D^{(\ast)}D^{\ast}}$, nb')
    # fig.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def main():
    table = read_table(DATAPATH + DATAFILE)
    plot_xsections(table)
    # energy, ddst_val, ddst_err = get_xsec_ddst(table)
    # plot_and_fit_ddst(energy, ddst_val, ddst_err)
    # energy, dstdst_val, dstdst_err = get_xsec_dstdst(table, 17)
    # plot_and_fit_ddst(energy, dstdst_val, dstdst_err)


if __name__ == '__main__':
    main()