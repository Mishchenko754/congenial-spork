from astro_pack import countforhist, square_number_of_shot, plot_of_means_of_S, D2_hist, save_histogramm, save_plot, tablesave
def func8(file_pathes, data_dir):
    maximum_S = square_number_of_shot.count_Sq_max(file_pathes)
    title = countforhist.count_hist(file_pathes)[1]
    tablesave.save_table(maximum_S, file_pathes, data_dir)
    PLOT = plot_of_means_of_S.plot(maximum_S, title = countforhist.count_hist(file_pathes)[1])
    Mo = countforhist.count_hist(file_pathes)[0]
    hist = D2_hist.D2_histogfamm(Mo, title)
    save_histogramm.save_hist(hist, file_pathes, data_dir)
    save_plot.save_plt(PLOT, file_pathes, data_dir)