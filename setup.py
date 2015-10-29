from distutils.core import setup

setup(
    # Application name:
    name="guesslang",

    # Version number (initial):
    version="0.1.1",

    # Application author details:
    author="Jonathan Pelletier",
    author_email="pelletier@mtrip.com",

    # Packages
    packages=["guesslang"],

    # Include additional files into the package
    include_package_data=True,

    description="returns the language of a peace of text",

    # Dependent packages (distributions)
    install_requires=[
        "argparse",
        "langdetect"
    ],
)
