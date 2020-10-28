import numpy as np
from matplotlib import pyplot as plt


def graph_press(t_i, t_ie, x, t_total, b, p_lim, control):
    graph = []
    cnt = p_lim / b ** 2 if control is "Pressure" else t_i / np.exp(-2 * t_i)
    for i in range(len(x)):
        value = fx(x[i], t_i, t_ie, cnt, t_total, p_lim, b, control)
        if value is None:
            value = 0
        graph.append(value)

    return graph


def fx(x, t_i, t_ie, cnt, t_total, p_lim, b, control):
    if t_ie < x <= t_total:
        return 0
    if control == "Pressure":
        if 0 < x <= b:
            return p_lim - cnt * (x - b) ** 2
        elif b < x <= t_i:
            return p_lim
        elif t_i < x <= t_ie:
            return (p_lim * np.exp(2 * t_i)) * np.exp(-2 * x)
    elif control == "Volume":
        if 0 < x <= t_i:
            return x
        elif t_i < x <= t_ie:
            return cnt * np.exp(-2 * x)


def values_graph(peep, p_lim, x, g, bpm):
    y = peep + ((p_lim - peep) * (np.divide(g, np.max(g))))

    new_x = np.arange(0., 60, 0.1)
    new_y = np.tile(y, bpm)

    fig = plt.figure()
    ax_gen = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax_prof = fig.add_axes([0.55, 0.55, 0.3, 0.3])

    ax_gen.plot(new_x, new_y)
    ax_gen.set_ylim(0, np.max(new_y) + 10)
    ax_gen.set_xlim(0, np.max(new_x))
    ax_gen.set_ylabel('P_ao')
    ax_gen.set_xlabel('Time (s)')
    ax_gen.set_title('Pressure on a minute')

    ax_prof.plot(x, y)
    ax_prof.set_ylim(peep, np.max(y) + 10)
    ax_prof.set_xlim(0, np.max(x))
    ax_prof.set_ylabel('P_ao')
    ax_prof.set_xlabel('Time (s)')
    ax_prof.set_title('Profile')

    plt.show()
