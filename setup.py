"""Setup file for Olfaction Prediction"""

import sys
import os

try:
    from pip.req import parse_requirements
    from pip.download import PipSession
except Exception:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession

from setuptools import setup, find_packages

# IPython 6.0+ does not support Python 2.6, 2.7, 3.0, 3.1, or 3.2
if sys.version_info < (3, 3):
    ipython = "ipython>=5.1,<6.0"
else:
    ipython = "ipython>=5.1"


def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join('.', 'requirements.txt')
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs


setup(
    name='olfaction_prediction',
    version=0.1,
    author='Rick Gerkin',
    author_email='rgerkin@asu.edu',
    packages=find_packages(),
    license='MIT',
    description=("A package for using the DREAM model for predicting olfactory descriptors from molecular features."),
    long_description="",
    install_requires=read_requirements(),
    )
