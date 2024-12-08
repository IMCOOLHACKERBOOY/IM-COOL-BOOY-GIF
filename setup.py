from setuptools import setup, find_packages

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A tool that can create GIFs easily."

setup(
    name="IM-COOL-BOOY-GIF",
    version="1.1.3",
    author="coolbooy",
    author_email="coolbooy@gmail.com",
    description="A tool that can create GIFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "imageio",
        "numpy",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "IM-COOL-BOOY-GIF=IM_COOL_BOOY_GIF.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    license="MIT",
)
