# Imports, parses, and converts data to JSON from an excel spreadsheet.

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run sxlxs cli application

$ sxlxs --help


### run pytest / coverage

$ make test
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `sxlxs`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it sxlxs --help
```
