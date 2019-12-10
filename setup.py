from setuptools import setup, Extension
from Cython.Distutils import build_ext

setup(
    name="sortable",
    packages=["src/sortable"],
    ext_modules=[
        Extension("src.sortable.c.algorithms", ["src/sortable/c/algorithms.pyx"])
    ],
    cmdclass={"build_ext": build_ext},
    install_requires=["Cython"],
)
