#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'cssorg',
    version = '0.0.1',
    author = 'John Song',
    author_email = 'john.song.toronto@gmail.com',
    description = ('Organize your CSS files'),
    url = 'https://github.com/JohnSongSoftware/CSS-Organizer',

    packages = ['src/Python'],
    classifiers = [
        'Development Status :: Alpha',
        'Programming Language :: Python :: 3',
    ],
    entry_points = {
        'console_scripts': [
                    'cssorg = python.__main__:main',
        ],
    }
)