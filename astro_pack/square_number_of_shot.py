import cv2
def count_Sq_max(file_pathes):
    maximum_S = []
    for i in range(len(file_pathes)):
        I = cv2.imread(str(file_pathes[i]))
        img1 = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
        ret,thresh_img = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        areas = []
        for j in range(len(contours)):
            area = cv2.contourArea(contours[j])
            size = area * (1/5.1) ** 2 # 5.1 pixel = 1 mkm
            areas.append(round(size, 3))
        max_area = max(areas)
        maximum_S.append(max_area)    
    return maximum_S