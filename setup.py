from setuptools import setup, find_packages

setup(
    name='EnToFa',
    version='1.4',
    py_modules=['translator'],
    install_requires=[
        'requests',
        'win10toast'
    ],
    entry_points='''
        [console_scripts]
        EnToFa=translator:main
    ''',
    package_data={
        '': ['README.md'],
        'EnToFa': ['assets/images/*'],
    },
    packages=find_packages(),
)
