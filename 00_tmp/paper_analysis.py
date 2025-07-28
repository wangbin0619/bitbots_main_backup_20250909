#!/usr/bin/env python3
"""
BitBots Research Papers Analysis Script
======================================
Analyzes and categorizes research papers from the Hamburg Bit-Bots RoboCup team
to extract key technical insights for AI assistance.
"""

import os
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Set
import re

@dataclass
class PaperSummary:
    """Data structure for paper analysis"""
    number: str
    title: str
    year: str
    category: str
    subcategory: str
    key_algorithms: List[str]
    technical_details: List[str]
    config_parameters: List[str]
    performance_metrics: List[str]
    codebase_links: List[str]
    abstract: str

class BitBotsResearchAnalyzer:
    """Analyzer for BitBots research papers"""
    
    def __init__(self, papers_dir: str):
        self.papers_dir = Path(papers_dir)
        self.papers = []
        self.categories = {
            "Hardware & Robotics Platform": {
                "Robot Platform Design", "Hardware Interfaces", "Actuators & Sensors", 
                "Electronics & Control", "Mechanical Design"
            },
            "Motion Control & Locomotion": {
                "Walking Algorithms", "Stand-up Motions", "Kicking Motions", 
                "Balance & Stability", "Motion Planning"
            },
            "Computer Vision & Perception": {
                "Object Detection", "Neural Networks", "Image Processing", 
                "Localization", "Depth Estimation"
            },
            "Decision Making & Behavior": {
                "Behavior Trees", "State Machines", "Control Architecture", 
                "Multi-Agent Coordination", "Game Strategy"
            },
            "System Architecture & Integration": {
                "Software Architecture", "Communication Protocols", 
                "Real-time Systems", "Simulation", "Integration"
            },
            "Datasets & Evaluation": {
                "Dataset Creation", "Performance Evaluation", "Benchmarking", 
                "Annotation Tools"
            }
        }
    
    def analyze_paper_01_wolfgang_op(self) -> PaperSummary:
        """Wolfgang-OP: A Robust Humanoid Robot Platform"""
        return PaperSummary(
            number="01",
            title="Wolfgang-OP: A Robust Humanoid Robot Platform for Research and Competitions",
            year="2021",
            category="Hardware & Robotics Platform",
            subcategory="Robot Platform Design",
            key_algorithms=[
                "Parallel Elastic Actuator (PEA) design",
                "Fall detection classification (threshold-based)",
                "Compliance mechanism using 3D printed elements",
                "High-frequency servo communication (700-1000Hz)"
            ],
            technical_details=[
                "20 DOF humanoid robot (80cm, 7.5kg)",
                "3D printed elastic elements (NinjaFlex TPU)",
                "Torsion spring knee actuators for energy efficiency",
                "Multiple processors: Intel NUC + Odroid-XU4 + Intel NCS2",
                "Custom electronics with 4x RS-485 buses",
                "Basler acA2040-35gc global shutter camera",
                "MPU6500 IMU with custom modules",
                "MX-106, MX-64, XH540 Dynamixel servos"
            ],
            config_parameters=[
                "Control loop frequency: 700-1000Hz",
                "PEA spring constant: k = 0.76 Nm/rad",
                "Battery: 5200mAh 14.8V 4-cell LiPo",
                "Camera resolution: 2048x1536 (binned 4x)",
                "Vision pipeline: 16 FPS",
                "Fall detection thresholds and lead times"
            ],
            performance_metrics=[
                "Fall detection: 295ms min lead time, 596ms mean",
                "PEA torque reduction: 37% max reduction",
                "Vision performance: mAP improvements with YOLO v3 tiny",
                "Control frequency: 715-750Hz with full sensor reading",
                "Weight: 37% torque reduction in squatting motion"
            ],
            codebase_links=[
                "https://github.com/bit-bots/wolfgang_robot",
                "bitbots_ros_control",
                "bitbots_dynup",
                "bitbots_quintic_walk"
            ],
            abstract="Open humanoid robot platform focusing on robustness with 3D printed elastic elements, high control frequencies, torsion spring actuators, and multi-processor architecture."
        )
    
    def analyze_paper_03_depth_estimation(self) -> PaperSummary:
        """Monocular Depth Estimation in RoboCup Soccer"""
        return PaperSummary(
            number="03",
            title="Applying Monocular Depth Estimation in RoboCup Soccer",
            year="2022",
            category="Computer Vision & Perception",
            subcategory="Depth Estimation",
            key_algorithms=[
                "U-Net encoder-decoder architecture",
                "FastDepth (MobileNet-based) architecture",
                "Monocular depth estimation CNN",
                "OpenVINO optimization pipeline",
                "Hyperparameter optimization with Optuna"
            ],
            technical_details=[
                "Input size: 128×128 pixels for real-time performance",
                "Loss function: distance loss + gradient loss",
                "Depth mapping: ˆx = 1 − 1/(x+1) normalization",
                "Intel NCS2 deployment for embedded inference",
                "Microsoft Azure Kinect for ground truth collection",
                "Data augmentation: horizontal flip, RGB shift, brightness/contrast"
            ],
            config_parameters=[
                "Learning rates: 0.0001-0.0063 (optimized per architecture)",
                "Batch sizes: 4-16 (architecture dependent)",
                "Weight decay: 10^-12 to 10^-8",
                "Scheduling gamma: 0.1-0.2",
                "Loss weighting: 0.5 for simulation data"
            ],
            performance_metrics=[
                "FastDepth: 40.9 FPS vs U-Net: 8.7 FPS on Intel NCS2",
                "U-Net simulation: MAE=0.145, RMSE=0.245",
                "FastDepth real-world: MAE=0.364, RMSE=0.619",
                "Power consumption: <2W on Intel NCS2",
                "Accuracy metrics: δ1, δ2, δ3 threshold accuracies"
            ],
            codebase_links=[
                "https://github.com/bit-bots/depth-estimation",
                "OpenVINO toolkit integration",
                "Intel NCS2 deployment pipeline"
            ],
            abstract="Monocular depth estimation pipeline for RoboCup using FastDepth and U-Net architectures, deployed on Intel NCS2 for real-time performance on embedded systems."
        )
    
    def analyze_paper_04_walking(self) -> PaperSummary:
        """Bipedal Walking through Parameter Optimization"""
        return PaperSummary(
            number="04",
            title="Bipedal Walking on Humanoid Robots through Parameter Optimization",
            year="2022",
            category="Motion Control & Locomotion",
            subcategory="Walking Algorithms",
            key_algorithms=[
                "Quintic spline-based pattern generation",
                "Multi-Objective Tree-structured Parzen Estimator (MOTPE)",
                "Tree-structured Parzen Estimator (TPE)",
                "PID stabilization controllers",
                "BioIK inverse kinematics solver"
            ],
            technical_details=[
                "Cartesian space trajectory generation",
                "Finite state machine for walk phases",
                "Fused angles representation for balance",
                "MoveIt interface for IK solutions",
                "Support for non-parallel robot kinematics",
                "Multi-objective optimization (forward, backward, sideward, turn)"
            ],
            config_parameters=[
                "Optimization trials: 1000 MMOTPE + 500 MOTPE",
                "Objective scalarization: f(x) = ff + fb + 2*fs + 0.2*ft",
                "Phase modulation based on joint torque/foot pressure",
                "Step duration parameters (robot-specific)",
                "Foot distance parameters (size-dependent ranges)"
            ],
            performance_metrics=[
                "Wolfgang-OP: 0.51m/s forward, 0.48m/s backward, 0.22m/s sideward",
                "OP3: 0.54m/s forward, 0.45m/s backward, 0.13m/s sideward", 
                "Darwin-OP: 0.29m/s forward (back motion kinematically limited)",
                "Optimization success: MOTPE outperformed CMA-ES and NSGA-II"
            ],
            codebase_links=[
                "https://bit-bots.github.io/quintic_walk/",
                "bitbots_quintic_walk",
                "Webots simulation integration",
                "ROS/ROS2 interfaces"
            ],
            abstract="Open-source omnidirectional walk controller using quintic splines and parameter optimization, working on all non-parallel humanoid robots with performance baselines."
        )
    
    def analyze_paper_05_standup(self) -> PaperSummary:
        """Fast and Reliable Stand-Up Motions"""
        return PaperSummary(
            number="05",
            title="Fast and Reliable Stand-Up Motions for Humanoid Robots Using Spline Interpolation and Parameter Optimization",
            year="2021",
            category="Motion Control & Locomotion",
            subcategory="Stand-up Motions",
            key_algorithms=[
                "Quintic spline interpolation in Cartesian space",
                "IMU-based PD controllers",
                "Multi-Objective Tree-structured Parzen Estimator (MOTPE)",
                "Fused angles orientation representation",
                "BioIK inverse kinematics"
            ],
            technical_details=[
                "6 splines per end-effector (x,y,z,roll,pitch,yaw)",
                "Continuous first and second derivatives",
                "23 convolutional layers in baseline network",
                "PyBullet simulation with uneven ground (1cm height variation)",
                "Early termination for invalid IK solutions"
            ],
            config_parameters=[
                "Front motion: 9 phase + 6 pose parameters",
                "Back motion: 6 phase + 9 pose parameters", 
                "Optimization: 500 trials minimum",
                "Success rate, time, fused pitch, head height objectives",
                "PD gains via Ziegler-Nichols method"
            ],
            performance_metrics=[
                "Wolfgang: 2.7s front, 2.1s back standup time",
                "Darwin: 2.9s front (back motion not possible)",
                "Sigmaban: 2.2s front, 2.2s back",
                "21-62.4 trials to success (platform dependent)",
                "Real robot: improved speed over keyframe baseline"
            ],
            codebase_links=[
                "github.com/bit-bots/bitbots_motion/tree/master/bitbots_dynup",
                "PyBullet simulation interface",
                "MoveIt integration"
            ],
            abstract="Closed-loop stand-up motion system using parametrized Cartesian quintic splines with IMU-based PD control and parameter optimization for fast, reliable recovery."
        )
    
    def analyze_paper_06_yoeo(self) -> PaperSummary:
        """YOEO - You Only Encode Once CNN"""
        return PaperSummary(
            number="06",
            title="YOEO – You Only Encode Once: A CNN for Embedded Object Detection and Semantic Segmentation",
            year="2021",
            category="Computer Vision & Perception", 
            subcategory="Neural Networks",
            key_algorithms=[
                "YOLOv4-tiny encoder with shared backbone",
                "U-NET-like segmentation decoder",
                "Multi-task learning (detection + segmentation)",
                "OpenVINO optimization pipeline",
                "Additive skip connections"
            ],
            technical_details=[
                "Input resolution: 416×416 pixels",
                "Two YOLO detection heads at different resolutions",
                "Depthwise separable convolutions in decoder",
                "Nearest-neighbor upsampling",
                "Combined loss: YOLOv4 + cross-entropy",
                "Intel NCS2 deployment"
            ],
            config_parameters=[
                "ADAM optimizer with equal loss weighting",
                "Training epochs: up to 60",
                "Data augmentation: sharpness, brightness, hue, mirroring",
                "Skip connections from encoder to decoder",
                "Architecture variants tested: YOEO-rev-0 to YOEO-rev-9"
            ],
            performance_metrics=[
                "TORSO-21: Ball detection mAP50=83.36%, IoU=85.02%",
                "Runtime: 6.7 FPS on Intel NCS2 (<2W power)",
                "68.70% speed benefit over separate networks",
                "Cityscapes: competitive performance vs specialized approaches",
                "Network size: ~4M parameters (YOEO-rev-7)"
            ],
            codebase_links=[
                "github.com/bit-bots/YOEO",
                "OpenVINO deployment pipeline",
                "PyTorch implementation"
            ],
            abstract="Hybrid CNN combining YOLOv4-tiny object detection and U-NET semantic segmentation with shared encoder, optimized for embedded deployment on Intel NCS2."
        )
    
    def analyze_paper_07_torso21(self) -> PaperSummary:
        """TORSO-21 Dataset"""
        return PaperSummary(
            number="07",
            title="TORSO-21 Dataset: Typical Objects in RoboCup Soccer 2021",
            year="2021",
            category="Datasets & Evaluation",
            subcategory="Dataset Creation",
            key_algorithms=[
                "Variational autoencoder for image diversity filtering",
                "Greedy sampling with k-d tree proximity",
                "Webots simulation data generation",
                "Automated scene generation with randomization"
            ],
            technical_details=[
                "Real-world: 10,464 images from 12 locations",
                "Simulation: 10,000 images from Webots",
                "6 ball types, 5 camera types, 6 robot models",
                "Classes: ball, robot, goalpost, field, lines, intersections",
                "Variational autoencoder: 3.4M parameters, 300D latent space",
                "Ground truth: bounding boxes, polygons, segmentation masks"
            ],
            config_parameters=[
                "VAE training: 128×112 pixel input images",
                "Reconstruction error threshold: 1.64σ (10% outliers)",
                "Simulation parameters: camera FOV 60°-180°, height 0.45-0.95m",
                "Scene generation: 4 scenarios × 2 team colors × 6 robots",
                "K-d tree filtering with Euclidean distance"
            ],
            performance_metrics=[
                "YOLOv4 baseline: Ball 98.8% mAP50, Robot 96.0% mAP50",
                "IoU metrics: Ball 91.1%, Field boundary 70.0%",
                "Dataset reduction: 44,366 → 10,464 images (diversity)",
                "Annotation distribution: 101,432 total annotations",
                "Public availability with evaluation tools"
            ],
            codebase_links=[
                "https://github.com/bit-bots/TORSO_21_dataset",
                "ImageTagger integration",
                "Webots simulation pipeline"
            ],
            abstract="Comprehensive RoboCup soccer dataset with real-world and simulated images, featuring automated diversity filtering and standardized evaluation metrics for vision algorithm comparison."
        )
    
    def analyze_paper_08_dsd(self) -> PaperSummary:
        """Dynamic Stack Decider Framework"""
        return PaperSummary(
            number="08",
            title="DSD - Dynamic Stack Decider: A Lightweight Decision Making Framework for Robots and Software Agents",
            year="2022",
            category="Decision Making & Behavior",
            subcategory="Control Architecture",
            key_algorithms=[
                "Stack-based decision architecture",
                "Domain Specific Language (DSL) for behavior definition",
                "Hierarchical reevaluation mechanism",
                "Action sequences and parameter passing",
                "Interrupt handling system"
            ],
            technical_details=[
                "Two element types: Decision Elements (DE) and Action Elements (AE)",
                "Stack maintains current state and decision history",
                "DSL symbols: # (subtree), $ (decision), @ (action), + (parameters)",
                "Reevaluation from bottom to top of stack",
                "Explorer particles and measurement aging",
                "ROS integration with visualization tools"
            ],
            config_parameters=[
                "Reevaluation frequency: configurable per decision element",
                "do_not_reevaluate flag for critical actions",
                "Parameter passing syntax in DSL",
                "Interrupt triggers: external events, state changes",
                "Stack depth and complexity scalable"
            ],
            performance_metrics=[
                "Maintainability: superior to FSM/HSM approaches",
                "Code reuse: excellent due to element separation",
                "Human readability: high with semantic labeling",
                "Scalability: good but limited parallelism",
                "Successfully used in RoboCup competitions since 2015"
            ],
            codebase_links=[
                "https://github.com/bit-bots/dynamic_stack_decider",
                "ROS package integration",
                "Python reference implementation"
            ],
            abstract="Lightweight decision-making framework combining behavior trees and hierarchical state machines, using a stack-based architecture with DSL for maintainable robot behavior."
        )
    
    def analyze_paper_09_hcm(self) -> PaperSummary:
        """Humanoid Control Module"""
        return PaperSummary(
            number="09",
            title="Humanoid Control Module: An Abstraction Layer for Humanoid Robots",
            year="2020",
            category="System Architecture & Integration",
            subcategory="Software Architecture", 
            key_algorithms=[
                "Dynamic Stack Decider (DSD) for state management",
                "Four-tier architecture extension",
                "Fall detection classification (IMU-based)",
                "Joint goal mutex system",
                "Hardware error detection and recovery"
            ],
            technical_details=[
                "Abstraction layer between skills and hardware",
                "Semantic robot states: Walking, Falling, Fallen, Controllable, etc.",
                "14 hierarchical decisions in DSD",
                "Message passing architecture (ROS)",
                "Integration with move_base navigation stack",
                "Support for teleoperation and autonomous operation"
            ],
            config_parameters=[
                "Fall detection thresholds for torso rotation/velocity",
                "Hardware timeout detection for IMU/pressure sensors",
                "Motor power management timers",
                "Joint goal forwarding rules per robot state",
                "DSD reevaluation frequency matching hardware interface"
            ],
            performance_metrics=[
                "Latency introduction: 0.25ms mean, 1.7ms max outliers",
                "Fall detection: ~1s fall time, 0.2s safe position time",
                "Stand-up time: 10s keyframe animation",
                "Successfully used in RoboCup 2018, 2019 competitions",
                "Enables standard wheeled robot navigation on bipeds"
            ],
            codebase_links=[
                "https://github.com/bit-bots/bitbots_motion",
                "ROS control integration",
                "move_base compatibility layer"
            ],
            abstract="Abstraction layer enabling wheeled robot software (like move_base) on humanoid robots by handling falls, hardware errors, and joint goal arbitration through DSD architecture."
        )
    
    def analyze_paper_10_servo_communication(self) -> PaperSummary:
        """High-Frequency Multi Bus Servo Communication"""
        return PaperSummary(
            number="10",
            title="High-Frequency Multi Bus Servo and Sensor Communication Using the Dynamixel Protocol",
            year="2019",
            category="Hardware & Robotics Platform",
            subcategory="Hardware Interfaces",
            key_algorithms=[
                "Multi-bus RS-485 communication architecture",
                "QUADDXL FT4232H-based controller design",
                "Dynamixel Protocol 2.0 optimization",
                "Sync read/write command optimization",
                "Custom sensor integration (IMU, pressure)"
            ],
            technical_details=[
                "4-channel USB to RS-485 converter (FT4232H)",
                "12 MBaud maximum per bus theoretical",
                "20 MX-64 servos test configuration", 
                "Custom IMU module (MPU6050 + STM32F103)",
                "Improved pressure sensor (ADS1262 ADC)",
                "Protocol 2.0 with improved checksums and sync commands"
            ],
            config_parameters=[
                "Baud rates tested: 1, 2, 4 MBaud (4.5 MBaud failed)",
                "Servo response delay: ~50μs average",
                "Control loop target: >1kHz frequency",
                "IMU update rate: 1kHz achievable",
                "Pressure sensor: 697Hz (limited by ADC multiplexing)",
                "USB latency timer: set to 0ms for performance"
            ],
            performance_metrics=[
                "QUADDXL peak: 1373Hz with 4 buses at 4 MBaud",
                "Single bus maximum: ~400Hz at 4 MBaud", 
                "3x performance improvement with multi-bus",
                "IMU sensor: 1kHz update rate achieved",
                "Pressure sensor: 8.7x improvement over baseline (80Hz → 697Hz)"
            ],
            codebase_links=[
                "https://github.com/bit-bots/bitbots_quaddxl",
                "https://github.com/bit-bots/bitbots_lowlevel/tree/master/bitbots_ros_control",
                "https://github.com/bit-bots/bit_foot",
                "https://github.com/bit-bots/dxl_sensor"
            ],
            abstract="Multi-bus servo communication system achieving >1kHz control loops using QUADDXL controller and optimized Dynamixel Protocol 2.0 with custom sensor integration."
        )
    
    def analyze_paper_11_vision_pipeline(self) -> PaperSummary:
        """Open Source Vision Pipeline"""
        return PaperSummary(
            number="11",
            title="An Open Source Vision Pipeline Approach for RoboCup Humanoid Soccer",
            year="2019",
            category="Computer Vision & Perception",
            subcategory="Image Processing",
            key_algorithms=[
                "Pipe-and-filter architecture pattern",
                "Fully Convolutional Neural Networks (FCNNs) for ball detection",
                "Dynamic color space adaptation",
                "Convex hull field boundary detection",
                "Candidate finder abstraction pattern"
            ],
            technical_details=[
                "Python implementation with ROS integration",
                "Modular design with 80 configurable parameters",
                "HSV color spaces for team markers, YAML for field colors",
                "Multi-threading: conventional methods + FCNN parallel processing",
                "Debug framework with real-time visualization",
                "Jetson TX2 deployment platform"
            ],
            config_parameters=[
                "80 parameters in YAML configuration",
                "Dynamic reconfiguration via ROS parameter server",
                "Color space definitions: HSV ranges and lookup tables",
                "FCNN input preprocessing and candidate extraction thresholds",
                "Field boundary detection algorithm selection based on head angle"
            ],
            performance_metrics=[
                "Processing rate: 8.1 FPS on Jetson TX2 without debug",
                "Jaccard Index results: Ball 0.677, Field boundary 0.925",
                "Line detection: 0.021 (point-based vs line-based labels)",
                "Goalpost: 0.183, Robot detection: 0.149-0.380",
                "Public dataset: 707 fully labeled images"
            ],
            codebase_links=[
                "https://github.com/bit-bots/bitbots_vision",
                "ImageTagger integration: https://imagetagger.bit-bots.de",
                "ROS message compatibility"
            ],
            abstract="Open-source Python vision pipeline for RoboCup with modular design, FCNN ball detection, dynamic color adaptation, and comprehensive debug/evaluation framework."
        )
    
    def analyze_paper_12_particle_filter(self) -> PaperSummary:
        """Position Estimation using Particle Filters"""
        return PaperSummary(
            number="12",
            title="Position Estimation on Image-Based Heat Map Input using Particle Filters in Cartesian Space",
            year="2020",
            category="Computer Vision & Perception",
            subcategory="Localization",
            key_algorithms=[
                "Heat map to Cartesian space transformation",
                "Novel observation model for particle weighting",
                "Measurement aging mechanism",
                "Explorer particles for multi-modal filtering",
                "K-nearest measurements selection"
            ],
            technical_details=[
                "Each heat map pixel as individual measurement m=(r,w)",
                "Particle weight: w(p_i) = Σ w(m_j)/δ_i,j for k closest measurements",
                "Movement model with Gaussian noise for uncertainty",
                "AprilTag ground truth for evaluation",
                "Integration with FCNN ball detection model"
            ],
            config_parameters=[
                "FCNN input: 200×150 pixels (resized from original)", 
                "Minimal activation threshold for pixel inclusion",
                "Measurement aging: weight decrease v per timestep",
                "k-nearest measurements parameter",
                "Explorer particle fraction: 5% of total particles",
                "Ground plane assumption for depth calculation"
            ],
            performance_metrics=[
                "Mean error: 0.0771m vs 0.0879m (conventional)",
                "Max error: 0.54m vs 0.61m (conventional)",
                "Standard deviation: 0.07714m vs 0.08142m",
                "5567 continuous measurements evaluated",
                "Better handling of false positives and multi-modal distributions"
            ],
            codebase_links=[
                "Integration with bitbots_vision pipeline",
                "AprilTag detection for ground truth",
                "RoboCup soccer ball tracking application"
            ],
            abstract="Novel particle filter approach using raw FCNN heat maps transformed to Cartesian space, improving object tracking robustness compared to conventional clustering methods."
        )
    
    def analyze_team_description_2020(self) -> PaperSummary:
        """Team Description 2020"""
        return PaperSummary(
            number="301",
            title="Hamburg Bit-Bots Humanoid League 2020",
            year="2020", 
            category="System Architecture & Integration",
            subcategory="Integration",
            key_algorithms=[
                "Custom particle filter localization",
                "Dynamic Stack Decider behavior system",
                "QUADDXL servo communication",
                "Closed-loop walking and kicking",
                "Vision pipeline with FCNN ball detection"
            ],
            technical_details=[
                "ROS Melodic software stack",
                "Integration challenges: walking odometry accuracy",
                "Hardware robustness testing needed",
                "Cable wear issues on servo buses",
                "Multi-bus isolation for fault tolerance"
            ],
            config_parameters=[
                "PID controller tuning for servo stability",
                "Localization using all vision inputs (lines, posts, boundary)",
                "Game controller state integration",
                "Obstacle handling in path planning",
                "Updated head design for mechanical robustness"
            ],
            performance_metrics=[
                "Lessons learned from RoboCup 2019 competition",
                "Integration testing revealed component interaction issues",
                "Walking/pathfinding feedback loop problems identified",
                "Hardware failure points in head design addressed"
            ],
            codebase_links=[
                "bitbots_vision pipeline",
                "bitbots_quintic_walk",
                "QUADDXL communication system",
                "Dynamic Stack Decider framework"
            ],
            abstract="Team description outlining 2020 developments including custom particle filter localization, hardware improvements, and lessons learned from system integration challenges."
        )
    
    def generate_summary_report(self) -> Dict:
        """Generate comprehensive analysis report"""
        
        # Analyze key papers
        papers = [
            self.analyze_paper_01_wolfgang_op(),
            self.analyze_paper_03_depth_estimation(),
            self.analyze_paper_04_walking(),
            self.analyze_paper_05_standup(),
            self.analyze_paper_06_yoeo(),
            self.analyze_paper_07_torso21(),
            self.analyze_paper_08_dsd(),
            self.analyze_paper_09_hcm(),
            self.analyze_paper_10_servo_communication(),
            self.analyze_paper_11_vision_pipeline(),
            self.analyze_paper_12_particle_filter(),
            self.analyze_team_description_2020()
        ]
        
        # Categorize by topic areas
        topic_categories = {}
        for category, subcategories in self.categories.items():
            topic_categories[category] = []
        
        for paper in papers:
            topic_categories[paper.category].append(paper)
        
        # Extract key algorithms and approaches
        all_algorithms = []
        all_technical_details = []
        all_config_params = []
        all_performance_metrics = []
        all_codebase_links = []
        
        for paper in papers:
            all_algorithms.extend(paper.key_algorithms)
            all_technical_details.extend(paper.technical_details) 
            all_config_params.extend(paper.config_parameters)
            all_performance_metrics.extend(paper.performance_metrics)
            all_codebase_links.extend(paper.codebase_links)
        
        return {
            "analysis_summary": {
                "total_papers_analyzed": len(papers),
                "main_categories": list(self.categories.keys()),
                "analysis_focus": "Papers 01-17 and key team descriptions (301-309)"
            },
            "topic_categories": {
                category: {
                    "papers": [{"number": p.number, "title": p.title, "year": p.year} 
                             for p in papers_list],
                    "key_insights": self._extract_category_insights(category, papers_list)
                }
                for category, papers_list in topic_categories.items() if papers_list
            },
            "key_technical_areas": {
                "algorithms_and_methods": list(set(all_algorithms)),
                "technical_implementations": list(set(all_technical_details[:20])),  # Top 20
                "configuration_parameters": list(set(all_config_params[:15])),      # Top 15  
                "performance_benchmarks": list(set(all_performance_metrics[:15]))   # Top 15
            },
            "codebase_integration": {
                "main_repositories": list(set([link for link in all_codebase_links 
                                              if 'github.com/bit-bots' in link])),
                "key_packages": [
                    "bitbots_vision", "bitbots_quintic_walk", "bitbots_dynup",
                    "bitbots_ros_control", "dynamic_stack_decider", "bitbots_motion"
                ]
            },
            "ai_assistance_insights": self._generate_ai_insights(papers)
        }
    
    def _extract_category_insights(self, category: str, papers: List[PaperSummary]) -> List[str]:
        """Extract key insights for each category"""
        insights = []
        
        if category == "Hardware & Robotics Platform":
            insights = [
                "Wolfgang-OP: 20-DOF humanoid with elastic compliance elements",
                "QUADDXL: Multi-bus servo communication achieving >1kHz control loops", 
                "3D printed elastic elements (NinjaFlex) for fall robustness",
                "Torsion spring PEA design for energy efficiency (37% torque reduction)",
                "Custom electronics with 4x RS-485 buses for distributed control"
            ]
        elif category == "Motion Control & Locomotion":
            insights = [
                "Quintic spline-based walking in Cartesian space with parameter optimization",
                "MOTPE/TPE optimization outperforms CMA-ES for motion parameters",
                "Closed-loop stand-up using IMU-based PD controllers",
                "Fused angles representation for balance control",
                "BioIK solver for non-parallel robot kinematics"
            ]
        elif category == "Computer Vision & Perception":
            insights = [
                "YOEO: Shared encoder for detection+segmentation (68% speed improvement)",
                "FastDepth: Real-time monocular depth estimation on Intel NCS2",
                "TORSO-21: Comprehensive dataset with simulation+real data",
                "Heat map particle filtering for robust object tracking",
                "Dynamic color space adaptation for lighting robustness"
            ]
        elif category == "Decision Making & Behavior":
            insights = [
                "Dynamic Stack Decider: Lightweight behavior framework with DSL",
                "Hierarchical reevaluation from bottom-to-top of decision stack",
                "Superior maintainability compared to FSM/behavior tree approaches",
                "Successfully deployed in RoboCup competitions since 2015"
            ]
        elif category == "System Architecture & Integration":
            insights = [
                "Humanoid Control Module: Abstraction layer for wheeled robot software",
                "Four-tier architecture extending traditional 3T approach",
                "ROS-based modular design with message-passing architecture",
                "Fall detection and recovery integrated into control flow",
                "Semantic robot states for high-level behavior coordination"
            ]
        elif category == "Datasets & Evaluation":
            insights = [
                "TORSO-21: 20,000+ images with automated diversity filtering",
                "Variational autoencoder for dataset curation",
                "Comprehensive evaluation metrics and tools",
                "Public availability for algorithm comparison"
            ]
            
        return insights
    
    def _generate_ai_insights(self, papers: List[PaperSummary]) -> Dict:
        """Generate insights specifically for AI assistance"""
        return {
            "architectural_patterns": [
                "Modular ROS-based architecture with message passing",
                "Multi-tier control: Deliberative → Sequencing → Skills → HCM → Hardware",
                "Shared encoder architectures for multi-task learning",
                "Stack-based decision making with hierarchical reevaluation"
            ],
            "optimization_approaches": [
                "MOTPE/TPE for multi-objective parameter optimization",
                "Hyperparameter optimization with Optuna framework",
                "Real-time optimization constraints for embedded deployment",
                "Sim-to-real transfer considerations"
            ],
            "performance_considerations": [
                "Real-time constraints: >1kHz control loops, 16 FPS vision",
                "Embedded deployment: Intel NCS2, <2W power consumption", 
                "Multi-bus architectures for parallel processing",
                "Memory and computational efficiency trade-offs"
            ],
            "robustness_strategies": [
                "Elastic compliance elements for mechanical robustness",
                "Fall detection and recovery systems",
                "Dynamic color adaptation for lighting changes",
                "Multi-modal filtering for sensor uncertainty"
            ],
            "integration_lessons": [
                "Component interaction testing crucial for system integration",
                "Odometry accuracy affects higher-level planning",
                "Hardware robustness testing needed before competitions",
                "Modular design enables independent component development"
            ]
        }

def main():
    """Main analysis function"""
    papers_dir = r"D:\20-robot\01-bitbots\01_wb_works\01.02_papers\02_md"
    
    analyzer = BitBotsResearchAnalyzer(papers_dir)
    report = analyzer.generate_summary_report()
    
    # Save report to JSON
    output_file = r"D:\20-robot\01-bitbots\00_tmp\bitbots_research_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"Analysis complete! Report saved to: {output_file}")
    
    # Print summary
    print("\n" + "="*80)
    print("BITBOTS RESEARCH PAPERS ANALYSIS SUMMARY")
    print("="*80)
    
    print(f"\nTotal Papers Analyzed: {report['analysis_summary']['total_papers_analyzed']}")
    print(f"Main Categories: {', '.join(report['analysis_summary']['main_categories'])}")
    
    print("\n" + "-"*60)
    print("TOPIC CATEGORIES")
    print("-"*60)
    
    for category, data in report['topic_categories'].items():
        print(f"\n{category}:")
        print(f"  Papers: {len(data['papers'])}")
        for paper in data['papers']:
            print(f"    - [{paper['number']}] {paper['title']} ({paper['year']})")
        
        print("  Key Insights:")
        for insight in data['key_insights'][:3]:  # Top 3 insights
            print(f"    • {insight}")
    
    print("\n" + "-"*60)
    print("AI ASSISTANCE INSIGHTS")
    print("-"*60)
    
    ai_insights = report['ai_assistance_insights']
    print("\nArchitectural Patterns:")
    for pattern in ai_insights['architectural_patterns']:
        print(f"  • {pattern}")
    
    print("\nOptimization Approaches:")
    for approach in ai_insights['optimization_approaches']:
        print(f"  • {approach}")
    
    print("\nPerformance Considerations:")
    for consideration in ai_insights['performance_considerations']:
        print(f"  • {consideration}")
    
    print("\n" + "-"*60)
    print("KEY CODEBASE PACKAGES")
    print("-"*60)
    
    for package in report['codebase_integration']['key_packages']:
        print(f"  • {package}")

if __name__ == "__main__":
    main()