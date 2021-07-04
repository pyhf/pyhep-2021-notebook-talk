echo "Setting up funcX Endpoint for pyhf"
module purge
module restore

module load gpu/0.15.4
module load cuda/11.0.2
module load anaconda3

conda activate pyhf-expanse-gpu
conda env list

module list
