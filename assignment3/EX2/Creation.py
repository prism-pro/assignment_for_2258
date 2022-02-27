import numpy as np
import array
"""the package is to create N*N list or numpy array or create N flat array"""
def create_list(N):
    A = [];
    for i in range(N):
        A.append(list(np.random.rand(N)))

    return A


def create_array(N):
    A = [];
    for i in range(N):
        A.append(array.array('d', np.random.rand(N)))
    return A


def create_numpy(N):
    A = np.random.rand(N, N)

    return A

if __name__ == "__main__":
    N=2
    F=create_numpy(2)
    f=F[0]
    print(f)
    print(f.shape)

