# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '0.1'
description = 'FIXME'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='cisl.portal.policy',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='FIXME',
    author='FIXME',
    author_email='FIXME',
    url='https://github.com/cislgovbr/cisl.portal.policy',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['cisl', 'cisl.portal'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'brasil.gov.portal',
        'cisl.portal.casosdesucesso',
        'plone.api',
        'plone.app.upgrade',
        'Products.CMFPlone >=4.3',
        'Products.GenericSetup',
        'setuptools',
        'zope.i18nmessageid',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
            'plone.app.testing [robot] >=4.2.2',
            'plone.browserlayer',
            'plone.testing',
            'robotsuite',
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
