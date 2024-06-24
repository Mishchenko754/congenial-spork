import cv2
import numpy as np
def count_hist(pathes_of_images_list):
    array = pathes_of_images_list[0].split('\\')
    title = array[5]
    I = cv2.imread(str(pathes_of_images_list[0]))
    img1 = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    Mo = np.zeros(img1.shape)
    for i in range(len(pathes_of_images_list) - 1):
        I = cv2.imread(str(pathes_of_images_list[i]))
        img1 = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
        img1[img1 >= 1] = 1
        M = cv2.imread(str(pathes_of_images_list[i+1]))
        img2 = cv2.cvtColor(M, cv2.COLOR_BGR2GRAY)
        img2[img2 >= 1] = 1
        M = img2 - img1
        M[M ==  255] = 0
        Mo = Mo + M
    return Mo, title