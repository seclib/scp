#!/usr/bin/env python3
"""
Packaging setup for Arsenal
"""
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text()

setup(
    name='arsenal-cli',
    version='1.1.1',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    url='https://github.com/Orange-Cyberdefense/arsenal',
    license='GPL-3.0',
    author='Guillaume Muh, mayfly',
    author_email='csr-audit.so@orange.com',
    description='Arsenal is just a quick inventory, reminder and launcher for pentest commands. ',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords=[
        'security',
        'pen testing',
        'cli',
        'tools',
        'tmux',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    exclude_package_data={"": ["my_cheats/", "mindmap/"]},
    package_data={'': ['data/cheats/*']},
    entry_points={
        'console_scripts': [
            'arsenal = arsenal.app:main',
        ],
    },
)
