import numpy as np
import ventilation_mode as vm
import graph_functions as gf

# Test for the system
if __name__ == '__main__':
    vent = vm.VentMode("Pressure", "AC", p_lim=100, peep=5, bpm=15, ie=np.array([1, 3]), r_s=0.5)
    vent.calc_param()

    x = np.arange(0, vent.t_total, 0.1)

    graph = gf.graph_press(t_i=vent.t_i,
                           t_ie=vent.t_ie,
                           x=x,
                           t_total=vent.t_total,
                           b=vent.b,
                           p_lim=vent.p_lim,
                           control=vent.control)

    gf.values_graph(peep=vent.peep,
                    p_lim=vent.p_lim,
                    x=x,
                    g=graph,
                    bpm=vent.bpm)
