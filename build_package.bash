python setup.py sdist bdist_wheel
pip install .
rm -r project_build
mkdir project_build
mv build project_build
mv i2pdf.egg-info project_build
mv dist project_build
clear
twine upload -r pypi project_build/dist/*
