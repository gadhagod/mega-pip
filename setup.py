import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mega-pip',
    version='1.0',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='Python packaging and distrubution made easy.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/mega-pip',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'click',
        'twine'
    ],
    scripts=['./bin/mp'],
    python_requires='>=3.6'
)