#!/bin/bash
module load anaconda cuda/11.1 cudnn/8.1.1_cuda11.x
source activate fbgan
export PYTHONUNBUFFERED=1
python wgan_gp_lang_gene_analyzer.py
