import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dreadnaut",
    version="0.0.1",
    author="Peter Cortez",
    author_email="innov.petercortez@gmail.com",
    description="A CLI tool for setting your Slack status for a specific workspace.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dreadnautxbuddha/not-slacking",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
