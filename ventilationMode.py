import numpy as np

# Here lies the Ventilation Mode Object
class ventMode:
    def __init__(self, control, mode):
        self.control = control
        self.mode = mode

    def evergreenParam(self, P_lim, PEEP, bpm, IE):
        self.P_lim = P_lim
        self.PEEP = PEEP
        self.bpm = bpm
        self.IE = IE

    def opcParam(self, t_apn=0, r_s=0):
        self.t_apn = t_apn
        self.r_s = r_s

    def calcParam(self):
        self.t_IE = 60 / self.bpm
        self.t_I = self.t_IE * self.IE[0] / np.sum(self.IE)
        self.t_E = self.t_IE * self.IE[1] / np.sum(self.IE)
        self.t_Total = self.t_IE + self.t_apn
        self.b = self.r_s * self.t_I