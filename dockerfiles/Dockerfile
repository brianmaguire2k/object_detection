# Dockerfile to build image for object detection api using TF 2.x

# use official tensorflow image as base
FROM tensorflow/tensorflow:2.3.0-gpu

# update repository and install system dependencies, create non-root user 'tensorflow'
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    protobuf-compiler \
    python3-tk \
	wget && \
	useradd -m tensorflow

# update pip then install python dependencies
RUN python -m pip install --no-cache-dir --upgrade pip && \
	python -m pip install --no-cache-dir pillow \
	lxml \
	matplotlib \
	Cython \
	contextlib2 \
	tf-slim \
	six \
	pycocotools \
	pandas \
	opencv-python \
	dataclasses \
	pyyaml \
	jupyter

# switch to non-root user, clone TF_VERSION model garden branch
ARG MODEL_DIR=/home/tensorflow/models
USER tensorflow
RUN git clone --depth 1	https://github.com/tensorflow/models.git ${MODEL_DIR}

# compile object detection protos
WORKDIR ${MODEL_DIR}/research
RUN	protoc object_detection/protos/*.proto --python_out=.

# add to PYTHONPATH
ENV PYTHONPATH=$PYTHONPATH:${MODEL_DIR}:${MODEL_DIR}/research

# expose port for jupyter notebook, copy local config file
EXPOSE 8888
COPY --chown=tensorflow jupyter_notebook_config.py /home/tensorflow/.jupyter/

# start in user home directory
WORKDIR /home/tensorflow/
