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
$ . expanse/setup_expanse_funcx_env_gpu.sh
```

### `funcX` endpoint

To generate the `funcX` endpoint first source the environment setup script

```console
$ . expanse/setup_expanse_funcx_env_gpu.sh
```

and then generate a default `funcX` configuration file and overwrite it with the prepared `funcX/expanse-config.py`

```console
$ funcx-endpoint configure pyhf
YYYY-MM-DD HH:MM:SS endpoint:177 [INFO]  No existing configuration found at /home/$USER/.funcx/config.py. Initializing...
A default profile has been create for <pyhf> at /home/$USER/.funcx/pyhf/config.py
Configure this file and try restarting with:
    $ funcx-endpoint start pyhf
$ cp funcX/expanse-gpu-config.py ~/.funcx/pyhf/config.py
```

then startup the endpoint

```console
$ funcx-endpoint start pyhf
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:173 [INFO]  Starting endpoint with uuid: 12345678-abcd-abcd-abcd-123456789101
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:238 [INFO]  Launching endpoint daemon process
$ funcx-endpoint list
+---------------+--------+--------------------------------------+
| Endpoint Name | Status |             Endpoint ID              |
+===============+========+======================================+
| pyhf          | Active | 12345678-abcd-abcd-abcd-123456789101 |
+---------------+--------+--------------------------------------+
```

**N.B.:** As this endpoint is going to be persistent after you log off of EXPANSE(!) you'll want to preserve its endpoint ID into a text file that you can save to the machine that will be used at submit time that is ignored from version control

```console
$ funcx-endpoint list | grep pyhf | awk '{print $(NF-1)}' > endpoint_id.txt
# From the machine to be used at submit time
# $ scp EXPANSE:~/pyhep-2021-notebook-talk/endpoint_id.txt .
# $ echo "endpoint_id.txt" >> .gitignore
```

## Useage

With the `funcx` endpoint up and running on EXPANSE you can now run the `expanse-example.ipynb` example on any computer.

## Monitoring

As EXPANSE uses SLURM, you can monitor jobs running with `squeue`

```console
$ squeue --user $USER
```

and if you have hung jobs or jobs that you want to kill you can cancel them with `scancel`

```console
$ scancel --user $USER
```
