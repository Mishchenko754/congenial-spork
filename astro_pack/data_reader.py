import cv2
import glob
from pathlib2 import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
def read_data(mask):
    '''
type(mask) - pathlib2.WindowsPath
Функция read_data принимает на вход пути к файлам.
Возвращает dataFrame, в столбце которого содержится информация о пути к изображениям. 
Пример:
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png')
all_images.read_data(mask)
'''
    file_names = glob(str(mask))
    file_names.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    paths_to_images = []
    for file_name in file_names:
        path_to_image = file_name
        paths_to_images.append(path_to_image)
    df_all = pd.DataFrame({
        'file_path' : paths_to_images})
    return df_all