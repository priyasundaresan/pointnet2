#!/bin/bash
python train.py --model pointnet2_part_seg --log_dir log --gpu 0 --max_epoch 201 > log.txt 2>&1 &
