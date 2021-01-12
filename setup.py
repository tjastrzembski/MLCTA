from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    package_data={
        'MLCGB': [
        'PSQL/*'
        ]
    },
    include_package_data=True,
    platforms=['Linux' ],
    python_requires='>=3.7',
    setup_requires=['flake8'],
    install_requires=[
        "antlr4-python3-runtime ; python_version>='4.8'",
        "PerFact-Python-Modules ; python_version>='3.15.1'",
        'pycurl'
        ]
    )