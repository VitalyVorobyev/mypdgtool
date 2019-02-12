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
              Correct errors examples:
               - float (single symmetric error)
               - [float, float, ...] (several symmetric errors)
               - (float, float) (single asymmetric error)
               - [float, (float, float)] (one symmetric and one asymmetric error)
               - [(float, float), (float, float), ...] (several asymmetric errors)
        """
        self.pcl  = pcl
        self.prop = prop
        self.val  = val
        self.unit = unit
        self.cl = cl
        self.nevt = nevt
        self.decay = decay
        self.comment = comment
        self.parseUncert(err)
        print(self.val, self.err())

    def __call_(self):
        """ Return val """
        return self.val

    def __parseErr(self, err):
        """ """
        if isinstance(err, float):
            return (err, err)
        elif isinstance(err, tuple):
            assert(len(err) == 2)
            return err

    def parseUncert(self, err):
        """ Calculate positive and negative uncertainties """
        if isinstance(err, list):
            epos, eneg = [], []
            for e in err:
                ep, en = self.__parseErr(e)
                epos.append(ep)
                eneg.append(en)
            self.errp = np.sqrt(np.sum(np.array(epos)**2))
            self.errn = np.sqrt(np.sum(np.array(eneg)**2))
        else:
            self.errp, self.errn = self.__parseErr(err)

    def err(self):
        """ Return (errp, errn]) """
        return (self.errp, self.errn)
