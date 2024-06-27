from astro_pack import count_for_hist, D2_hist, plot_of_square_of_events, save_histogramm
from astro_pack import save_plot, square_of_max_area, table_save
def start_analysis(file_paths, data_dir_save):
    '''
Функция принимает на выход массив из строк, элементы являются адресами изображений.

Запускает анализ для отдельной записи с полной обработкой с сохранением результатов.
Пример:
from glob import glob
from pathlib2 import Path
data_dir = r'C:/Task_Astrocytes/31_08_2020_tser1/events'
mask = Path(data_dir)/'***.png'
file_paths = glob(str(mask))
data_dir = r'C:/Users/sibir/Desktop/results'
processing_single_record.start_analysis(file_paths, data_dir)

После вызова функции анализируются все изображения из папки events. 
По ним строятся гистограмма и графики, данные сохраняются в таблицу. 
Результаты анализа (график, гистограмма, таблица) сохраняются в папку results.
    '''
    squares_max = square_of_max_area.count_max_square(file_paths)
    title = count_for_hist.count_hist(file_paths)[1]
    table_save.save_table(squares_max, file_paths, data_dir_save)
    PLOT = plot_of_square_of_events.plot_square_to_time(squares_max, title)
    array_for_hist = count_for_hist.count_hist(file_paths)[0]
    hist = D2_hist.D2_histogfamm(array_for_hist, title)
    save_histogramm.save_hist(hist, file_paths, data_dir_save)
    save_plot.save_plt(PLOT, file_paths, data_dir_save)