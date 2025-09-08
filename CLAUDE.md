# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Hamburg Bit-Bots RoboCup Humanoid Soccer team software stack built on ROS 2 Iron. The codebase contains packages for robot perception, behavior, motion control, simulation, and team communication for autonomous humanoid soccer robots.

## Essential Commands

### Build and Development
- `make install` - Full installation (pulls libraries, dependencies, sets up workspace)  
- `make install-no-root` - Installation without root privileges
- `make update` - Update codebase, dependencies, and setup hooks
- `make pull-all` - Update all repositories and download model files
- `make fresh-libs` - Clean and re-setup third-party libraries (DESTRUCTIVE)

### Code Quality and Testing  
- `make format` - Format all code using pre-commit hooks
- `make pre-commit` - Install pre-commit hooks
- `colcon build --symlink-install` - Build ROS 2 packages (from /colcon_ws)
- `colcon test --event-handlers console_direct+ --return-code-on-test-failure` - Run tests

### Linting and Style
- `ruff check --fix` - Python linting with auto-fix
- `ruff format` - Python formatting
- `clang-format -i` - C++ formatting  
- `pre-commit run --all-files` - Run all pre-commit hooks

## Architecture Overview

This is a **ROS 2 Iron-based robotics stack** for the Hamburg Bit-Bots RoboCup team, organized as a multi-package workspace.

### Key Package Categories
- **bitbots_behavior/** - High-level robot behaviors and decision making
- **bitbots_motion/** - Movement, walking, kicking, and animation systems
- **bitbots_vision/** - Computer vision and object detection
- **bitbots_world_model/** - State estimation and filtering
- **bitbots_navigation/** - Localization, path planning, and mapping
- **bitbots_misc/** - Utilities, diagnostics, and common functionality
- **bitbots_simulation/** - Webots and PyBullet simulation environments
- **lib/** - Third-party dependencies managed via workspace.repos

### Build System
- **CMake + package.xml** for ROS 2 packages
- **colcon** for workspace building and testing
- **vcs** for multi-repository management (workspace.repos)

### External Dependencies
- Neural network models downloaded from https://data.bit-bots.de/
- Third-party ROS packages managed in lib/ via workspace.repos
- Hardware interfaces for Dynamixel servos and cameras

### Testing Strategy
- Python tests use pytest conventions
- C++ tests integrated with colcon test framework
- Pre-commit hooks enforce code quality (ruff, clang-format, cppcheck)
- CI runs full build and test suite on Ubuntu Jammy

## Development Workflow

1. **Setup**: Run `make install` for full setup or `make update` for incremental updates
2. **Build**: Use `colcon build --symlink-install` from workspace root (/colcon_ws in CI)
3. **Test**: Run `colcon test` to verify changes
4. **Format**: Use `make format` before committing
5. **Models**: Large files (neural networks) are fetched separately via `make pull-files`

## Important Notes
- ROS 2 Iron is the target distribution
- Wolfgang robot hardware specifications in bitbots_robot/
- Simulation environments support both Webots and PyBullet
- Code style enforced via pre-commit hooks (ruff for Python, clang-format for C++)
