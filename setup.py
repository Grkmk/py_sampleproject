import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-polls-GRKMK",
    version="0.0.1",
    author="Gorkem Kockaya",
    author_email="gorkem@example.com",
    description="A Django app to conduct Web-based polls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grkmk/py_sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment"
        "Framework :: Django"
        "Framework :: Django :: 3.0"
        "Intended Audience :: Developers"
        "Topic :: Internet :: WWW/HTTP"
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
    ],
    python_requires='>=3.6',
)