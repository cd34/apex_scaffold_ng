from setuptools import find_packages
from setuptools import setup

version = '1.0.0'

setup(
    version=version,
    name='Apex Scaffolds',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points="""\
        [pyramid.scaffold]
        raja=apex_scaffolds:RajaTemplate
    """,
)
