""" """

import numpy as np

sqrt2pi = np.sqrt(2*np.pi)

def Gauss(x, mean, sigma):
    """ Gaussian pdf """
    return np.exp(-0.5 * (x - mean)**2 / sigma) / (sigma * sqrt2pi)

def BifurGauss(x, mean, sigmas):
    """ Gaussian pdf """
    result = np.empty(len(x), dtype=np.float32)
    mask = x < mean
    result[mask] = Gauss(x[mask], mean, sigmas[1])
    result[~mask] = Gauss(x[~mask], mean, sigmas[0])
    return result

def GaussPlot(mvec):
    """ Takes list of measurements and makes a Gauss plot """
    fig = plt.figure()

    legde, redge = np.infty, -np.infty
    mean, sigma, label = [], [], []
    for m in mvec:
        mean.append(m.val)
        sigma.append(m.err())
        label.append(m.comment)
        legde = min(legde, m.val - 3.*m.errn)
        redge = max(redge, m.val + 3.*m.errp)
    print(legde, redge)
    x = np.linspace(legde, redge, 1000)
    print(x)
    line = np.zeros(len(x), dtype=np.float32)
    for m, s, l in zip(mean, sigma, label):
        # y = BifurGauss(x, m, s)
        y = Gauss(x, m, max(s))
        plt.plot(x, y, label=l)
        line = line + y
    plt.plot(x, line, label='Total')
    plt.grid()
    plt.legend(loc='best')
    plt.tight_layout()
    return fig

if __name__ == '__main__':
    from ds2573 import massDs2573
    import matplotlib.pyplot as plt
    fig = GaussPlot(massDs2573())
    plt.show()
