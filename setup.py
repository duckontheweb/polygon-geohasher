import re
from setuptools import setup, find_packages


# Get version without importing, which avoids dependency issues
def get_version():
    with open("polygon_geohasher/version.py") as version_file:
        return re.search(
            r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""", version_file.read()
        ).group("version")


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements.txt") as f:
        return f.read()


setup(
    name="polygon-geohasher-2",
    version=get_version(),
    author="Alberto Bonsanto; maintained by Jon Duckworth",
    author_email="",
    url="https://github.com/duckontheweb/polygon-geohasher",
    description="""Wrapper over Shapely that returns the set of geohashes that form a Polygon.""",
    long_description=readme(),
    license="MIT",
    packages=find_packages(),
    install_requires=requirements(),
    include_package_data=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["polygon", "geohashes"],
)
