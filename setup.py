"""Setuptools configuration"""

import os
from setuptools import setup, find_packages


HERE = os.path.dirname(os.path.abspath(__file__))
LONG_DESC = open(os.path.join(HERE, 'README.rst')).read()

setup(
    name='citrus',
    version='0.1.0-prod',
    description='Custom Input Tabletop RPG Utility System',
    long_description=LONG_DESC,
    author='Fathomless Games',
    author_email='fathomlessgames@gmail.com',
    url='https://github.com/Parephax/citrus-manager/',
    packages=find_packages(include=['citrus']),
    include_package_data=True,
    install_requires=[
        'django==3.2.13',
        'django-npm=1.0.0'
        'channels',
        'channels_redis'
    ],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
