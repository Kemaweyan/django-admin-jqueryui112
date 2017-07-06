#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-admin-jqueryui112',
    version='1.12.1b5',
    license='BSD License',
    author='Piotr Kilczuk -- Hint, Taras Gaidukov -- Kemaweyan',
    author_email='piotr@hint.pl, kemaweyan@gmail.com',
    url='https://github.com/Kemaweyan/django-admin-jqueryui112',
    description='A fork of the django-admin-jqueryui. Simply adds a jquery ui to the admin panel',
    packages=find_packages(),
    provides=['admin_jqueryui', ],
    include_package_data=True,
    package_data = {"admin_jqueryui": ["static/admin_jqueryui/js/*.js"]},
    classifiers=[
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
