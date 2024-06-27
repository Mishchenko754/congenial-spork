import cv2
import numpy as np
def count_hist(file_paths):
    '''
type(pathes_of_images_list)
 - numpy.ndarray

Функция count_hist принимает на вход список строк - адресов изображений.   
Пример использования функции:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_paths = glob(str(mask))
countforhist.count_hist(file_paths)
Выводит кортеж: 2D массив, элементы которого соответствуют числу загораний пикселя,
и title - строковый объект, указывающий на папку, в которой расположены изображения.
'''
    file_paths_as_list = file_paths[0].split('\\')
    title = file_paths_as_list[5]
    shape_hist = cv2.imread(str(file_paths[0]))
    shape_hist = cv2.cvtColor(shape_hist, cv2.COLOR_BGR2GRAY)
    array_for_hist = np.zeros(shape_hist.shape)
    for i in range(len(file_paths) - 1):
        one_image = cv2.imread(str(file_paths[i]))
        one_image_in_gray = cv2.cvtColor(one_image, cv2.COLOR_BGR2GRAY)
        one_image_in_gray[one_image_in_gray >= 1] = 1
        following_image = cv2.imread(str(file_paths[i+1]))
        following_image_in_gray = cv2.cvtColor(following_image, cv2.COLOR_BGR2GRAY)
        following_image_in_gray[following_image_in_gray >= 1] = 1
        difference = following_image_in_gray - one_image_in_gray
        difference[difference == 255] = 0
        array_for_hist = array_for_hist + difference
    return array_for_hist, title