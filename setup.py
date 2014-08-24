# -*- coding: utf-8 -*-
from setuptools import setup


description = ("A django package that allows easy identification of visitors' "
               "browser, operating system and device information (mobile "
               "phone, tablet or has touch capabilities).")

setup(
    name='django-user_agents',
    version='0.3.0',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['django_user_agents'],
    url='https://github.com/selwin/django-user_agents',
    license='MIT',
    description=description,
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['django', 'user-agents'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
