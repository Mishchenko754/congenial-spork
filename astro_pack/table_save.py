from pathlib import Path
import pandas as pd
def save_table(squares_max, file_paths, data_dir_save):
    '''
Функция принимает на вход:

- squares_max (numpy.ndarray) - массив, элементами которого являются значения площади;

- file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений;

- data_dir_save (str) - адрес директории, где сохранится таблица.

Длины массивов maximum_S и file_pathes должны совпадать.
Пример:
squares_max = [0]
file_paths = ['a\\b\\c\\d\\e\\r']
table_save.save_table(squares_max, file_paths, data_dir=r'C:/Users/users')

Таблица сохраняется в файл r.xlsx в папку users.

    '''
    data_path = Path(data_dir_save)
    file_system_objects = file_paths[0].split('\\')
    title = file_system_objects[5]
    table_for_part = pd.DataFrame({
        'Square_max, кв. мкм': squares_max, 'file_path': file_paths})
    table_for_part.to_excel(data_path / f'{title}.xlsx', index=False)