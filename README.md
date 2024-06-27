# Astrocytes

## Что делает
Обработка наборов изображений кальциевой активности астроцитов:
построение двумерной гистограммы, характеризующей для каждого
пикселя количество моментов времени, когда он начинал гореть
(то есть смена значения пикселя с 0 на 1)
и графика зависимости площади самой большой области в зависимости от номера кадра.
## Примеры изображений
Примеры графиков и гистограмм, которые можно построить при вызове функций и astro_pack.

![Двумерная гистограмма](/results/31_08_2020_tser1_hist.png)

![График](/results/31_08_2020_tser1_plot.png)

## Список функций:

### all_IMAGES.read_data(mask) 
type(data_dir) - str\
Функция read_data принимает на вход путь к директории.\
Возвращает dataFrame, в котором содержится информация о пути к изображениям.
```cmd
data_dir = r'C:/nn/Task_Astrocytes/Task_Astrocytes'
all_images.read_data(mask = Path(data_dir) / '**'/ '**' / '**'/ '***.png')
```

### convert_to_list.select_rows_by_value(df_all, value_for_select):

Принимает на вход:

+ df_all (pandas.core.frame.DataFrame) - дата фрейм с данными\
(в столбцах находятся пути к анализируемым изображениям);

+ value_for_select (str) - строковый объект, входящий в состав пути к изображениям\
и соответствующий определенной видеозаписи. Нужен для отбора строк из df_all по значению.

```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
df_all = pd.DataFrame({'file_pathes' : file_names})
value_for_select = 'record_1'
convert_to_list.select_rows_by_value(df_all, value_for_select)
```

Возвращает список строк - путей к картинкам,
находящимся в одной папке и полученных из одной записи.

### square_of_max_ares.count_max_square(file_paths):

type(file_paths)
 - numpy.ndarray
```cmd
from glob import glob
from pathlib2 import Path
data_fir = r'C:/nn/Task_Astrocytes/Task_Astrocytes'
mask = Path(data_dir)/'**/'**'/'**'/'***.png'
file_paths = glob(str(mask))
square_of_max_ares.count_max_square(file_paths)
```
Функция принимает на вход список из строк, которые соответствуют адересам изображений.

Возвращает массив из вещественных чисел -\
значений максимальной площади, рассчитанной\
для каждого изображения, путь к которому находится в pathes_of_images_list.

### plot_of_square_of_events.plot_square_to_time(squares_max, title):

Принимает на вход:

+ squares_max (list) - массив, содержащий в себе значения максимальной\
площади светлой области для каждого кадра;

+ title (str)- строковый объект, который будет являтся\
заголовком графика и указывать на тип видеозаписи.
```cmd
squares_max  = [1.1, 1.1, 2.2, 3.3]
plot_of_square_of_events.plot_square_to_time(squares_max, title)
```

На выходе функция выдает график, по оси X которого отложено время (мин),\
по оси Y - значения площади (в кв. мкм). Объtrn сохраняется в переменную PLOT.

### count_for_hist.count_hist(file_paths) 

type(file_paths)
 - numpy.ndarray

Функция count_hist принимает на вход список строк - адресов изображений.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_paths = glob(str(mask))
countforhist.count_hist(file_paths)
```

Выводит кортеж: 2D массив, элементы которого соответствуют числу загораний пикселя,
и title - строковый объект, указывающий на папку, в которой расположены изображения.

### D2_hist.D2_histogram(array_for_hist, title)

Функция D2_histogramm принимает на вход:
+ array_for_hist (numpy.ndarry) - двумерный массив,
элементами которого являются числа,
соответствующие цветам пикселя (0 - черный, 255 - белый).

+ title (str) - заголовок; является указанием на расположение папки с кадрами.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
I = cv2.imread(str(file_pathes[0]))
D2_hist.D2_histogram(I, title = 'example')
```
На выход выводится изображение (двумерная гистограмма с colorbar)\
и сохраняется в переменную hist.

### save_hist.savehist(hist, file_paths, data_dir_save)

Функция принимает на вход: 
+ file_paths (numpy.ndarray) - список, элементами которого являются адреса изображений;

+ data_dir_save (str) - адрес директории, куда сохранится гистограмма; 

+ hist (matplotlib.figure.Figure) - двумерная гистограмма.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
hist = cv2.imread(str(file_pathes[0]))
save_hist.savehist(hist, file_pathes=['c\\d\\d\\d\\d\\d\\v'], data_dir=r'C:/Users/users')
```    
Сохраняет построенную гистограмму в файл png по адресу директории\
- в папку users.  Название файла будет зависеть от file_pathes -\
file_pathes[0]split(\\)[5]_hist. В примере названием файла будет d_hist.png.

### save_plot.saveplt(PLOT, file_paths, data_dir_save)

Функция принимает на вход: 

+ PLOT (matplot.figure.Figure) - график;

+ file_paths (numpy.ndarray) - список, элементами которого являются адреса изображений;

+ data_dir (str) - адрес директории, куда сохранится график.
```cmd
x = [1, 1, 1, 1, 2]
y = [2, 4, 5, 5, 6]
PLOT = plt.figure()
plt.plot(x, y)
save_plot.saveplt(hist, file_pathes =  ['a\\b\\c\\d\\e\\r'], data_dir=r'C:/Users/users')
``` 

Сохраняет построенный график в файл r_plot.png по адресу директории - в папку users.

### table_save.save_table(squares_max, file_paths, data_dir_save)

Функция принимает на вход: 

+ squares_max (numpy.ndarray) - массив, элементами которого являются значения площади

+ file_paths (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir_save (str) - адрес директории, куда сохраанится таблица. 

Длины массивов squares_max и file_pathes должны совпадать.\   
```cmd
data_dir_save = r'C:/Users/users'
table_save.save_table(squares_max=[0], file_paths=['a\\b\\c\\d\\e\\r'], data_dir_save)
```
Таблица после выполнения функции из примера:

| Square_max, кв. мкм| file_path      |
|:------------------:|:--------------:|
|  0                 |a\\b\\c\\d\\e\\r|

Таблица сохраняется в файл r.xlsx в папку users.

### processing_single_record.start_analysis(file_paths, data_dir_save):

Функция принимает на выход:

+ file_paths - список путей к изображениям.

+ data_dir_save (str) - адрес, где сохранятся результаты обработки.

Запускает анализ для отдельной записи с полной обработкой с сохранением результатов.
```cmd
from glob import glob
from pathlib2 import Path
data_dir = r'C:/Task_Astrocytes/31_08_2020_tser1/events'
mask = Path(data_dir) / '***.png'
file_paths = glob(str(mask))
file_for_func8.func8(file_pathes, data_dir = r'C:/Users/sibir/Desktop/results')
```
После вызова функции анализируются все изображения из папки events.\
По ним строятся гистограмма и графики, данные сохраняются в таблицу.\
Результаты анализа (график, гистограмма, таблица) сохраняются в папку results.

### full.processing.analizes_full(mask, dir_folders, data_dir_save):

Функция принимает на вход:

+ mask - пути ко всем изображениям;

+ dir_folders - адрес папки, в которой находятся папки с анализируемыми изображениями;

+ data_dir_save - адрес, в котором сохранятся результаты анализа.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
data-dir_save = data_dir_save = r'C:/Users/users'
data_dir = r'C:/Task_Astrocytes'
mask = Path(data_dir) /'**'/ '***.png'
```
Функция запускает функцию запуска анализа изображений  для всех видеозаписей,
расположенных по адресу C:/Task_Astrocytes, и сохраняет результаты анализа в папку users.