
from setuptools import setup, find_packages
from sxlxs.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sxlxs',
    version=VERSION,
    description='Imports, parses and displays an excel worksheet.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Ryker Rumsey',
    author_email='rykerrumsey@outlook.com',
    url='https://github.com/rykerrumsey/sxlxs',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'sxlxs': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        sxlxs = sxlxs.main:main
    """,
)
