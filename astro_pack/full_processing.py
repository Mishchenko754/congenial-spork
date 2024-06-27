from astro_pack import processing_single_record
from glob import glob
from pathlib import Path
def analizes_full(mask, dir_folders, data_dir_save):
    '''
Функция принимает на вход DataFrame df_ev; в столбцах содержатся значения, 
соответствующие адресам изображений типа event. В датафрейме 1 столбец под названием 'file_pathes'. 
Пример:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
df_all = pd.DataFrame({'file_pathes' : file_names}) 
full_processing.function_to_func8(df_ev = df_all[df_all.file_path.str.contains('event')], data_dir = r'C:/Users/sibir/Desktop/results')

Функция запускает функцию запуска анализа изображений  для всех видеозаписей, 
расположенных по адресу C:/Task_Astrocytes, и сохраняет результаты анализа в папку results. 
    '''
    list_of_all_paths = glob(str(mask))
    list_of_all_paths.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    mask_for_folders = Path(dir_folders)/'**'
    folders = glob(str(mask_for_folders))
    file_paths = list(filter(lambda x: folders[1] in x, list_of_all_paths))
    for i in range(len(folders)):
        file_paths = list(filter(lambda x: folders[i] in x, list_of_all_paths))
        processing_single_record.start_analysis(file_paths, data_dir_save)