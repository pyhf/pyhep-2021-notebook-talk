# EXPANSE Example

## Setup

### Creating virtual environment on EXPANSE

First create the environment by clone this repository down to EXPANSE under your user area `HOME` and then running the environment creation script

```console
$ cd expanse
$ bash create_expanse_funcx_env.sh
```

This will take a long time as it uses Conda which can be very slow. In the future, the environment can be setup by simply sourcing the setup script

```console
$ . expanse/setup_expanse_funcx_env.sh
```

### `funcX` endpoint

To generate the `funcX` endpoint first source the environment setup script

```console
$ . expanse/setup_expanse_funcx_env.sh
```

and then generate a default `funcX` configuration file and overwrite it with the prepared `funcX/expanse-config.py`

```console
$ funcx-endpoint configure pyhf
2021-07-04 15:53:23 endpoint:177 [INFO]  No existing configuration found at /home/$USER/.funcx/config.py. Initializing...
A default profile has been create for <pyhf> at /home/$USER/.funcx/pyhf/config.py
Configure this file and try restarting with:
    $ funcx-endpoint start pyhf
$ cp funcX/expanse-config.py ~/.funcx/config.py
```
