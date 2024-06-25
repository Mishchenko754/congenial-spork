from astro_pack import D2_hist, countforhist
from pathlib import Path
def save_hist(hist, file_pathes, data_dir):
    data_path = Path(data_dir)
    array = file_pathes[0].split('\\')
    title = array[5]
    file_location_png = data_path/f'{title}_hist.png'
    hist.savefig(file_location_png, dpi=300, bbox_inches='tight')