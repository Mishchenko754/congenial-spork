# Astrocytes

## Что делает
Обработка наборов изображений кальциевой активности астроцитов: построение двумерной гистограммы, характеризующей для каждого пикселя количество моментов времени, когда он начинал гореть (то есть смена значения пикселя с 0 на 1) и графика зависимости площади самой большой области в зависимости от номера кадра.

## Список функций:

### all_IMAGES.read_data(mask) 
type(data_dir) - str\
Функция read_data принимает на вход путь к директории.\
Возвращает dataFrame, в котором содержится информация о пути к изображениям\
```cmd
all_IMAGES.read_data(mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png')
```

### xy_dataFrame.part_of_df_all(df_all, v_record)

Принимает на вход:

+ df_all (pandas.core.frame.DataFrame) - дата фрейм с данными (в столбцах находятся пути к анализируемым изображениям);

+ v_record (str) - строковый объект, входящий в состав пути к изображениям и соответствующий определенной видеозаписи. Нужен для отбора строк из df_all по значению.

```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
df_all = pd.DataFrame({'file_pathes' : file_names})
xy_dataFrame.events1800(df_all, v_record = 'video_rec_1)
```

Возвращает список строк - путей к картинкам, находящимся в одной папке и полученных из одной записи.

### square_number_of_shot.count_Sq_max(file_pathes)

type(pathes_of_images_list)
 - numpy.ndarray
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
square_number_of_shot.count_Sq_max(file_pathes)
```
Функция принимает на вход список из строк, которые соответствуют адересам изображений.
Возвращает массив из вещественных чисел - значений максимальной площади, рассчитанной для каждого изображения, путь к которому находится в pathes_of_images_list.

### plot_of_means.plot(maximum_S, title) 

Принимает на вход:

+ maximum_S (list) - массив, содержащий в себе значения максимальной площади светлой области для каждого кадра;

+ title (str)- строковый объект, который будет являтся заголовком графика и указывать на тип видеозаписи.
```cmd
maximum_S  = [1.1, 1.1, 2.2, 3.3]
plot_of_means_of_S.plot(maximum_S, title)
```

На выходе функция выдает график, по оси X которого отложено время (мин), по оси Y - значения площади (в кв. мкм). Объtrn сохраняется в переменную PLOT.

### countforhist.count_hist(file_names) 

type(pathes_of_images_list)
 - numpy.ndarray

Функция count_hist принимает на вход список строк - адресов изображений.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
countforhist.count_hist(file_pathes)
```

Выводит кортеж: 2D массив, элементы которого соответствуют числу загораний пикселя, и title - строковый объект, указывающий на папку, в которой расположены изображения.

### D2_hist.D2_histogram(Mo, title)

Функция D2_histogramm принимает на вход:
+ Mo (numpy.ndarry) - двумерный массив, элементами которого являются числа, соответствующие цветам пикселя (0 - черный, 255 - белый).

+ title (str) - заголовок; является указанием на расположение папки с кадрами.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
I = cv2.imread(str(file_pathes[0]))
D2_hist.D2_histogram(I, title = 'example')
```
На выход выводится изображение (двумерная гистограмма с colorbar) и сохраняется в переменную hist.

### save_hist.savehist(hist, file_pathes, data_dir)

Функция принимает на вход: 
+ file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 

+ hist (matplotlib.figure.Figure) - двумерная гистограмма
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/nn/Task_Astrocytes/Task_Astrocytes') / '**'/ '**' / '**'/ '***.png'
file_pathes = glob(str(mask))
hist = cv2.imread(str(file_pathes[0]))
save_hist.savehist(hist, file_pathes = ['c\\d\\d\\d\\d\\d\\d\\dddsdvsdv'], data_dir = r'C:/Users/users')
```    
Сохраняет построенную гистограмму в файл png по адресу директории - в папку users.  Название файла будет зависеть от file_pathes - file_pathes[0]split(\\)[5]_hist. В примере названием файла будет d_hist.png.

### save_plot.saveplt(PLOT, file_pathes, data_dir)

Функция принимает на вход: 

+ PLOT (matplot.figure.Figure) - график

+ file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 
```cmd
x = [1, 1, 1, 1, 2]
y = [2, 4, 5, 5, 6]
PLOT = plt.figure()
plt.plot(x, y)
save_plot.saveplt(hist, file_pathes =  ['a\\b\\c\\d\\e\\r'], data_dir = r'C:/Users/users')
``` 

Сохраняет построенный график в файл r_plot.png по адресу директории - в папку users.

### tablesave.save_table(maximum_S, file_pathes, data_dir)

Функция принимает на вход: 

+ maximum_S (numpy.ndarray) - массив, элементами которого являются значения площади

+ file_pathes (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 

Длины массивов maximum_S и file_pathes должны совпадать.\   
```cmd
table_save.save_table(maximum_S = [0], file_pathes =  ['a\\b\\c\\d\\e\\r'], data_dir = r'C:/Users/users')
```
Таблица после выполнения функции из примера:

| Square_max, кв. мкм| file_path      |
|:------------------:|:--------------:|
|  0                 |a\\b\\c\\d\\e\\r|

Таблица сохраняется в файл r.xlsx в папку users

### file_with_6dfs.type_videorecords(df_ev)

Функция принимает на вход DataFrame; в столбцах содержатся значения, соответствующие адресам изображений типа event. 

Функция возвращает кортеж, в состав которого входят дата фреймы, в столбцах которых содержатся адреса изображений каждого вида видеозаписи (в каждом датафрейме будут строки из df_ev, содержащие ttser1, tser2, tser3, tser4, 2016-05-18  и 201605-26)

### file_for_func8.func8(file_pathes)

Функция принимает на выход массив из строк, элементы являются адресами изображений.

Запускает анализ для отдельной записи с полной обработкой с сохранением результатов.
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes/31_08_2020_tser1-20240514T075719Z-001/31_08_2020_tser1/events) / '***.png'
file_pathes = glob(str(mask))
file_for_func8.func8(file_pathes, data_dir = r'C:/Users/sibir/Desktop/results')
```
После вызова функции анализируются все изображения из папки events. По ним строятся гистограмма и графики, данные сохраняются в таблицу. Результаты анализа (график, гистограмма, таблица) сохраняются в папку results.

### astro_pack.file_for_func_to_func8(df_ev)

Функция принимает на вход DataFrame df_ev; в столбцах содержатся значения, соответствующие адресам изображений типа event. В датафрейме 1 столбец под названием 'file_pathes'. 
```cmd
from glob import glob
from pathlib2 import Path
mask = Path(r'C:/Task_Astrocytes') / '**'/ '**'/ '***.png'
file_names = glob(str(mask))
df_all = pd.DataFrame({'file_pathes' : file_names}) 
file_for_func_to _func8.function_to_func8(df_ev = df_all[df_all.file_path.str.contains('event')], data_dir = r'C:/Users/sibir/Desktop/results')
```
Функция запускает функцию запуска анализа изображений  для всех видеозаписей, расположенных по адресу C:/Task_Astrocytes, и сохраняет результаты анализа в папку results. 