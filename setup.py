from setuptools import setup, find_packages

setup(
    name='solarconnect',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=False,
    url='',
    license='',
    author='SolarFresh',
    author_email='shangyuhuang@gmail.com',
    description='',
    install_requires=[
        "google-api-python-client>=1.5.5",
        "maxminddb>=1.3.0",
        "mysql-connector>=2.2.3",
        "oauth2client>=3.0.0",
        "pandas>=0.20.3",
        "PyHive>=0.2.1",
        "pymongo>=3.4.0",
        "pyOpenSSL>=16.2.0",
        "requests>=2.18.2",
        "sasl>=0.2.1",
        "sqlalchemy>=1.2.0b2",
        "thrift>=0.10.0",
        "thrift-sasl>=0.2.1",
    ]
)
