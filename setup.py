import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="lowercase_booleans",
    version="1.0.0",
    author="Jonathan Hacker",
    author_email="github@jhacker.de",
    description="lowercase booleans for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathanhacker/lowercase_booleans",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
