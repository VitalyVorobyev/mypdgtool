""" Set of tools for summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

import pandas as pd

class RefInfo(object):
    """ Standard reference info """
    def __init__(self, exp, year, auth, title, ref, doi, arx, comment=None):
        """ Constructor """
        self.data = pd.Series({'exp' : exp, 'year' : year, 'auth' : auth,  'title' : title,
                               'ref' : ref,  'doi' : doi,   'arx' : arx, 'comment' : comment})

    def exp(self):
        """ """
        return self.data['exp']

    def year(self):
        """ """
        return self.data['year']

    def auth(self):
        """ """
        return self.data['auth']

    def title(self):
        """ """
        return self.data['title']

    def ref(self):
        """ """
        return self.data['ref']

    def doi(self):
        """ """
        return self.data['doi']

PDGPUB = {
    ### Ds(2317) and Ds(2460) ###
    49615 : RefInfo('Belle', 2003, 'P. Krokovny et al. (Belle Collaboration)',
                    r'Observation of the $D_{sJ}(2317)$ and $D_{sJ}(2457)$ in $B$ Decays',
                    'Phys. Rev. Lett. 91 (2003) 262002', '10.1103/PhysRevLett.91.262002',
                    'hep-ex/0308019'
                    ),
    49583 : RefInfo('CLEO', 2003, 'D. Besson et al. (CLEO Collaboration)',
                    r'Observation of a narrow resonance of mass $2.46 GeV/c^2$\
                    decaying to $D^{*+}_s\pi^0$ and confirmation of the $D{*}_{sJ}(2317)$ state',
                    'Phys. Rev. D68 (2003) 032002', '10.1103/PhysRevD.75.119908',
                    'hep-ex/0305017', 'Erratum 10.1103/PhysRevD.75.119908'
                    ),
    49417 : RefInfo('BaBar', 2003, 'B. Aubert et al. (BaBar Collaboration),',
                    r'Observation of a Narrow Meson Decaying to $D_s^+\pi^0$\
                    at a Mass of $2.32 GeV/c^2$',
                    'Phys. Rev. Lett. 90 (2003) 242001', '10.1103/PhysRevLett.90.242001',
                    'hep-ex/0304021'
                    ),
    ### Ds1(2536) ###
    40914 : RefInfo('ARGUS', 1989, 'H. Albrecht et al. (ARGUS Collaboration)',
                    'Observation of a new charmed-strange meson',
                    'Phys. Lett. B230 (1989) 162', '10.1016/0370-2693(89)91672-9', ''
                    ),
    40916 : RefInfo('FNAL-E-0180', 1988, 'A.E. Asratyan, A.V. Fedotov, P.A. Goritchev et al.',
                    r'Studying $\bar{c}s$ spectroscopy in $\bar{\nu}N$ collisions',
                    'Z. Phys. C 40 (1988) 483', '10.1007/BF01560218', '',
                    r'$\bar{\nu}N collisions$'
                    ),
    43667 : RefInfo('CERN-PPE-93-190', 1994, 'A.E. Asratyan, M. Aderholz, V.V. Ammosov et al.',
                    r'Observation of $D_s^{**}(2536)$ meson production by neutrinos in BEBC',
                    'Z. Phys. C 61 (1994) 563', '10.1007/BF01552622', '',
                    r'$\bar{\nu}N collisions$'
                   )
}

class PDGref(object):
    """ PDG references encoding """
    def __init__(self, pdgid, results, comment=None):
        """ Constructor """


if __name__ == '__main__':
    import arxiv
    paper = arxiv.query(id_list=['hep-ex/0308019'])[0]
    for key, val in paper.iteritems():
        print('{} : {}'.format(key, val))
    # print(paper)
