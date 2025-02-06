# Dev Container

Dev Container is used based on bitbots code base.

## .zshrc

1. The file in 00_wb_works is for Ubuntu Server system setup.
2. The file in .devcontainer is for building docker image of bitbots.
3. Test

## Dev Container buildup steps

1. Use Dockerfile in 00_wb_works/step_01_ubuntu_cuda_ros2 to add ROS2 on base of nvidia/cuda:12.2.0-Ubuntu 22.02
   FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

2. Use Dockerfile in .00_wb_works/step_02_ubuntu_cuda_ros2_bitbots to add additional bitbots required packages.
   FROM wb_cuda_devel_ros2:latest

3. In VScode, build the DevContainder using Dockerfile in .devcontainer.
4. Docker Images List as below:
    ID       CREATED         SIZE
    vsc-bitbots_main-7bf6c5d452d4483615d2b20d84d313089ff59569694f38a4082194f8fed030ad   latest                     wb_cuda_devel_ros2_bitbots                                                          latest                     wb_cuda_devel_ros2                                                                  latest

## Directory Path within Dev Container

1. /srv/host_home/git/bitbots/software
2. /root/colcon_ws/src/bitbots_main/.devcontainer

## Nvidia Docker Container

```bash
# On the host system, make sure no-cgroups is false.
sudo nano /etc/nvidia-container-runtime/config.toml
# Set no-cgroups = false

docker run --rm --privileged \
  --gpus all \
  nvidia/cuda:12.4.0-runtime-ubuntu22.04 nvidia-smi

docker run --rm \
  --gpus all \
  --device /dev/nvidia0:/dev/nvidia0 \
  --device /dev/nvidia-uvm:/dev/nvidia-uvm \
  --device /dev/nvidia-uvm-tools:/dev/nvidia-uvm-tools \
  --device /dev/nvidiactl:/dev/nvidiactl \
  nvidia/cuda:12.4.0-runtime-ubuntu22.04 nvidia-smi
```

## Forwarding display from docker container to host

**(Done in Dev Container devcontainer.json)**

1. First, exit the container if you're in it.

2. On your host machine (Ubuntu), allow X server connections:

```bash
xhost +local:docker
```

3. When running the Docker container, add these flags to allow GUI applications:

```bash
docker run -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    your_image_name
```

Or if you're using `docker exec` to enter a running container:

```bash
docker exec -it \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    container_name bash
```

After this, try running the turtlesim node again:

```bash
ros2 run turtlesim turtlesim_node
```

If you still have issues, you might need to install additional QT dependencies in your Docker container:

```bash
apt-get update && apt-get install -y \
    qt5-default \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5core5a
```

Remember to revoke X server access when you're done:

```bash
xhost -local:docker
```
