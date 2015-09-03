from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

setup(
  cmdclass = {'build_ext': build_ext},
  ext_modules = [
    Extension("mean3", ["mean3.pyx"],
              include_dirs=[np.get_include()],
              extra_compile_args=['-fopenmp'],
              extra_link_args=['-fopenmp', '-lgomp']),
  ]
)
