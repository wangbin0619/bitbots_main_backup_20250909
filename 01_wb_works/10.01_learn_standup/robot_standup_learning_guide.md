# Robot Standup System - Learning Guide

## System Overview

The Hamburg Bit-Bots robot standup system (`bitbots_dynup`) enables humanoid robots to recover from falls using **IMU-based closed-loop control** with **quintic spline trajectories**. The system achieves **2.1-2.7 second recovery times** and operates on artificial turf conditions similar to RoboCup competitions.

## Key Technical Components

### 1. **Spline-Based Motion Generation**
- **Quintic polynomial splines** generate smooth trajectories in Cartesian space
- **Continuous position, velocity, and acceleration** profiles prevent jerky movements
- **4 end-effectors controlled**: left/right hands and feet
- **6 DOF per end-effector**: x, y, z position + roll, pitch, yaw orientation

### 2. **Closed-Loop Stabilization**
- **IMU-based PD controllers** using fused angles representation
- **Real-time error correction** during dynamically unstable phases
- **Pitch and roll stabilization** prevents falls during transition
- **295ms minimum lead time** for fall detection and recovery initiation

### 3. **Multi-Direction Recovery**
- **Front standup**: Arms push forward, legs pull under body, transition to feet
- **Back standup**: Arms push backward, simultaneous leg positioning, roll-to-feet
- **Side recovery**: Roll to back position, then execute back standup procedure

### 4. **Parameter Optimization**
- **MOTPE/TPE algorithms** for automatic parameter tuning
- **15-24 free parameters** per direction (timing + pose parameters)
- **Multi-objective optimization**: balance speed vs stability
- **Sim-to-real transfer** validated on multiple robot platforms

## How the System Works

### Motion Pipeline
```
Fall Detection → Spline Generation → Stabilization → Inverse Kinematics → Motor Commands
```

1. **Spline Generation** (`dynup_engine.cpp:20-45`)
   - Creates quintic polynomial trajectories for each end-effector
   - Defines motion phases with semantic timing parameters
   - Initial pose = current robot position for smooth start

2. **Stabilization** (`dynup_stabilizer.cpp`)
   - Uses IMU fused angles (avoids gimbal lock)
   - PD controllers adjust foot placement to correct trunk orientation
   - Only active during dynamically unstable phases

3. **Inverse Kinematics** (BioIK solver)
   - Converts Cartesian end-effector poses to joint angles
   - Handles non-parallel kinematic chains in humanoid robots
   - Approximates unreachable poses for low-DOF arms

### Core Configuration Parameters (`dynup_config.yaml`)

**Timing Parameters (Front)**:
- `time_hands_side`: 0.3s - Move arms to sides
- `time_hands_rotate`: 0.3s - Rotate arms forward
- `time_hands_front`: 0.3s - Push arms forward
- `time_foot_ground_front`: 0.132s - Place feet on ground
- `time_torso_45`: 0.462s - Lift torso to 45°
- `time_to_squat`: 0.924s - Transition to squat position

**Pose Parameters**:
- `leg_min_length_front`: 0.244m - Minimum leg extension
- `max_leg_angle`: 71.71° - Maximum leg angle during recovery
- `trunk_overshoot_angle_front`: -5.0° - Torso overshoot compensation

## Getting Started Guide

### Step 1: Understand the Architecture
1. **Read the research paper**: `01_wb_works/01.02_papers/02_md/05 Fast and Reliable Stand-Up Motions...md`
2. **Study the README**: `bitbots_motion/bitbots_dynup/README.md`
3. **Examine configuration**: `bitbots_motion/bitbots_dynup/config/dynup_config.yaml`

### Step 2: Explore the Code Structure
```
bitbots_dynup/
├── include/bitbots_dynup/
│   ├── dynup_engine.hpp      # Main motion generation engine
│   ├── dynup_stabilizer.hpp  # IMU-based stabilization
│   ├── dynup_ik.hpp          # Inverse kinematics wrapper
│   └── dynup_node.hpp        # ROS2 node interface
├── src/
│   ├── dynup_engine.cpp      # Spline generation and control logic
│   ├── dynup_stabilizer.cpp  # PD controller implementation
│   └── dynup_node.cpp        # ROS2 integration
└── config/
    ├── dynup_config.yaml     # Main configuration parameters
    └── dynup_sim.yaml        # Simulation-specific parameters
```

### Step 3: Key Files to Study First

1. **`dynup_engine.cpp:20-100`** - Understand spline initialization
2. **`dynup_config.yaml:58-228`** - Learn parameter meanings
3. **Research paper pages 287-440** - Grasp theoretical foundation
4. **`dynup_stabilizer.cpp`** - Study closed-loop control implementation

### Step 4: Hands-On Learning Path

**Beginner (Week 1-2)**:
- Run existing standup motions in simulation
- Modify timing parameters and observe effects
- Study spline generation mathematics (quintic polynomials)
- Learn fused angles representation for orientation

**Intermediate (Week 3-4)**:
- Implement custom pose sequences
- Test parameter optimization with MOTPE
- Study stabilization PD controller tuning
- Compare open-loop vs closed-loop performance

**Advanced (Week 5-8)**:
- Port to new robot platform (different kinematics)
- Implement multi-objective optimization objectives
- Add new motion phases or recovery strategies
- Optimize for specific competition conditions

### Step 5: Development Environment Setup

**Required Dependencies**:
```bash
# Install ROS2 Iron
sudo apt install ros-iron-desktop

# Install optimization libraries
pip install optuna matplotlib

# Clone and build workspace
git clone <bitbots-repo>
cd bitbots
make install
colcon build --packages-select bitbots_dynup
```

**Test Commands**:
```bash
# Launch standup system
ros2 launch bitbots_dynup dynup.launch

# Test in simulation
ros2 launch bitbots_dynup test.launch

# Monitor debug output
ros2 topic echo /dynup_engine_debug
```

## Key Learning Resources

### Primary Sources
1. **Research Paper**: "Fast and Reliable Stand-Up Motions for Humanoid Robots Using Spline Interpolation and Parameter Optimization" (2021)
2. **Implementation**: `bitbots_motion/bitbots_dynup/` package
3. **Configuration Guide**: Parameter meanings in `dynup_config.yaml`

### Theoretical Background
- **Quintic Spline Mathematics**: Continuous acceleration/velocity trajectories
- **Fused Angles**: Singularity-free orientation representation 
- **BioIK**: Non-linear inverse kinematics for humanoid robots
- **MOTPE**: Multi-objective Bayesian optimization

### Performance Benchmarks
- **Speed**: 2.1-2.7s recovery time (optimized vs 3-4s manual)
- **Success Rate**: 85-95% on artificial turf
- **Platforms**: Wolfgang-OP, Darwin-OP, Sigmaban robots tested
- **Competition Validation**: RoboCup Humanoid League since 2015

## Next Steps for Deeper Learning

1. **Implement parameter optimization** for custom robot platform
2. **Study multi-contact dynamics** in complex recovery scenarios  
3. **Explore reinforcement learning** alternatives and comparisons
4. **Investigate sim-to-real transfer** challenges and solutions
5. **Design new recovery strategies** for specific failure modes

This system represents a mature, competition-tested approach to humanoid robot recovery that balances theoretical rigor with practical performance requirements.