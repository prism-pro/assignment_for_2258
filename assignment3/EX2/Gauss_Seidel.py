import numpy as np
import matplotlib.pyplot as plt
from Cython.Build import cythonize
import TimeRecord
import Creation
import GS_cython


"""parameters: f is a N*N array, N is the width of f, t is iteration times """
@TimeRecord.timefn
def GS_iteration(f,t):
    for i in range(t):
        newf = GS_cython.GS_numpy(f)
    return newf


def GS_numpy(newf):
    a=newf.shape[0]
    b=newf.shape[1]
    for i in range(1, a - 1):
        for j in range(1, b - 1):
            newf[i, j] = 0.25 * (newf[i, j + 1] + newf[i, j - 1] +
                                 newf[i + 1, j] + newf[i - 1, j])
    return newf

def main():
    N=16
    l=np.logspace(2,8,N,base=2,dtype= int)
    t=np.linspace(0,15,N)
    for i in range(N):
        p=Creation.create_numpy(l[i])
        p,t[i] = GS_iteration(p,1000)

    plt.figure(figsize=(8.4, 6.4))
    plt.semilogx(l, t)
    plt.xlabel('grid width ')
    plt.ylabel('operation time  in seconds ')
    plt.title('operation time VS grid width')
    plt.savefig("{}.png".format('GS_1'))
    plt.show()

if __name__ == "__main__":
    main()

