BACHELORTHESISComparisonofMeasurementSystemsforKinematicCalibrationofaHumanoidRobotvorgelegtvonJasperGüldensteinMIN-FakultätFachbereichInformatikTechnischeAspekteMultimodalerSystemeStudiengang:InformatikMatrikelnummer:6808089Erstgutachter:Prof.Dr.JianweiZhangZweitgutachter:M.Sc.MarcBestmannAbstract

An accurate kinematic model is crucial for all robotics applications utilizing for-
ward or inverse kinematics. These applications include but are not limited to
motion planning, many types of sensor data processing, and simulation. Accuracy
is especially required for the transforms between the sensors and the robot’s in-
ternal reference frame to calculate the positions of the sensors’ measurements in
relation to the other kinematic chains of the robot.
While the known dimensions of the robot’s mechanical parts can be used to create
a kinematic model, calibration might be required to reduce inaccuracies in this
model caused by manufacturing tolerances, assembly, and deformation.
This bachelor thesis describes the modeling and calibration of the Wolfgang hu-
manoid robot platform. Three measurement systems are compared and evaluated
for this calibration. A signi(cid:12)cant error reduction of reprojection error is achieved.

Zusammenfassung

Ein genaues kinematisches Modell ist f(cid:127)ur alle Robotikanwendungen die Vorw(cid:127)arts-
oder Inverskinematik verwenden von entscheidender Bedeutung. Diese Anwendun-
gen umfassen Bewegungsplanung, viele Arten von Sensordatenverarbeitung, und
Simulation, sind jedoch nicht darauf beschr(cid:127)ankt. Genauigkeit ist insbesondere
f(cid:127)ur die Transformationen zwischen den Sensoren und dem internen Referenzkor-
dinatensystem des Roboters erforderlich, um die Positionen der Sensormessungen
relativ zu den anderen kinematischen ketten des Roboters zu berechnen.
W(cid:127)ahrend die bekannten Abmessungen der mechanischen Teile des Roboters zur Er-
stellung eines kinematischen Modells verwendet werden k(cid:127)onnen, ist oft eine Kalib-
rierung erforderlich sein, um Ungenauigkeiten in diesem Modell zu reduzieren.
Diese Ungenauigkeiten entstehen durch Fertigungstoleranzen, Montage und Ver-
formung verursacht und weitere Faktoren entstehen.
Diese Bachelorarbeit beschreibt die Modellierung und Kalibrierung der hu-
manoiden Roboterplattform Wolfgang.
F(cid:127)ur diese Kalibrierung werden drei
Messsysteme verglichen und ausgewertet. Eine signi(cid:12)kante Reduzierung des Re-
projektionsfehlers wird erreicht.

Contents

Abstract

List of Figures

1 Introduction

1.1 RoboCup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Thesis Goal

2 Related Work

2.1 Classical Industrial Approaches
. . . . . . . . . . . . . . . . . . . .
2.2 Humanoid Robot Calibration . . . . . . . . . . . . . . . . . . . . .
2.3 Approaches in the RoboCup . . . . . . . . . . . . . . . . . . . . . .

iii

viii

1
2
4
4

5
5
6
7

3 Basics

9
9
3.1 Joint Encoder Transfer Function . . . . . . . . . . . . . . . . . . . .
3.2 Kinematic Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 Camera Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4 Object Transformation in the RoboCup . . . . . . . . . . . . . . . . 19
3.5 AprilTag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.6 PhaseSpace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7 Non-Linear Least Squares Optimization . . . . . . . . . . . . . . . . 22

25
4 Robot Platform
4.1 Hardware
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

5 Calibration Approaches

37
5.1
Intrinsic Camera Calibration . . . . . . . . . . . . . . . . . . . . . . 37
5.2 Feature Positioning . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.3 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.4 Calibration using the PhaseSpace . . . . . . . . . . . . . . . . . . . 43
5.5 Calibration using AprilTags and the Head Camera . . . . . . . . . . 45
5.6 Calibration using AprilTags and an External Camera . . . . . . . . 45

v

Contents

6 Evaluation

49
6.1 Measurement Method . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6.2 Kinematic Model Veri(cid:12)cation . . . . . . . . . . . . . . . . . . . . . 49
6.3 Evaluation of the Calibration using the PhaseSpace . . . . . . . . . 51
6.4 Evaluation of the Calibration using AprilTags and the Head Camera 53
58
6.5 Evaluation of Calibration using AprilTags and an External Camera

7 Discussion

61
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
7.1 Kinematic Model
7.2 Comparison of Calibration Approaches . . . . . . . . . . . . . . . . 61
. . . . . . . . . . . . . . . . 62
7.3 Practicality of Calibration Approaches

8 Conclusion and Future Work

63
8.1 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
8.2 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

Abbreviations

Bibliography

Appendices

A Reprojection Error Before and After Calibration

65

67

73

75

vi

List of Figures

1.1 Picture of the Wolfgang robot platform . . . . . . . . . . . . . . . .

3

3.1 Transfer functions for joint encoder readings . . . . . . . . . . . . . 10
3.2 Diagram of a joint in a kinematic chain . . . . . . . . . . . . . . . . 12
3.3 Kinematic diagram of a 2D robot . . . . . . . . . . . . . . . . . . . 14
3.4 Ambiguity of inverse kinematics . . . . . . . . . . . . . . . . . . . . 15
. . . . . . . . . . . . . . . . . . . . . . . 16
3.5 The pinhole camera model
3.6 Relationship between a point on a distorted image and on the ideal

image

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3.7 Tranformation of image coordinates to Cartesian coordinates in the

RoboCup Humanoid League . . . . . . . . . . . . . . . . . . . . . . 20

3.8 Error introduced by angle o(cid:11)sets into transformation of image co-

ordinates to Cartesian coordinates . . . . . . . . . . . . . . . . . . . 21
3.9 Depiction of an AprilTag . . . . . . . . . . . . . . . . . . . . . . . . 21

4.1 Wolfgang robot platform with visualization, kinematic, and collision

model

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2 Overview of the electronics of the Wolfgang robot Platform . . . . . 28
4.3 Dynamixel MX Motors . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.4 Kinematic chains in the Wolfgang robot platform . . . . . . . . . . 34

5.1 Camera calibration procedure . . . . . . . . . . . . . . . . . . . . . 38
5.2 AprilTags and PhaseSpace LED positioning for calibration . . . . . 39
5.3 Measurement points for calibration using an AprilTag . . . . . . . . 43
5.4 Phasespace motion capture system . . . . . . . . . . . . . . . . . . 44
5.5 Kinematic chains and measurement devices for the three calibration

methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

6.1 Reprojection error with old and new URDF . . . . . . . . . . . . . 50
6.2 Calibration results of the PhaseSpace . . . . . . . . . . . . . . . . . 52
6.3 Calibration results for AprilTags with the internal camera for leg

calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

6.4 Calibration results for AprilTags with the internal camera for head

and camera coordinate system calibration . . . . . . . . . . . . . . 56
6.5 Reprojection error before and after calibration . . . . . . . . . . . . 57
6.6 Calibration results for AprilTags with the external camera . . . . . 59

vii

List of Figures

A.1 Reprojection error of old URDF, new URDF and after calibration . 75
A.2 Reprojection error of old URDF, new URDF and after calibration . 76
A.3 Reprojection error of old URDF, new URDF and after calibration . 77
A.4 Reprojection error of old URDF, new URDF and after calibration . 78
A.5 Reprojection error of old URDF, new URDF and after calibration . 79

viii

1 Introduction

Robots are widely used in many industrial applications ranging from manufactur-
ing to assembly. In the future, they might be able to assist humans in an even
larger variety of scenarios. A huge potential exists in the domestic context where
many tasks could be automated or eased through the use of robots. The domestic
context is much less structured than the industrial one where designated safety
zones for robots and precisely controlled processes exist. Many tasks in the domes-
tic context also require a combination of mobility and dexterity. Industrial robotic
arms do not have the mobility required for this context. Wheeled or humanoid
robots can potentially ful(cid:12)ll many tasks in the domestic context.
For robots to be able to complete motion tasks in both contexts, their internal
representation of their physical body needs to align with reality. If the model’s
deviations are too high from reality several problems arise: Firstly, collisions might
occur which can damage equipment or people. The kinematic model might predict
the robot to be close to a wall, but in reality, it already collides with this wall.
Secondly, robots with legs (i.e., humanoid or animal-like robots) might fall and get
damaged. Many walking algorithms rely on the correct positioning of the feet of
such robots. The foot position or the required joint angles for a given foot position
is calculated using the kinematic model of the robot and is inaccurate if the model
is inaccurate. Finally, a correct model of the pose of the internal sensor is required
to use the information they provide about the environment. When a robot detects
an object relative to its sensor, but this sensors position is incorrectly modeled,
the detected objects position relative the rest of the robot is also incorrect.
A good kinematic model of a robot whose parts are precision milled can be created
using the physical dimensions of these parts. A variety of factors can a(cid:11)ect the
accuracy of this model:

(cid:15) Manufacturing tolerances can cause the geometry of parts to be di(cid:11)erent

from the parts in computer aided design (CAD) software.

(cid:15) Deformation of the robot’s parts can be caused by wear or accident.

(cid:15) Encoders measuring the position of joints might not have the same zero
position as the kinematic model or feature a nonlinear transfer function of
sensor reading to joint position.

(cid:15) Errors or imprecision can occur during assembly of a robot.

1

1 Introduction

A solution to reducing the error in the kinematic model is robot calibration. In
robot calibration, the pose or partial pose of the robots end e(cid:11)ector is captured by
a measurement system. This procedure is repeated for multiple poses of the robot.
Changing the parameters of the kinematic model, so the pose of the end e(cid:11)ector
is more similar to the measured position is a solvable optimization problem.
This thesis only examines the geometrical model of the robot and therefore only
geometric calibration. Non-geometric calibration would include factors such as
modeling of deformations under load of the robots links and backlash of gearboxes.
In this thesis a calibration procedure to estimate geometric parameters is per-
formed on the Wolfgang humanoid robot platform pictured in (cid:12)gure 1.1. Multiple
measurement systems are used to perform this calibration and compared. These
measurements systems are the motion capture system PhaseSpace [1] and the vi-
sual marker system AprilTags [Ols11, WO16] with an external and the internal
camera of the robot platform.
Chapter 2 presents various related work in the (cid:12)eld of robot calibration from early
approaches on industrial robots to recent approaches on humanoids. In chapter 3
several essentials for robot calibration as well as principles and systems speci(cid:12)c to
the experiments done in this thesis are explained. The Wolfgang robot platform,
the humanoid robot on which the experiments were conducted, is described in
chapter 4. Chapter 5 describes the approaches used to calibrate the kinematics of
this robot. The results of these approaches are presented and discussed in chapter 6
and discussed in 7. Chapter 8 gives a conclusion of the results and evaluation of
this thesis and provides an outlook on possible enhancements to the presented
approach.
In this introduction a brief overview of the RoboCup is given in section 1.1, since
the Wolfgang robot platform is used in the RoboCup competition. This section
provides some insights into the following motivation given in section 1.2. The goal
of this thesis is described concisely in section 1.3.

1.1 RoboCup

The RoboCup [KANM98] [2] is a robot competition in a variety of leagues. The
main focus is on playing soccer with robots. Several leagues exist within the
RoboCup. This section will focus on the leagues which use humanoid robots,
namely the Standard Platform League (SPL) and the Humanoid League.
Soccer is chosen as a competition since it is appealing and understandable by the
general public and reasonably achievable by robots. The RoboCup aims to promote
science and research on robust robotic systems through competition and coopera-
tion. Comparability between di(cid:11)erent approaches to robotics is increased through
competition in a standardized context with annually updated rules. Furthermore,

2

1.1 RoboCup

Figure 1.1: Picture of the Wolfgang robot platform. The experiments described in

this thesis were conducted on this robot platform.

its purpose is to increase public involvement in and enthusiasm for robotics.

The international RoboCup competition is held annually. The event generally lasts
a week. Teams participating in the event usually have two setup days to prepare
the robots and adjust to the environment of the event venue. The competition
usually lasts for four days. During the competition days, the robots must play in
several games per day with little time between each game.

Opposed to demonstrations in the laboratories, the robots must be able to per-
form at the competition multiple times and in less controlled environments. This
requires more robust hard- and software.

In the SPL all participating robots are NAO robots from Soft Bank Robotics.
In the Humanoid League all robots which comply with a set of rules regarding
their physical dimensions may be used. The humanoid league is divided into
three size classes, KidSize, TeenSize, and AdultSize. The Wolfgang robot platform
complies with the KidSize and TeenSize of the Humanoid League and is used by
the RoboCup teams Hamburg Bit-Bots and WF Wolves. Figure 1.1 shows this
humanoid robot platform.

3

1 Introduction

1.2 Motivation

Calibration and accurate kinematic modeling are required for a multitude of ap-
plications on robots.
Well modeled legs of a humanoid robot are crucial for a stable walk. It is essential
that the robot kinematic model, which is used in many walking algorithms, is close
the kinematics of the physical robot because the calculations which are supposed
to guarantee the stability of the walk are only valid if the model is valid.
The exact kinematic model is also highly interesting for applications in simulation.
Simulation is relevant for robotics since it reduces the wear on the physical system.
Therefore it can be used for machine learning which might require long training
periods. Furthermore, the e(cid:11)ort of development, as opposed to a real robot, is
reduced in simulation. Not only the kinematic structure but also the mass distri-
bution of the robot is essential for accurate simulation. The work described in this
thesis does not aim to produce an accurate model of the dynamics of the system
but rather a geometrical model.
A well calibrated kinematic model is crucial for mapping the information of sensor
data to real-world coordinates. Small angular errors in the position of a sensor can
lead to signi(cid:12)cant errors in position detection in Cartesian space. Improving the
accuracy of the sensor position in the kinematic model improves the positioning
accuracy of the objects detected by the sensor. In the RoboCup, this is signi(cid:12)cant
to accurately detect the position of objects on the soccer playing (cid:12)eld to make
strategical decisions.

1.3 Thesis Goal

The work done in this thesis aims to create an accurate model of the Wolfgang
robot platform and develop a calibration procedure which can be reliably and
quickly performed for each robot.
The calibration procedure should reliably increase the performance robot in terms
of sensor data to real-world coordinates mapping. A quick calibration is required
since recalibration might be necessary between the RoboCup games because of the
frequent falls the robot has to endure.
A more elaborate calibration which accounts for inaccuracies in the robot’s legs
can be performed at the laboratory and may be more time-consuming.

4

2 Related Work

The topic of robot calibration has been widely researched for industrial robots.
Many approaches to calibrating robotic arms using multiple measurements tools
or mechanical constraints have been established. Mathematical models describing
the kinematics of a robotic system such as the Denavit-Hartenberg method [HD55]
are well-understood.
More recently, humanoid robots have been an important topic in robotics research.
Their kinematic chains also need to have proper absolute positioning. Firstly, this
ensures that the placement of the feet is accurate which is essential for maintaining
balance. Secondly, the accuracy of sensors such as cameras or range-(cid:12)nding devices
can be signi(cid:12)cantly improved since their pose in space is more accurately known
in a calibrated robot.
In the context of the RoboCup, calibration can signi(cid:12)cantly increase the perfor-
mance of the robot competitors by improving their vision and motion capabilities.
Since falls are frequent in the Humanoid and Standard Platform Leagues of the
RoboCup, frequent recalibration is required.
Section 2.1 describes approaches designed for calibrating industrial manipulators.
Section 2.2 presents recent approaches made to calibrate single or multiple kine-
matic chains of humanoid robots. Approaches made in the context of the RoboCup
are elaborated in section 2.3.

2.1 Classical Industrial Approaches

Mooring et al. [MRD91] elaborate the need for robot calibration in the preface to
Fundamentals of Robot Calibration. Classically, industrial robots were taught mo-
tions by a skilled operator. This process was usually very time-consuming. A high
repeatability of end e(cid:11)ector positioning is required for reliable task completion.
High absolute precision is not required for these motions.
When a robot needs to be replaced, the same set of joint goals, which make up the
taught motion, played on a di(cid:11)erent robot may not perform the task the original
robot could. The replacement robot would need to be retaught the motions.
Furthermore, the need for motions to be programmed o(cid:11)-line arose from the in-
crease in complexity of tasks a robot should perform. O(cid:11)-line programmed motions
are generated by algorithms. Long sequences of motions that would be tedious to
teach by hand and adaptive tasks can be performed using this method. It also
eliminates the necessity of a skilled operator.

5

2 Related Work

The drawback is that a high absolute positioning and not just high repeatability
of motions is required.
Mooring et al.
[MRD91] elaborate on the general problem of robot calibration.
Their book describes modeling techniques for robots suitable for robot calibration,
various measurement methods, and parameter identi(cid:12)cation algorithms. The im-
plementation of the parameters of the robot’s kinematics is discussed in terms of
forward and inverse kinematics.
In An Overview of Robot Calibration Roth et al. [RMR87] describe three levels of
robot calibration.
The (cid:12)rst level of robot calibration only includes (cid:12)nding the parameters of the
transfer function, which translates the readings of the joint encoder to the real
position of the joint. A suitable transfer function which models the mechanical
system must be chosen. Here the pose and dimensions of the links of the robotic
system is assumed to be modeled correctly.
The second level of robot calibration is the calibration of the kinematic parameters
of the robot description (e.g., the Denavit-Hartenberg [HD55] parameters).
Level 3 calibration is the incorporation of a dynamics model of the robot. While
the pose of the robot is assumed to be only dependent on the state of the joints and
the kinematic parameters in level one and two calibration, this type of calibration
includes velocity and torque measurements as well as a time component for model-
ing the previous states of the robot. This type of error is called non-geometric since
the model does not only include geometric parameters. A non-geometric model
can describe e(cid:11)ects such as (cid:13)exibility of robot links or backlash in gearboxes. Its
drawback is the hugely increased complexity as opposed to the previous levels of
robot calibration.
The robot operating system (ROS)[QCG+09] package robot calibration [3],
which is used for the experiments in this thesis, aims to be a universal solution for
calibrating a multitude of robots. The calibration process is described by a set of
kinematic chains to be calibrated, a set of feature finders that abstract from
the speci(cid:12)cs of the used measurement systems and process their measurement into
a list of observations, a de(cid:12)nition of the free parameters of the system and their
initial values, and a list of error blocks that de(cid:12)ne how the error between two ob-
servations is computed. A more elaborate description of this software is provided
in section 5.3.

2.2 Humanoid Robot Calibration

Two major di(cid:11)erences exist between calibrating a humanoid robot and standard
calibration in industrial contexts:
Firstly, the main sensor of the system, in humanoids often a (depth) camera, is not

6

2.3 Approaches in the RoboCup

static relative to the environment but attached to a moving joint. The modeling
of this calibration problem is described by Horaud et al. [HD95].
Secondly, multiple kinematic chains need to be calibrated, which can be bene(cid:12)cial
since multiple kinematic chains can be calibrated against each other.
Pradeep et al. [PKB14] present an approach to calibrate multiple sensors as well
as the kinematic chains to which they are attached. They validated their method
on a PR2 robot. A checkerboard pattern is attached to the robot’s gripper and
measured by multiple cameras and a tilting LiDAR.
Birbach et al. [BBF12] present an automatic calibration procedure for a humanoid
upper body. Instead of using a calibration pattern, they use a speci(cid:12)c feature on
the robot’s wrist. Furthermore, the elasticity of the joints transmissions is modeled
and compensated for.
A calibration of a complete humanoid robot is described by Maier et al. [MWB15].
Checkerboard markers were attached to a NAO’s wrists and feet. An algorithm
for the generation of con(cid:12)gurations valuable to calibration is also developed and
explained in the publication.

2.3 Approaches in the RoboCup

Kastner et al.
[KRL15] of team B-Human from the Standard Platform League
presented an approach to calibrate a NAO humanoid robot by attaching markers
to its feet. While calibration results were not always usable, it provided a good
guess for a manual calibration procedure.
[AFG+18] of team RHoban from the Humanoid KidSize League de-
Allali et al.
scribe the calibration of the external and internal parameters of their camera as
well as the orientation of the inertial measurement unit (IMU). A calibration setup
was designed, in which the robots feet position is (cid:12)xed. The robot observes markers
of the calibration setup while motions are performed.
[MFG+19] of the team
A similar calibration setup is used by Mahmoudi et al.
MRL HSL from the Humanoid KidSize League. In addition to the o(cid:11)set between
the projected and measured pose of the markers, they also minimize the variance
to reduce the e(cid:11)ect of outliers in the measurement set.
Fan et al.[FCJ+19] of the team ZJU Dancers which participate in the Humanoid
KidSize League have also implemented a calibration procedure for the extrinsic
parameters of the camera using visual markers.

7

2 Related Work

8

3 Basics

This chapter describes some of the mathematical and theoretical background re-
quired for robot calibration as well as some systems used in this thesis.
Section 3.1 describes the reasoning behind the chosen transfer function for the joint
encoder readings. The parameters of this model are part of the kinematic model
and are calibrated. Forward and inverse kinematics, as well as the underlying
kinematic modeling of the robot’s joints and links, are described in section 3.2.
Cameras are used for the observations in the robot calibration process. Their
modeling is discussed in section 3.3. The calculations required for transforming
image coordinate to Cartesian coordinates in the RoboCup domain are presented
in ??. The visual (cid:12)ducial system AprilTag is described in section 3.5. AprilTags
and the internal camera of the robot or an external camera make up one of the
measurement systems evaluated in this thesis. The other employed technology, the
commercial motion capture system PhaseSpace, is explained in section 3.6. The
procedure required for optimizing the parameters of the kinematic model in regard
to the observations made is described in section 3.7.

3.1 Joint Encoder Transfer Function

An error model of the joint encoder is required for calibration. This model describes
how the output of the rotary encoder in the motor can be translated to the real
position of the joint. This transfer function depends on the sensor and the gearbox.
Multiple kinds of transfer functions are displayed in (cid:12)gure 3.1.
The motors used in the Wolfgang humanoid platform are described in 4.1.3. A
Hall e(cid:11)ect sensor in the servo motor measures the angle of a magnet (cid:12)xed to the
rotor with a magnetic (cid:12)eld orthogonal to the rotation axis. The data sheet of the
Hall e(cid:11)ect sensor used in the Motors (AS5045) [4] speci(cid:12)es its accuracy with a
centered magnet to be within (cid:6)0:5(cid:14).
While the sensor features some nonlinearity in the measurement of the angle, it
is minimal due to the spinning current Hall e(cid:11)ect sensor in the IC. Instead of
measuring the displacement of electrons in a single direction, the current and
sensing direction is changed in a circular pattern. Its advantages are described by
Munter [Mun90].
Hall e(cid:11)ect sensors measure the absolute angle of the rotor. A procedure from the
manufacturer of the motors to calibrate this zero position on a partially disassem-
bled motor is described in section 4.1.3.

9

3 Basics

Figure 3.1: Transfer functions for joint encoder readings. The ideal transfer func-
tion is linear and has no o(cid:11)set to the zero position. The o(cid:11)set transfer
function has an o(cid:11)set which is the same across the function. An ab-
solute rotary position sensor often has such a function since the zero
position of the encoder does not match the zero position of the kine-
matic model. The transfer function labeled linear is caused by an
encoder where the full scale input does not match a full rotation. The
non-linear transfer function has a sinusoidal component. This graph
does not cover all possible kinds of transfer function for joint encoders.
Combinations of these functions are possibly more valid than a single
function.

The kinematic model used in the robot calibration in this thesis assumes the
transfer function to be linear. The real position of the motor q is assumed to be
the measured value ^q o(cid:11)set by a parameter qof f set which will be calibrated.

q = ^q + qof f set

(3.1)

3.2 Kinematic Modeling

In robotics, kinematics describes the motion of the physical robot system. The
model allows to make predictions about the state of the system such as its pose or
velocity in space. Firstly, the modeling of kinematic chains is explained in section
3.2.1. The calculations required for calculating the pose of the robot from a given
kinematic structure and robot state are described in section 3.2.2. Methods to
determine the robot state given a pose are explained in section 3.2.3.

10

01024204830724096encoder reading in bit0/23/22joint angle in radiansidealoffsetlinearnon-linear3.2 Kinematic Modeling

3.2.1 Kinematic Chains

This section is based on chapter 2 of the Springer Handbook of Robotics [SK16].
Kinematic chains model the geometry of robotic manipulators. A kinematic chain
is de(cid:12)ned as a set of links and a set of joints. Each joint is de(cid:12)ned at a pose
relative to its parent link and connects the parent link to a child link. Links are
assumed to be rigid for this thesis.
The kinematic chains discussed in this thesis are tree-like. There exists one
base link at the root of the tree. Each node of the tree is a link and each directed
edge is a joint. Each leaf of the tree is an end e(cid:11)ector of the robot. Therefore a
description of the kinematic chains of the robot consists of a set of n links and a
set of n (cid:0) 1 joints.
It is useful to attach a coordinate system (also called frame) to each link of the
robot to be able to calculate the transformations between the links and positions
relative to the links. An exemplary use for these transformation is calculating
the relative position of an object to the hand of the robot, when the position
measurement comes from the camera sensor. The transformation between the
camera frame and the hand frame at the time of object detection must be available
to solve this example.
A transformation between coordinate systems is de(cid:12)ned as a translation and a
rotation. The translation is a three-dimensional vector for the three spatial di-
mensions. It de(cid:12)nes the position of the child frame relative to the parent frame.
Several possibilities exist to describe the rotation between two frames. Firstly
it can be described as a three-dimensional vector for the rotations around each
axis of the coordinate system. This representation is called Euler angles. These
rotations are called roll around the x-axis, pitch around the y-axis and yaw around
the z-axis of the coordinate system. One problem of this representation is called
Gimbal Lock which can cause problems in mechanical systems [Klu74]. It occurs
when two axes of rotation are parallel to each other because of a previous rotation.
Gimbal Lock reduces the degrees of freedom (DoF) of the system to two instead
of three. Another disadvantage is the ambiguity in the interpretation of the three-
dimensional vector. The advantage of the Euler angle representation is that they
are intuitive to understand.
A di(cid:11)erent representation of rotation is quaternions [Sho85]. These are four-
dimensional vectors which can be normalized for comparison. While they are
less intuitive to understand, they avoid the problem of Gimbal Lock and are an
unambiguous representation. Rotation matrices may also be used to describe these
rotations but they are also not intuitive and require nine parameter instead of the
four parameters required for quaternions.
Multiple methods exist for attaching coordinate systems to links. The De-
navit{Hartenberg method [HD55] can be used. Here, each link is assigned a frame

11

3 Basics

Figure 3.2: Diagram of a joint connecting a child link to its parent link. The pose
of the joint is de(cid:12)ned relative to the parent link’s coordinate frame.
For a revolute joint, the axis of revolution is also de(cid:12)ned. The child
coordinate frame is equivalent to the joint coordinate frame. When the
joint rotates, the child frame rotates with it. [5]

with a given set of rules. The advantage of this method is the need for only four
parameters per joint. These parameters can be converted to transformation ma-
trices. The disadvantage is the sometimes non-intuitive placement of coordinate
frames.
Another method is to directly specify the pose of the joint in relation to the pre-
vious link. While six parameters (three for translation and three for rotation with
Euler angles) are required, it produces more intuitive placement of the coordinate
frames. Furthermore, it is easier to understand since the Denavit{Hartenberg
rules [HD55] do not have to followed. This method is used for the modeling of the
Wolfgang robot platform (see chapter 4).
The pose of each link’s frame is de(cid:12)ned either as the base link or the pose of the
joint connecting the link to its parent link . Figure 3.2 shows how a joint connects
two links and how the coordinate frames are positioned.
Joints can have one or multiple DoF. DoF are the number of independent parame-
ters required to describe the state of a system. A typical motor has one DoF since
its state can be described by a single variable, the angle around the motor’s axis.
In this thesis, two types of joints are considered since these are the joints used
in the Wolfgang robot platform. Firstly, rotary joints, which rotate around a

12

3.2 Kinematic Modeling

speci(cid:12)ed axis and secondly static joints with no DoF. The other class of common
joints is prismatic joints which can extend in a given axis. Joints with multiple
DoF are modeled as a set of 1 DoF joints connected by links with length 0.
The state of a robot can be described in two spaces. The joint space is an n
dimensional space, where n equals the number of joints of a robot. The second
space is the Cartesian space with dimensions (x; y; (cid:18)) for 2D and (x; y; z; (cid:11); (cid:12); (cid:13))
for 3D. The calculations required for translating between these spaces are called
forward kinematics for a joint space to Cartesian space transition, and inverse
kinematics for a transition from Cartesian to joint space.

3.2.2 Forward Kinematics

Forward kinematics solves the problem of calculating the pose of a link (e.g., the
end e(cid:11)ector of a robot) given the joint states and the robot’s kinematic model.
Figure 3.3 shows an example of a 2D kinematic structure. Its state is de(cid:12)ned by
joint angles (cid:18)0::(cid:18)n. The pose of the end e(cid:11)ector or any frame of the system may
be calculated using trigonometric functions. Forward kinematics always yields a
single solution since these trigonometric functions also only have a single solution.

3.2.3 Inverse Kinematics

The goal of inverse kinematics is to calculate a set of joint angles which cause a
link of the robot to reach a given pose.
The optimal solving technique highly depends on the robot’s kinematic structure,
its joint constraints, and workspace. Some kinematic chains have a closed form
solution for each pose in the workspace given the joint constraints.
A su(cid:14)cient requirement for 6-DoF manipulators to have a closed form solution is
three axis of rotation intersecting in a single point and three consecutive parallel
joints [SK16]. Often robotic manipulators are designed to comply with these re-
quirements to simplify inverse kinematic equations. The Wolfgang robot platform
does not ful(cid:12)ll these requirements since not all three axes of the hip intersect.
Depending on the kinematic structure, some poses might not be reachable by the
end e(cid:11)ector. Reachability depends on the robot’s DoF. A robot with less than
six DoF cannot reach an arbitrary pose in its workspace since six independent
parameters specify a pose in 3D space.
Opposed to forward kinematics, not only a single solution must exist for a given
goal pose. Figure 3.4 shows this ambiguity where two sets of joint states equate
the same end e(cid:11)ector pose.
Multiple techniques exist for solving inverse kinematics for arbitrary kinematic
chains. Iterative algorithms to solve this problem such as TRAC-IK [BA15] exist

13

3 Basics

Figure 3.3: Kinematic diagram of a 2D robot with four links and three joints.
The base link is located at the origin of the coordinate system. Joints
j0::j2 are displayed as circles with an angle (cid:18)n from their zero position
indicated by a dashed line. Links l0::l3 are displayed as lines. The end
of the last link in the kinematic chain (l3 here) is called the end e(cid:11)ector.
The pose of the end e(cid:11)ector is speci(cid:12)ed by an x and y coordinate and
an angle (cid:18).

but are not guaranteed to converge and have a much longer runtime than closed
form solutions. Another approach is an evolutionary inverse kinematics solver.
It allows for specifying secondary goals (e.g., the position of the center of mass
of the robot). Such an algorithm (BIO IK 2 [RHSZ18]) is currently used for the
Wolfgang robot platform. Neural networks have also been used for solving inverse
kinematics but have not yet reached the level of accuracy as iterative approaches
[ADK16].

3.3 Camera Model

A camera in combination with the AprilTags described in section 3.5 or other
visual features can be used as a measurement system for robot calibration. The
standard model of how the output of the camera sensor, the image, can be re-
lated to coordinates is the pinhole camera model. It describes how a 3D scene is
projected to a 2D image. The model is described in section 3.3.1.

14

j1j2l1l2l3end effector pose(x,y,θ)j0θ1θ0θ2xyl03.3 Camera Model

Figure 3.4: Multiple joint angles of the same kinematic structure leading to the
same end e(cid:11)ector pose. See (cid:12)gure 3.3 for an explanation of symbols.
While the joint angles (cid:18)0,(cid:18)1 and (cid:18)2 are di(cid:11)erent between the chains
colored black and red respectively, the end e(cid:11)ector pose de(cid:12)ned by x,y
and (cid:18) is equal for both chains.

Since the pinhole camera model does not account for any distortion in the image
introduced by the lenses used in a camera objective, a second method to rectify
distorted images is presented in section 3.3.2.

3.3.1 Pinhole Camera Model

section is based on the camera calibration method presented by

This
Zhang [Zha00].
Figure 3.5 shows how an object is projected trough a point onto an image plane.
Equation 3.2 describes the relationship between the object height and distance to
the focal length and height of projected object in the image.

H
d

=

h
f

(3.2)

Here, H is the object height, d the distance from the pinhole to the object, f the
focal length, and h the height of the object in the image.
It is often useful to
specify the focal length f in pixels since the height of an object in the image d is
usually measured in pixels.

15

j1j2l1l2l3end effector pose(x,y,θ)j0θ1θ0θ2xyl0j1θ1l2l1θ2θ03 Basics

Figure 3.5: The pinhole camera model. An Object is projected through a pinhole
onto an image plane. Equation 3.2 describes the relationship between
focal length, height in the image, distance to object and object height.
Objects on the projection plane are the same height as objects on the
image plane since it has the same distance to the pinhole. Unlike
objects on the image plane, objects on the projection plane are not
(cid:13)ipped.

16

Focal Length (f) Distance to Object (d)ObjectHeight (H) Height inImage (h) PinholeProjectionPlaneObjectImagePlaneFocal Length (f) 3.3 Camera Model

For a 3D to 2D projection as opposed to a 2D to 1D projection, two focal lengths
fx and fy are required. Furthermore it is assumed that the image plane is not
perfectly centered behind the pinhole but speci(cid:12)ed by the image center coordinates
cx and cy. Equation 3.3 shows how these parameters make up the intrinsic camera
matrix K.

0

K =

@

1

fx
0
0

0
fy
0

cx
cy
1

A

(3.3)

To calculate the image coordinates pimg of a 3D point p, the point p multiplied
with the intrinsic camera matrix K to calculate the intermediates u, v and w as
seen in equations 3.4. p needs to be in the camera coordinate system.

pimg = K (cid:1) p

1

0

A =

@

0

@

u
v
w

fx
0
0

0
fy
0

1

0

A (cid:1)

@

x
y
z

cx
cy
1

1

0

A =

@

x (cid:1) fx + z (cid:1) cx
y (cid:1) fy + z (cid:1) cy
z

1

A

(3.4)

(3.5)

To calculate the image coordinates ximg and yimg, u and v are scaled by 1
in 3.6 and 3.7.

w as seen

ximg =

yimg =

u
w

v
w

(3.6)

(3.7)

If image coordinates of certain features are known (e.g., sections 3.4, 3.5, or 3.6),
backprojection can be used to gain information about the feature’s 3D coordinates.
Backprojection is the inverse operation to projection. The 3D coordinate cannot
be restored from a 2D image since depth information is not available in a typical
camera, but a ray on which the feature lies can be calculated.
This ray passes through the center of the camera and through a point on arbi-
trarily chosen projection plane with distance z to the camera. A z-distance of 1 is
chosen for simplicity. Equations 3.8 and 3.9 show the calculations for this point’s
coordinates. The equation for the ray is given in 3.10 where s 2 IR+.

xray =

yray =

ximg (cid:0) cx
fx

ximg (cid:0) cy
fy

(3.8)

(3.9)

17

3 Basics

1

0

A = s (cid:1)

@

0

@

x
y
z

1

A

xray
yray
1

(3.10)

To calculate the 3D coordinates of a point in an image three possibilities are
discussed. Firstly, the calculation for objects with known properties such as in the
RoboCup in 3.4, secondly, application of information about features in an image
in 3.5, and, (cid:12)nally, triangulation using multiple cameras in 3.6.

3.3.2 Camera Distortion Model

This section is based on the OpenCV library [Bra00].
Some lenses signi(cid:12)cantly distort the image captured by the cameras sensor. This
invalidates the pinhole camera model. This distortion can be modeled, and dis-
torted images can be recti(cid:12)ed. Recti(cid:12)ed images may be used with the pinhole
camera model.
Distortion is generally modeled in two components. Radial distortion is the dis-
placement of pixels away from or towards the image center based on their coordi-
nate. Tangential distortion is the displacement of pixels along a circle around the
image center. This is illustrated by (cid:12)gure 3.6.
The parameters for radial and tangential distortion of a given camera can be
calibrated as described in section 5.1.

Figure 3.6: Relationship between a point on a distorted image and on the ideal
image. p0 is the point on the captured image. To use the pinhole
camera model, the point needs to be translated in tangential and radial
direction. dt and dr are a function of the image coordinate. [LZHT14]

18

drdtPosition withdistortionIdeal positiondr Radial distortiondt Tangential distortionOp'p3.4 Object Transformation in the RoboCup

Rectifying a distorted image is essential for robot calibration. The calculations
regarding the positions at which markers (e.g., AprilTag or LEDs) are detected,
are only valid for an undistorted image.

3.4 Object Transformation in the RoboCup

If some information about the position of an object is known from the context,
this information can be combined with the backprojection. This may yield the
entire 3D position in Cartesian space.
In the context of the RoboCup (see section 1.1) the detected objects such as the
soccer ball, (cid:12)eld lines, goalposts, and other robots are on the playing (cid:12)eld. This
playing (cid:12)eld is plane and ideally parallel to the pose of the robot’s supporting foot
since this foot lies mostly (cid:13)at on the ground.
The position of an object is the intersection of the ray cast by the backprojec-
tion and the ground plane. This is illustrated in (cid:12)gure 3.7 for a 2D example for
transformation for planar and non-planar objects.
These calculation highly depend on the accuracy of the angle of the robots camera
to the ground. Figure 3.8 shows that an o(cid:11)set in this angle can invalidate these
calculations signi(cid:12)cantly.
Other methods of calculating the position of a detected object exist such as the
known size of the ball or goalposts.

3.5 AprilTag

AprilTag [Ols11, WO16] is a visual (cid:12)ducial system. They are square markers whose
pose can be calculated when their size is known. AprilTags can also be uniquely
identi(cid:12)ed. Figure 3.9 shows an example from the most commonly used family.
Multiple families of tags with di(cid:11)erent resolutions and minimum hamming dis-
tances between each tag exist. The tag family used in the experiments in this
thesis is Tag36h11 since there are no special requirements regarding the number
of di(cid:11)erent tags or the false positive rate of detection. 587 tags exist in this family
with a minimum Hamming distance of 11 bit.
AprilTags can be printed using ordinary inkjet or laser printers on standard white
paper. They are therefore a cheap and easy to produce visual marker.
In the
experiments conducted for this thesis, the mounting plates for the AprilTags were
3D printed, but the tags can be attached to any (cid:13)at surface.
A fast and robust detection algorithm is proposed by Wang and Olson [WO16].
Its integration into robot operating system (ROS) which is used in this thesis is
described by Malyuta [Mal17].

19

3 Basics

Figure 3.7: Tranformation of image coordinates to Cartesian coordinates in the
RoboCup Humanoid League. Most objects detected in the image in
the context of the RoboCup are on the ground plane. The orientation
of the plane and distance to the camera is calculated from the position
of the support foot (or feet if both feet are on the ground). A ray is
cast from the origin of the camera coordinate system through the point
on the projection plane which corresponds to the position of an object
in the image. In the top image, the intersection with the ground plane
is the position of the object. In the bottom image, a ball’s position is
calculated by raising the intersection plane by the radius of the ball.

20

Ground PlaneBackprojectionRay ProjectionPlaneIntersectionGround PlaneBackprojectionRay ProjectionPlaneIntersectionBall Center Plane3.5 AprilTag

Figure 3.8: Error introduced by angle o(cid:11)sets into transformation of image coor-
dinates to Cartesian coordinates. The blue line is the transformation
without any joint error. The dashed green lines show the transforma-
tion with an error of 0:025 radians (1:43(cid:14)) in the camera coordinate
system, the red lines with an error of 0:05 radians (2:86(cid:14)), and the
magenta line with an error of 0:075 radians (4:30(cid:14)).

Figure 3.9: AprilTag [Ols11, WO16] 42 from the Tag36h11 tag family. The outline
around the image is used to di(cid:11)erentiate the white border of the tag
from the background. The outline does not belong to the tag while the
border does.

21

0.0/8/43/8angle of reprojection ray to ground in radian0123456distance to object in meters3 Basics

The position of a tag relative to the camera can be calculated when the camera
intrinsics and the tags size are known. Its orientation can be calculated from the
di(cid:11)erences in side lengths of the AprilTag in the image.
The accuracy of the detected pose depends on a multitude of factors. Most sig-
ni(cid:12)cant is the image resolution and accuracy of the camera intrinsic parameters.
A noisy image or poor lighting conditions can also deteriorate the accuracy of the
algorithm.

3.6 PhaseSpace

The PhaseSpace is a high-speed tracking system by PhaseSpace Inc.
[1]. It uses
multiple cameras to detect LEDs which are uniquely identi(cid:12)able by their blinking
frequency.
The cameras used in the tracking system are dual line scan cameras with 3600
pixels each. The cameras are each equipped with a cylinder lens oriented orthogo-
nally to each other. Cylinder lenses focus the light into a line. The light detected
by the line sensors is the sum of all horizontal or vertical pixels in a full image.
The two-dimensional position of the LEDs projection on the image plane are the
combined coordinates from the orthogonal sensors.
This technique is only possible since LEDs are uniquely identi(cid:12)able by their blink-
ing frequency.
Due to the reduced processing required for line scan cameras as opposed to a full
image, high update rates with high precision can be achieved.
Through a calibration procedure using an object with known LED locations, the
cameras’ positions relative to each other are calibrated.
Using the cameras’ intrinsic parameters, a ray for each camera detecting a given
LED is calculated. It starts at the optical center of the camera and passes through
the point where an LED was detected on the image plane. The 3D position can be
triangulated using the two or more rays. Since each ray is in its respective camera
coordinate system, they need to be transformed into a world coordinate system.
The poses of the cameras relative to each other is known from the calibration
procedure. Due to measurement noise and imperfect camera calibration caused
by measurement noise, these rays generally do not intersect. Therefore the point
closest to all rays is calculated.

3.7 Non-Linear Least Squares Optimization

Non-linear least squares optimization [Mar63] describes a class of problems (cid:12)tting
a set of observations m to a parametrized model to minimize the error between
the model’s predictions and the observations.

22

3.7 Non-Linear Least Squares Optimization

For robot calibration, the model is the kinematic equations described in 3.2.1.
While all parameters of this model can be optimized, usually only a subset is
used. Only a subset is used when one is con(cid:12)dent about certain parameters such
as the length certain links of to reduce dimensionality.
The observations are the measurements made during the calibration process.
The error function is de(cid:12)ned as the following equation:

e((cid:18); mi; ^qi) = mi (cid:0) predict((cid:18); ^qi)

(3.11)

Where mi is the measured position of an observation point, predict((cid:18); ^qi) calculates
the predicted position of the observation point given the joint angles ^qi at the time
of observation and the parameters of the kinematic model (cid:18).
E(cid:14)cient algorithms for minimizing non-linear error functions exist. They generally
do not guarantee to reach a global minimum.
High-performance implementations such as the Ceres Solver [6], which is used in
this thesis, allow for computing a viable robot calibration in a reasonable time.

23

3 Basics

24

4 Robot Platform

This chapter describes the Wolfgang robot platform pictured in (cid:12)gure 4.1. It is a
humanoid robot based on the NimbRo-OP [SPA+14] robot platform.
The Wolfgang robot platform is currently used by the RoboCup teams WF Wolves
and Hamburg Bit-Bots [BBE+19]. The WF Wolves from the Ostfalia University of
Applied Sciences made multiple changes to the mechanical structure of the NimbRo
robot. These hardware modi(cid:12)cations were made to comply with the rules [7] for
both the KidSize and the TeenSize of the RoboCup opposed to the Nimbro-OP
which is only allowed in the TeenSize.
In 2018 the Hamburg Bit-Bots started using this robot platform and competed
in the RoboCup 2018 competition with it. We have made several changes to the
robot’s hardware such as the addition of another computation unit (Odroid XU4),
a 3D printed camera mount, and improved power electronics.
This chapter is divided in two parts. Firstly, an overview of the robot’s hardware
in section 4.1, and secondly, in section 4.2 the components of the software stack
used by the Hamburg Bit-Bots which are relevant to robot calibration is explained.

4.1 Hardware

The Wolfgang robot platform is a 20 degree of freedom (DoF) humanoid robot.
It has six DoF per leg, three in each arm and two in the head. This equates to
(cid:12)ve kinematic chains when viewed from the base link which is positioned at the
bottom of the torso. Figure 4.4 shows the kinematic chains of the robot platform.
A Dynamixel servo motor by Robotis [8] actuates each joint.
The robot’s arms and head are actuated by MX64 servos [9]. Due to the higher
torques required for walking, MX106 servos [10] are used the legs. A more detailed
description of the actuators is provided in section 4.1.3.
The mechanical structure is described in detail in section 4.1.1. The controlling
electronics and the servo motors are explained in 4.1.2. Section 4.1.3 provides an
overview of the servo motors used in the robot platform.

4.1.1 Mechanical Structure

The mechanical parts of the robot are made from thee di(cid:11)erent materials:

(cid:15) Aluminum is used for parts with medium complexity geometry and high
strength requirements. The torso is milled from two square tubes, which sig-

25

4 Robot Platform

Figure 4.1: The Wolfgang robot platform. Top left: Picture of physical robot.
Top right: Robot model used for visualization. Bottom left: Coor-
dinate systems of the robot with. Bottom right: Collision model of
the Robot. Polygon count is greatly reduced in contrast to the visual
model.

26

4.1 Hardware

ni(cid:12)cantly reduces the amount of material required while being much stronger
than bent sheet metal. The connectors from the torso to the hip are milled
from u-pro(cid:12)les for the same reason.

(cid:15) Carbon (cid:12)ber reinforced polymer (CFRP) is used for parts with low
complexity geometry and high strength requirements. It is a very light ma-
terial but due to our manufacturing constraints only usable in sheet form.
Therefore it is only utilized in the arms and legs of the robot. In some cases,
aluminum parts are required as a connection between motors and CFRP
parts.

(cid:15) 3D-printed polylactic acid (PLA) is used in parts with intricate geom-
etry and medium strength requirements. It is the material for the head, the
mounting plates for the electronics, and some stability increasing parts be-
tween the leg and arm parts. Since 3D printing allows for rapid prototyping
through its ease of manufacturing, upgrades to the electronics or camera are
more easily integrated into the robot.

4.1.2 Electronics

The electronics of the Wolfgang robot platform are vastly improved over its pre-
decessor. The main processing unit (i. e. ZBOX nano XS) of the Nimbro-OP has
been replaced by a more powerful Intel NUC. Two more computation units have
been added: Firstly, the Nvidia Jetson TX2 with its powerful computer vision
processing capability and secondly, the Odroid XU4.
The communication between these systems is realized through a Gigabit Ethernet
connection and a network switch. The system can be interfaced through this
network switch as well for visualization or debugging.
The camera sensor is connected to the Nvidia Jetson TX2, which is responsible
for image processing, via USB2. This reduces the amount of data that is commu-
nicated through the network since the image does not have to be transmitted over
the Ethernet connection.
Other sensor readings and motor communication are handled by the Intel NUC
to minimize latency since motor commands are generated on this computer. A
RHoban DXL Board [11] connected via USB is used for this purpose. It interfaces
with the Dynamixel servo motors and feet pressure sensor via RS-485 (also known
as EIA-485 or TIA-485). The servo motors are explained in section 4.1.3. Fur-
thermore, it provides sensor readings from the onboard inertial measurement unit
(IMU).

27

4 Robot Platform

Figure 4.2: Overview of the electronics of the Wolfgang robot Platform. The main
computing units (i. e. the Intel NUC, the Nvidia Jetson TX2 and the
Odroid XU4) communicate via Ethernet through a network switch.
The camera sensor is connected to the Nvidia Jetson TX2, where vi-
sion processing is done. The communication to the motors and feet
pressure sensors as well as the reading of the inertial measurement
unit is handled by a RHoban DXL Board which has an STM32F103 as
a processor.

28

Intel NucRhoban DXL BoardNvidia Jetson TX2Odroid XU4IMULogitech C920Feet PressureSensorsDynamixel MotorsEthernetUSBUSBI2CRS485 Bus4.1 Hardware

4.1.2.1 RHoban DXL Board

The RHoban DXL Board [11] is an open-source hardware project by the RoboCup
team RHoban FC [12]. It consists of a Maple Mini from LeafLabs, three RS-485
transceivers and an IMU. The Maple Mini is an Arduino-like prototyping board
with an STM32F103 as a microprocessor. It is connected to the Intel NUC via
USB. Three RS-485 transceivers allow the board to communicate to the motors.
The transceivers allow the RHoban DXL Board to communicate to the motors and
other peripheral devices such as the foot pressure sensors. The IMU is connected to
the STM32F103 via I2C and provides data about linear accelerations and angular
velocities.
Since the (cid:12)rmware developed by team RHoban is not able to perform certain
instructions speci(cid:12)ed by the protocol and does not support the current version
of the communication protocol, the Hamburg Bit-Bots implemented an improved
version [13]. Performance tests showed that that the overhead of processing on
the microprocessor required for using multiple transceivers (and therefore multiple
communication buses to servo motors) outweighed possible bene(cid:12)ts. Therefor all
motors are connected on a single bus.

4.1.3 Dynamixel MX Servos

Dynamixel MX64 and MX106 motors [9, 10] from Robotis [8] are used as actuators
in the Wolfgang robot platform. They consist of a brushed DC motor, a gearbox,
and several electrical components for controlling and measuring the motor and
communication over RS-485. An MX106 motor is pictured in (cid:12)gure 4.3.
MX64 and MX106 are electrically and mechanically almost identical. The MX106
features a larger and more powerful brushed DC motor and is therefore slightly
physically larger in one dimension.
The sensor for detecting the rotation of the (cid:12)nal gear of the gearbox (i. e. the
position of the motor) is the AS5045. It is a 12-bit absolute rotary position encoder.
It uses the Hall e(cid:11)ect to measure the magnetic (cid:12)eld of a magnet attached to last
gear, perpendicular to the rotation axis. More speci(cid:12)cally, it uses a spinning
current Hall e(cid:11)ect sensor, in which the displacement of electrons caused by the
(cid:12)eld of the magnet is measured in multiple directions in a circular pattern. This
con(cid:12)guration, as opposed to a sensor with a single current direction, reduces o(cid:11)set
voltage induced through misalignment of the magnet [Mun90].
Since the placement of the magnet in zero position depends on the assembly of the
gearbox, a calibration is required. The sensor itself features functionality to set
the zero position, but it is not known if it is utilized by the closed-source (cid:12)rmware
of the servo, or a custom solution is used.
The manufacturer provides a calibration procedure to set the zero position. A

29

4 Robot Platform

(a)

(b)

(c)

(d)

Figure 4.3: Dynamixel MX motors. (a) Disassembled motor with printed circuit
board lifted to show the hall e(cid:11)ect sensor. This sensor lies right below
the magnet. The magnet is attached to the rotor and its magnetic
(cid:12)eld is orthogonal to the rotation axis. (b) Assembled motor with its
rotor visible. An indentation in the rotor indicates the zero position.
(c) Motor with attached calibration tool from Robotis. The plastic
part is form (cid:12)tted to the geometry of the motor and does not allow
the rotor to move. (d) Motor with attached motor horn. Its threaded
holes allow for attaching the motor to other mechanical parts.

plastic attachment to (cid:12)x the position of the rotor in the zero position is placed
on the motor as displayed in (cid:12)gure 4.3.c. Then the rotor is turned by 90(cid:14) and
measured again. This procedure is repeated for 180(cid:14) and 270(cid:14).
Due to the closed-source (cid:12)rmware, it is not known how these calibration results
are processed.
In the assembled robot a horn is mounted on the rotor (pictured in (cid:12)gure 4.3.d).
Errors in assembly can occur during this process since the zero marking is covered
when attaching the horn.
The main disadvantage of this calibration process is the need for disassembling
the robot and the motor. Furthermore, the calibration procedure can fail due to
a power disconnection or other unknown factors, and no feedback about this is
given to the user by the manufacturer’s software.

30

4.2 Software

4.2 Software

While a large software stack exists for this robot platform to be able to participate
in the RoboCup, this section will focus on the software required for controlling the
motors, software components regarding the robot model, and the driver for the
camera sensor.
Section 4.2.1 describes the robot operating system (ROS) framework used on the
robot platform and the advantages gained in contrast to a custom framework.
In section 4.2.2 the format of the robot description and the creation of such a
description for the Wolfgang robot platform is described.
In section 4.2.3 the
utilized forward kinematic engine is presented. Section 4.2.4 describes the inverse
kinematic software BioIK 2 [RHSZ18]. Software related to sending commands to
the motors is described in section 4.2.5. A brief introduction of the camera driver
is given in section 4.2.6.

4.2.1 ROS

The software used by the Hamburg Bit-Bots uses ROS [QCG+09] as a middleware.
Before 2017 a custom framework was developed and used. The transition to ROS
was realized and is described in [Bes17]. Mainly it was undertaken to be able
to interchange software components with other teams competing in the RoboCup,
ease the use of existing software from other robotics research groups, and for better
visualization and debug possibilities.
ROS is a middleware between the operating system (Ubuntu Linux) and the ap-
plication. In contrast to a monolithic approach, the software can be divided into
several components. These components are called nodes. They can run on mul-
tiple cores of a CPU or even in a distributed system such as the Wolfgang robot
platform. ROS manages the communication between these nodes.
Each node can publish information in a de(cid:12)ned format to an information channel.
The information packages are called messages. The information channels are called
topics. Each node can receive messages by subscribing to a topic.
ROS is not responsible for the transfer of messages between the nodes. It only
manages connecting publishing nodes to subscribing nodes. This architecture elim-
inates the problem of a communication bottleneck cause by a central communica-
tion node.
Through standardization of message types and interpretation as well as the en-
capsulation of functionality into multiple nodes, reuse of software components is
possible.

31

4 Robot Platform

4.2.2 URDF

1
2
3
4
5
6
7
8
9
10
11
12

13
14
15
16
17
18

19
20
21

The Uni(cid:12)ed Robot Description Format (URDF) [14] is an XML format for spec-
ifying joints and links of a robot. Each link is a part of the robot that does not
move relative to itself (e.g., torso, upper leg). Listing 4.1 shows an example of
a link speci(cid:12)cation. Lines 2-8 specify the inertial model of the robot which can
be used for calculating the dynamics of the system. Lines 9-15 specify the visual
model of the robot. An STL (cid:12)le de(cid:12)nes the geometry of this model. A collision
model de(cid:12)ned in lines 16-21 can be used to calculate whether the robot collides
with itself or other objects. It is made from signi(cid:12)cantly fewer polygons than the
visual model to speed up calculations regarding collisions.
< link name = " r_foot " >

< inertial >

< origin xyz = " 0.003669 -0.0081165 -0.030903 " rpy = " 0 0 0 " / >

< mass value = " 0.1488 " / >
< inertia ixx = " 0.00018527 " ixy = " -1.1504 E -05 "
ixz = " -7.2667 E -06 " iyy = " 0.00060485 "
iyz = " 5.8883 E -06 " izz = " 0.00075217 " / >

</ inertial >
< visual >

< origin xyz = " 0 0 0 " rpy = " 0 0 0 " / >
< geometry >

< mesh filename = " package :// wolfgang_description / mesh /

right_foot . stl " / >

</ geometry >

</ visual >
< collision >

< origin xyz = " 0 0 0 " rpy = " 0 0 0 " / >
< geometry >

< mesh filename = " package :// wolfgang_description / mesh /

right_foot_collision . stl " / >

</ geometry >

</ collision >

</ link >

Listing 4.1: Description in the URDF format of the Wolfgang robot platform’s
right foot. An inertia matrix describes the inertial model. A visual
and collision model of the link are each speci(cid:12)ed by a triangle mesh.

A joint speci(cid:12)es the relationship between a parent and a child link. The type of
the joint is most commonly either a revolute joint, which rotates around a given
axis, or (cid:12)xed joint which is (cid:12)xed and has no DoF. Other types of joints exist but
are not relevant for this robot platform. An example of revolute joint is shown in
listings 4.2. The pose of the joint relative to its parent link is speci(cid:12)ed in line 2.
The parent and child link of the joint are de(cid:12)ned in lines 3 and 4. The axis of rota-
tion is speci(cid:12)ed in line 5. Limits regarding the capabilities of the joint such as the

32

4.2 Software

1
2
3
4
5
6
7
8
9

1
2
3
4
5

maximum torque it can deliver or limits to the rotation angle are described in lines
6 and 7. The calibration tag de(cid:12)nes how the joint encoder’s zero position is o(cid:11)set
to the zero position of the model. The identi(cid:12)er is called rising for legacy reasons.
< joint name = " HeadPan " type = " revolute " >

< origin xyz = " -0.0095 0 0.146501 " rpy = " 0 0 0 " / >
< parent link = " torso " / >
< child link = " neck " / >
< axis xyz = " 0 0 1 " / >
< limit effort = " 2.5 " velocity = " 5.6548668 "
lower = " -1.2 " upper = " 1.2 " / >

< calibration rising = " 0.0 " / >

</ joint >

Listing 4.2: Description of the HeadPan joint (a revolute joint) of the Wolfgang
robot platform in the URDF format. A joint connects the parent and
the child link. The origin speci(cid:12)es the pose of the joint in relation to
the parent link and therefore the origin of the child link. Furthermore
the axis and limits of rotation are speci(cid:12)ed. The calibration tag gives
information about the o(cid:11)set of the joint and can be (cid:12)lled by the
software used for robot calibration. The itenti(cid:12)er is caled rising for
legacy reasons.

A (cid:12)xed joint speci(cid:12)es the relationship between two links that do not move rel-
ative to each other.
It is useful in scenarios where some information is known
relative to one link but required in another coordinate system. An example of
this is the camera. Objects in the image are detected relative to the camera but
are often required to be transformed into a di(cid:11)erent coordinate system. An ex-
ample of the description of a (cid:12)xed joint is shown in listing 4.3. This description
speci(cid:12)es the pose of the joint and therefore the pose of its child link relative to
the parent link in line 2, the parent link in line 3 and the child link in line 4.
< joint name = " head_to_camera " type = " fixed " >
< origin xyz = " 0.02 0 0.1115 " rpy = " 0 0 0 " / >
< parent link = " head " / >
< child link = " camera " / >
</ joint >

Listing 4.3: Description of a (cid:12)xed joint of the Wolfgang robot platform in the
URDF format. A (cid:12)xed joint speci(cid:12)es the transformation between two
links.

A URDF of the Wolfgang robot platform with measurements from computer aided
design (CAD) models was created as part of this thesis. Existing CAD models of
the robot parts were assembled in software to be able to make the necessary mea-
surements. Figure 4.4 shows the kinematic chains of the Wolfgang robot platform
described by the URDF.

33

4 Robot Platform

Figure 4.4: Kinematic chains in the Wolfgang robot platform. Each node in the
graph represents a link. Each solid edge is a revolute joint and each
dashed edge a (cid:12)xed joint.

34

base_linktorsol_hip_1LHipYawr_hip_1RHipYawneckHeadPanl_shoulderLShoulderPitchr_shoulderRShoulderPitchheadcameraHeadTiltl_lower_arml_wristl_upper_armLElbowl_footl_solel_toel_ankleLAnkleRollr_lower_armr_wristr_upper_armRElbowr_footr_soler_toer_ankleRAnkleRolll_lower_legLAnklePitchl_upper_legLKneeLShoulderRolll_hip_2LHipPitchLHipRollr_lower_legRAnklePitchr_upper_legRKneeRShoulderRollr_hip_2RHipPitchRHipRoll4.2 Software

4.2.3 Forward Kinematics

Forward kinematics solves the problem of calculating the pose of a link given the
joint angles and the robot’s kinematic model (see section 3.2). ROS comes with
stable and well working tools for this application. The robot state publisher
[15] reads the URDF and receives the current position of the joints. It publishes
the translation and rotation between the links based on this information. An
application requiring information about the forward kinematics (e.g., solving a
question such as "What is the position of an object relative to my base link given
its position in the camera coordinate system?") can use the tf2 [16] library to not
only solve this problem at the current state of the robot but also at a state in the
recent past. It is often required to calculate transformations between coordinate
systems at a point in time in the past because processing times causes information
to be delayed.

4.2.4 Inverse Kinematics

Inverse kinematic solves the opposite problem of forward kinematics. The Hamburg
Bit-Bots currently use BioIK 2 [RHSZ18] for this task. It is an evolutionary inverse
kinematics engine. An analytic solution to the inverse kinematics of the Wolfgang
is not used since the hip yaw motors axis of rotation does not intersect with the
hip pitch motors (see section 3.2.3).
BioIK 2 is well integrated into ROS. The kinematic structure is read from the
URDF (see section 4.2.2), an easy to interface is provided and ROS standard
messages are used as much as possible.
BioIK 2 uses an evolutionary algorithm to compute the required joint angles to
reach speci(cid:12)ed goals. Multiple kinds of goals exist. These include pose goals,
where the desired pose for a robot frame speci(cid:12)ed, or balance goals, where the
robot’s center of mass is held above its support polygon.

4.2.5 Motor Control

The servo motors communicate with the computer with a protocol designed by
Robotis called Protocol 2.0 [17]. It de(cid:12)nes multiple instruction packets for writing
data to and read data from the servos.
In a usual update cycle, the position,
velocity, and torque (through current measurement) are read and depending on
control mode of the motor either goal position, velocity or torque are set. In most
scenarios, it is favorable to use position control where the internal PID controller of
the microchip on the servo handles the amount of current delivered to the motor.
To increase the update rate of the system synchronous writing and reading of the
system is used. Here a single instruction is sent to the motors, and they answer

35

4 Robot Platform

in the order speci(cid:12)ed by the instruction. For a description of how the motors are
connected to the computer refer to section 4.1.2.
A hardware interface [18] provides an abstraction from the speci(cid:12)cs of
Protocol 2.0 . The ros control [CMEM+17] framework allows multiple controllers
to be in operation and exchanged during operation. A large collection of controllers
for di(cid:11)erent purposes exist. Some are simple like the position controller which sim-
ply writes the goal position for the servos to the hardware interface while others
calculate required torques to execute a given trajectory.
The Hamburg Bit-Bots have adapted the position controller to be able to enforce
maximum velocities, accelerations, and torques.

4.2.6 Camera Driver

The Logitech C920 webcam is used in the Wolfgang robot platform and one of
the sensors used for the calibration experiments in this thesis. It is supported by
the Video for Linux (V4L) software. A camera driver integrating the sensor into
the ROS environment has been implemented by the WF Wolves. An improvement
allowing for a camera calibration procedure (see section 5.1) has been developed
by the Hamburg Bit-Bots.

36

5 Calibration Approaches

Reducing errors in the kinematic should lead to two major performance increases.
Firstly, balance during motions should be improved since the feet of the humanoid
are positioned more accurately. Secondly, the positioning error of objects detected
in the main sensor of the platform, the camera, should be reduced. This chapter de-
scribes the approaches taken to estimate the kinematic parameters of a humanoid
robot.
In section 5.1 the (cid:12)rst step of the actual calibration procedure, the calibration of
the intrinsic parameters of the camera, is described. Section 5.2 describes how
the features (the AprilTags and the LEDs detected by the PhaseSpace) are strate-
gically positioned on the robot for accurate measurement of robot poses. The
software which was used and extended is described in section 5.3.

5.1 Intrinsic Camera Calibration

Before any joint or frame calibration was attempted, the intrinsic parameters of
the cameras including its distortion coe(cid:14)cients were calibrated.
To calibrate the cameras the camera calibration robot operating system (ROS)
package [19] which is based on the OpenCV library [Bra00] was used. A checker-
board pattern with known dimensions is captured in multiple poses. The internal
camera features signi(cid:12)cant motion blur and e(cid:11)ects of rolling shutter. Therefore
the checkerboard and camera are (cid:12)rst brought into a stable pose before capturing
an image. Figure 5.1 shows the operator’s view during the calibration procedure.

5.2 Feature Positioning

Robot calibration requires the pose or some dimensions of the pose of a link of the
robot to be measured. The two systems used are AprilTags and the PhaseSpace.
Both require features to be placed on the robot.
The AprilTags were printed using a laser printer and applied to 3D-printed parts
using double-sided tape. One AprilTag was applied to each foot and one to the
torso. The AprilTags on the feet were positioned at a distance of 0:2 meters to
the center of each foot. This allows for the recognition of the AprilTags in more
poses than positioning on the feet itself would, because the tags are occluded in

37

5 Calibration Approaches

Figure 5.1: Camera calibration procedure [19][Bra00]. A checkerboard of known
dimensions is captured by the camera in multiple poses. The colored
points at the inner corners of the checkerboard are drawn into the
image to signalize a correct detection. The bars on the top right show
the spread of poses in which the checkerboard was captured. When the
calibrate button is pressed, the intrinsic parameters and the distortions
coe(cid:14)cients are calculated.

38

5.2 Feature Positioning

fewer poses by the legs. Figure 5.2 shows the AprilTags on one of the feet and the
torso of the robot.
PhaseSpace LEDs were positioned at each corner of the feet with a 3D-printed
mount as well as the torso. In the (cid:12)rst iteration, only four LEDs were positioned
on the torso. Since the distance between the LEDs in the vertical direction was
relatively low with 52mm, the pose reconstruction of the torso was inaccurate in
one rotational direction. Two additional LEDs were therefore added to the bottom
of the torso. All these markers are pictured in (cid:12)gure 5.2.

(b)

(c)

(a)

Figure 5.2: AprilTags and PhaseSpace LED positioning for calibration. (a) One
of the robot’s feet, the AprilTag is glued on a 3D-printed plate which is
screwed into the foot plate. The PhaseSpace LEDs are form-(cid:12)tted in a
3D-printed part at each corner of the foot. (b) The upper part of the
torso is (cid:12)tted with a 3D-printed part. Four LEDs and an AprilTag are
mounted on it. (c) Two additional LEDs at the bottom of the torso
were added to increase pose measuring accuracy.

As previously mentioned, the pose of the torso and feet can be reconstructed using

39

5 Calibration Approaches

at least three LEDs. This requires the placement of the LEDs at a known position
relative to the reconstructed link. Since the LEDs are form-(cid:12)tted into 3D-printed
parts of known dimensions, their location can be measured easily in computer
aided design (CAD).

5.3 Software

The software used in this thesis is the robot calibration ROS package [3]. Its
extension [20] allows to also use AprilTags for calibration. Further adaptation of
the code was required to use AprilTags detected by an external camera since the
external camera is not part of the robot kinematic model. An implementation to
use measurements of the PhaseSpace system for calibration was also integrated
into the robot calibration.
Two con(cid:12)guration (cid:12)les are used for the calibration. The (cid:12)rst con(cid:12)guration (cid:12)le
speci(cid:12)es the capture of observations. The capture con(cid:12)guration (cid:12)le used for cali-
brating the robot using the internal camera and is shown in listing 5.1. Kinematic
chains and their joints, which provide the predicted position of the observations
are de(cid:12)ned in lines 1-13. Starting in line 14, the feature (cid:12)nders (i.e., software
that abstracts from measurement systems) are declared and parametrized. For
the AprilTag feature (cid:12)nder the source of the image and the source of the camera
intrinsic matrix must be speci(cid:12)ed. The ID of the used AprilTags and its size must
also be declared.

Listing 5.1: Capture con(cid:12)guration (cid:12)le

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

chains :

- name : right_leg

joints :

- RHipYaw
- RHipRoll
- RHipPitch
- RKnee
- RAnklePitch
- RAnkleRoll

- name : head
joints :

- HeadPan
- HeadTilt

features :

apriltags2_finder :

type : robot_calibration / AprilTags2Finder
topic : / image_rect_color
camera_info_topic : / camera_info
camera_sensor_name : camera
chain_sensor_name : right_leg

40

5.3 Software

21

22
23
24
25
26
27
28
29
30
31
32
33
34

tag_family :

’ tag36h11 ’ # options : tag36h11 , tag36h10 ,

tag25h9 , tag25h7 , tag16h5

tag_border :
1
tag_threads :
2
tag_decimate :
1.0
tag_blur :
0.0
1
tag_refine_edges :
tag_refine_decode : 0
0
tag_refine_pose :
0
tag_debug :
true
publish_tf :
standalone_tags :
[
{ id : 43 , size : 0.08} ,
]

# default : 1
# default : 2
# default : 1.0
# default : 0.0
# default : 1
# default : 0
# default : 0
# default : 0
# default : false

The second con(cid:12)guration (cid:12)le de(cid:12)nes the free parameters during calibration as well
as the method of error calculation. The con(cid:12)guration (cid:12)le used for calibrating the
right leg using the internal camera with an AprilTag is shown in listing 5.2. It
de(cid:12)nes the base link for calibration into which all measurements are transformed
in line 1. Line 2-9 de(cid:12)ne the two sensor models. The right leg is a kinematic
chain which does the prediction and the camera is the sensor which does the
measurement as described in section 3.7. The free parameters are described in
lines 10-33. Firstly, joints which can have an o(cid:11)set in 10-18, and, secondly, free
poses of coordinate systems. Since an initial estimate can greatly improve the
convergence of the solver, estimates for the frames are de(cid:12)ned in lines 35-48. The
error blocks which de(cid:12)ne the method of error calculation is employed. When the
type chain3d to chain3d (lines 49-53) is selected, the Euclidean distance between
the measurement points is the error.

Listing 5.2: Calibration con(cid:12)guration (cid:12)le

r

l e g

f o o t

- name:

- name: c a m e r a

r i g h t
t y p e : c h a i n
frame:

1 b a s e l i n k : b a s e l i n k
2 models:
3
4
5
6
7
8
9
10 f r e e p a r a m s :
- H e a d T i l t
11
- HeadPan
12
- RHipYaw
13

t y p e : c a m e r a 3 d
frame:
t o p i c : / i m a g e r e c t c o l o r

c a m e r a o p t i c a l

f r a m e

41

5 Calibration Approaches

t a g 4 3

- name:

f r e e f r a m e s :

x: t r u e
y: t r u e
z: t r u e
r o l l : t r u e
p i t c h : t r u e
yaw: t r u e

x: t r u e
y: t r u e
z: t r u e
r o l l : t r u e
p i t c h : t r u e
yaw: t r u e

- RHipRoll
- RHipPitch
- RKnee
- RAnklePitch
- RAnkleRoll

14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49 e r r o r b l o c k s :
- name:
50
t y p e :
51
m o d e l a : c a m e r a
52
model b:
53

x: 0 . 2 8 3
y: (cid:0) 0 . 0 1 5
z: (cid:0) 0 . 0 3 3
r o l l : 0 . 0
p i t c h : 0 . 0
yaw: (cid:0) 1 . 5 7 1

x: 0 . 0 2
y: 0 . 0
z: 0 . 1 1 5
r o l l : 0 . 0
p i t c h : 0 . 0
yaw: 0 . 0

- name:

t a g 4 3

r i g h t

42

- name: h e a d t o c a m e r a

f r e e f r a m e s i n i t i a l v a l u e s :

- name: h e a d t o c a m e r a

f o o t e y e
c h a i n 3 d t o c h a i n 3 d

l e g

5.4 Calibration using the PhaseSpace

Figure 5.3: Measurement points for calibration using an AprilTag. Since the cal-
ibration uses 3D points while the AprilTag detection generates 6D
poses, evenly spread points on the AprilTags surface are generated by
the software to encode the orientation information of the ApriTag.

During the calibration procedure, the robot kinematic chain is moved into an
observable and suitable position for calibration. Then, the software requests the
current position of the features speci(cid:12)ed by the capture calibration (cid:12)le as well as
the predicted position of these features by the kinematic chain.
In the optimization step the Ceres Solver [6] is used to minimize the error in this
non-linear system.
The software produces an updated robot description with updated joint o(cid:11)sets and
frames. This o(cid:11)set is used to correct the motor position by the hardware interface.
While the pose of an AprilTag can be measured, the software can only deal with
points of observation. To encode the orientation of the detected AprilTag, an
evenly spread set of points on the AprilTag is used in the software. This spread
of points on the AprilTag can be seen in (cid:12)gure 5.3.

5.4 Calibration using the PhaseSpace

One source of calibration data is the PhaseSpace. Its working principle is described
in 3.6. In the setup used in this thesis, ten cameras are directed at the working

43

5 Calibration Approaches

area. This is required in some cases to reliably detect LEDs since they might be
occluded by links of the robot. Figure 5.4 shows a picture of the PhaseSpace setup
used for calibration.

Figure 5.4: Phasespace motion capture system. The ten cameras used to detect
the positions of the LEDs are highlighted. The workspace is captured
by the cameras from multiple angles to reduce detection failure caused
by occlusion.

The system provides information about the 3D position of each detected LED
relative to a reference frame. The full robot is positioned in this reference frame
by reconstructing the 6D pose of the base link from the six LEDs mounted on the
torso.
At each calibration pose, the positions of the LEDs on the foot are captured and
transformed from the reference frame of the tracking system to the robot’s base
link coordinate system. Each calibration pose adds four measurement points, one
for each LED.
Since only the kinematic chain from the base link to the end e(cid:11)ector of the leg
is measured, the pose of the internal camera cannot be calibrated. The links and
joints of this chain are shown in (cid:12)gure 5.5a.
A large variety of con(cid:12)guration poses can be captured using the PhaseSpace since
multiple cameras are used, allowing for a variety of con(cid:12)gurations, which would
not be possible to capture with the other systems used.

44

5.5 Calibration using AprilTags and the Head Camera

5.5 Calibration using AprilTags and the Head Camera

The internal camera of the Wolfgang robot platform is the main sensor for external
information of the system. It is a Logitech C910 webcam using USB2 for image
transport. An image with a resolution of 1920x1080 is captured at about 2 Hz.
Since the camera has a rolling shutter and a long exposure time, images of motion
are extremely blurry. It is crucial that the robot is not moved when capturing a
calibration pose.
It is possible to achieve a higher frame rate and faster shutter time by using a
lower resolution. Since the pose accuracy of the detected AprilTags increases with
a higher image resolution, the full HD image was chosen.
At each calibration pose, the pose of the AprilTag relative to the camera is cap-
tured. Then the set of points used to encode the pose (see section 5.3) is added to
the measurements.
Since the pose of the AprilTag is detected relative to the camera and the camera
is part of the kinematic model of the robot, it does not need to be transformed.
Three con(cid:12)gurations of free parameters were evaluated with this calibration setup.

1. calibration of all joints in the kinematic chain from the camera to the foot

2. calibration of the head joints and the pose of the camera relative to the head

3. calibration of the pose of the camera relative to the head

The joints and links of the kinematic chain which were calibrated are displayed in
(cid:12)gure 5.5b.
Even with the AprilTag mounted at a signi(cid:12)cant distance to the foot, there still
exists a large number of poses which can not be measured by this con(cid:12)guration.

5.6 Calibration using AprilTags and an External Camera

For the calibration using an external camera, a Kinect 2 was chosen as a camera.
While it is also a depth camera, only the RGB image was used for the experiments.
It delivers images of 1920x1080 resolution at about 30 Hz. Rolling shutter and
motion blur are much less signi(cid:12)cant in this camera than the internal Logitech
C910.
The external camera may be positioned at any pose, which allows it to fully observe
the torso AprilTag and the AprilTag on the foot at the same time. Its position is
calculated using the AprilTag on the torso using the camera positioner [21].
Similar to the capture of measurement points using the head camera, a set of points
is used to represent the orientation of the AprilTag. Similar to the PhaseSpace

45

5 Calibration Approaches

capturing procedure, the points need to be transformed into the robot’s base link
coordinate system before adding them to the set of measurements.
Since the pose between the torso and the leg is measured, only this kinematic chain
can be calibrated. Figure 5.5c shows the links and joints of this chain.
Poses of the robot in which the AprilTag mounted to the foot is near parallel and
faces the opposite direction to the AprilTag on the torso cannot be captured by
the system.

46

5.6 Calibration using AprilTags and an External Camera

(a)

(b)

(c)

Figure 5.5: Kinematic chains and measurement devices for the three calibration
methods. Nodes represent links, black arrows represent joints of the
kinematic chain. Solid black arrows have a label of the rotary joint’s
name they represent. Dotted black arrows are static joints. Red arrows
show which links are measured by the respective measurement system.
(a) The PhaseSpace measures the positions of the LEDs attached to
the torso and the foot. (b) The internal camera measures the pose of
the AprilTag on the foot. (c) The external camera (Kinect 2) measures
the pose of the AprilTag on the torso and on the foot.

47

base_linktorsor_hip_1r_hip_2r_upper_legRAnklePitchr_lower_legRAnkleRollr_ankler_footleds_footleds_torsoPhaseSpaceRHipYawRHipRollRHipPitchRKneebase_linkHeadPantorsor_hip_1r_hip_2r_upper_legRAnklePitchr_lower_legRAnkleRollr_ankler_footapriltag_footRHipYawRHipRollRHipPitchRKneeHeadTiltneckheadcamerabase_linktorsor_hip_1r_hip_2r_upper_legRAnklePitchr_lower_legRAnkleRollr_ankler_footapriltag_footapriltag_torsokinectRHipYawRHipRollRHipPitchRKnee5 Calibration Approaches

48

6 Evaluation

This chapter presents the calibration results obtained by the calibration approaches
presented in chapter 5.
Firstly, the method of calibration veri(cid:12)cation through measurement is explained
in section 6.1. The manual correction of the robot kinematics description in the
Uni(cid:12)ed Robot Description Format (URDF) [14] of the Wolfgang robot platform
described in section 6.2. The results of the individual calibration approaches are
presented in section 6.3, 6.4, and 6.5 respectively.

6.1 Measurement Method

Two concepts are used to verify the correctness of the calibration results. Firstly,
the reprojection error, for which the internal camera is used to compare the re-
projected visual model of the robot and the position of the mechanical parts in
the image. The results of this method are more relevant to the calibration using
the internal camera and AprilTags since the pose of the camera coordinate system
contributes more to the reduction of the reprojection error than the calibration of
the robot’s leg. The external sensors can not calibrate the pose of this internal
camera since they cannot measure it.
Secondly, measurement of the position of the AprilTags and PhaseSpace LEDs
In this
using the external or internal camera and the PhaseSpace respectively.
method, the features are captured at manually chosen poses. These poses are dif-
ferent from the ones used for calibration. The distances between the four LEDs po-
sitions measured by the PhaseSpace and their positions predicted by the kinematic
model are the error displayed in the following graphs regarding the PhaseSpace.
The 6D pose of the AprilTag captured by the camera is encoded in a set of
points similar to the points generated for the calibration procedure (see (cid:12)gure 5.3).
The distance between the measured and the predicted position of these points is
the error in the following graphs regarding measurements done with cameras and
AprilTags.

6.2 Kinematic Model Veri(cid:12)cation

A correct kinematic model is crucial for forward and inverse kinematics as well as
calculations regarding the transformation of sensor data (see section 3.4).

49

6 Evaluation

(a)

(b)

Figure 6.1: Reprojection error with old and new URDF [14]. (a) Modi(cid:12)ed URDF
of the Nimbro OP [SPA+14] with physically measured robot dimen-
sions.
(b) URDF created for this thesis with CAD models of the
mechanical parts.

The previously used kinematic model of the Wolfgang robot platform was a modi-
(cid:12)ed version of the Nimbro OP [SPA+14] robot. The lengths of the modi(cid:12)ed robot’s
links in this model were measured on the physical robot using calipers.
While a highly accurate robot model might require calibration, measuring the
computer aided design (CAD) models of the individual links can be used to create
a more accurate model than through physical measurement. Therefore a kinematic
model based on the CAD models of the mechanical parts was created. This model
can not account for joint o(cid:11)sets in the servo motors and manufacturing tolerances
or deformations of the mechanical parts.
The model was veri(cid:12)ed by measuring the end e(cid:11)ector pose with the PhaseSpace
system and calculating the corresponding joint angles using the inverse kinematics
solver. Firstly large joint o(cid:11)sets were found in the HipPitch, Knee and AnklePitch
motors.
Analysis of the robot’s hardware interface revealed that the o(cid:11)sets in the
HipPitch and AnklePitch motors were made in software to account for inac-
curacies of the previous robot description. The cause of the o(cid:11)set in the Knee
joint was found to be an error in the robot description. It is caused by an uncon-
ventional geometry of the thigh part of the robot which was not modeled correctly
at (cid:12)rst. Figure 6.1 shows the reprojection of the robot’s old and new visual model
onto an image of the internal camera.

50

6.3 Evaluation of the Calibration using the PhaseSpace

6.3 Evaluation of the Calibration using the PhaseSpace

The calibration was performed as described in section 5.4. Multiple attempts at
calibration were made, and multiple sets of joint o(cid:11)sets calculated by the solver
were collected. These sets of joint o(cid:11)sets were used to update the kinematic model
and evaluate the di(cid:11)erence between the measurement and the updated models as
described in section 6.1.
The free parameters of the calibration process were the six joint o(cid:11)sets of the leg
which was calibrated. The best performing calibration was chosen. Its results are
displayed in (cid:12)gure 6.2. The calibration was unsuccessful as can be seen by the
increase in the increasing mean from before and after the calibration procedure.
This is most probably caused by multiple reasons which increase the measurement
error of the system:

(cid:15) The accuracy of the measurement system is limited by the resolution of
the cameras. The system should be evaluated for absolute accuracy in its
workspace.

(cid:15) Occlusion of LEDs leads to the wrong detection. Sometimes re(cid:13)ections an

LED is detected as the LED itself.

(cid:15) If the pose of the robot is not completely still, a di(cid:11)erence between the
prediction of the model and the measurement occurs because the measure-
ment by the joint encoders is captured at a slightly di(cid:11)erent time than the
measurement of the PhaseSpace system.

(cid:15) The positions of the LEDs relative to the torso and the feet might not be
modeled accurately enough. Though the LEDs were form (cid:12)tted into 3D
printed parts, these parts are slightly di(cid:11)erent in dimension to the CAD
models. This is caused by shrinking during the cooling process after printing
or inaccuracies during printing itself.

In some instances, the solver was not able to (cid:12)nd a solution or the solution was
unfeasible. This was probably caused by measurement error. The kinematic model
cannot be parameterized to (cid:12)t the observed data well when the measurement points
were caused by factors utterly di(cid:11)erent than the free parameters of the kinematic
model such as measurement error.
Since the measurement system only captured the pose of the torso and the foot,
the pose of the camera coordinate system could not be calibrated. Even if an
additional set of markers were used to capture to pose of the robot’s head, the
transformation from the head to the optical center of the internal camera would
still not be measurable.

51

6 Evaluation

(a)

(b)

(c)

(d)

Figure 6.2: Calibration results of the PhaseSpace. The mean (cid:22) and standard de-
viation (cid:27) are given for each distribution. (a) Error before calibra-
tion measured by external camera using AprilTags; (cid:22) = 0:0278m,
(cid:27) = 0:0201m; (b) Error after calibration measured by external cam-
era using AprilTags; (cid:22) = 0:0341m, (cid:27) = 0:0206m; (c) Error before
calibration measured by the PhaseSpace; (cid:22) = 0:0229m, (cid:27) = 0:0134m;
(d) Error after calibration measured by the PhaseSpace; (cid:22) = 0:0307m,
(cid:27) = 0:0133; The error after calibration is greater than before.

52

0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples6.4 Evaluation of the Calibration using AprilTags and the Head Camera

6.4 Evaluation of the Calibration using AprilTags and the Head

Camera

Three di(cid:11)erent sets of free parameters of the kinematic model were calibrated with
the internal camera. The (cid:12)rst set of parameters include, as with the calibration of
the external camera and the PhaseSpace, the joint o(cid:11)sets in the leg and additionally
the o(cid:11)sets in the head joints and the pose of the camera coordinate system. The
head joints and camera frame were calibrated as well since they are part of the
kinematic chain in the measurement system. This kinematic chain is displayed
in (cid:12)gure 5.5. The pose of the AprilTag mounted to the foot was another free
parameter to decrease the error caused by assembly and manufacturing tolerances
of the mounting plate of the AprilTag.
Similar to the calibration using the PhaseSpace, multiple sets of poses were cap-
tured, and calibration was performed on them. The number of poses varied be-
tween 15 and 25. No correlation was found between the number of poses and the
quality of the calibration. The results of the best performing set of parameters
are visualized in (cid:12)gure 6.3. The mean error after calibration is higher than before.
This implies that the calibration was not successful since the goal of reducing the
error in the joints was not achieved. Multiple factors which increase measurement
error might be responsible for this:

(cid:15) E(cid:11)ects of motion blur and rolling shutter distort the capturing and therefore

the pose estimation of the AprilTag.

(cid:15) The pose estimation of the AprilTags is limited by the camera’s resolution

and the accuracy of the camera intrinsics calibration.

A di(cid:11)erent explanation of the unsuccessful calibration is the larger amount of
parameters which increase the dimensionality of the search space the optimization
algorithm has to traverse. The calibration using the PhaseSpace as a measurement
system had only 6 free parameters, for each joint o(cid:11)set in the leg. The calibration
using the internal AprilTag had a total of 20 free parameters, 6 from the leg joints,
2 for the head joints, 6 for the pose of the camera coordinate system in relation
to the head, and 6 for the pose of the AprilTag relative to the robot’s foot. 6
parameters are required for the poses since they are described by a translation in
x, y, and z-direction and a rotation described by the Euler angles roll, pitch, and
yaw (see section 3.2.1).
To reduce the number of free parameters a second set of free parameters was
chosen. It includes the o(cid:11)sets in the joints of the head and the pose of the camera
coordinate system relative to the head. Again also the pose of the AprilTag relative
to the robot’s foot is described by free parameters. This amounts to a total of 14

53

6 Evaluation

(a)

(b)

(c)

(d)

Figure 6.3: Calibration results for AprilTags with the internal camera for leg
calibration. The mean (cid:22) and standard deviation (cid:27) are given for
each distribution.
(a) Error before calibration measured by exter-
nal camera using AprilTags; (cid:22) = 0:0278m, (cid:27) = 0:0201m; (b) Er-
ror after calibration measured by external camera using AprilTags;
(cid:22) = 0:0521m, (cid:27) = 0:0247m; (c) Error before calibration measured by
the PhaseSpace; (cid:22) = 0:0229m, (cid:27) = 0:0134m; (d) Error after calibra-
tion measured by the PhaseSpace; (cid:22) = 0:0425m, (cid:27) = 0:0132m.

54

0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples6.4 Evaluation of the Calibration using AprilTags and the Head Camera

parameters. 2 parameters are the joint o(cid:11)sets in the head, 6 parameters are the
pose of the camera coordinate system relative the head, and 6 parameters are the
pose of the AprilTag relative to the foot.
This set of parameters proved to greatly reduce the reprojection error compared to
the set of 20 parameters. This observation was (cid:12)rst made by looking at the robot’s
visual model reprojected into the image of the internal camera. This can be seen
in (cid:12)gure 6.5. A set of images from multiple poses can be found in appendix A.
To evaluate whether the o(cid:11)sets in the head joint are signi(cid:12)cant, a di(cid:11)erent set
of free parameters was used for calibration on the same data. This set of free
parameters only consists of the pose of the AprilTag and the pose of the camera
coordinate system totaling to 12 free parameters.
Both calibrations seem to have very similar success in reducing the reprojection
o(cid:11)set, so an error analysis similar to the procedure to calculate the error of the
calibration for all joints of the kinematic chain was performed. The predicted
positions of the points spread evenly across the AprilTag (see (cid:12)gure 5.3) are com-
pared to the position measured by the internal camera. The internal camera is
chosen as the sensor since the external measurement systems (i.e., PhaseSpace and
external camera with AprilTags) cannot measure the pose of the head. The error
is measured in several poses of the robot which are di(cid:11)erent from the poses used
for calibration. The results are shown in (cid:12)gure 6.4.
This calibration procedure proved successful, which can be seen in the reduction
of the error between prediction and measurement. Both sets of free parameters
performed very similarly at decreasing the error between model and observation
with a means of (cid:22) = 0:0192m for the calibration of the camera coordinate system
and the head joints and (cid:22) = 0:0184m for the calibration of only the camera
coordinate system.
The similar results of both methods can be explained by the strong correlation of
the o(cid:11)set in the HeadTilt motor and the pitch component (i.e., rotation around
the y-axis). Both parameters rotate the camera coordinate system around parallel
axes. The distance between these axes is relatively small compared to the distance
of the camera to the AprilTag.

55

6 Evaluation

(a)

(b)

(c)

Figure 6.4: Calibration results for AprilTags with the internal camera for head
and camera coordinate system calibration. All graphs show the error
between the measured position of the AprilTag by the internal cam-
era and predicted position by the kinematic model. The mean (cid:22) and
standard deviation (cid:27) are given for each distribution. (a) Before cali-
bration; (cid:22) = 0:0382m, (cid:27) = 0:0076m; (b) After calibration of camera
coordinate system and head joints; (cid:22) = 0:0192m, (cid:27) = 0:0063m; (c)
After calibration of the camera coordinate system’s pose; (cid:22) = 0:0184m,
(cid:27) = 0:0064m.

56

0.000.050.100.150.20error in meters0102030405060708090100density of samples0.000.050.100.150.20error in meters0102030405060708090100density of samples0.000.050.100.150.20error in meters0102030405060708090100density of samples6.4 Evaluation of the Calibration using AprilTags and the Head Camera

(a)

(b)

(c)

Figure 6.5: Reprojection error before and after calibration. (a) reprojection before
calibration; (b) reprojection after calibration of the pose of the camera
frame and head joints. (c) reprojection after calibration of the pose of
the camera frame.

57

6 Evaluation

6.5 Evaluation of Calibration using AprilTags and an External

Camera

The kinematic chain between the base link of the robot and the foot was calibrated
using the external camera with AprilTags as described previously in section 5.6.
Though the camera could be moved during the calibration process, many poses
could not be captured due to the constraints of the camera’s (cid:12)eld of view. An
AprilTag on the opposite side of the foot would increase the amount of poses that
can be captured with the external camera.
The free parameters of this calibration process were the 6 coordinates each of the
poses of the AprilTags on the robot’s foot and its torso, and the 6 joint o(cid:11)sets in
the leg. A total of 18 parameters were attempted to be optimized.
Measurement sets consisting of 15 to 25 poses were used for calibration. Similar to
the calibration using AprilTags and the internal camera of the robot, no correlation
between the number of poses used for calibration and the error after calibration
was found.
The results of the calibration with the lowest error are displayed in (cid:12)gure 6.6.
The measurement of error is done identically to the evaluation of the calibration
described in 6.3. The mean error (cid:22) increased signi(cid:12)cantly from before to after
calibration. This implies that no calibration using the presented method was
successful.
Multiple reasons may be responsible for this:

(cid:15) A general problem of the AprilTag detection already mentioned in the pre-
vious section: When the robot is not completely still in the image, e(cid:11)ects
of rolling shutter and motion blur can deteriorate the performance of the
detection of the AprilTag’s pose. This can introduce faulty measurements
into the set of observations used for calibration.

(cid:15) The camera measures two AprilTags. Since there is an error in each pose de-
tection, the overall error increases compared to the detection of an AprilTag
using the internal camera.

(cid:15) The number of free parameters is relatively high similar to the calibration
of the whole kinematic chain using the internal camera with AprilTags de-
scribed in 6.4.

Similar to the calibration using the PhaseSpace, the pose of the internal camera
could not be calibrated.

58

6.5 Evaluation of Calibration using AprilTags and an External Camera

(a)

(b)

(c)

(d)

Figure 6.6: Calibration results for AprilTags with the external camera for leg
calibration. The mean (cid:22) and standard deviation (cid:27) are given for
each distribution.
(a) Error before calibration measured by exter-
nal camera using AprilTags; (cid:22) = 0:0278m, (cid:27) = 0:0201m; (b) Er-
ror after calibration measured by external camera using AprilTags;
(cid:22) = 0:0855m, (cid:27) = 0:0270m; (c) Error before calibration measured by
the PhaseSpace; (cid:22) = 0:0229m, (cid:27) = 0:0134m; (d) Error after calibra-
tion measured by the PhaseSpace; (cid:22) = 0:0474m, (cid:27) = 0:0166m.

59

0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples0.000.050.100.150.20error in meters01020304050density of samples6 Evaluation

60

7 Discussion

This chapter discusses the results acquired from the experiments and presented
and evaluated in chapter 6. Section 7.1 discussed the creation, validation and
In section
correction of the kinematic model of the Wolfgang robot platform.
7.2 the proposed calibration approaches are compared. Section 7.3 discusses and
compares the approaches for practicality in the (cid:12)eld.

7.1 Kinematic Model

The joint o(cid:11)sets in the motors of the robot were much smaller than initially ex-
pected. The largest deviations were caused by the robot’s kinematic model. The
error in the kinematic model became evident through the use of the measurement
systems. This kinematic model was corrected as the (cid:12)rst step of this thesis. The
corrections in this model are the largest contribution of error reduction achieved
in this work. While the carbon (cid:12)ber reinforced polymer (CFRP) and aluminum
parts of the robot are precision milled, the camera mount is 3D-printed which is
less precise. The pose of the camera was found to be the greatest error source.

7.2 Comparison of Calibration Approaches

Though the calibration attempts using the PhaseSpace and the external camera
with AprilTags failed, the calibration of the camera coordinate system’s pose sig-
ni(cid:12)cantly reduced the reprojection error between the detected and predicted pose
of the AprilTag by the internal camera.
Only the approach using the internal camera with AprilTags is able to calibrate
the pose. While the head position is measurable with the other two measurement
systems presented in this thesis, the camera pose itself is not. The accuracy after
the calibration procedure for the head joints and camera coordinate system is
su(cid:14)cient for the use case RoboCup.
The accuracy of the calculations required in this context regarding the transfor-
mation of objects from image to Cartesian coordinates (see section 3.4) has been
greatly improved. The (cid:12)nal o(cid:11)set in the camera coordinate frame’s pose or in the
HeadTilt joint were both about 0:06 radians (3:4(cid:14)) in the pitch rotation. An object
detected at a distance of 4:5m (half the current (cid:12)eld length in the Humanoid Kid-
Size and TeenSize League) would be located at a distance of 6; 77m in reality. This

61

7 Discussion

is a signi(cid:12)cant increase in accuracy which will become especially relevant with the
increasing (cid:12)eld size proposed by the technical committee of the Humanoid League
of the RoboCup [7].

7.3 Practicality of Calibration Approaches

While measurements done by the PhaseSpace motion capture system seem to be
more precise than the measurements using AprilTags, a large and expensive setup
is required. When the pose of the cameras is changed, a recalibration procedure
needs to be performed. In the RoboCup domain it would not be practical to use
this setup at the competition.
The presented approaches using AprilTags are portable and low cost, because
AprilTags can be printed on standard Inkjet- and laser-printers, the mounting
plates can be manufactured using a 3D printer, and either the internal camera
which is already present in the robot or a an external camera can be used as a
sensor.

62

8 Conclusion and Future Work

This chapter gives a conclusion on the methods and results presented in this thesis
in section 8.1. Furthermore, possibilities for future work are discussed in sec-
tion 8.2.

8.1 Conclusion

In this thesis a robot description in the Uni(cid:12)ed Robot Description Format (URDF)
was created and veri(cid:12)ed for the Wolfgang robot platform and multiple approaches
to calibrate the o(cid:11)sets in the motor’s rotary encoders and the camera coordinate
system of the humanoid robot were proposed. While the calibration of the robot’s
legs was unsuccessful due to the measurement error of the employed systems,
the proposed method for calibrating the head joints and the camera coordinate
system’s pose reduced the reprojection error signi(cid:12)cantly.
The calibration of the robot greatly improves the accuracy of the calculations
regarding the position of objects relative to the robot. This can signi(cid:12)cantly
improve the performance of several software components used in the RoboCup
that rely on such information such as the localization or the behavior module of
the robot.
The error between reality and robot model is signi(cid:12)cantly reduced by the new
robot description. While the dynamic properties of the system are not measured
yet, an accurate model of the robot is a prerequisite to simulate the robot in a
realistic manner. The more accurate kinematic model can also improve the motion
generation of the robot such as the currently employed walking algorithm.

8.2 Future Work

The proposed calibration procedures can be improved in several ways: The calibra-
tion pose selection could be automated. This can reduce the number of poses re-
quired for successful calibration signi(cid:12)cantly [MWB15]. An algorithm for increas-
ing robustness against false measurements of the optimization procedure was al-
ready tested on a di(cid:11)erent robot platform and showed promising results [MWB15].
The calibration process could be automated to reduce the error introduced by the
operator and reduce the time required for calibration. This is especially important

63

8 Conclusion and Future Work

in the RoboCup domain since recalibration might be necessary frequently due to
the robot falling and limited time to perform the calibration procedure.
Another possibility which might increase the robustness and performance of the
calibration is to capture measurements of both legs of the humanoid at the same
time. While this increases the number of free parameters in the system, it could
help to eliminate some local minima of the error function.
Evaluation of the PhaseSpace’s position detection accuracy and repositioning of
the cameras to reduce measurement error of the system might be required.
It
would also be useful to evaluate where in the workspace spacial resolution of the
system is highest to position the robot accordingly during calibration.

64

Acronyms

CAD computer aided design. 29

CFRP carbon (cid:12)ber reinforced polymer. 23

DoF degree of freedom. 1, 8, 10, 12, 21

IMU inertial measurement unit. 5, 23, 25, 26

PLA polylactic acid. 23

ROS robot operating system. 4, 18, 26, 27, 29, 31, 33, 34, 38

SPL Standard Platform League. 2

URDF Uni(cid:12)ed Robot Description Format. 26, 27, 29, 31, 41

V4L Video for Linux. 31

65

Acronyms

66

Bibliography

[ADK16]

[AFG+18]

Ahmed RJ Almusawi, L Canan D(cid:127)ulger, and Sadettin Kapucu. A
new arti(cid:12)cial neural network approach in solving inverse kinemat-
ics of robotic arm (Denso VP6242). Computational intelligence and
neuroscience, 2016.

Julien Allali, R(cid:19)emi Fabre, Loic Gondry, Ludovic Hofer, Olivier Ly,
Steve N’Guyen, Gr(cid:19)egoire Passault, Antoine Pirrone, and Quentin
Rouxel. Rhoban football club: Robocup humanoid kid-size 2017
champion team paper. In Hidehisa Akiyama, Oliver Obst, Claude
Sammut, and Flavio Tonidandel, editors, RoboCup 2017: Robot
World Cup XXI, pages 423{434, Cham, 2018. Springer International
Publishing.

[BA15]

Patrick Beeson and Barrett Ames. TRAC-IK: An Open-Source Li-
brary for Improved Solving of Generic Inverse Kinematics. In Pro-
ceedings of the IEEE RAS Humanoids Conference, 2015.

[BBE+19] Marc Bestmann, Hendrik Brandt, Timon Engelke, Niklas Fiedler,
Alexander Gabel, Jasper G(cid:127)uldenstein, Jonas Hagge, Judith Hart-
(cid:12)ll, Tom Lorenz, Tanja Heuer, Martin Poppinga, Ivan David Ria~no
Salamanca, and Daniel Speck. Hamburg Bit-Bots and WF Wolves
Team Description for RoboCup 2019 Humanoid TeenSize. Technical
report, Universit(cid:127)at Hamburg, 2019.

[BBF12]

[Bes17]

[Bra00]

Oliver Birbach, Berthold Bauml, and Udo Frese. Automatic and self-
contained calibration of a multi-sensorial humanoid’s upper body. In
2012 IEEE International Conference on Robotics and Automation.
IEEE, 2012.

Marc Bestmann. Towards using ROS in the RoboCup Humanoid
Soccer League, 2017. Master thesis, Universit(cid:127)at Hamburg.

G. Bradski. The OpenCV Library. Dr. Dobb’s Journal of Software
Tools, 2000.

[CMEM+17] Sachin Chitta, Eitan Marder-Eppstein, Wim Meeussen, Vijay
Pradeep, Adolfo Rodr(cid:19)(cid:16)guez Tsouroukdissian, Jonathan Bohren,

67

Bibliography

David Coleman, Bence Magyar, Gennaro Raiola, Mathias L(cid:127)udtke,
and Enrique Fernandez Perdomo. Ros control: A generic and simple
control framework for ROS. The Journal of Open Source Software,
2(20):456, 2017.

[FCJ+19] Wu Fan, Xinxin Chen, Jiajun Jiang, Chenghui Li, Yusu Pan, Chun-
lin Zhou, and Rong Xiong. ZJUDancer Team Description Paper.
Technical report, Zhejiang University, China, 2019.

[HD55]

Richard S Hartenberg and Jacques Denavit. A kinematic notation
for lower pair mechanisms based on matrices. Journal of applied
mechanics, 77(2):215{221, 1955.

[HD95]

Radu Horaud and Fadi Dornaika. Hand-eye calibration. The inter-
national journal of robotics research, 14(3):195{210, 1995.

[KANM98] H. Kitano, M. Asada, I. Noda, and H. Matsubara. Robocup: robot
world cup. IEEE Robotics Automation Magazine, 5(3):30{36, Sep.
1998.

[Klu74]

[KRL15]

Allan R. Klumpp. Apollo lunar descent guidance. Automatica,
10(2):133{146, 1974.

Tobias Kastner, Thomas R(cid:127)ofer, and Tim Laue. Automatic Robot
Calibration for the NAO. In Reinaldo A. C. Bianchi, H. Levent Akin,
Subramanian Ramamoorthy, and Komei Sugiura, editors, RoboCup
2014: Robot World Cup XVIII, pages 233{244. Springer Interna-
tional Publishing, 2015.

[LZHT14]

Yunting Li, Jun Zhang, Wenwen Hu, and Jinwen Tian. Laboratory
calibration of star sensor with installation error using a nonlinear
distortion model. Applied Physics B, 115(4):561{570, 2014.

[Mal17]

[Mar63]

Danylo Malyuta. Guidance, Navigation, Control and Mission Logic
for Quadrotor Full-cycle Autonomy, 2017. Master thesis, Jet Propul-
sion Laboratory, 4800 Oak Grove Drive, Pasadena, CA 91109, USA.

Donald W Marquardt. An algorithm for least-squares estimation
of nonlinear parameters. Journal of the society for Industrial and
Applied Mathematics, 11(2):431{441, 1963.

[MFG+19] Hamed Mahmoudi, Alireza Fatehi, Amir Gholami, Mohammad Hos-
sein Delavaran, Soheil Khatibi, Bita Alaee, Saeed Tafazol, Maryam
Abbasi, Mona Yeghane Doust, Asal Jafari, and Meisam Teimouri.

68

Bibliography

MRL team description paper for Humanoid KidSize League of
RoboCup 2019. Technical report, Mechatronics Research Lab, Dept.
of Computer and Electrical Engineering, Qazvin Islamic Azad Uni-
versity, Qazvin, Iran, 2019.

[MRD91]

Benjamin W Mooring, Zvi S Roth, and Morris R Driels. Fundamen-
tals of manipulator calibration. Wiley New York, 1991.

[Mun90]

PJA Munter. A low-o(cid:11)set spinning-current hall plate. Sensors and
Actuators A: Physical, 22(1-3):743{746, 1990.

[MWB15]

[Ols11]

[PKB14]

Daniel Maier, Stefan Wrobel, and Maren Bennewitz. Whole-body
self-calibration via graph-optimization and automatic con(cid:12)guration
selection. In 2015 IEEE International Conference on Robotics and
Automation (ICRA), pages 5662{5668. IEEE, 2015.

Edwin Olson. Apriltag: A robust and (cid:13)exible visual (cid:12)ducial system.
In 2011 IEEE International Conference on Robotics and Automation,
pages 3400{3407. IEEE, 2011.

Vijay Pradeep, Kurt Konolige, and Eric Berger. Calibrating a multi-
arm multi-sensor robot: A bundle adjustment approach. In Experi-
mental robotics, pages 211{225. Springer, 2014.

[QCG+09] Morgan Quigley, Ken Conley, Brian Gerkey, Josh Faust, Tully Foote,
Jeremy Leibs, Rob Wheeler, and Andrew Y Ng. Ros: an open-source
robot operating system. In ICRA workshop on open source software,
volume 3, page 5. Kobe, Japan, 2009.

[RHSZ18]

[RMR87]

[Sho85]

Philipp Ruppel, Norman Hendrich, Sebastian Starke, and Jianwei
Zhang. Cost functions to specify full-body motion and multi-goal ma-
nipulation tasks. In 2018 IEEE International Conference on Robotics
and Automation (ICRA), pages 3152{3159. IEEE, 2018.

ZVIS Roth, B Mooring, and Bahram Ravani. An overview of robot
calibration. IEEE Journal on Robotics and Automation, 3(5):377{
385, 1987.

Ken Shoemake. Animating rotation with quaternion curves. In ACM
SIGGRAPH computer graphics, volume 19, pages 245{254. ACM,
1985.

[SK16]

Bruno Siciliano and Oussama Khatib. Springer handbook of robotics.
Springer, 2016.

69

Bibliography

[SPA+14]

Max Schwarz, Julio Pastrana, Philipp Allgeuer, Michael Schreiber,
Sebastian Schueller, Marcell Missura, and Sven Behnke. Humanoid
TeenSize Open Platform NimbRo-OP.
In Sven Behnke, Manuela
Veloso, Arnoud Visser, and Rong Xiong, editors, RoboCup 2013:
Robot World Cup XVII, pages 568{575. Springer Berlin Heidelberg,
2014.

[WO16]

[Zha00]

John Wang and Edwin Olson. Apriltag 2: E(cid:14)cient and robust (cid:12)du-
cial detection. In 2016 IEEE/RSJ International Conference on In-
telligent Robots and Systems (IROS), pages 4193{4198. IEEE, 2016.

Z. Zhang.
A (cid:13)exible new technique for camera calibration.
IEEE Transactions on Pattern Analysis and Machine Intelligence,
22(11):1330{1334, 2000.

70

Internet Sources

[1] \PhaseSpace Motion Capture." http://phasespace.com/. Accessed: 2019-

01-28.

[2] \RoboCup Federation o(cid:14)cial website." http://www.robocup.org/. Accessed:

2019-03-11.

[3] M. Ferguson, \robot calibration - ROS Wiki." http://wiki.ros.org/robot_

calibration. Accessed: 2019-01-22.

[4] ams AG, \AS5045 - 12-bit Rotary Position Sensor." https://ams.com/as5045.

Accessed: 2019-03-12.

[5] \Urdf/XML/joint - ROS Wiki." http://wiki.ros.org/urdf/XML/joint. Ac-

cessed: 2019-01-28.

[6] S. Agarwal, K. Mierle, and Others, \Ceres solver." http://ceres-solver.

org. Accessed: 2019-01-02.

[7] \Rules and roadmap of the RoboCup Humanoid League." https://www.

robocuphumanoid.org/materials/rules/. Accessed: 2019-03-12.

[8] \ROBOTIS." http://en.robotis.com/. Accessed: 2019-02-04.

[9] \ROBOTIS e-Manual for the Dynamixel MX106." http://emanual.robotis.

com/docs/en/dxl/mx/mx-64-2/. Accessed: 2019-03-12.

[10] \ROBOTIS e-Manual for the Dynamixel MX64." http://emanual.robotis.

com/docs/en/dxl/mx/mx-106/. Accessed: 2019-03-12.

[11] \Rhoban communication board,

featuring 9DOF IMU and 3 dynamixel

buses." https://github.com/Rhoban/DXLBoard. Accessed: 2019-02-08.

[12] \Rhoban website." http://rhoban.com/. Accessed: 2019-02-06.

[13] Hamburg Bit-Bots, \Custom (cid:12)rmware for the Rhoban DXL Board." https:

//github.com/bit-bots/DXLBoard. Accessed: 2019-03-12.

[14] I. Sucan and J. Kay, \URDF - ROS Wiki." http://wiki.ros.org/urdf.

Accessed: 2019-03-12.

71

Internet Sources

[15] I. Sucan, J. Kay, and W. Meeussen, \Robot state publisher - ROS Wiki."
http://wiki.ros.org/robot_state_publisher. Accessed: 2019-02-06.

[16] T. Foote, E. Marder-Eppstein, and W. Meeussen, \Tf2 - ROS Wiki." http:

//wiki.ros.org/tf2/. Accessed: 2019-02-06.

[17] ROBOTIS, \Protocol 2.0." http://emanual.robotis.com/docs/en/dxl/

protocol2/. Accessed: 2019-02-08.

[18] W. Meeussen and A. R. Tsouroukdissian, \Hardware interface - ROS Wiki."

http://wiki.ros.org/hardware_interface. Accessed: 2019-02-06.

[19] J. Bowman and P. Mihelich, \Camera calibration - ROS Wiki." http://

wiki.ros.org/camera_calibration. Accessed: 2019-02-06.

[20] Y. Jonetzko, \Apriltags feature (cid:12)nder for the robot calibration ROS pack-
age." https://github.com/Jntzko/robot_calibration. Accessed: 2019-01-
30.

[21] Universit(cid:127)at Hamburg TAMS group, \camera positioner." https://github.

com/TAMS-Group/camera_positioner. Accessed: 2019-03-08.

72

Appendices

73

A Reprojection Error Before and After Calibration

(a)

(b)

(c)

(d)

Figure A.1: Reprojection error of old URDF, new URDF and after calibration.
(a) old URDF; (b) URDF created for this thesis; (c) after calibration
of the camera’s pose; (d) after calibration of the camera’s pose and
head joints

75

A Reprojection Error Before and After Calibration

(a)

(b)

(c)

(d)

Figure A.2: Reprojection error of old URDF, new URDF and after calibration.
(a) old URDF; (b) URDF created for this thesis; (c) after calibration
of the camera’s pose; (d) after calibration of the camera’s pose and
head joints

76

(a)

(b)

(c)

(d)

Figure A.3: Reprojection error of old URDF, new URDF and after calibration.
(a) old URDF; (b) URDF created for this thesis; (c) after calibration
of the camera’s pose; (d) after calibration of the camera’s pose and
head joints

77

A Reprojection Error Before and After Calibration

(a)

(b)

(c)

(d)

Figure A.4: Reprojection error of old URDF, new URDF and after calibration.
(a) old URDF; (b) URDF created for this thesis; (c) after calibration
of the camera’s pose; (d) after calibration of the camera’s pose and
head joints

78

(a)

(b)

(c)

(d)

Figure A.5: Reprojection error of old URDF, new URDF and after calibration.
(a) old URDF; (b) URDF created for this thesis; (c) after calibration
of the camera’s pose; (d) after calibration of the camera’s pose and
head joints

79

Eidesstattliche Erkl(cid:127)arung

Hiermit versichere ich an Eides statt, dass ich die vorliegende Arbeit im Bach-
elorstudiengang Informatik selbstst(cid:127)andig verfasst und keine anderen als die
angegebenen Hilfsmittel { insbesondere keine im Quellenverzeichnis nicht be-
nannten Internet-Quellen { benutzt habe. Alle Stellen, die w(cid:127)ortlich oder sin-
ngem(cid:127)a(cid:25) aus Ver(cid:127)o(cid:11)entlichungen entnommen wurden, sind als solche kenntlich
gemacht. Ich versichere weiterhin, dass ich die Arbeit vorher nicht in einem an-
deren Pr(cid:127)ufungsverfahren eingereicht habe und die eingereichte schriftliche Fassung
der auf dem elektronischen Speichermedium entspricht.

Hamburg, den 18.03.2018

Jasper G(cid:127)uldenstein

Ver(cid:127)o(cid:11)entlichung

Ich stimme der Einstellung der Arbeit in die Bibliothek des Fachbereichs Infor-
matik zu.

Hamburg, den 18.03.2018

Jasper G(cid:127)uldenstein

