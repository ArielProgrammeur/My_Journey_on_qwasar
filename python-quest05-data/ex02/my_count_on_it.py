def my_count_on_it (param):
    tab = [0] * len(param)
    for i in range(len(param)):
        tab[i] = len(param[i])
    return tab
