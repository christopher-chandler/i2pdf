from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='i2pdf',
    version='1.0.9',
    packages=['src', 'src.auxiliary'],
    entry_points={
            'console_scripts': [
                'image2pdf=src.main_app:app',
                'i2pdf=src.main_app:app'
                ]
                },
    url='https://github.com/christopher-chandler',
    license='MIT',
    install_requires=["typer", "PyYAML", "Pillow", "PyPDF2"],
    author='Christopher Michael Chandler',
    author_email='christopher.chandler@outlook.de',
    description='A simple CLI app that combines images to a single .pdf',
    long_description=long_description,
    long_description_content_type='text/markdown'
    )
