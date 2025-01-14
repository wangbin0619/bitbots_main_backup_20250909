# Dev Container

Dev Container is used based on bitbots code base.

## Directory Path

1. /srv/host_home/git/bitbots/software
2. /root/colcon_ws/src/bitbots_main/.devcontainer

## Nvidia Docker Container

```bash
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
