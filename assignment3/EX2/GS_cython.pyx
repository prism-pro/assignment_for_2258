#GS_cython.pyx


def GS_numpy( newf):
    cdef signed int a = newf.shape[0]
    cdef signed int b = newf.shape[1]
    cdef unsigned int i,j
    for i in range(1, a - 1):
        for j in range(1, b - 1):
            newf[i, j] = 0.25 * (newf[i, j + 1] + newf[i, j - 1] +
                                 newf[i + 1, j] + newf[i - 1, j])
    return newf