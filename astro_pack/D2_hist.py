import cv2
import numpy as np
import matplotlib.pyplot as plt
def D2_histogfamm(Mo, title):
    h, w = Mo.shape[0], Mo.shape[1]
    hist = plt.figure(figsize=(6.5,3.37))
    plt.title(f'{title}')
    plt.gca().invert_yaxis()
    plt.plot([w - 71, w - 20], [h - 20, h - 20], color='w', linewidth=1)
    plt.text(w - 75, h-25, '10 $\mu$m', color = 'w', style='italic', size='small')
    plt.imshow(Mo, cmap = 'gray')
    cbar = plt.colorbar(label= "Количество смен значения пикселя", orientation="vertical",shrink=.75)
    return hist