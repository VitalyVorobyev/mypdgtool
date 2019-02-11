""" Set of tools to summarizing experimental results in particle physics

    Author: Vitaly Vorobyev (vvorob@inp.nsk.su)
    Version: 0.1
    Last modification: 24.12.2018
"""

from PDGid import PDGid
from PDGref import PDGref

from Measurement import Measurement
from Publication import Publication

M172Nodes = {
    'M172M'   :             r'{} MASS'.format(PDGid.get('M172')),
    'M172DM'  : r'm_{{{}}} - m_{{{}}}'.format(PDGid.get('M172'), PDGid.get('S034')),
    'M172W'   :            r'{} WIDTH'.format(PDGid.get('M172')),
    'M172215' :      r'{} DECAY MODES'.format(PDGid.get('M172')),
    'M172215' : r'{} BRANCHING RATIOS'.format(PDGid.get('M172')),
}

def ref49615():
    """ Belle', 2003, 'P. Krokovny et al """
    return Publication(49615,[
        Measurement('M172', 'M172M',  '123.8 x 10^6 BBbar events'),
        Measurement('M172', 'M172DM', '123.8 x 10^6 BBbar events')
    ]

    )

if __name__ == '__main__':
    print('{} summary (PDG ID {})'.format(PDGid.get('M172'), 'M172'))
    for key, val in M172Nodes.items():
        print('{} : {}'.format(key, val))
