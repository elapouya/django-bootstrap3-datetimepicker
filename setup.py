import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

VERSION = '3.0.0'

setup(
    name='django2-bootstrap3-datetimepicker',
    packages=['bootstrap3_datetime'],
    include_package_data=True,
    version=VERSION,
    description='Bootstrap3 compatible datetimepicker for Django 2.x projects.',
    long_description=long_description,
    author='Nakahara Kunihiko/Samuel Colvin/Eric Lapouyade',
    author_email='elapouya@gmail.com',
    url='https://github.com/elapouya/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
