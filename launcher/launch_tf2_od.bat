@echo off

:: local directory with notebooks/code/etc
set HOST_WORK=C:/PATH_TO_SAMPLES_DIRECTORY
:: local directory to save models (so they only need to be downloaded once)
set HOST_SAVED_MODELS=C:/PATH_TO_SAVED_MODELS

:: mount local directories to container
:: configure port for jupyter notebook
:: launch bash shell in user home directory
:: remove --gpus all if no gpus
docker run -it --rm --gpus all -p 8888:8888 ^
-v %HOST_WORK%:/home/tensorflow/work ^
-v %HOST_SAVED_MODELS%:/home/tensorflow/models/research/object_detection/test_data ^
tf2_od bash
