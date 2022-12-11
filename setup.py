# Standard
# None

# Pip
from setuptools import setup
from pathlib import Path

# Custom
# None

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="i2pdf",
    version="1.1.1",
    scripts=["main_app.py"],
    packages=["auxiliary"],
    entry_points={"console_scripts": ["image2pdf=i2pdf:app",
                                      "i2pdf= i2pdf:app"]},
    url="https://github.com/christopher-chandler",
    license="MIT",
    install_requires=["typer", "PyYAML", "Pillow", "PyPDF2"],
    author="Christopher Michael Chandler",
    author_email="christopher.chandler@outlook.de",
    description="A simple CLI app that combines images to a single .pdf",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
