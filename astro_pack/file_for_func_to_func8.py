from astro_pack import file_with_6dfs, file_for_func8
def function_to_func8(df_ev):
    result = file_with_6dfs.type_videorecords(df_ev)
    for i in range(len(result)):
        pathes_of_images_list = result[i]['file_path'].values
        file_for_func8.func8(pathes_of_images_list)