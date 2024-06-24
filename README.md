# Astrocytes

## Что делает
Обработка наборов изображений кальциевой активности астроцитов: построение двумерной гистограммы, характеризующей для каждого пикселя количество моментов времени, когда он начинал гореть (то есть смена значения пикселя с 0 на 1) и графика зависимости площади самой большой области в зависимости от номера кадра.

## Список функций:

### astro_pack.all_IMAGES.read_data(data_dir) 
type(data_dir) - str\
Функция read_data принимает на вход путь к директории.\
Возвращает dataFrame, в котором содержится информация о пути к изображениям\
```cmd
all_IMAGES.read_data(data_dir = r'C:/Users/Dexstop/images')
```

### astro_pack.xy_dataFrame.part_of_df_all(df_all, v_record)

Принимает на вход:

+ df_all (pandas.core.frame.DataFrame) - дата фрейм, в столбце которого содержатся пути к изображениям;

+ v_record (str) - строковый объект, входящий в состав пути к изображениям и соответствующий определенной видеозаписи. 

Возвращает список строк - путей к картинкам, находящимся в одной папке и полученных из одной записи.



### count_Sq_max(pathes_of_images_list) 

type(pathes_of_images_list)
 - numpy.ndarray

Функция принимает на вход список из строк, которые соответствуют адересам изображений.
Возвращает массив из вещественных чисел - значений максимальной площади, рассчитанной для каждого изображения, путь к которому находится в pathes_of_images_list.

### astro_pack.plot_of_means.plot(maximum_S, title) 

Принимает на вход:

+ maximum_S (list) - массив, содержащий в себе значения максимальной площади светлой области для каждого кадра;

+ title (str)- строковый объект, который будет являтся заголовком графика и указывать на тип видеозаписи.

На выходе функция выдает график, по оси X которого отложено время (мин), по оси Y - значения площади.

### astro_pack.countforhist.count_hist(pathes_of_images_list) 

type(pathes_of_images_list)
 - numpy.ndarray

Функция count_hist принимает на вход список строк - адресов изображений.

Выводит 2D массив, элементы которого соответствуют числу загораний пикселя.

### astro_pack.D2_hist.D2_histogram(Mo, title)

Функция D2_histogramm принимает на вход:
+ Mo (numpy.ndarry) - двумерный массив, элементами которого являются числа, соответствующие цветам пикселя (0 - черный, 255 - белый).

+ title (str) - является указанием на расположение папки с кадрами.

На выход выводится изображение (двумерная гистограмма) и сохраняется в переменную hist.

### astro_pack.save_hist.savehist(pathes_of_images_list, data_dir)

Функция принимает на вход: 
+ pathes_of_images_list (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 
    
Сохраняет построенную гистограмму в файл png по адресу директории.

### astro_pack.save_plot.saveplt(pathes_of_images_list, data_dir)

Функция принимает на вход: 

+ pathes_of_images_list (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 
    
Сохраняет построенный график в файл png по адресу директории.

### astro_pack.tablesave.onerecord_table(pathes_of_images_list, data_dir)

Функция принимает на вход: 

+ pathes_of_images_list (numpy.ndarray) - список, элементами которого являются адреса изображений; 

+ data_dir (str) - адрес директории. 
    
Сохраняет построенную гистограмму в файл png по адресу директории.

### astro_pack.file_with_6dfs.type_videorecords(df_ev)

Функция принимает на вход DataFrame; в столбцах содержатся значения, соответствующие адресам изображений типа event. 

Функция возвращает кортеж, в состав которого входят дата фреймы, в столбцах которых содержатся адреса изображений каждого вида видеозаписи.

### astro_pack.file_for_func8.func8(pathes_of_images_list)

Функция принимает на выход список строк, элементы являются адресами изображений.

Запускает анализ для отдельной записи с полной обработкой с сохранением результатов.

### astro_pack.file_for_func_to_func8(df_ev)

Функция принимает на вход DataFrame; в столбцах содержатся значения, соответствующие адресам изображений типа event. 

Функция запускает функцию запуска анализа изображений  для всех видеозаписей и сохраняет результаты анализа в папку results.