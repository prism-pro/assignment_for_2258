from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import numpy as np
import array
from numexpr import evaluate


def dgemm(a, b, c, N,numexpr_on = False):
    if type(a) == array.array:  # array.array has only 1 demension, we have to use another way to calculate it
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    c[i * N + j] = c[i * N + j] + a[i * N + k] * b[k * N + j]
    elif type(a) == np.ndarray:
        #print('a')
        if numexpr_on == False:
            for i in range(N):
                for j in range(N):
                    c[i,j]= c[i,j]+ sum(a[i,:]*b[:,j])
        else:
            c=traid_with_numexpr(a,b,c)
            print(c.size)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c


def traid_with_numexpr(a,b,c):
    evaluate("c+a*b",out=c)
    return c

def create_list(N):
    A = [];
    B = [];
    C = [];
    for i in range(N):
        A.append(list(np.random.rand(N)))
        B.append(list(np.random.rand(N)))
        C.append(list(np.random.rand(N)))
    return A, B, C


def create_array(N):
    A = array.array('d', np.random.rand(N ** 2))
    B = array.array('d', np.random.rand(N ** 2))
    C = array.array('d', np.random.rand(N ** 2))
    return A, B, C


def create_numpy(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    C = np.random.rand(N, N)
    return A, B, C


def measure_time(start=3,end=7, N=15,numexpr_on=False):
    """measure """
    size = np.logspace(start, end, N, base=2, dtype=int)
    print(size)
    t_record1 = np.linspace(0, end, N)
    t_record2 = np.linspace(0, end, N)
    t_record3 = np.linspace(0, end, N)
    f_record1 = np.linspace(0, end, N)
    f_record2 = np.linspace(0, end, N)
    f_record3 = np.linspace(0, end, N)
    t1 = 0
    t2 = 0
    for i in range(N):
        A_l, B_l, C_l = create_list(size[i])
        t1 = timer()
        dgemm(A_l, B_l, C_l, size[i])
        t2 = timer()
        t_record1[i] = t2 - t1
        f_record1[i] = 2*size[i]**3/(1000000 * t_record1[i])
        print('list...',t2-t1)
    for i in range(N):
        A_a, B_a, C_a = create_array(size[i])
        t1 = timer()
        dgemm(A_a, B_a, C_a, size[i])
        t2 = timer()
        t_record2[i] = t2 - t1
        f_record2[i] = 2 * size[i] ** 3/(1000000 * t_record2[i])
        print('array...',t2 - t1)
    for i in range(N):
        A_n, B_n, C_n = create_numpy(size[i])
        t1 = timer()
        dgemm(A_n, B_n, C_n, size[i],numexpr_on=numexpr_on)
        t2 = timer()
        t_record3[i] = t2 - t1
        f_record3[i] = 2 * size[i] ** 3 / (1000000 * t_record3[i])
        print('np...',t2 - t1)
    """draw """
    plt.figure(figsize=(8.4, 6.4))
    # fig, plt = plt.subplots(figsize=(8.4, 6.4))
    plt.semilogx(size, t_record1, label='list')
    plt.semilogx(size, t_record2, label='array')
    plt.semilogx(size, t_record3, label='numpy with numexpr')
    plt.xlabel('size in width ')
    plt.ylabel('operation time  in seconds ')
    plt.title('operation time VS size in width')
    plt.legend()
    plt.savefig("{}.png".format('time_vs_size1'))

    plt.figure(figsize=(8.4, 6.4))
    # fig, plt = plt.subplots(figsize=(8.4, 6.4))
    plt.semilogx(size, f_record1, label='list')
    plt.semilogx(size, f_record2, label='array')
    plt.semilogx(size, f_record3, label='numpy')
    plt.xlabel('size in width ')
    plt.ylabel('operation speed  in MFLOPS/s ')
    plt.title('operation speed VS size in width')
    plt.legend()
    plt.savefig("{}.png".format('speed_vs_size1'))



if __name__ == "__main__":
    N = 2
    A = array.array('d', [1.0, 1.1, 1.2, 1.3])
    B = array.array('d', [1.2, 1.3, 1.4, 1.5])
    C = array.array('d', [0.0, 0.0, 0.0, 0.0])
    a_l = [[1.0, 1.1], [1.2, 1.3]]
    b_l = [[1.2, 1.3], [1.4, 1.5]]
    c_l = [[0.0, 0.0], [0.0, 0.0]]
    A, B, C = create_numpy(N)
    #print(A)
    #print(B)
    #C=dgemm(A,B,C,N)
    #print(C)
    measure_time()
    #measure_time(numexpr_on=True)
