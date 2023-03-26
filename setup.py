import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Endian",
    version = "0.0.5",
    author = "kunal hedaoo ",
    author_email = "kunalhedaoo25@gmail.com",
    description = "Change string to little endian & big endian",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/kunaldesign/Endian", 
    project_urls = {
        "Bug Tracker": "https://github.com/kunaldesign/Endian/issues", 
    },
    classifiers = [
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)