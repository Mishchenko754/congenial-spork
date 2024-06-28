import matplotlib.pyplot as plt
import numpy as np
def plot_square_to_time(squares_max, title):
    '''
Принимает на вход:

squares_max (list) - массив, содержащий в себе значения
максимальной площади светлой области для каждого кадра;

- title (str) - строковый объект, который будет являтся
заголовком графика и указывать на тип видеозаписи.
Пример:
squares_max = [1.1, 1.1, 2.2, 3.3]
plot_of_square_of_events.plot_square_to_time(squares_max, title='square, S')

На выходе функция выдает график, по оси X которого отложено время (мин),
по оси Y - значения площади (в кв. мкм).
Объект сохраняется в переменную PLOT.
    '''
    t = np.arange(0, len(squares_max)) / 2
    plt.rcParams['font.family'] = 'serif'
    figure = plt.figure(figsize=(6.5, 3.37), dpi=300.0)
    plt.rc('axes', titlesize=8)
    plt.title("Зависимость площади самой большой области от номера кадра ")
    plt.plot(t, squares_max, '#FF0055', linewidth=2, label=f'{title}')
    plt.ylabel('Площадь (S), $\mu$m$^2$')
    plt.legend()
    plt.xlabel('Время t, мин')
    plt.grid(which='major')
    plt.grid(which='minor')
    plt.minorticks_on()
    minits = []
    for i in range(len(t)):
        if t[i] % 60 == 0:
            minits.append(int(t[i] // 60))
    plt.xticks (ticks=np.arange(min(t), max(t), 60.0), labels=minits)
    plt.show()
    return figure