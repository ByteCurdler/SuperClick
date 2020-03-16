import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superclick-ILikePython256", # Replace with your own username
    version="0.0.1",
    author="ILikePython256",
    description="A tool for clicking at speeds up to 180+ clicks/s.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ILikePython256/SuperClick",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPL 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    	'pynput',
    ],
    python_requires='>=3.6',
)
