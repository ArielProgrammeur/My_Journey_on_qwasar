def my_is_sort (param):
    is_ascending = True
    is_descending = True

    for i in range(len(param) - 1) :
        if param[i] > param [i + 1] :
            is_ascending = False
        if param[i] < param [i + 1] :
            is_descending = False
    return is_ascending or is_descending
