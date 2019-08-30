from setuptools import setup, find_packages
import os


def __get_version(developement=False):
    file = open("../version.txt", "r")
    version = file.readlines()[0]
    if developement:
        version += ".dev1"
    return version



def get_schema_files():
    return [
        '../schema/base-model.yaml',
        'bounded-context.yaml',
        'c4-model.yaml',
        'physical - relational - erd.yaml'
    ]


def __get_schema_files():
    return "schema", list(map(lambda d: d.path, os.scandir("../schema")))


setup(
    name='system-model-schema',

    version=__get_version(developement=True),

    description="System Model Schema Python API",
    long_description='''
        TBD
    ''',

    url='https://github.com/zalum/system-model-schema',

    author='florin',
    author_email='https://github.com/zalum',

    license='MIT',

    keywords='system model schema',
    python_requires=">=3.5",
    install_requires=[
        "jinja2>=2.10.1",
        "pyyaml>=5.1.2"
    ],
    packages=find_packages(exclude=['tests'], include=['sms', 'sms.*']),
    package_dir={'sms': 'sms'},
    package_data={'sms': ['*.yaml']}
)
