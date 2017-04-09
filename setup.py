from setuptools import setup, find_packages

from prophetly import __version__

setup(
	name='prophetly-server',
	version=__version__,
	description='Interactive Time Series Forecasting Tool',
	keywords='timeseries forecasting data',
	author='Pravendra Singh',
	author_email='hackpravj@gmail.com',
	url='https://github.com/pravj/prophetly-server',
	packages=find_packages(exclude=['tests*']),
	install_requires=['docopt == 0.6.2', 'pandas == 0.19.2', 'plotly == 2.0.6', 'tornado == 4.3'],
	package_data={
		'prophetly.server.static': ['*.html', '*.css', '*.js']
	},
	entry_points={
		'console_scripts': ['prophetly-server = prophetly.main:main']
	},
)
