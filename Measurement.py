""" Set of tools to summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

import numpy as np

class Measurement(object):
    """ Single measurement """
    def __init__(self, pcl, prop, val, err, unit, cl, nevt, decay, comment):
        """ Construtor 
            Args:
              pcl  : studied particle (PDG code)
              prop : property measured (PDG code)
              nevt : signal yield
              val  : central value measured
              unit : units
              err  : tuple of lists for positive and negative uncertainties
        """
        self.pcl  = pcl
        self.prop = prop
        self.val  = val
        self.unit = unit
        self.err  = err

    def __call_(self):
        """ Return val """
        return self.val

    def Errp(self):
        """ Posi error """
        return np.sqrt(np.sum(self.errp**2))
    
    def Errn(self):
        """ Nega error """
        return np.sqrt(np.sum(self.errn**2))

    def err(self):
        """ Return [errp, errn] """
        [self.errp(), self.errn()]
