def part_of_df_all(df_all,  v_record):
    v_record = df_all[df_all.file_path.str.contains(f'{v_record}')]
    pathes_of_images_list = v_record[v_record.file_path.str.contains('event')]
    pathes_of_images_list = pathes_of_images_list['file_path'].values
    return pathes_of_images_list