from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Columnwise Shift',
    ext_modules=cythonize("task8_cy.pyx"),
    zip_safe=False,
)
