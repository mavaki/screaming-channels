from setuptools import setup, find_packages

setup(
    name="ScreamingChannels",
    version="3.0",
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "sc-experiment = screamingchannels.reproduce:cli",
            "sc-attack = screamingchannels.attack:cli",
        ]
    },
    install_requires=[
        "click==8.1.7",
        "numpy==2.0.0",
        "scipy==1.14.0",
        "pyserial==3.5",
        "matplotlib==3.9.1",
        "enum34",
        "pmt==0.0.4",
        "pyts==0.13.0",
        "llvmlite==0.43.0",
        "numba==0.60.0",
        "statsmodels==0.14.2",
        "pandas==2.2.2",
        "scikit-learn==1.5.1",
        "future==1.0.0",
        "pycryptodome==3.20.0",
        "pyzmq==26.0.3",
        "peakutils==1.3.5",
        "tabulate==0.9.0",
        "kiwisolver==1.4.5",
        "pyparsing==3.1.2"


# to use system packages
#        ln -s /usr/lib/python2.7/site-packages/gnuradio ../../../../screaming-channel/nRF52832/experiments/VENV_sc/lib/python2.7/site-packages
#        "gnuradio",
#        "osmosdr",
    ],

    author="S3@EURECOM",
    author_email="camurati@eurecom.fr, poeplau@eurecom.fr, muench@eurecom.fr",
    description="Code for our screaming channel attacks",
    license="GNU General Public License v3.0"
    # TODO URLs
)
