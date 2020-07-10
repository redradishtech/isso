#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import subprocess

from setuptools import setup, find_packages
from distutils.command.build import build as _build
import setuptools.command.build_py

requires = ['itsdangerous', 'Jinja2', 'misaka>=2.0,<3.0', 'html5lib',
            'werkzeug>=1.0', 'bleach', 'flask-caching>=1.9']

if sys.version_info < (3, ):
    raise SystemExit("Python 2 is not supported.")
elif (3, 0) <= sys.version_info < (3, 4):
    raise SystemExit("Python 3 versions < 3.4 are not supported.")

# On build, fetch our JS dependencies and build embed.min.js and friends. Ref. https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/
class BuildPyCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):
        subprocess.call(
              ['make', 'init', 'js']
              )
        setuptools.command.build_py.build_py.run(self)


setup(
    name='isso',
    version='0.12.3dev0',
    author='Martin Zimmermann',
    author_email='info@posativ.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/posativ/isso/',
    license='MIT',
    description='lightweight Disqus alternative',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=requires,
    setup_requires=["cffi>=1.3.0"],
    entry_points={
        'console_scripts':
            ['isso = isso:main'],
    },
    cmdclass={'build_py': BuildPyCommand}
)
