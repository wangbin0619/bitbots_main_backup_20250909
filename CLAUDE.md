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
- **Quintic polynomial walking engine** in bitbots_quintic_walk/ - Uses Cartesian space spline generation optimized with MOTPE/TPE algorithms
- **Dynamic kicking system** in bitbots_dynamic_kick/ - Reactive kicking with real-time trajectory adaptation
- **Stand-up motions** in bitbots_dynup/ - IMU-based closed-loop control with fused angles representation, achieving 2.1-2.7s recovery times
- **Animation system** for pre-recorded motions in bitbots_animation_server/ - Spline-based keyframe interpolation
- **BioIK inverse kinematics** solver for non-parallel robot configurations
- **Walking performance**: 0.51m/s forward, 0.48m/s backward, 0.22m/s sideward on Wolfgang-OP

### Hardware Interface  
- **Dynamixel servo communication** via bitbots_ros_control/ using QUADDXL multi-bus architecture (>1kHz control loops)
- **Wolfgang-OP robot**: 20-DOF humanoid with elastic compliance elements (NinjaFlex 3D printed parts)
- **Parallel Elastic Actuator (PEA)** design providing 37% torque reduction through torsion springs
- **Multi-bus servo system**: 4x RS-485 buses achieving 1373Hz peak communication rate
- **IMU, pressure sensors, buttons** integrated in ros_control framework with custom electronics
- **Robot-specific configurations** in config/ directories (amy, donna, jack, melody, rory)
- **Fall detection**: 295ms minimum lead time with threshold-based classification

### Vision System
- **YOEO neural network** (You Only Encode Once) - Shared encoder for detection+segmentation with 68% speed improvement
- **CNN-based ball and robot detection** in bitbots_vision/ achieving mAP50=83.36% on TORSO-21 dataset
- **FastDepth monocular depth estimation** for embedded deployment on Intel NCS2 (40.9 FPS, <2W power)
- **Dynamic color space adaptation** for robust performance under varying lighting conditions
- **Heat map particle filtering** for robust object tracking with multi-modal uncertainty handling
- **Vision pipeline performance**: 16 FPS processing rate, 6.7 FPS YOEO inference on Intel NCS2
- **TORSO-21 dataset**: 20,000+ curated images with automated diversity filtering using variational autoencoders
- **Model files** downloaded from https://data.bit-bots.de/models/

### Behavior & Decision Making
- **Dynamic Stack Decider (DSD)** framework - Lightweight behavior management with hierarchical reevaluation
- **Four-tier architecture**: Deliberative → Sequencing → Skills → HCM → Hardware layers
- **Humanoid Control Module (HCM)** abstraction layer enabling wheeled robot software adaptation
- **Stack-based decision making** with bottom-to-top reevaluation for reactive behavior
- **Semantic robot states** for high-level behavior coordination and fall recovery integration

### Simulation
- **PyBullet physics simulation** support with accurate Wolfgang-OP modeling
- **Webots robotic simulation** environment integration for development and testing
- **Simulation-specific configuration variants** with parameter adaptation for sim-to-real transfer
- **Competition-validated algorithms** - All systems tested in RoboCup Humanoid League competitions since 2015

## Algorithm Implementation Guide

### Core Algorithms & Optimization
- **MOTPE/TPE optimization**: Multi-Objective Tree-structured Parzen Estimator for parameter tuning (preferred over CMA-ES)
- **Quintic spline generation**: Cartesian space trajectory planning with smooth acceleration profiles
- **Hierarchical reevaluation**: DSD framework processes decisions bottom-to-top for reactive behavior
- **Shared encoder architectures**: YOEO approach reduces computation by 68% compared to separate networks
- **Heat map particle filtering**: Multi-modal tracking with explorer particles for robustness
- **BioIK solver**: Handles non-parallel kinematic chains in humanoid robots
- **Fused angles representation**: IMU-based orientation control for balance and stability

### Performance Benchmarks & Targets
- **Control frequencies**: Target >1kHz for servo communication, 715-750Hz achieved with full sensor reading
- **Vision processing**: 16 FPS pipeline, 6.7 FPS neural inference on embedded hardware (<2W power)
- **Motion performance**: Walking speeds up to 0.3m/s, kick ball speeds 3-8m/s, stand-up time 2-5 seconds
- **Vision accuracy**: Ball detection 85-95%, robot detection 70-90%, processing latency 50-200ms
- **System performance**: ROS 2 latency 1-10ms, CPU usage 60-90%, memory usage 2-8GB
- **Communication**: Team communication 2-10Hz, UDP multicast, message timeout 1000-5000ms
- **Fall detection**: Minimum 295ms lead time required for successful recovery initiation

### Configuration Guidelines
- **Robot-specific parameters**: Always check for robot variants (amy, donna, jack, melody, rory) in config files
- **Motion control**: Walking frequency 1.0-2.0Hz, step length 0.02-0.08m, kick execution time 1.0-3.0s, balance threshold ±30°
- **Vision processing**: Camera resolution 640x480 to 1920x1080, processing frequency 30-60 FPS, detection confidence 0.5-0.9
- **Simulation vs real**: Separate parameter sets needed for sim-to-real transfer, especially for motion control
- **Embedded deployment**: Consider Intel NCS2 constraints (<2W power, real-time inference requirements)
- **Multi-task learning**: Prefer shared encoder architectures when implementing multiple vision tasks
- **System integration**: Modular ROS nodes, configuration-driven parameters, hardware abstraction layers

## Research Foundation

This codebase implements algorithms and approaches from **60 research papers and theses** by the Hamburg Bit-Bots team (1997-2024), representing 27 years of continuous research and development. The comprehensive research archive provides deep technical insights across all major robotics domains.

### Academic Publication Categories (60 papers total)
- **Core Research Papers (17)**: Fundamental technical contributions and novel algorithms
- **Academic Theses (28)**: Bachelor's and Master's theses with detailed technical implementations  
- **Team Description Papers (8)**: System evolution and architecture from 2012-2020 competitions
- **Project Reports (5)**: Course projects and practical implementations
- **ROS/System Papers (2)**: ROS 2 performance analysis and concurrency studies

### Technical Domain Coverage (by research focus)
- **Hardware Platform (0.43)**: Wolfgang-OP robots, sensors, actuators, communication protocols
- **Machine Learning (0.34)**: Neural networks, optimization, parameter tuning, learning algorithms
- **Computer Vision (0.31)**: CNN-based detection, depth estimation, semantic segmentation, datasets
- **System Architecture (0.29)**: ROS integration, modular design, real-time systems, abstractions
- **Simulation Modeling (0.24)**: Physics simulation, validation environments, sim-to-real transfer
- **Motion Control (0.22)**: Quintic walking, dynamic kicking, balance, stand-up motions
- **Team Coordination (0.21)**: Multi-agent systems, communication protocols, strategy planning
- **Behavior Decision (0.19)**: DSD framework, state machines, action selection, planning

### System Evolution Timeline
- **2012-2014 Foundation**: Wolfgang-OP platform establishment, basic vision, manual parameter tuning
- **2015-2017 Intelligence**: Machine learning integration, advanced motion control, CNN-based detection
- **2018-2020 Integration**: ROS 2 migration, system-wide optimization, real-time performance focus

### Research Archive & Analysis
- **Full research papers**: Available in `01_wb_works/01.02_papers/02_md/` (Markdown format)
- **Comprehensive analysis**: `00_tmp/bitbots_papers_comprehensive_summary.md` (60 papers analyzed)
- **Technical knowledge extract**: `00_tmp/bitbots_technical_knowledge_extract.md` (AI assistance guide)
- **Structured data**: `00_tmp/bitbots_comprehensive_papers_analysis.json` (machine-readable insights)

## Important Notes

- **Never commit to lib/ directory** - contains third-party code managed by workspace.repos
- **Large files** (neural network models) are fetched via wget from data.bit-bots.de
- **Robot configurations** are robot-specific - always check config files for variants
- **Use make commands** for multi-repository operations rather than individual git commands
- **Competition-tested algorithms** - most systems have been validated in RoboCup competitions since 2015
- **Performance-critical code** - many components have real-time constraints requiring optimization
- **Research-backed design** - implementation decisions based on extensive academic research and competition experience