import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qcpython",
    version="1.1.1",
    author="Brennan Freeze, Paris Osuch, Aundre Barras, Soren Richenberg, Suzanne Rivoire",
    author_email="freezebrennan@gmail.com, osuch@sonoma.edu, barras@sonoma.edu, richenbe@sonoma.edu, rivoire@sonoma.edu",
    description="QCpy is an open source python library and collaborative project for flexible simulations and visualizations of quantum circuits. Designed by college students with students in mind, this library contains a powerful set of tools to teach computer scientists about the emerging discipline of quantum computing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QCpython/QCpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "matplotlib==3.7.2",
        "numpy==1.25.1",
        "setuptools==65.5.0",
        "scipy==1.11.2",
        "pytest==7.4.2",
    ],
)
