import cv2
import glob
from pathlib2 import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
def read_data(mask):
    file_names = glob(str(mask))
    file_names.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    im_path_es = []
    for file_name in file_names:
        file_path = Path(file_name)
        im_path = file_name
        im_path_es.append(im_path)
    df_all = pd.DataFrame({
        'file_path': im_path_es})
    return df_all