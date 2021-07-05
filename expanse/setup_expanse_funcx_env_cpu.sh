#!/bin/bash
echo "Setting up CPU enabled funcX Endpoint for pyhf"
module purge
module restore

module load cpu
module load anaconda3

conda activate pyhf-expanse-gpu
conda env list

module list
