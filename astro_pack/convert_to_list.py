def select_rows_by_value(df_all,  value_for_select):
    '''
Принимает на вход:

- df_all (pandas.core.frame.DataFrame) - дата фрейм с данными
(в столбцах находятся пути к анализируемым изображениям);

- value_for_select (str) - строковый объект, входящий в состав пути к изображениям
 и соответствующий определенной видеозаписи (названию папки).
Нужен для отбора строк из df_all по значению.
Ex.:
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
df_all = pd.DataFrame({'file_pathes' : file_names})
xy_dataFrame.events1800(df_all, value_for_select = 'video_rec_1)

Возвращает список путей к картинкам, находящимся в одной папке. 
    '''
    selected_part = df_all[df_all.file_path.str.contains(f'{value_for_select}')]
    selected_part_by_event = selected_part[selected_part.file_path.str.contains('event')]
    file_paths = selected_part_by_event['file_path'].values
    return file_paths