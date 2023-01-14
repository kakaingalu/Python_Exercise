def no_c(my_string):
    new_string = ''
    for a in my_string:
        if a == 'c' or a == 'C':
            continue
        new_string += a
    return new_string
