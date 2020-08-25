# Object Detection via Docker

This repo contains everything needed to build a Docker image for object detection using Tensorflow 2.3. This varies slightly from the official Tensorflow OD API docker images (available [here](https://github.com/tensorflow/models/tree/master/research/object_detection/dockerfiles/tf2) for reference) to include a few additional packages and a modified file structure for work/data/models/etc.

Docker images provide a clean and consistent way to configure a development environment and all dependencies. This image runs Ubuntu 18.04 with Tensorflow and the Object Detection API pre-installed. GPU support is included; you do not need to install CUDA toolkit on the host machine. Note that this can be run from any OS with Docker support, although running from Windows is a little more complicated. Sample launch scripts for Linux and Windows are included in the repo (as well as slightly modified version of a few official TF OD API tutorial notebooks).

## Prerequisites
- [Install Docker](https://docs.docker.com/get-docker/) on host machine
- Install/update official NVIDIA GPU driver (note you do NOT need to install CUDA Toolkit on the host machine!)
- [Install NVIDIA Docker support](https://github.com/NVIDIA/nvidia-docker)

## Installation
While the image can be built remotely using this repository as the build context, it is strongly suggested to clone the repository and build locally to include the samples and future collaborative work.

- Create a local directory and clone this repository:

    ```
    git clone https://github.com/brianmaguire2k/object_detection.git
    ```

- Navigate to the dockerfiles directory and run ```docker build``` to build the image. This might take a while!
<pre><code>    cd {REPO_ROOT}/dockefiles
    docker build -t tf2_od .
</code></pre>

- Verify installation by checking installed docker images

    ```
    docker image ls
    ```

If everything worked as intended, you should see a list including the ```tf2_od``` image you just built, along with the core tensorflow image that was used as the base.

## Usage
Sample scripts to launch the container are included in the ```launcher``` directory. The script mounts local volumes to the container, configures the port for accessing jupyter notebook, then launches a bash shell that starts in the ```tensorflow``` user's home directory.
### Mounting volumes
This script mounts several volumes from the host machine to the container:

- ```HOST_WORK```: mounted as ~/work in the container, local working directory that you want access to (ie project, code, notebooks, etc). Note that everything in this directory can be modified/deleted from the container so be careful.
- ```HOST_SAVED_MODELS```: local directory for caching downloaded tensorflow saved models. Create a directory and update variable name so you don't have to re-download models every time you run the container.
- ```HOST_DATA```: currently unused, in future work this will be the mount point for any local train/test data.

### Running sample notebooks
The ```samples``` directory contains slightly modified versions of several tutorial notebooks included with the TF OD API. Run them as follows:

- Change ```HOST_WORK``` in the launch script to point to the local ```samples``` directory
- Run the launch script
- From the command prompt, run ```jupyter notebook```
- Copy and paste the provided link to a browser on the host machine
- Navigate to ```~/work``` and run the notebooks (start with the inference tutorial)
