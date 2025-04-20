from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(here)

about = {}
init_file_path = os.path.join(here, 'tamilkavi', '__init__.py')
with open(init_file_path, 'r', encoding='utf-8') as f:
    exec(f.read(), about)


readme_path = os.path.join(project_root, 'README.md')
long_description = open(readme_path, encoding='utf-8').read() if os.path.exists(readme_path) else ''


setup(
    name='tamilkavi', 
    version=about.get('__version__', '0.0.0'), 
    packages=find_packages(),
    package_data={
        'tamilkavi': ['kavisrc/*.json'], 
    },
    include_package_data=True, 
    description='A Python package for accessing Tamil Kavithai data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about.get('__author__', 'ANAND SUNDARAMOORTHY SA'), 
    author_email=about.get('__contact__', 'sanand03072005@gmail.com'), 
    url='https://github.com/anandsundaramoorthysa/tamilkavi', 
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Tamil',
    ],
    keywords='kavithai tamil poetry data literature',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tamilkavi=tamilkavi._cli:main',
        ],
    },
)