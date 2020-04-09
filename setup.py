from setuptools import setup

setup(
    name='eventum-group-ms',
    packages=['resources'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'pymysql'
    ],
)