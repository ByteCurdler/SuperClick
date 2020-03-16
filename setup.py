import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superclick-ILikePython256", # Replace with your own username
    version="0.0.1",
    author="ILikePython256",
    description="A tool for clicking at insane speeds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ILikePython256/superclick",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPL 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
