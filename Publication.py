""" Set of tools to summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

class Publication(object):
    """ Experimental Publication """
    def __init__(self, pdgid, results, comment=None):
        """ Constructor """
        self.pdgid = pdgid
        self.meas = results
        self.comm = comment
