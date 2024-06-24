from pathlib2 import Path
from astro_pack import plot_of_means_of_S, square_number_of_shot, countforhist
def save_plt(pathes_of_images_list, data_dir):
    data_path = Path(data_dir)
    array = pathes_of_images_list[0].split('\\')
    title = array[5]
    PLOT = plot_of_means_of_S.plot(maximum_S=square_number_of_shot.count_Sq_max(pathes_of_images_list), title= countforhist.count_hist(pathes_of_images_list)[1])
    file_location_png = data_path / f'{title}_plot.png'
    PLOT.savefig(file_location_png, dpi=300, bbox_inches='tight')