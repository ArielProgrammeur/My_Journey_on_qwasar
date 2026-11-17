def my_data_transform (param):
    lines = param.replace('\\n','\n').split('\n')
    if not lines or lines[0] == "":
        return []
    header_str = lines[0]
    header = header_str.split(',')

    email_idx = header.index('Email')
    age_idx = header.index('Age')
    order_idx = header.index('Order At')

    result = [header_str]

    for line in lines [1:]:
        if line.strip() == "":
            continue
        cols = line.split(',')

        email = cols[email_idx]
        provider = email.split('@')[1] if '@' in email else email
        cols[email_idx] = provider

        age = int(cols[age_idx])
        if 1 <= age <= 20:
            cols[age_idx] = "1->20"
        elif 21 <= age <= 40:
            cols[age_idx] = "21->40"
        elif 41 <= age <= 65:
            cols[age_idx] = "41->65"
        else:
            cols[age_idx] = "66->99"

        order_time = cols[order_idx]
        hour = int(order_time.split(' ')[1].split(':')[0])
        if 6 <= hour <12:
            cols[order_idx] = "morning"
        elif 12 <= hour <18:
            cols[order_idx] = "afternoon"
        else:
            cols[order_idx] = "evening"

        new_row = ','.join(cols)
        result = result + [new_row]
    return result