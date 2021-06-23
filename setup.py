from setuptools import setup, find_packages

###taken from orbitize!
def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

setup(
name=”elliptical-mask”,
version=”0.1”,
description="makes arbitrary elliptical, circular, and annular binary masks for image processing",
url='https://github.com/briley-lewis/elliptical-mask',
license='MIT',
packages=find_packages(),
install_requires=get_requires()
)

