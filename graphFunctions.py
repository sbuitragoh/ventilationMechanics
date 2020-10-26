import numpy as np
from matplotlib import pyplot as plt

def graphPress(t_I, t_IE, x, t_Total, b, P_lim, control):
    graph = []
    cnt = P_lim / b**2 if control is "Pressure" else t_I / np.exp(-2*t_I)
    for i in range(len(x)):
        value = fx(x[i],t_I, t_IE, cnt, t_Total, P_lim, b, control)
        if value is None: value=0
        graph.append(value)

    return graph

def fx(x,t_I, t_IE, cnt, t_Total, P_lim, b, control):
    if (t_IE < x <= t_Total): return 0
    if control is "Pressure":
        if (0 < x <= b): return P_lim - cnt * (x - b) ** 2
        elif (b < x <= t_I): return P_lim
        elif (t_I < x <= t_IE): return (P_lim * np.exp(2 * t_I)) * np.exp(-2 * x)
    elif control is "Volume":
        if (0 < x <= t_I): return x
        elif (t_I < x <= t_IE): return cnt * np.exp(-2 * x)

def valuesGraph(PEEP, P_lim, x, g, bpm):
    y = PEEP + ((P_lim - PEEP) * (np.divide(g, np.max(g))))

    newX = np.arange(0., 60, 0.1)
    newY = np.tile(y, bpm)

    fig = plt.figure()
    ax_gen = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax_prof = fig.add_axes([0.55, 0.55, 0.3, 0.3])

    ax_gen.plot(newX, newY)
    ax_gen.set_ylim(0, np.max(newY) + 10)
    ax_gen.set_xlim(0, np.max(newX))
    ax_gen.set_ylabel('P_ao')
    ax_gen.set_xlabel('Time (s)')
    ax_gen.set_title('Pressure on a minute')

    ax_prof.plot(x, y)
    ax_prof.set_ylim(PEEP, np.max(y) + 10)
    ax_prof.set_xlim(0, np.max(x))
    ax_prof.set_ylabel('P_ao')
    ax_prof.set_xlabel('Time (s)')
    ax_prof.set_title('Profile')

    plt.show()