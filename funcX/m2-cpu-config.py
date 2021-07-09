from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname
from parsl.launchers import SrunLauncher
from parsl.providers import SlurmProvider

# PLEASE UPDATE user_opts BEFORE USE
user_opts = {
    "expanse": {
        "worker_init": ". ~/workarea/pyhep-2021-notebook-talk/m2/setup_m2_funcx_env_cpu.sh",
    }
}

# https://www.sdsc.edu/support/user_guides/expanse.html#running
config = Config(
    executors=[
        HighThroughputExecutor(
            label="Expanse_CPU",
            address=address_by_hostname(),
            provider=SlurmProvider(
                "shared",  # Partition / QOS
                account="nsa106",
                nodes_per_block=1,
                max_blocks=4,
                init_blocks=1,
                # string to prepend to #SBATCH blocks in the submit
                # script to the scheduler eg: '#SBATCH --constraint=knl,quad,cache'
                # scheduler_options=user_opts["expanse"]["scheduler_options"],
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init=user_opts["expanse"]["worker_init"],
                launcher=SrunLauncher(),
                walltime="00:10:00",
                # Slurm scheduler on Cori can be slow at times,
                # increase the command timeouts
                cmd_timeout=120,
            ),
        ),
    ],
)
