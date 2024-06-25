from astro_pack import file_with_6dfs, file_for_func8
def function_to_func8(df_ev, data_dir):
    result = file_with_6dfs.type_videorecords(df_ev)
    for i in range(len(result)):
        file_pathes = result[i]['file_path'].values
        file_for_func8.func8(file_pathes, data_dir)