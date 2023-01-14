from functools import reduce
def max_integer(my_list=[]):
    mixa = reduce(max, my_list)
    return mixa