from setuptools import setup

setup(
    name="customplottinglibrary",
    version="1.0.0",
    packages=["customplottinglibrary"],
    url="https://github.com/gjkhai/custom-plotting-library/",
    author="@ganjk",
    description="Custom matplotlib charts for trading & financial related data",
    long_description_content_type="text/markdown",
    install_requires=[
        "setuptools",
        "pandas",
        "numpy",
        "matplotlib"
    ],
)

