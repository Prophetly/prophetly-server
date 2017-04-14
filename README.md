<p align="center">
  <a href="http://prophetly.github.io">
    <img alt="Prophetly" src="https://avatars2.githubusercontent.com/u/26736074?v=3&s=150" width="144">
  </a>
</p>

<h3 align="center">
  Prophetly
</h3>

<p align="center">
  Interactive Time Series Forecasting on the Fly
</p>

<p align="center">
  <a href="https://github.com/Prophetly/Prophetly">
    <img src="https://img.shields.io/badge/phase-develoment-brightgreen.svg">
  </a>
</p>

## Prophetly Server [![Build Status][build-img]][build] [![Supported Version][version-img]][version] [![Distribution Format][format-img]][format]

PyPI Package for Prophetly powered by tornado and [prophetly-client](https://github.com/Prophetly/prophetly-client)

```bash
 ___                  _          _    _
| _ \ _ _  ___  _ __ | |_   ___ | |_ | | _  _
|  _/| '_|/ _ \| '_ \| ' \ / -_)|  _|| || || |
|_|  |_|  \___/| .__/|_||_|\___| \__||_| \_, |
               |_|                       |__/

Prophetly Server v0.0.2.a1
```

### Installation

For now the package is only available on [testpypi](https://testpypi.python.org/pypi/prophetly-server).

```bash
pip install --extra-index-url https://testpypi.python.org/pypi prophetly-server
```

### Usage

```bash
prophetly-server start
```

```bash
 __________________
| Prophetly Server |

Command Line Interface to Prophetly\'s Time Series Forecasting Tool.

Visit https://github.com/Prophetly/prophetly-server for feedback.

Usage:
  prophetly-server start [--port=<PORT>] [--upload_path=<PATH>]
  prophetly-server (-h | --help)
  prophetly-server --version

Options:
  -h --help     Show this screen.
  --version     Show version.
```

##### Customizing the Port

The default port for `prophetly-server` is **9009**, you can change it using the `--port=<PORT>` flag.

##### Upload Directory

By default, `prophetly-server` will create a directory named `uploads` in the current working directory. You can point it to a different directory using `--upload_path=<PATH>` flag.

[build-img]: https://travis-ci.org/Prophetly/prophetly-server.svg?branch=master
[build]: https://travis-ci.org/Prophetly/prophetly-server
[version-img]: https://img.shields.io/badge/Python-2.7,%203.4,%203.5,%203.6-brightgreen.svg
[version]: https://github.com/Prophetly/prophetly-server
[format-img]: https://img.shields.io/badge/format-wheel-brightgreen.svg
[format]: https://github.com/Prophetly/prophetly-server
