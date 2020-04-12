from distutils.core import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="Cython1", sources=["Cython1.pyx"])
setup(ext_modules=cythonize(ext))
