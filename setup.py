# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

with open('test-requirements.txt') as f:
    test_requires = [line.strip() for line in f.readlines()]

setup(
    name="hypothesis-ros",
    version="0.1.0",
    url="https://github.com/ros-testing/hypothesis-ros",
    license='GPLv3',
    author="Florian Kromer",
    author_email="florian.kromer@mailbox.org",
    description="Property Based Testing for the ROS node level.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Testing'
    ],
)
