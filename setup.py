from setuptools import setup, find_packages

from prophetly import __version__

setup(
	name='prophetly-server',
	version=__version__,
	description='CLI for Prophetly, Interactive Time Series Forecasting Tool',
	keywords='timeseries forecasting data',
	author='Pravendra Singh',
	author_email='hackpravj@gmail.com',
	url='https://github.com/pravj/prophetly-server',
	packages=find_packages(exclude=['tests*']),
	install_requires=[
		'docopt == 0.6.2',
		'pandas == 0.19.2',
		'plotly == 2.0.6',
		'tornado == 4.3',
		'matplotlib == 2.0.0',
	],
	package_data={
		'prophetly.server.static': ['*.html', 'css/*.css', 'js/*.js', 'favicon.ico', 'media/*.svg'],
	},
	entry_points={
		'console_scripts': ['prophetly-server = prophetly.main:main']
	},
)
