def events1800(df_all,  v_record):
    v_record = df_all[df_all.file_path.str.contains(f'{v_record}')]
    v_record_events = v_record[v_record.file_path.str.contains('event')]
    file_pathes = v_record_events['file_path'].values
    return file_pathes