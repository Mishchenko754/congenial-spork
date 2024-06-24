from astro_pack import countforhist, square_number_of_shot, plot_of_means_of_S, D2_hist, save_histogramm, save_plot, tablesave
def func8(pathes_of_images_list):
    tablesave.onerecord_table(maximum_S=square_number_of_shot.count_Sq_max(pathes_of_images_list), pathes_of_images_list = pathes_of_images_list, data_dir = r'C:/Users/sibir/Desktop/results/table')
    plot_of_means_of_S.plot(maximum_S = square_number_of_shot.count_Sq_max(pathes_of_images_list), title = countforhist.count_hist(pathes_of_images_list)[1])
    D2_hist.D2_histogfamm(Mo = countforhist.count_hist(pathes_of_images_list)[0], title=countforhist.count_hist(pathes_of_images_list)[1])
    save_histogramm.save_hist(pathes_of_images_list, data_dir = r'C:/Users/sibir/Desktop/results/hist')
    save_plot. save_plt(pathes_of_images_list, data_dir = r'C:/Users/sibir/Desktop/results/plot')