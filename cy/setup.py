"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
from Cython.Build import cythonize

setup (
        name = 'CyToy',   
        version='0.1.2', 
        ext_modules=cythonize("*.pyx"),
        zip_safe=False,
)
