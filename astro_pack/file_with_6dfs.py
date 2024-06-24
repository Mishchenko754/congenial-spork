def type_videorecords(df_ev):
    df1 = df_ev[df_ev.file_path.str.contains('tser1')]
    df2 = df_ev[df_ev.file_path.str.contains('tser2')]
    df3 = df_ev[df_ev.file_path.str.contains('tser3')]

    df4 = df_ev[df_ev.file_path.str.contains('tser4')]
    
    df5 = df_ev[df_ev.file_path.str.contains('2016-05-18')] 
    
    df6 = df_ev[df_ev.file_path.str.contains('2016-05-26')]
    
    return df1, df2, df3, df4, df5, df6