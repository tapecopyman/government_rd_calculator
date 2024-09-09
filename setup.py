from setuptools import setup, find_packages

setup(
    name="government_rd_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'rd_calculator=main:main',
        ],
    },
)