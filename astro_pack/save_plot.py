from pathlib2 import Path
from astro_pack import plot_of_means_of_S, square_number_of_shot, countforhist
def save_plt(PLOT, file_pathes, data_dir):
    data_path = Path(data_dir)
    array = file_pathes[0].split('\\')
    title = array[5]
    file_location_png = data_path / f'{title}_plot.png'
    PLOT.savefig(file_location_png, dpi=300, bbox_inches='tight')