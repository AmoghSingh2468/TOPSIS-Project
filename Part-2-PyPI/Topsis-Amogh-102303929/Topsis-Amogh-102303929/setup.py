from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Topsis-Amogh-102303929",
    version="1.0.0",
    author="Amogh Singh",
    description="Rank alternatives with TOPSIS multi-criteria decision analysis, from the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["topsis_amogh"],
    install_requires=["pandas", "numpy"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "topsis=topsis_amogh.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
