import numpy as np
import ventilation_mode as vm
import graph_functions as gf
import serialInformation as si

if __name__ == '__main__':
    vent = vm.VentMode("Shark",
                       "AC",
                       p_lim = 100,
                       peep = 5,
                       bpm = 15,
                       ie = np.array([1, 3]),
                       t_apn = 2,
                       r_s = 0.5)

    vent.calc_param()

    x = np.arange(0, vent.t_total, 0.1)

    args = (x, vent.p_lim, vent.peep)
    kwargs = {"b": vent.b,
              "t_i": vent.t_i,
              "t_ie": vent.t_ie,
              "t_total": vent.t_total}

    y = gf.graph_press(vent.control, *args, **kwargs)


    gf.values_graph(peep = vent.peep,
                    bpm = vent.bpm,
                    x = x,
                    y = y)

    y = y[..., np.newaxis]
    si.toSent(y, peep=vent.peep, bpm=vent.bpm, t_apn=vent.t_apn)