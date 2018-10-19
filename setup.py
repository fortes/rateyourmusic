import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fr:
    requirements = fr.read().splitlines()

setuptools.setup(
    name="rateyourmusic",
    version="0.0.1",
    author="Filipe Fortes",
    author_email="accounts@fortes.com",
    description="RateYourMusic review scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fortes/rateyourmusic",
    license='MIT',
    platforms='ALL',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ])
