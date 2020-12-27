from setuptools import setup, find_packages

s = setup(
    name="image-sizes",
    version="1.0.0",
    license="MIT",
    description="Creates Python Dictionary of image dimensions.",
    url="https://github.com/charlescforgy/image_size",
    packages=find_packages(),
    install_requires=[],
    python_requires = ">= 3.4",
    author="Charles C. Forgy",
    author_email="ccforgy@gmail.com",
    )
