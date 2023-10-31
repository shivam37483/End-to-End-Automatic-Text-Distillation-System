#This file contains all the package information as well as info regarding the developer of project which will automatically created when requirement.txt file  is run.

import setuptools

with open("README.md", "r") as fh:            # Read the README.md file; open() returns a file object
    long_description = fh.read()              # Read the file object and store it in long_description

__version__ = "0.0.1"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "HeliosX"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "vatshivam498@gmail.com"

setuptools.setup(              #this function will create a package for all folders containing __init__.py file
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for NLP app", 
    long_description=long_description ,
    long_description_content_type="text/markdown",      #long_description is in markdown format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)