def my_csv_parser (param_1, param_2):
    lines = param_1.split("\n")
    result = []

    for line in lines :
        if line != "":
            row = line.split(param_2)
            result = result + [row]
    return result
