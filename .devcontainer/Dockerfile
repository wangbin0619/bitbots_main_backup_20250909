#FROM ros:iron
FROM wb_cuda_devel_ros2_bitbots:latest

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set zsh as default shell
SHELL ["/bin/zsh", "-c"]

# This is required for sharing Xauthority
ENV QT_X11_NO_MITSHM=1

# Switch to the workspace directory
WORKDIR "/root/colcon_ws"


