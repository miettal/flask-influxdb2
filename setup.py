"""
Flask-InfluxDB2
---------------

Flask extension for InfluxDB 2.0 client
"""
from setuptools import setup


setup(
    name='Flask-InfluxDB2',
    version='0.1',
    url='https://github.com/miettal/flask-influxdb2/',
    license='BSD',
    author='Hiromasa Ihara',
    author_email='iharahiromasa@gmail.com',
    description='Flask extension for InfluxDB 2.0 client',
    long_description=__doc__,
    py_modules=['flask_influxdb2'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
