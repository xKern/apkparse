from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = ('Simply python utility wrapping around apktool to extract apk'
               'information')
LONG_DESCRIPTION = Path('readme.md').read_text()

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="apkparse",
    version=VERSION,
    author="Haider Ali",
    author_email="neo@xkern.net",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'xmltodict'
    ],

    keywords=['django', 'djangorestframework', 'responses', 'xkern'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only"
    ])
