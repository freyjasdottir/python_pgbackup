from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup (
    name='pgbackup',
    version='0.1.0',
    author='Hannah Read',
    description='A utility for backup up PostgreSQL databases'
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src')
)
