# -*- coding: utf-8 -*-
from setuptools import setup


description = ("A django package that allows easy identification of visitor's "
               "browser, operating system and device information (mobile "
               "phone, tablet or has touch capabilities).")

setup(
    name='django-user_agents',
    version='0.1.1',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['django_user_agents'],
    url='https://github.com/selwin/django-user_agents',
    license='MIT',
    description=description,
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data = { '': ['README.rst'] },
    #install_requires=['user-agents'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
