from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup( ext_modules=cythonize("GS_cython.pyx",
                              compiler_directives={"language_level":"3"}))