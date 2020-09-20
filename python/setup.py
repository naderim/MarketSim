#
#  Copyright (c) 2018 Mohsen Naderi
#

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='msim',
      version='0.1',
      description='Mohsen Naderi\'s market simulation toolbox',
      url='https://mnaderi.com/git-repos/MarketSim',
      author='Mohsen Naderi',
      author_email='mohsen@mnaderi.com',
      license='MIT',
      packages=['msim'],
      zip_safe=False)
