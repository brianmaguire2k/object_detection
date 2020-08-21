#!/bin/bash

# local directory with notebooks/code/etc
HOST_WORK="/home/bmaguire/repos/object_detection/samples"
# local directory with train/test data
#HOST_DATA="/home/bmaguire/data/VOC"
# local directory to save models (so they only need to be downloaded once)
HOST_SAVED_MODELS="/home/bmaguire/models"

# mount local directories to container
# configure port for jupyter notebook
# launch bash shell in user home directory
# remove --gpus all if no gpus (duh)
docker run -it --rm --gpus all \
	-v $HOST_SAVED_MODELS:/home/tensorflow/models/research/object_detection/test_data \
    -v $HOST_WORK:/home/tensorflow/work \
	-p 8888:8888 \
	tf2_od bash
