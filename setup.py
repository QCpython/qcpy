import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QCpython",
    version="1.0.3",
    author='Brennan Freeze, Paris Osuch, Aundre Barras, Soren Richenberg, Suzanne Rivoire',
    author_email='freezebrennan@gmail.com, osuch@sonoma.edu, barras@sonoma.edu, richenbe@sonoma.edu, rivoire@sonoma.edu',
    description="QCpy is a comprehensive and user-friendly library for quantum computing, providing a wide range of functionality for quantum algorithms and quantum circuits. It is built on using open-source libraries NumPy and Matplotlib; compatible with Python 3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QCpython/QCpy",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.22.0",
        "matplotlib>=3.5.1",
        "six>=1.16.0",
        "pyparsing>=3.0.4",
        "pytest>=6.2.4"
    ],
)
