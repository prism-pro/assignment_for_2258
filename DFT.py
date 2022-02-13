from timeit import default_timer as timer
import numpy as np
from functools import wraps
import matplotlib.pyplot as plt

def timefn(fn):  # decorator to  measure time
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = timer()
        result = fn(*args, **kwargs)
        # print(result)
        t2 = timer()

        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result, t2 - t1

    return measure_time


@timefn
def cal_FFT(xr, xi, xr_o, xi_o, N):  # N is the size of arrays
    p = np.linspace(0, N, N, endpoint=False, dtype=float)
    Pi2 = 3.1415926 * 2
    p = p * Pi2 / N
    for k in range(N):
        xr_o[k] = sum(xr * np.cos(k * p) + xi * np.sin(k * p))
        xi_o[k] = sum(xi * np.cos(k * p) - xr * np.sin(k * p))
    return xr_o, xi_o


@timefn
def cal_FFT_std(xi):  # calculate FFt with standard lib, return a complex array
    xo = np.fft.fft(xi)
    return xo


def create_np_array(size, dtype=float):  # create array of different size& type
    if dtype == complex:
        c = np.random.rand(size)
        b = np.random.rand(size)
        a = c + 1j * b
    else:
        a = np.random.rand(size)
    return a


def measure(size_start=3, size_end=10, std=False):
    N = size_end - size_start + 1
    record = np.linspace(0, size_end - size_start, N)
    size = np.logspace(size_start, size_end, N, base=2,dtype=int)
    for i in range(N):
        if std == False:
            xr = create_np_array(size[i], dtype=float)
            xi = create_np_array(size[i], dtype=float)
            Xr_out = create_np_array(size[i], dtype=float)
            Xi_out = create_np_array(size[i], dtype=float)
            re,record[i] = cal_FFT(xr,xi,Xr_out,Xi_out,size[i])
        else:
            x= create_np_array(size[i],dtype=complex)
            re,record[i]= cal_FFT_std(x)
    return size,record

def main():
    size, reco1 = measure(3, 10, std=False)
    plt.figure(figsize=(8.4, 6.4))
    size, reco2 = measure(3, 10, std=True)
    # fig, plt = plt.subplots(figsize=(8.4, 6.4))
    plt.loglog(size, reco1, label='hand write dft')
    plt.loglog(size, reco2, label='standard fft')
    plt.xlabel('array size')
    plt.ylabel('operation time  in seconds ')
    plt.title('operation time VS array size')
    plt.legend()
    plt.savefig("{}.png".format('dft_time_vs_size1'))

if __name__ == "__main__":
    main()

