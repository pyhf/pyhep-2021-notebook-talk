echo "Setting up FuncX Endpoint for pyhf"
module purge
module restore
module load cuda
module load anaconda3
conda activate pyhf-expanse-gpu

module list
