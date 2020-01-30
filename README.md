# AWS Elasticsearch Speedtest Data Shipper

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/Made%20With-Python%203.7-blue.svg?style=for-the-badge" alt="Made with Python 3.7">
    </a>
</p>
<p align="center">
    <a href="https://img.shields.io/badge/Version-1.3.3-lightgrey.svg">
        <img src="https://img.shields.io/badge/Version-1.0.1-lightgrey.svg" alt="Version 1.0.1">
    </a>
</p>


<p align="center">
 Programatically ship Speedtest CLI results to an AWS Elasticsearch Service from an endpoint of your choosing.
</p>

## Table of Contents

- [Speedtest Shipper](#AWS-Elasticsearch-Speedtest-Shipper)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Run This Yourself](#run-this-yourself)
    - [Local Development](#local-development)
      - [Without Docker](#without-docker)
      - [With Docker](#with-docker)
    - [Production](#production)
      - [Without Docker](#prod-without-docker)
      - [With Docker](#prod-with-docker)
  - [Dependencies](#dependencies)
  - [Meet the Team](#meet-the-team)

## Overview
A python script which uses the [Speedtest CLI](https://www.speedtest.net/apps/cli) to programatically ship results to an AWS Elasticsearch Service from an endpoint.

## Project Structure

See below for an explanation of the files in the tree.

```text
├── Pipfile → Pipenv requirements.
├── Pipfile.lock → Pipenv lock file.
├── README.md
├── requirements.txt → Python requirements.
├── run.py → Run script.
└── src
    ├── __init__.py
    ├── config.py → Developer created config file.
    ├── config_template.py → Template for config.py file.
    ├── cronTab.py →
    └── speedtestShipper.py → Main shipper script.
└── test
    ├── __init__.py
    └── test.py → Unittest.
```

## Run This Yourself

### Local Development

This data shipper is running on `Python 3.7`. We strongly advise the use of either [Anaconda](https://www.anaconda.com/distribution/) or [pipenv](https://pipenv.readthedocs.io/en/latest/) to manage a virtual environment in which you can install the dependencies for local development.

#### Without Docker

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install the dependencies.
3. Generate some (AWS Elasticsearch Service) keys, and put them in a `src/config.py` file like so:

_Please use [`src/config_template.py`](src/config_template.py) file as a template._

```python
AWS_ES_ENDPOINT = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'host': '',
    'region': '',
    'service': ''
}
```

4. To add the Elasticsearch index and source specific details look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

``` python
ES_INDEX = {
    'index': '',
    'doc_type': '',
    'source': ''
}
```
5. Install the [Speedtest CLI](https://www.speedtest.net/apps/cli) using the workflow specific to your OS:
    - On macOS: `brew install speedtest --force`
        - Tap the Speedtest CLI by running the command: `brew tap teamookla/speedtest`
        - Update Homebrew by running: `brew update`
        - Install the Speedtest CLI by running: `brew install speedtest --force`
        - Confirm it installed by running: `speedtest --version`
    - For more OSs please reference the [Speedtest Website](https://www.speedtest.net/apps/cli).


#### With Docker

1. Clone this repository.
3. Generate some (AWS Elasticsearch Service) keys, and put them in a `src/config.py` file like so:

_Please use [`src/config_template.py`](src/config_template.py) file as a template._

```python
AWS_ES_ENDPOINT = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'host': '',
    'region': '',
    'service': ''
}
```

4. To add the Elasticsearch index and source specific details look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

``` python
ES_INDEX = {
    'index': '',
    'doc_type': '',
    'source': ''
}
```

5. Build the docker container with `docker build -t aws-es-speedtest-shipper .`

6. Run the docker container with `docker run aws-es-speedtest-shipper python run.py --verbose=no` and your off!

### Production

This data shipper is running on `Python 3.7`. We strongly advise the use of [Anaconda](https://www.anaconda.com/distribution/) to manage a virtual environment in which you can install the dependencies.

#### Prod Without Docker

We strongly recommend that this data shipper be run on a docker instance (due to the ease of installation) on the host machine, however if you choose not to, the steps below outline the installation procedure.

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install the dependencies.
3. Generate some (AWS Elasticsearch Service) keys, and put them in a `src/config.py` file like so:

_Please use [`src/config_template.py`](src/config_template.py) file as a template._

```python
AWS_ES_ENDPOINT = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'host': '',
    'region': '',
    'service': ''
}
```

4. To add the Elasticsearch index and source specific details look into the `src/config.py` you created, and put them in like so:

_Please use [`src/config_template.py`](src/config_template.py) as a reference._

``` python
ES_INDEX = {
    'index': '',
    'doc_type': '',
    'source': ''
}
```
5. Run `./run.py` and you're off!

## Dependencies

## Meet the Team
<div>
  <p align="center">
    <a href="https://github.com/coreysabia">
      <img src="https://avatars1.githubusercontent.com/u/12410796?s=400&u=ee153e9c9496939767c01315212efb65936c01e8&v=4" height="100px" width="100px" alt="Version 1.0">
    </a>
    <p align="center"><strong>Corey Sabia</strong></p>
    <p align="center">Lead Developer</p>
    <p align="center"></p>
  </p>
</div>
