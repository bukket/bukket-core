from setuptools import setup, find_packages

setup(
    name="bucket",
    version="0.1.0",
    description="A sentient Bucket, heavily inspired by XKCD's bucket",
    url="https://github.com/bucket-corp",
    license="GPLv3",
    packages=find_packages(exclude=('tests',))
)
