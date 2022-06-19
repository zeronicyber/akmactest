import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="akmactest",
    version="0.1",
    scripts=['akmactest'] ,
    author="Arunkumar Muthukumarasamy",
    author_email="zeronicyber@gmail.com",
    description="A small example test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zeronicyber/akmactest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
)
