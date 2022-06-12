# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BcwrDU5yktsFqiFUDzYBk9c1QWFTjYar
"""

import setuptools
from pathlib import Path
#from setuptools import setup
setuptools.setup(name='gym_switching',
      version='0.0.0',
      description="A OpenAI Gym Env for optimal switching",
      long_description=Path("README.md").read_text(),
      long_description_content_type="text/markdown",
                 author="Claudia Viaro",
                 license="MIT",
      packages=setuptools.find_packages(include="gym_switching*"),
      install_requires=['gym']  # And any other dependencies needed
)