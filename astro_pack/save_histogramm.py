from astro_pack import D2_hist, count_for_hist
from pathlib import Path
def save_hist(hist, file_pathes, data_dir_save):
    '''
Функция принимает на вход: 
- file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений; 

- data_dir (str) - адрес директории. 

- hist (matplotlib.figure.Figure) - двумерная гистограмма
Пример:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
hist = cv2.imread(str(file_pathes[0]))
save_hist.savehist(hist, file_pathes = ['c\\d\\d\\d\\d\\d\\d\\dddsdvsdv'], data_dir = r'C:/Users/users')
```    
Сохраняет построенную гистограмму в файл png по адресу директории - в папку users.  
Название файла будет зависеть от file_pathes - file_pathes[0]split(\\)[5]_hist. 
В примере названием файла будет d_hist.png.
    '''
    data_path = Path(data_dir_save)
    objects_of_file_system = file_pathes[0].split('\\')
    title = objects_of_file_system[5]
    file_location_png = data_path / f'{title}_hist.png'
    hist.savefig(file_location_png, dpi=300, bbox_inches='tight')