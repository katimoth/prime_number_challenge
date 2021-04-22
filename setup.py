"""Setup configuration for application."""

from setuptools import setup

setup(
    name='primes',
    version='0.1.0',
    packages=['primes'],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.6',
)
