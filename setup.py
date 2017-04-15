from os import path
from codecs import open
from setuptools import setup, find_packages

from prophetly import __version__

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='prophetly-server',
	version=__version__,
	description='CLI for Prophetly, Interactive Time Series Forecasting Tool',
	long_description=long_description,
	keywords='timeseries forecasting data cli',
	author='Pravendra Singh',
	author_email='hackpravj@gmail.com',
	url='https://github.com/pravj/prophetly-server',
	packages=find_packages(exclude=['tests*']),
	install_requires=[
		'docopt',
		'pandas',
		'plotly',
		'tornado',
		'matplotlib',
	],
	package_data={
		'prophetly.server.static': ['*.html', 'css/*.css', 'js/*.js', 'favicon.ico', 'media/*.svg'],
	},
	entry_points={
		'console_scripts': ['prophetly-server = prophetly.main:main']
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Environment :: Web Environment',
		'Natural Language :: English',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Scientific/Engineering :: Visualization',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
	],
)
