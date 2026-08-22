from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


def read_version():
    """Read __version__ from the package without importing it."""
    for line in read(os.path.join('tamilkavi', '__init__.py')).splitlines():
        if line.startswith('__version__'):
            return line.split('=', 1)[1].strip().strip('"').strip("'")
    raise RuntimeError('could not find __version__ in tamilkavi/__init__.py')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tamilkavi',
    version=read_version(),
    description='A command-line tool for exploring Tamil Kavithaigal.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ANAND SUNDARAMOORTHY SA and Boopalan S',
    author_email='sanand03072005@gmail.com, content.boopalan@gmail.com',
    url='https://github.com/anandsundaramoorthysa/tamilkavi',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: Tamil',
        'Topic :: Text Processing',
        # Add specific Python versions you support (>=3.7)
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=['tamil', 'kavi', 'poetry', 'tamil poetry', 'text processing'],

    install_requires=[
        'importlib_resources ; python_version < "3.9"'
    ],

    package_data={
        'tamilkavi': ['kavisrc/*.json'],
    },

    entry_points={
        'console_scripts': [
            'tamilkavi = tamilkavi.tamilkavipy:main',
        ],
    },

    python_requires='>=3.7',

    include_package_data=True,
)
