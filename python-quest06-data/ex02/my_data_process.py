import json

def my_data_process (param):
    if not param or len(param) == 0:
        return "{}"
    
    header = param[0].split(',')
    discarded = ['FirstName', 'LastName', 'UserName', 'Coffee Quantity']

    valid_cols = []
    col_indices = []
    for i in range(len(header)):
        col = header[i]
        if col not in discarded:
            valid_cols = valid_cols + [col]
            col_indices = col_indices + [i]
    count = {}
    for col in valid_cols:
        count[col] = {}
    for line in param[1:]:
        if not line.strip():
            continue
        cols = line.split(',')
        for j in range (len(valid_cols)):
            col = valid_cols[j]
            idx = col_indices[j]
            if idx < len(cols):
                val = cols[idx]
                if val in count[col]:
                    count[col][val] += 1
                else:
                    count[col][val] = 1
    return json.dumps(count, separators=(',',':'))
        
    