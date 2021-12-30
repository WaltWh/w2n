import re

from setuptools import setup

version = ""
with open("discord/__init__.py") as f:
    search = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if search is not None:
        version = search.group(1)

    else:
        raise RuntimeError("Could not grab version string")

if not version:
    raise RuntimeError("version is not set")

with open("README.rst") as f:
    readme = f.read()

setup(
    name='longsphinx-word2number',
    packages=['w2n'],
    version=version,
    license='MIT',
    description='Convert number words eg. three hundred and forty two to numbers (342). '
                'Forked for https://github.com/WaltWh/LongSphinx, not intended for public use.',
    author='Akshay Nagpal & Walt Whiteside',
    author_email='tinman@mage.city',
    url='https://github.com/WaltWh/w2n',  # use the URL to the GitHub repo
    download_url='https://github.com/WaltWh/w2n/tarball/1.2',
    keywords=['numbers', 'convert', 'words'],  # arbitrary keywords
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10'
    ],
    long_description=readme,
    long_description_content_type="text/x-rst",
    python_requires=">=3.10.0",  # Probably not, but I haven't tested anything else
    test_suite="unit_testing"
)
