from setuptools import setup

setup(
    name='EnToFa',
    version='1.0',
    py_modules=['translator'],
    install_requires=[
        'requests',
        'win10toast'
    ],
    entry_points='''
        [console_scripts]
        EnToFa=translator:main
    '''
)
