from pathlib2 import Path
def save_plt(figure, file_paths, data_dir_save):
    '''
Функция принимает на вход:

- PLOT (matplot.figure.Figure) - график

- file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений;

- data_dir_save (str) - адрес директории, куда нужно сохранить график. 
Пример:
x = [1, 1, 1, 1, 2]
y = [2, 4, 5, 5, 6]
PLOT = plt.figure()
plt.plot(x, y)
save_plot.save_plt(hist, file_paths=['a\\b\\c\\d\\e\\r'], data_dir=r'C:/Users/users')
``` 

Сохраняет построенный график в файл r_plot.png по адресу директории - в папку users.
    '''
    data_path = Path(data_dir_save)
    objects_of_file_system = file_paths[0].split('\\')
    title = objects_of_file_system[5]
    file_location_png = data_path / f'{title}_plot.png'
    figure.savefig(file_location_png, dpi=300, bbox_inches='tight')