from setuptools import setup, find_packages

with open("README.md", "rb") as fh:
    long_description = fh.read().decode('utf-8', errors='ignore')

setup(
    name='usellm',
    version='0.0.5',
    author='Siddhant',
    author_email='siddhant@jovian.com',
    url='https://github.com/usellm/usellm-py',
    description='Use Large Language Models in Python App',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["usellm"], exclude=["examples"]),
    install_requires=[
        'requests>=2.31.0'
    ],
)
