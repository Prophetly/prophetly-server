from setuptools import setup

setup(
	name='prophetly-server',
	version='0.1.0',
	description='Interactive Time Series Forecasting Tool',
	keywords='timeseries forecasting data',
	author='Pravendra Singh',
	author_email='hackpravj@gmail.com',
	url='https://github.com/pravj/prophetly-server',
	packages=['prophetly'],
	install_requires=['docopt == 0.6.2'],
	entry_points={
		'console_scripts': ['prophetly-server = prophetly.prophetly:main']
	},
)
