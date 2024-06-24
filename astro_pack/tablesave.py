from pathlib import Path
import pandas as pd
def onerecord_table(maximum_S, pathes_of_images_list, data_dir):
    data_path = Path(data_dir)
    array = pathes_of_images_list[0].split('\\')
    title = array[5]
    table_for_part = pd.DataFrame({
        'Square_max, кв. мкм': maximum_S, 'file_path': pathes_of_images_list})
    table_for_part.to_excel(data_path /f'{title}.xlsx', index= False )