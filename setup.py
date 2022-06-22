from setuptools import setup

setup(name='labyrinth',
      version='0.1',
      url='https://github.com/Antymon/labyrinth',
      author='Szymon Brych',
      author_email='szymon.brych@gmail.com',
      license='MIT',
      packages=['labyrinth'],
      install_requires=[
          'numpy==1.22.0',
          'matplotlib==3.1.2',
      ],
      zip_safe=False)