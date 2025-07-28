# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Hamburg Bit-Bots RoboCup Humanoid Soccer team software stack built on ROS 2 Iron. The codebase contains packages for robot perception, behavior, motion control, simulation, and team communication for autonomous humanoid soccer robots.

## Core Development Commands

### Build and Setup
- `make install` - Full installation including Basler SDK and all dependencies (requires root)
- `make install-no-root` - Installation without root privileges  
- `make update` - Update repositories and install all dependencies
- `make update-no-root` - Update without root privileges
- `make pull-all` - Pull all repositories and large files (neural network weights)
- `make fresh-libs` - Clean and reinstall third-party libraries (WARNING: deletes lib/ changes)

### Code Quality
- `make format` - Format all code using pre-commit hooks
- `pre-commit run --all-files` - Run all pre-commit checks
- `ruff check .` - Python linting
- `ruff format .` - Python formatting

### Dependencies
- `make rosdep` - Install ROS dependencies
- `make pip` - Install Python dependencies from requirements/dev.txt

## Architecture Overview

### Main Package Groups
- **bitbots_behavior/** - High-level robot behavior and decision making using Dynamic Stack Decider
- **bitbots_motion/** - Motion control including walking, kicking, dynamic movements, and animation
- **bitbots_vision/** - Computer vision for ball and robot detection
- **bitbots_lowlevel/** - Hardware interfaces for servos, sensors, buttons
- **bitbots_misc/** - Utilities, bringup configurations, cameras, diagnostics
- **bitbots_simulation/** - PyBullet and Webots simulation environments
- **bitbots_team_communication/** - Multi-robot communication and coordination
- **bitbots_navigation/** - Localization and path planning (limited implementation)
- **bitbots_world_model/** - Ball and robot tracking/filtering
- **bitbots_robot/** - Robot description files for Wolfgang humanoid robot

### Key Launch Files
- `bitbots_misc/bitbots_bringup/launch/teamplayer.launch` - Main robot launch file
- `bitbots_misc/bitbots_bringup/launch/simulator_teamplayer.launch` - Simulation launch
- `bitbots_misc/bitbots_bringup/launch/highlevel.launch` - Behavior and vision only
- `bitbots_misc/bitbots_bringup/launch/motion.launch` - Motion control only

### Configuration Structure
Most packages have a `config/` directory with YAML configuration files. Robot-specific configs often have variants for different robots (amy, donna, jack, melody, rory).

## Development Environment

### Dependencies
- ROS 2 Iron on Ubuntu
- Python 3.x with packages from requirements/ directory
- C++17 for compiled components
- Third-party libraries managed via workspace.repos in lib/ directory

### Code Style
- Python: Ruff linting and formatting (120 char line length)
- C++: clang-format with project .clang-format config
- CMake: cmake-format for CMakeLists.txt files
- Pre-commit hooks enforce style automatically

### Build System
- ROS 2 packages use standard CMakeLists.txt/package.xml structure
- Python packages use setup.py/setup.cfg
- Makefile provides convenience commands for multi-repo operations

## Testing
Individual packages may have test directories. Use standard ROS 2 testing patterns:
- `colcon test --packages-select <package_name>`
- Python tests typically use pytest

## Key Technical Details

### Motion Control
- Quintic polynomial walking engine in bitbots_quintic_walk/
- Dynamic kicking system in bitbots_dynamic_kick/
- Stand-up motions in bitbots_dynup/
- Animation system for pre-recorded motions in bitbots_animation_server/

### Hardware Interface
- Dynamixel servo communication via bitbots_ros_control/
- IMU, pressure sensors, buttons integrated in ros_control framework
- Robot-specific configurations in config/ directories

### Vision System
- CNN-based ball and robot detection in bitbots_vision/
- Model files downloaded from https://data.bit-bots.de/models/
- Image processing and field mapping capabilities

### Simulation
- PyBullet physics simulation support
- Webots robotic simulation environment integration
- Simulation-specific configuration variants

## Important Notes

- Never commit to lib/ directory - it contains third-party code managed by workspace.repos
- Large files (neural network models) are fetched via wget from data.bit-bots.de
- Robot configurations are robot-specific - check config files for variants
- Use make commands for multi-repository operations rather than individual git commands