import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "soil_test"
Author_USER_NAME = "Kavin-Hanzo"
SRC_NAME = "soiltester"
AUTHOR_EMAIL = "kesivakavin@gmail.com"

setuptools.setup(
    name=SRC_NAME,
    version=__version__,
    author=Author_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for soiltester",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" :f"https://github.com/{Author_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)