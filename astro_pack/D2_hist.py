import cv2
import numpy as np
import matplotlib.pyplot as plt
def D2_histogfamm(array_for_hist, title):
    '''
Функция D2_histogramm принимает на вход:
 - array_for_hist (numpy.ndarry) - двумерный массив, элементами которого являются числа, 
 соответствующие цветам пикселя (0 - черный, 255 - белый).

 - title (str) - заголовок; является указанием на расположение папки с кадрами.
Пример использования функции:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
I = cv2.imread(str(file_pathes[0]))
D2_hist.D2_histogram(I, title = 'example')
На выход выводится двумерная гистограмма с colorbar и сохраняется в переменную hist.
    '''
    h, w = array_for_hist.shape[0], array_for_hist.shape[1]
    hist = plt.figure(figsize=(6.5, 3.37))
    plt.title(f'{title}')
    plt.gca().invert_yaxis()
    plt.plot([w - 71, w - 20], [h - 20, h - 20], color='w', linewidth=1)
    plt.text(w - 75, h - 25, '10 $\mu$m', color='w', style='italic', size='small')
    plt.imshow(array_for_hist, cmap='gray')
    cbar = plt.colorbar(label="Количество загораний", orientation="vertical", shrink=.75)
    return hist