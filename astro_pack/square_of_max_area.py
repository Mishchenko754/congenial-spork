import cv2
def count_max_square(file_paths):
    '''
type(file_paths)
 - numpy.ndarray
Пример:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_paths = glob(str(mask))
square_of_max_area.count_max_squares(file_paths)

Функция принимает на вход список из строк, которые соответствуют адересам изображений.
Возвращает массив из вещественных чисел - значений максимальной площади,
рассчитанной для каждого изображения, путь к которому находится в pathes_of_images_list.
    '''
    squares_max = []
    for i in range(len(file_paths)):
        image = cv2.imread(str(file_paths[i]))
        image_in_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret,thresh_img = cv2.threshold(image_in_gray, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        areas = []
        for j in range(len(contours)):
            area = cv2.contourArea(contours[j])
            size = area * (1/5.1) ** 2 # 5.1 pixel = 1 mkm
            areas.append(round(size, 3))
        max_area = max(areas)
        squares_max.append(max_area)    
    return squares_max