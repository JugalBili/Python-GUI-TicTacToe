from setuptools import setup

setup(
    name='TicTacToe',
    version='0.1.0',
    author='Jugal Bilimoria',
    description="A gui tic tac toe game made using tkinter",
    url='https://github.com/JugalBili/Python-GUI-TicTacToe',
    license='license.txt',
    long_description=open('README.md').read(),
    install_requires=[
        "tk >= 8.6.10"
    ],
    python_requires='>=3.6',
)