"""Installer
"""

import setuptools

dist = setuptools.setup(
    name='tellasign',
    version='0.3.5',
    url='http://github.com/kevinballard/tellasign',
    author='Kevin Ballard',
    author_email='kevin@tellapart.com',
    packages=setuptools.find_packages('py/'),
    package_dir={'': 'py'},
    include_package_data=True,
    namespace_packages=['tellasign'],
    entry_points={
        'console_scripts': [
            'tellasign = tellasign.scripts.tellasign_breath_main:main',], }, )
