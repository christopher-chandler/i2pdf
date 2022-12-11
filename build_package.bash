clear
pip install -r requirements.txt
python setup.py sdist bdist_wheel
pip install .
rm -r project_build
mkdir project_build
mv build project_build
mv i2pdf.egg-info project_build
mv dist project_build