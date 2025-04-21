from setuptools import setup, find_packages
import os 

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='tamilkavi', 
    version='0.1.0',
    description='A command-line tool for exploring Tamil Kavithaigal.',
    long_description=read('README.md'), 
    long_description_content_type='text/markdown', 
    author='ANAND SUNDARAMOORTHY SA', 
    author_email='sanand03072005@gmail.com', 
    url='https://github.com/anandsundaramoorthysa/tamilkavi',
    license='MIT', 
    packages=find_packages(),
classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # 'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: Tamil',
        'Topic :: Text Processing',
        'Topic :: Cultural',
    ],
keywords=['tamil', 'kavi', 'poetry', 'tamil poetry', 'text processing'],

    install_requires=[
        'prettytable>=3.0.0', 
    ],

    package_data={
        'tamilkavi': ['kavisrc/*.json'],
    },

    entry_points={
        'console_scripts': [
            'tamilkavi = tamilkavi.tamilkavipy:main',
        ],
    },

    python_requires='>=3.6', 
)