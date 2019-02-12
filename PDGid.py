""" Set of tools to summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

PDGPID = {
    ### Unflavored ###

    ### Charmed ###
    'S031' : r'D^{\pm}',
    'S032' : r'D^{0}',
    'M061' : r'D^{*}(2007)^{0}',
    'M062' : r'D^{*}(2010)^{\pm}',
    ### Charm-strange ###
    'S034' : r'D_{s}^{\pm}',
    'M074' : r'D_{s}^{*\pm}',
    'M172' : r'D_{s0}^{*}(2317)^{\pm}',
    'M173' : r'D_{s1}(2460)^{\pm}',
    'M148' : r'D_{s2}(2573)^{\pm}',
    ### Bottom ###
    'S041' : r'B^{\pm}',
    'S042' : r'B^{0}',
}

class PDGid(object):
    ID = PDGPID
    """ PDG particle encoding """
    def __init__(self):
        """ Constructor """
    
    @staticmethod
    def __call__(code):
        """ """
        assert(code in PDGid.ID)
        return PDGid.ID[code]

    @staticmethod
    def get(code):
        """ """
        assert(code in PDGid.ID)
        return PDGid.ID[code]
