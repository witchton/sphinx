# -*- coding: utf-8 -*-
"""
sphinx main module
Created on Fri Aug  5 20:28:53 2016

@author: joonaskorhonen
"""

from sys import argv

from init import Initialisation
from system import System


if __name__ == '__main__':
    initpath = argv[1]
    respath = argv[2]
    init = Initialisation(initpath)
    system = System(init)
    while not system.has_ended:
        system.run_timestep()
        system.write_results(respath)
        print(system.state)
