#!/bin/bash
#SBATCH -A research
#SBATCH -n 4
#SBATCH --gres=gpu:4
#SBATCH --mem-per-cpu=2048
#SBATCH --time=4-00:00:00
#SBATCH --mail-type=END
eval "$(conda shell.bash hook)"
conda activate cohere
python main.py --inference --arch mtl --epochs 10 --gpus 4 --batch_size 8 --corpus gcdc --sub_corpus all --model_name roberta-base --freeze_emb_layer --online_mode 0 --task 3-way-classification


