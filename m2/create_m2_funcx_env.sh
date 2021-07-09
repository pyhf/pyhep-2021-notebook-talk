echo "Create funcX Endpoint for pyhf: pyhf-funcx"

module load python

conda env create -f expanse-environment.yml
conda activate pyhf-expanse-gpu
conda env list

module list
