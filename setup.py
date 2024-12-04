from setuptools import setup, find_packages

setup(
    name="p12cracker",
    version="0.0.1",
    author="KcanCurly",
    description=" simple tool to brute force a password for a password-protected PKCS#12 (PFX/P12) file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/p12Cracker",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "pyOpenSSL"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "p12cracker.py=src.p12Cracker:main",  
        ],
    },
)