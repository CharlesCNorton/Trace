import os
import setuptools

install_requires = [
    "pyautogen@git+https://github.com/microsoft/autogen.git@57ec13c#egg=autogen",
    "graphviz==0.20.1"
]

setuptools.setup(
    name="opto",
    version="0.1.0",
    author="Trace Team",
    author_email="chinganc@microsoft.com",
    url="https://github.com/microsoft/trace",
    license='MIT LICENSE',
    description="An AutoDiff-like tool for training AI systems end-to-end with general feedback",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(include=["opto*"], exclude=["test*"]),
    install_requires=install_requires,
    python_requires=">=3.8",
)
