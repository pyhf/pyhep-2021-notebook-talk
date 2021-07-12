from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint.executors import HighThroughputExecutor
from parsl.providers import LocalProvider
from parsl.launchers import SimpleLauncher

user_opts = {
    "dgx": {
        "worker_init": ". ${HOME}/code/pyhep-2021-notebook-talk/dgx/worker_env_setup.sh",
    }
}

config = Config(
    executors=[
        HighThroughputExecutor(
            label="DGX",
            provider=LocalProvider(
                init_blocks=1,
                min_blocks=0,
                max_blocks=2,
                nodes_per_block=1,  # default value
                parallelism=1,  # default value
                worker_init=user_opts["dgx"]["worker_init"],
                launcher=SimpleLauncher(),
                walltime="00:10:00",
            ),
        )
    ],
    funcx_service_address="https://api2.funcx.org/v2",
)

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "pyhf",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    "visible_to": [],
}
