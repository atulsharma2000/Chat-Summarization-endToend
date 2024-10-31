import setuptools

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"  # Initial version of our package

# Package metadata
REPO_NAME = "Text-Summarization-endToend"
AUTHOR_USER_NAME = "atulsharma2000"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "atullsharma2000@gmail.com"


# it will look for constructor file in every folder and it will install it as my local package

# Setup configuration
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's name
    author_email=AUTHOR_EMAIL,  # Author's email
    description="A small Python package for NLP (text summarization) application",  # Short description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",  # Content type for long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the package repository
    project_urls={  # Additional URLs related to the project
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Source directory for packages
    packages=setuptools.find_packages(where="src"),  # Automatically find packages in src directory
)

