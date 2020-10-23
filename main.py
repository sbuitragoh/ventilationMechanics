import numpy as np
import ventilationMode as vm
import graphFunctions as gf

# Test for the system
if __name__ == '__main__':
    vent = vm.ventMode("Pressure", "AC")
    vent.evergreenParam(P_lim = 100, PEEP = 5, bpm = 15, IE = np.array([1, 3]))
    vent.opcParam(r_s = 0.5)
    vent.calcParam()

    x = np.arange(0, vent.t_Total, 0.1)

    graph = gf.graphPress(t_I = vent.t_I,
                          t_IE = vent.t_IE,
                          x = x,
                          t_Total = vent.t_Total,
                          b = vent.b,
                          P_lim = vent.P_lim,
                          control = vent.control)

    gf.valuesGraph(PEEP = vent.PEEP,
                P_lim = vent.P_lim,
                x = x,
                g = graph,
                bpm = vent.bpm)