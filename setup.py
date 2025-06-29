"""Setup script for TransCMFD package"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="transcmfd",
    version="0.1.0",
    author="Your Name",  # Change this
    author_email="your.email@gmail.com",  # Change this
    description="TransCMFD: An Adaptive Transformer for Copy-Move Forgery Detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/TransCMFD-Copy-Move-Forgery-Detection",  # Change this
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "flake8>=4.0.0", "mypy>=0.950"],
    },
)
