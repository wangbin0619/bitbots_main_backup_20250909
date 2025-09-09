#FROM ros:iron
FROM wb_cuda_devel_ros2_bitbots:latest

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set zsh as default shell
SHELL ["/bin/zsh", "-c"]

# This is required for sharing Xauthority
ENV QT_X11_NO_MITSHM=1

# Install pre-commit
RUN pip3 install pre-commit

# First, install Node.js and npm
RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Next, install the Claude Code CLI
RUN npm install -g @anthropic-ai/claude-code

# Create robot user with sudo privileges
RUN useradd -m -s /bin/zsh robot && \
    usermod -aG sudo robot && \
    echo "robot ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Copy zsh configuration from root to robot user
RUN cp /root/.zshrc /home/robot/.zshrc && \
    cp -r /root/.oh-my-zsh /home/robot/.oh-my-zsh && \
    chown -R robot:robot /home/robot/.oh-my-zsh /home/robot/.zshrc

# Add claude-skip alias for robot user
RUN echo 'alias claude-skip="claude --dangerously-skip-permissions"' >> /home/robot/.zshrc

# Switch to robot user
USER robot

# Switch to the workspace directory
WORKDIR "/home/robot/colcon_ws"


