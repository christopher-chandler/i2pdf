python setup.py bdist_wheel --universal
pip install .
# twine upload -r pypi dist/*
