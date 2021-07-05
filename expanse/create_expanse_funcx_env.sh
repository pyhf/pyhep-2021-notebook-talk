echo "Create funcX Endpoint for pyhf: pyhf-expanse-gpu"
module purge
module restore

module load gpu/0.15.4
module load cuda/11.0.2
module load anaconda3

conda env create -f expanse-environment.yml
conda activate pyhf-expanse-gpu
conda env list

module list
