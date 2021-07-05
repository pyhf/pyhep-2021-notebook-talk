# [Distributed statistical inference with `pyhf`](https://indico.cern.ch/event/1019958/contributions/4418598/)

Jupyter notebook talk given at [PyHEP 2021](https://indico.cern.ch/event/1019958/) on distributed statistical inference with `pyhf`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyhf/pyhep-2021-notebook-talk/HEAD?urlpath=lab/tree/talk.ipynb)

## Setup

In a Python virtual environment run the following

```console
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r binder/requirements.txt
```

### Globus account

To use `funcX` requires the use of [Gloubs](https://www.globus.org/) and so will require you to first login to a Globus account to use the `funcx-sdk`. Globus allows authentication through existing organizational logins or through Google accounts or [ORCID iD](https://orcid.org/) so this shouldn't be a barrier to use.

## EXPANSE Example

First create the environment by clone this repository down to EXPANSE under your user area `HOME` and then running the environment creation script

```console
$ cd expanse
$ bash create_expanse_funcx_env.sh
```

This will take a long time as it uses Conda which can be very slow. In the future, the environment can be setup by simply sourcing the setup script

```console
$ . expanse/setup_expanse_funcx_env.sh
```

## Google Cloud Platform Example

WIP

## Additional references

- [Distributed Inference with `pyhf` and `funcX`](https://github.com/matthewfeickert/distributed-inference-with-pyhf-and-funcX)

# REMOVE:

(Launch Binder build)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyhf/pyhep-2021-notebook-talk/feat/add-explaining-text?urlpath=lab/tree/talk.ipynb)
