"""Setuptools configuration"""

import os
from setuptools import setup, find_packages

from citrus import __version__


HERE = os.path.dirname(os.path.abspath(__file__))
LONG_DESC = open(os.path.join(HERE, 'README.rst')).read()


setup(
    name='foo',
    version='1.0',
    description='A useful module',
    author='Man Foo',
    author_email='foomail@foo.com',
    packages=['foo'],  # same as name
    install_requires=['bar', 'greek'],  # external packages as dependencies
)
