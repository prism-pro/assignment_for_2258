import numpy as np
import DGEMM

def test_DGEMM_4():
  n1= 4
  a= np.random.random((n1, n1))
  b= np.random.random((n1, n1))
  c = np.random.random((n1, n1))
  d = DGEMM.dgemm(a, b, c, n1)
  c= c+a*b

  assert d.all() == c.all()

def test_DGEMM_16():
    n1 = 16
    a = np.random.random((n1, n1))
    b = np.random.random((n1, n1))
    c = np.random.random((n1, n1))
    d = DGEMM.dgemm(a, b, c, n1)
    c = c + a * b

    assert d.all() == c.all()

def test_DGEMM_64():
    n1 = 64
    a = np.random.random((n1, n1))
    b = np.random.random((n1, n1))
    c = np.random.random((n1, n1))
    d = DGEMM.dgemm(a, b, c, n1)
    c = c + a * b

    assert d.all() == c.all()


def test_DGEMM_256():
  n1 = 256
  a = np.random.random((n1, n1))
  b = np.random.random((n1, n1))
  c = np.random.random((n1, n1))
  d = DGEMM.dgemm(a, b, c, n1)
  c = c + a * b

  assert d.all() == c.all()