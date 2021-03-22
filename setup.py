import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cto-ai",
    version="2.3.2",
    author="CTO.ai",
    author_email="devops@cto.ai",
    description="SDK for The Ops Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cto-ai/sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.22"
    ],
)
