import matplotlib.pyplot as plt
import numpy as np
def plot(maximum_S, title):
    t = np.arange(0, len(maximum_S))/2
    plt.rcParams['font.family'] = 'serif'
    PLOT = plt.figure(figsize = (6.5, 3.37), dpi = 300.0)
    plt.rc('axes', titlesize =  8) 
    plt.title("Зависимость площади самой большой области от номера кадра ")
    plt.plot(t, maximum_S, '#FF0055', linewidth = 2, label = f'{title}')
    plt.ylabel('Площадь (S), $\mu$m$^2$')
    plt.legend()
    plt.xlabel('Время t, мин')
    plt.grid(which = 'major')
    plt.grid(which = 'minor')
    plt.minorticks_on()
    df = []
    for i in range(len(t)):
        if t[i] % 60 == 0:
            df.append(int(t[i]//60))
    plt.xticks (ticks=np.arange(min(t), max(t), 60.0), labels=df) 
    plt.show()
    return PLOT