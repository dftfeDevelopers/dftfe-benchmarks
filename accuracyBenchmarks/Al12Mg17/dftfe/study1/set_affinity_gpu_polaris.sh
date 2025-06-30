#!/bin/bash
num_gpus=$(nvidia-smi -L | wc -l)
#gpu=$((${num_gpus} - 1 - ${PMI_LOCAL_RANK} % ${num_gpus}))
gpu=$((${PMI_LOCAL_RANK} % ${num_gpus}))
export CUDA_VISIBLE_DEVICES=$gpu
echo “RANK= ${PMI_RANK} LOCAL_RANK= ${PMI_LOCAL_RANK} gpu= ${gpu}”
exec "$@"
