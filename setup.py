from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qcpython",
    version="1.1.1",
    author="Brennan Freeze, Paris Osuch, Aundre Barras, Soren Richenberg, Suzanne Rivoire",
    author_email="freezebrennan@gmail.com, osuch@sonoma.edu, barras@sonoma.edu, richenbe@sonoma.edu, rivoire@sonoma.edu",
    description="QCpy is an open source python library and collaborative project for flexible simulations and visualizations of quantum circuits. Designed by college students with students in mind, this library contains a powerful set of tools to teach computer scientists about the emerging discipline of quantum computing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QCpython/QCpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    # Need to update to read requirements.txt
    install_requires=[
        "setuptools>=65.5.0",
        "scipy>=1.11.2",
        "pytest>=7.4.2",
        "contourpy>=1.2.1",
        "cycler>=0.12.1",
        "fonttools>=4.51.0",
        "kiwisolver>=1.4.5",
        "matplotlib>=3.8.4",
        "numpy>=1.26.4",
        "packaging>=24.0",
        "pillow>=10.3.0",
        "pyparsing>=3.1.2",
        "python-dateutil>=2.9.0.post0",
        "six>=1.16.0",
        "cupy-cuda12x>=13.0.0",
    ],
)
