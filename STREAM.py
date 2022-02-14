import matplotlib.pyplot as plt
import numpy as np
import array
from timeit import default_timer as timer
import sys
import time


def test_list(STREAM_ARRAY_SIZE):
    a_list = list(1 for i in range(STREAM_ARRAY_SIZE))
    b_list = list(2 for i in range(STREAM_ARRAY_SIZE))
    c_list = list(3 for i in range(STREAM_ARRAY_SIZE))
    for j in range(STREAM_ARRAY_SIZE):
        a_list[j] = 1.0
        b_list[j] = 2.0
        c_list[j] = 0.0
    scalar = 2.0
    print('type is ', type(a_list))
    times = [0, 0, 0, 0]

    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c_list[j] = a_list[j]
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        b_list[j] = scalar * c_list[j]
    times[1] = timer() - times[1]
    # sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        c_list[j] = a_list[j] + b_list[j]
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a_list[j] = b_list[j] + scalar * c_list[j]
    times[3] = timer() - times[3]

    copy = 2 * sys.getsizeof(a_list[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    add = 2 * sys.getsizeof(a_list[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    scale = 3 * sys.getsizeof(a_list[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    triad = 3 * sys.getsizeof(a_list[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    print("For list, copy  bandwidth is ", round(copy / times[0], 4), "MB/s")
    print("For list, add   bandwidth is ", round(add / times[1], 4), "MB/s")
    print("For list, scale bandwidth is ", round(scale / times[2], 4), "MB/s")
    print("For list, triad bandwidth is ", round(triad / times[3], 4), "MB/s")
    return [copy / times[0], add / times[1], scale / times[2], triad / times[3]]


def test_array(STREAM_ARRAY_SIZE):
    a_array = array.array('f', range(STREAM_ARRAY_SIZE))
    b_array = array.array('f', range(STREAM_ARRAY_SIZE))
    c_array = array.array('f', range(STREAM_ARRAY_SIZE))
    for i in range(STREAM_ARRAY_SIZE):
        c_array[i]=0.0
    scalar = 2.0
    print('type is ', type(a_array))
    times = [0, 0, 0, 0]

    times[0] = timer()
    c_array = a_array
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    for i in b_array:
        i = i * scalar
    times[1] = timer() - times[1]
    # sum
    times[2] = timer()
    c_array = b_array +a_array
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a_array[j] = b_array[j] + scalar * c_array[j]
    times[3] = timer() - times[3]
    print(times)
    copy = 2 * sys.getsizeof(a_array[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    add = 2 * sys.getsizeof(a_array[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    scale = 3 * sys.getsizeof(a_array[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    triad = 3 * sys.getsizeof(a_array[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    print("For array, copy  bandwidth is ", round(copy / times[0], 4), "MB/s")
    print("For array, add   bandwidth is ", round(add / times[1], 4), "MB/s")
    print("For array, scale bandwidth is ", round(scale / times[2], 4), "MB/s")
    print("For array, triad bandwidth is ", round(triad / times[3], 4), "MB/s")
    return [copy / times[0], add / times[1], scale / times[2], triad / times[3]]


def test_numpy(STREAM_ARRAY_SIZE):
    a_np = np.arange(0.0, STREAM_ARRAY_SIZE, 1.0)
    b_np = np.arange(0.0, STREAM_ARRAY_SIZE, 1.0)
    c_np = np.arange(0.0, STREAM_ARRAY_SIZE, 1.0)
    for j in range(STREAM_ARRAY_SIZE):
        a_np[j] = 1.0
        b_np[j] = 2.0
        c_np[j] = 0.0
    scalar = 2.0
    print('type is ', type(a_np))
    #print(sys.getsizeof(a_np[0]))
    times = [0, 0, 0, 0]

    times[0] = timer()
    c_np = a_np
    times[0] = timer() - times[0]

    # scale
    times[1] = timer()
    c_np = scalar * b_np
    times[1] = timer() - times[1]
    # sum
    times[2] = timer()
    c_np = a_np + b_np
    times[2] = timer() - times[2]

    # triad
    times[3] = timer()
    c_np = a_np + b_np*scalar
    times[3] = timer() - times[3]

    copy = 2 * sys.getsizeof(a_np[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    add = 2 * sys.getsizeof(a_np[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    scale = 3 * sys.getsizeof(a_np[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    triad = 3 * sys.getsizeof(a_np[0]) * STREAM_ARRAY_SIZE / 2 ** 20
    print("For numpy, copy  bandwidth is ", round(copy / times[0], 4), "MB/s")
    print("For numpy, add   bandwidth is ", round(add / times[1], 4), "MB/s")
    print("For numpy, scale bandwidth is ", round(scale / times[2], 4), "MB/s")
    print("For numpy, triad bandwidth is ", round(triad / times[3], 4), "MB/s")
    return [copy / times[0], add / times[1], scale / times[2], triad / times[3]]

def drawing(STREAM_ARRAY_SIZE,test,name='1'):
    plt.figure(figsize=(8.4,6.4))
    #fig, ax = plt.subplots(figsize=(8.4, 6.4))
    #plt.semilogx(STREAM_ARRAY_SIZE, test[:,0], label='copy')
    plt.semilogx(STREAM_ARRAY_SIZE, test[:,1], label='add')
    plt.semilogx(STREAM_ARRAY_SIZE, test[:,2], label='scale')
    plt.semilogx(STREAM_ARRAY_SIZE, test[:,3], label='triad')
    plt.xlabel('size ')
    plt.ylabel('bandwith in MB/s ')
    #plt.title(name)
    plt.legend()
    plt.savefig("{}.png".format(name))
    plt.show()

if __name__ == "__main__":
    STREAM_ARRAY_SIZE = np.logspace(4, 20, 24, base=2,dtype=int)
    STREAM_ARRAY_SIZE = STREAM_ARRAY_SIZE * 10
    # test & record
    record_list = np.array(0.0)
    record_arr = np.array(0.0)
    record_np = np.array(0.0)
    for i in STREAM_ARRAY_SIZE:
        #record_list = np.append(record_list,test_list(i))
        #record_arr = np.append(record_arr, test_array(i))
        record_np = np.append(record_np, test_numpy(i))
    record_np = np.delete(record_np,[0])
    record_arr = np.delete(record_arr, [0])
    record_list = np.delete(record_list,[0])
    record_np = record_np.reshape(24,4)
    #record_arr = record_arr.reshape(24, 4)
    #record_list = record_list.reshape(24, 4)
    # drew figures
    #drawing(STREAM_ARRAY_SIZE, record_list,name='list')
    #drawing(STREAM_ARRAY_SIZE,record_arr,name='array')
    drawing(STREAM_ARRAY_SIZE, record_np,name='numpy')


