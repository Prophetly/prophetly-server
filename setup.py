from setuptools import setup

setup(
	name='prophetly-server',
	version='0.1.18',
	description='Interactive Time Series Forecasting Tool',
	keywords='timeseries forecasting data',
	author='Pravendra Singh',
	author_email='hackpravj@gmail.com',
	url='https://github.com/pravj/prophetly-server',
	packages=['prophetly', 'prophetly.server', 'prophetly.server.handlers', 'prophetly.server.static'],
	install_requires=['docopt == 0.6.2', 'pandas == 0.19.2', 'plotly == 2.0.6', 'tornado == 4.3'],
	package_data={
		'prophetly.server.static': ['*.html', '*.css', '*.js']
	},
	entry_points={
		'console_scripts': ['prophetly-server = prophetly.prophetly:main']
	},
)
