import re

from setuptools import find_packages
from setuptools import setup


def get_version():
    with open("commander/__init__.py") as fp:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", fp.read()).group(1)


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


setup(
    name='commander-py',
    version=get_version(),
    url='https://github.com/ozcanyarimdunya/commander',
    license='MIT',
    author='Özcan Yarımdünya',
    author_email='ozcanyd@gmail.com',
    description='A very simple tool to create beautiful console application.',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages("."),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
