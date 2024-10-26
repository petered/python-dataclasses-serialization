from setuptools import setup, find_packages
import re
# Get the version, following advice from https://stackoverflow.com/a/7071358/851699

VERSIONFILE="_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
    name='dataclass-serialization',
    author='Madman Bob (with some additions by Peter)',
    author_email='',
    url='https://github.com/petered/python-dataclasses-serialization',
    long_description='Serialization for dataclasses .',
    install_requires=['dataclasses', 'more_properties', 'typing_inspect', 'toolz', 'toposort'],
    version=verstr,
    packages=find_packages(),
    scripts=[])
