FROM osrf/ros:iron-desktop-full-jammy

# Copy .deb files into the container
COPY pylon_*.deb .
COPY codemeter*.deb .

# Install wget and .deb packages
RUN apt-get update && apt-get install -y wget \
    && apt-get install -y ./pylon_*.deb ./codemeter*.deb \
    && rm pylon_*.deb codemeter*.deb \
    && rm -rf /var/lib/apt/lists/*
