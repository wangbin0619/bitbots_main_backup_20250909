# Dev Container

Dev Container is used based on bitbots code base.

## Folder Structure

1. The file in 00_wb_works is for Ubuntu Server system setup.
2. The file in .devcontainer is for building docker image of bitbots.

## Dev Container buildup steps

Step 1. Use Dockerfile in 00_wb_works/step_01_ubuntu_cuda_ros2 to add ROS2 on base of nvidia/cuda:12.2.0-Ubuntu 22.02
   FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

Step 2. Use Dockerfile in .00_wb_works/step_02_ubuntu_cuda_ros2_bitbots to add additional bitbots required packages.
   FROM wb_cuda_devel_ros2:latest

Step 3. In VScode, build the DevContainder using Dockerfile in .devcontainer. (Claude Code included)

4. Docker Images List as below:
  ID       CREATED         SIZE
  vsc-bitbots_main-7bf6c5d452d4483615d2b20d84d313089ff59569694f38a4082194f8fed030ad   latest                          
  wb_cuda_devel_ros2_bitbots                                                          latest                     
  wb_cuda_devel_ros2                                                                  latest

## Directory Path within Dev Container
The default user is "robot"
1. /srv/host_home/git/bitbots/software
2. /robot/colcon_ws/src/bitbots_main/.devcontainer

## Nvidia Docker Container - Ensure it works

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

## Remote SSH Access with Display Forwarding (Windows + WSL to Ubuntu Server) - Not verified. 
**Since it work after Dev Container start up after Remote SSH + Dev Container.**

When accessing the Ubuntu server remotely via SSH from a Windows laptop with WSL, additional X11 forwarding configuration is needed.

### On Windows Laptop (WSL)

1. Install an X server like VcXsrv or X410, or use WSL2's built-in X11 forwarding
2. If using VcXsrv, configure it to accept connections from network clients

### SSH Connection with X11 Forwarding

Connect to the Ubuntu server with X11 forwarding enabled:

```bash
ssh -X username@ubuntu_server_ip
# or for trusted X11 forwarding:
ssh -Y username@ubuntu_server_ip
```

### On Ubuntu Server (before starting Dev Container)

Configure X11 forwarding for SSH connections:

```bash
# Allow X11 forwarding for SSH connections
xhost +local:docker
xhost +SI:localuser:$USER
# For remote connections, you may also need:
xhost +inet:your_laptop_ip
```

### Dev Container Configuration

Ensure your devcontainer.json includes these environment variables:

```json
"containerEnv": {
    "DISPLAY": "${localEnv:DISPLAY}",
    "QT_X11_NO_MITSHM": "1",
    "XDG_RUNTIME_DIR": "/tmp"
}
```

### Testing the Setup

1. SSH with X11 forwarding: `ssh -X user@server`
2. Start Dev Container
3. Test X11 forwarding: `xclock` or `xeyes`
4. Test ROS2 GUI: `ros2 run turtlesim turtlesim_node`

The key difference from local access is enabling X11 forwarding through SSH and ensuring the X server on your Windows laptop accepts network connections.

## Robot Repository Full Build

Hello there! Welcome to the Bit-Bots ROS 2 development environment!
If you just (re)build this container a few manual steps are nessessary:
Create a ssh key with 'ssh-keygen -q -f /home/robot/.ssh/id_rsa -N "" &&  cat /home/robot/.ssh/id_rsa.pub'.
Copy the commands output and add it to your GitHub account ('https://github.com/settings/keys') (ctrl+click to open in browser).

Now you can install the rest of the workspace and compile everything with **'make install && cba'**.
To update an existing workspace you can use 'make update && cba'.
To compile all packages in the workspace use 'cba'. If you want to compile only a specific package use 'cbs <package_name>'.

Run 'xhost local:root' in a terminal on the host machine to enable GUI applications (e.g. rviz2) in the container. This needs to be done after every restart of the host machine.
