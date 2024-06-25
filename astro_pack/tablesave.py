from pathlib import Path
import pandas as pd
def save_table(maximum_S, file_pathes, data_dir):
    data_path = Path(data_dir)
    array = file_pathes[0].split('\\')
    title = array[5]
    table_for_part = pd.DataFrame({
        'Square_max, кв. мкм': maximum_S, 'file_path': file_pathes})
    table_for_part.to_excel(data_path /f'{title}.xlsx', index= False)