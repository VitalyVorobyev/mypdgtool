#! /usr/bin/python3

""" Set of tools to summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

import numpy as np
import matplotlib.pyplot as plt

PN = {
    'dsst' : r'D_{s}^{*+}',
    'ds0'  : r'D_{s0}^{\ast}\left(2317\right)^+',
    'ds1'  : r'D_{s1}^{+}(2460)'
}

OBS = {
    'M173R1' : r'B(' + PN['ds1'] + ' \to ' + PN['dsst'] + '\pi^{0})'
}

def average(meas):
    """ Average over several measurements """
    vals = np.array([m.val for m in meas])
    errp = np.array([m.Errp() for m in meas])
    errn = np.array([m.Errn() for m in meas])
    err = 0.5 * (errp + errn)
    errp = 1./np.sqrt(sum([1./x**2 for x in errp]))
    errn = 1./np.sqrt(sum([1./x**2 for x in errn]))
    print(vals)
    print(1./err**2)
    return (np.average(vals, weights=1./err**2), [[errp], [errn]])

def ds0_masses():
    """ List of Ds0(2317) mass measurements """
    par = r'$m\left(' + PN['ds0'] + r'\right)$'
    unit = r'MeV/$c^2$'
    return [
        Measurement(2318.3, [1.2, 1.2], par=par, unit=unit,\
            ref='PRD86.051103', year=2018, col='BESIII'),
        Measurement(2319.6, [0.2, 1.4], par=par, unit=unit,\
            ref='PRD74.032007', year=2006, col='BaBar'),
        Measurement(2317.2, [0.5, 0.9], par=par, unit=unit,\
            ref='PRL92.012002', year=2004, col='Belle'),
    ]

def ds1_masses():
    """ List of Ds1(2460) mass measurements """
    par = r'$m(D_{s1}^{+}(2460))$'
    unit = r'MeV/$c^2$'
    return [
        Measurement(2460.1, [0.2, 0.8], par=par, unit=unit,\
            ref='PRD74.032007', year=2006, col='BaBar'),
        Measurement(2456.5, [1.3, 1.3], par=par, unit=unit,\
            ref='PRL92.012002', year=2004, col='Belle'),
    ]

def make_figure(meas):
    """ Comparison plot """
    plt.rc('font', size=16)

    val, errp, errn, lbl = [], [], [], ['Average']
    par_name = meas[0].par + ', ' + meas[0].unit
    for m in meas:
        val.append(m.val)
        errp.append(m.Errp())
        errn.append(m.Errn())
        lbl.append(m.col + ' ' + str(m.year))

    fig = plt.figure(num=1, figsize=(6, len(meas)), dpi=120, facecolor='w', edgecolor='k')
    y = list(range(len(meas)+1))
    plt.yticks(y, lbl)
    plt.errorbar(val, y[1:], xerr=[errp, errn], fmt='o', markersize=4, linewidth=2)
    mean, merr = average(meas)
    print('Average: {} +- {}'.format(mean, merr[0][0]))
    plt.errorbar(mean, y[0], xerr=merr, fmt='o', markersize=4, linewidth=2)
    plt.grid()
    plt.xlabel(par_name)
    plt.tight_layout()
    return fig

def mass_dso_plot(meas):
    """ Dso plot """
    fig = make_figure(meas)
    plt.gca().set_xticks(np.linspace(2316, 2321, 26), minor=True)
    plt.gca().xaxis.grid(True, which='minor', linestyle='--', linewidth=0.5)
    plt.show()

def main():
    """ The main """
    mass_dso_plot(ds0_masses())

if __name__ == '__main__':
    main()
