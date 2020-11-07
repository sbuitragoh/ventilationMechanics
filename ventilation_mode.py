import numpy as np


# Here lies the Ventilation Mode Object
class VentMode:
    def __init__(self, control, mode, p_lim, peep, bpm, ie, t_apn=0, r_s=0):
        self.control = control
        self.mode = mode
        self.p_lim = p_lim
        self.peep = peep
        self.bpm = bpm
        self.ie = ie
        self.t_apn = t_apn
        self.r_s = r_s
        self.t_ie = 0
        self.t_i = 0
        self.t_e = 0
        self.t_total = 0
        self.b = 0

    def calc_param(self):
        self.t_ie = 60 / self.bpm
        self.t_i = self.t_ie * self.ie[0] / np.sum(self.ie)
        self.t_e = self.t_ie * self.ie[1] / np.sum(self.ie)
        self.t_total = self.t_ie
        self.b = self.r_s * self.t_i