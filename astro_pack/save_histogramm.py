from astro_pack import D2_hist, countforhist
from pathlib import Path
def save_hist(pathes_of_images_list, data_dir):
    data_path = Path(data_dir)
    array = pathes_of_images_list[0].split('\\')
    title = array[5]
    file_location_png = data_path / f'{title}_hist.png'
    hist = D2_hist.D2_histogfamm(Mo = countforhist.count_hist(pathes_of_images_list)[0], title = countforhist.count_hist((pathes_of_images_list))[1])
    hist.savefig(file_location_png, dpi=300, bbox_inches='tight')