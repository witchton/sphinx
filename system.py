# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:37:45 2016

@author: joonaskorhonen
"""


class System:
    def __init__(self, init):
        """ Construct simulation

        Arguments
        =========
        init: Initialisation
            The system initial state and parameters
        """
        return

    @property
    def has_ended(self):
        return self.time >= self.total_time

    @property
    def state(self):
        return

    def run_system():
        """ Run the system forward for one timestep.
        """
        return

    def write_state(respath=None):
        """ Write current system state into file

        Arguments
        =========
        respath: None | fpath
            If None, results are written into stdout, otherwise they are
            appended into file in fpath.
        """
        return
