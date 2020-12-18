"""Setuptools configuration"""

import os
from setuptools import setup, find_packages


HERE = os.path.dirname(os.path.abspath(__file__))
LONG_DESC = open(os.path.join(HERE, 'README.rst')).read()


setup(
    name='foo',
    version='0.0.1-indev.1',
    description='A useful module',
    author='Man Foo',
    author_email='foomail@foo.com',
    packages=['foo'],  # same as name
    install_requires=['bar', 'greek'],  # external packages as dependencies
)
