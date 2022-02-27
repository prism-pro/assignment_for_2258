def copy_test(a_list,c_list,STREAM_ARRAY_SIZE):
    for j in range(STREAM_ARRAY_SIZE):
        c_list[j] = a_list[j]
    return c_list
def scale_test(b_list,c_list,scalar,STREAM_ARRAY_SIZE):
    for j in range(STREAM_ARRAY_SIZE):
        b_list[j] = scalar * c_list[j]
    return b_list
def sum_test(a_list,b_list,c_list,scalar,STREAM_ARRAY_SIZE):
    for j in range(STREAM_ARRAY_SIZE):
        c_list[j] = a_list[j] + b_list[j]
    return   c_list
def triad_test(a_list,b_list,c_list,scalar,STREAM_ARRAY_SIZE):
     for j in range(STREAM_ARRAY_SIZE):
        a_list[j] = b_list[j] + scalar * c_list[j]
     return  a_list

