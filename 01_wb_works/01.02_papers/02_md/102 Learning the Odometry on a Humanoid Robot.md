Bachelor’s Thesis

Learning the Odometry on a Humanoid

Robot

Fachbereich Informatik

MIN Fakultät

Universität Hamburg

Autorin:

Valerie Bartel

Studiengang:

B. Sc. Informatik

Matrikel-Nr.:

7406472

Erstgutachter:

Prof. Dr. Jianwei Zhang

Zweitgutachter: Niklas Fiedler

Betreuer:

Jasper Güldenstein

Abgabedatum:

2. Mai 2024

Abstract

In this thesis we present a lightweight method of calculating the odometry of a bipedal humanoid

robot  which  is  independent  of  environmental  conditions  like  lighting.  Our  approach  consists  of

training a neural network to predict the walking step length based on proprioceptive sensor data.

Through  the  integration  of  these  predictions,  the  robot’s  current  pose  relative  to  a  designated

origin is determined. This approach is developed and evaluated in the RoboCup Humanoid Soccer

League domain.

We collect two distinct datasets: One in simulation using the Webots simulator and one in the

real world using a motion capture system. Diﬀerent neural network architectures are trained and

the best-performing model is integrated into the existing software stack of the Hamburg Bit-Bots

RoboCup team. Subsequently, it is compared against two established odometry approaches that

have been used to win competitions. Our new approach decreased the average drift over a ﬁve-

second  period  by  80  percent  in  simulation  and  by  14  on  real-world  data  in  comparison  to  the

baseline methods.

Zusammenfassung

In dieser Abschlussarbeit wird ein umgebungsunabhängiger und leichtgewichtiger Ansatz zur Bes-

timmung der Odometrie eines zweibeinigen humanoiden Roboters präsentiert. Ein neuronales Netz

wird auf propriozeptiven Daten trainiert, um die Schrittlänge des Roboters vorherzusagen. Indem

man diese integriert, erhält man die aktuelle Position des Roboters im Verhältnis zu einem Ur-

sprung. Die Umgebung, in welcher dieser Ansatz entwickelt und ausgewertet wird, ist die RoboCup

Humanoid Soccer League.

Es werden zwei separate Datensätze aufgenommen: Einer in Simulation unter Nutzung des Webots

Simulators  und  einer  in  der  realen  Welt  mit  einem  Motion-Capture-System.  Dann  werden  ver-

schiedene Modellarchitekturen trainiert und das performanteste Modell in die bestehende Software

des Hamburg Bit-Bots RoboCup-Teams integriert. Wir vergleichen unseren Ansatz mit zwei beste-

henden Ansätzen für Odometrie, welche genutzt wurden, um Wettbewerbe zu gewinnen. Unser

neuer Ansatz verringerte den durchschnittlichen Drift nach fünf Sekunden um 80 Prozent in der

Simulation und um 14 Prozent in der echten Welt im Vergleich zu bestehenden Ansätzen.

Contents

1 Introduction .................................................................................................... 1

2 Fundamentals .................................................................................................. 4
2.1 RoboCup ................................................................................................... 4
2.2 Wolfgang OP ............................................................................................. 5
2.3 Odometry .................................................................................................. 7
2.4 Supervised Learning ................................................................................ 11
2.5 ROS 2 ...................................................................................................... 18
2.6 Simulation ............................................................................................... 19

3 Related Work ................................................................................................ 22
3.1 Traditional Approaches ........................................................................... 22
3.2 Neural Network-based Odometry ............................................................ 24

4 Approach ....................................................................................................... 26
4.1 Data Collection ....................................................................................... 26
4.2 Data Processing ....................................................................................... 31
4.3 Neural Networks ...................................................................................... 35
4.4 Integration ............................................................................................... 36

5 Evaluation ..................................................................................................... 41
5.1 Baseline ................................................................................................... 41
5.2 Hyperparameters ..................................................................................... 42
5.3 Experiments ............................................................................................ 44
5.4 Results ..................................................................................................... 45

6 Conclusion ..................................................................................................... 56

Bibliography ..................................................................................................... 58

IV

List of Figures

Figure 1: RoboCup Humanoid Soccer League Game. ........................................ 1

Figure 2: RoboCup Humanoid League match. ................................................... 5

Figure 3: The Wolfgang OP. .............................................................................. 6

Figure 4: The Webots model of Wolfgang. ......................................................... 6

Figure 5: Frames of the robot. ........................................................................... 7

Figure 6: A perceptron. .................................................................................... 13

Figure 7: A multi-layer perceptron. .................................................................. 14

Figure 8: A recurrent neural network. .............................................................. 16

Figure 9: A Long-short-term memory. ............................................................. 17

Figure 10: ROS 2 concepts. .............................................................................. 18

Figure 11: The Webots soccer ﬁeld. ................................................................. 20

Figure 12: The motion capture setup. .............................................................. 29

Figure 13: Reﬂective spheres on the robot’s feet. ............................................. 29

Figure 14: The height of the soles during walking. .......................................... 32

Figure 15: Similar patterns in the data for IMU and transform. ..................... 33

Figure 16: The node diagram. .......................................................................... 37

Figure 17: Walk support state and height of the soles. .................................... 38

Figure 18: Pressure detected by soles’ cleats and sole heights. ........................ 39

Figure 19: Foot pressure based walk support state and height of the soles. .... 40

Figure 20: Walk engine and motion odometry with ground truth. .................. 42

Figure 21: Similarity between tfs and ground truth. ........................................ 44

Figure 22: Odometry approaches and ground truth trajectory using SimNet and
simulation data. ............................................................................................... 46

Figure 23: Quiver plot of the odometry approaches using SimNet on simulation
data. ................................................................................................................. 47

Figure 24: Two walk trajectories of the odometry approaches using the SimNet
on simulation data. .......................................................................................... 48

Figure 25: Histogram of the odometry approaches using the SimNet on
simulation data. ............................................................................................... 48

V

Figure 26: Boxplots of the odometry approaches with the SimNet on simulation
data. ................................................................................................................. 49

Figure 27: Walk trajectories of the odometry approaches in the real world using
the RealWorldNet. ........................................................................................... 51

Figure 28: Histogram of the odometry approaches using the RealWorldNet on
real-world data. ................................................................................................ 51

Figure 29: Boxplots of the odometry approaches using the RealWorldNet. ..... 52

Figure 30: Histogram of the odometry approaches using the SimNet on real-
world data. ....................................................................................................... 54

Figure 31: Boxplot of the odometry approaches using the SimNet on real-world
data. ................................................................................................................. 54

Figure 32: SimNet on real-world data trajectories. .......................................... 55

List of Tables

Table 1: The labels used for training the neural network. ................................ 34

Table 2: The features used for training the neural network. ............................ 34

Table 3: The hyperparameter space. ................................................................ 35

Table 4: Best performing hyperparameters. ..................................................... 43

Table 5: Performance of the odometry approaches in simulation using the
SimNet. ............................................................................................................ 46

Table 6: Performance of the odometry approaches in the real world using the
RealWorldNet. .................................................................................................. 50

Table 7: Performance of odometry approaches on real-world data using the
SimNet. ............................................................................................................ 53

Table 8: Performance of the odometry approaches in the real world using the
RealWorldNet and SimNet. .............................................................................. 53

VI

1 Introduction

Autonomous mobile robots can explore and interact with their environment inde-
pendently. To navigate and take further action, they need to localize themselves,
which is the process of determining where the robot is positioned on a map of the
environment [HD99]. This is particularly important in the RoboCup Humanoid
Soccer League, where bipedal humanoid robots compete autonomously in soccer
matches, as seen in Figure 1.

The robots need to localize themselves on a map of the playing ﬁeld for tactical
play and high-level behavior, such as eﬀective passing. They also require knowl-
edge of how their current position relates to where they started, as the ﬁelds are
symmetric. Otherwise, they can confuse the enemy’s side of the ﬁeld with theirs,
leading to their own goal. Due to the limitation of computational resources and
the need to make decisions in real-time, the approach should be computationally
inexpensive and fast. Additionally, the Humanoid League imposes sensor restric-
tions by only allowing those that can measure what humans can perceive.

Figure 1: Robots of two diﬀerent teams during the RoboCup 2023 in Bordeaux. They need to
enter the playing ﬁeld autonomously and position themselves for the kick-oﬀ. Source: [Bit24]

Odometry is a solution to these challenges. This method consists of integrating
motion estimations [SK16] [p.737] to obtain a pose in relation to a starting point.
For that, it is often only relying on information gained from proprioceptive sensors
like joint encoders and inertial measurement units (IMUs), making it inexpensive
to compute and conforming to the Humanoid League’s rules. Odometry can either
be used as a lightweight localization approach if the starting position in the world
is known or be integrated with other measurements in more complex localization
algorithms like the Monte-Carlo-Localization [Del+99, Thr+01].

For wheeled robots, it is relatively simple to infer knowledge of their current po-
sition from past motion sensors as they always have a speciﬁed link with ground
contact called support link and a simple wheel model [SK16] [p.737].
For legged robots, on the other hand, it is more complicated. Their current posi-

1

tion can be computed by counting the walking step sizes and integrating them,
assuming stable foot-to-ground contact during step-taking.

Regarding  the  Humanoid  Soccer  League,  this  approach  often  suﬀers  from  un-
bounded drift. The step lengths are computed incorrectly if the robot’s geometric
model is inaccurate, which is probable as they are mostly low-cost. Cheap sensors
are usually less accurate and noisy. Inexpensive actuators tend to suﬀer from more
backlash. If the robot has 3D-printed parts, which are light and cheap to produce,
they are also prone to being unstiﬀ. Additionally, the stable foot-to-ground-con-
tact assumption is often violated when slippages happen. These frequently occur
as walking with only two legs can be unstable, and the playing ﬁeld consisting of
artiﬁcial grass is slippery.

To  address  these  issues,  we  propose  a  method  to  improve  legged  odometry  by
using  machine  learning.  The  systematic  error  originating  from  irregularities  in
the geometric model can be learned from the discrepancy between the step sizes
the  robot  computes  based  on  joint  angles  and  the  actual  distance  between  the
feet.  The  dynamic  error  caused  by  slippages  or  deformation  diﬀerences  can  be
estimated by using measurements of an inertial measurement unit, which detects
linear acceleration and angular velocity.
We present a lightweight solution to the problem of unbounded drift of simple
odometry for low-cost and resource-constrained bipedal robots. We achieve this by
training a neural network on data generated in simulation or the real world to pre-
dict the step size based on proprioceptive sensor data and then integrating these
predictions to determine the robot’s current pose relative to a designated origin.
This  can  be  used  as  a  localization  or  to  enhance  other  localization  algorithms.
In the RoboCup Humanoid Soccer League this is a fundamental requirement for
robots  to  participate  in  the  game  usefully.  Additionally,  we  investigate  the  im-
provement of legged odometry through the machine learning model by comparing
it with two existing odometry approaches, which have been used successfully by
the Hamburg Bit-Bots RoboCup team in competitions. Furthermore, we assess
the transferability of results obtained in simulation to real-world scenarios, as data
collection is performed in both environments.

First,  the  basic  knowledge  to  understand  this  thesis  is  introduced  in  Chapter
2, where we present the environment and robot platform used. We also explain
odometry, supervised learning, and other software used.
Second, other approaches that also implement odometry are presented in Chapter
3. These can be divided into traditional and machine-learning approaches, shown
in Section 3.1 and Section 3.2.
Then, we present our approach in Chapter 4. In Section 4.1 and Section 4.2, we
show  how  we  collect  and  process  data  in  simulation  and  the  real  world.  Next,
the neural network architectures and the training procedure are described in Sec-

2

tion 4.3 and their integration into the existing software of the Hamburg Bit-Bots
RoboCup-team is shown in Section 4.4. The code used in this Chapter is made
publicly available on GitHub.¹
In Chapter 5, we discuss the best-performing neural networks and evaluate our
odometry against two already existing odometry approaches used by the Hamburg
Bit-Bots.
Finally, a conclusion is given in Chapter 6, and future work is brieﬂy outlined.

¹https://github.com/val-ba/model-odometry

3

2 Fundamentals

This Chapter provides the basic knowledge needed to understand this thesis. We
oﬀer a brief overview of the environment the odometry proposed in this thesis is
set and evaluated in by introducing the RoboCup in Section 2.1 and the robotic
hardware platform in Section 2.2. Afterwards, as we want to calculate the odome-
try of a humanoid robot, we deﬁne the robot’s motion mathematically and present
an approach for odometry on legged robots in Section 2.3. Enhancements by the
addition  of  diﬀerent  sensors  are  also  mentioned.  Then,  we  explain  the  concept
of supervised learning in Section 2.4, with an emphasis on neural networks and
their peculiarities in Section 2.4.1 and Section 2.4.2, as they can approximate the
errors present in conventional odometry. Following that is an introduction to ROS
2 in Section 2.5, which is the underlying robotics middleware worked with, and a
presentation of the advantages and disadvantages of simulation in Section 2.6 and
Webots Section 2.6.1 for data collection.

2.1 RoboCup

The RoboCup is an annual robotics competition with the objective to win against
the reigning soccer world champions adhering to oﬃcial FIFA rules by 2050. It
ﬁrst  took  place  in  1997  to  foster  the  public’s  interest  in  robotics  and  artiﬁcial
intelligence [Fed24]. Initially focused on soccer due to it being a popular sport
with many challenges like navigation, object detection, self-localization, and high-
level behavior, the competition now includes leagues to advance robotics usage in
domestic tasks, crisis response, or logistics.

We are interested in the Humanoid Soccer Leagues, where humanoid robots must
play entirely autonomously, as depicted in Figure 2. In the following, we focus on
the Humanoid Soccer Kid-Size League, which is mostly similar to the Adult-Size
League but diﬀers in the height of the robots, the size of the playing ﬁeld, and
some peculiarities regarding robot handling.
The robots compete in teams of four under modiﬁed FIFA rules [Fed23]. Their
heights can range from 40 cm to 100 cm, and they can have custom hardware,
which has to be humanoid. This means the model has to have a structure similar
to  a  human  body,  and  the  sensors  are  restricted  to  the  ones  that  can  measure
features humans can sense. The playing ﬁeld has an area of 6 times 9 meters and
consists  of  artiﬁcial  grass,  making  it  non-trivial  to  walk  on.  The  ﬁeld  lines  are
modeled after real soccer ﬁeld lines but scaled down.

4

Figure 2: RoboCup Humanoid League match in Bordeaux 2023. Source: [Bit24]

Besides the main league, there occasionally is the Humanoid League Virtual Sea-
son taking place in simulation using Webots which is described in Section 2.6.1.
Here, matches on a modeled ﬁeld seen in Figure 11 and digital models of robots
and their behavior are simulated.

A good odometry can either reduce the complexity of or function as a naive local-
ization during soccer matches. This is important because localization on the ﬁeld
is one of the key problems that must be solved before intelligent play can occur.
Because of the playing ﬁeld’s symmetry, even good localization needs some sort
of knowledge of which side the robot stands on.
The odometry needs to be computationally eﬃcient and should not rely on non-
human sensor modalities due to the computational restrictions of mobile robots
and the limitation of sensors imposed by the Humanoid League rules.
Additionally, it needs to handle inaccuracies in the robot model and slippages on
the artiﬁcial grass. That is why the RoboCup provides an environment in which
odometry can be developed and tested under non-trivial conditions.

2.2 Wolfgang OP

Wolfgang-OP [Bes+21] is the robot platform used to participate in the RoboCup
Humanoid League by the Hamburg Bit-Bots RoboCup team. It is a low-cost hu-
manoid robot platform that is derived from the Nimbro-OP. It is 80 centimeters
tall, weighs 7.5 kilograms, and has 20 degrees of freedom. It is made of aluminum,
carbon, and PLA, which are light materials, and TPU, which is ﬂexible. An ASUS
Mini PC PN51 is mounted on the robot and provides the computational resources.
The actuators used are Dynamixel MX-64, MX-106. and XH540, which have joint
angle  encoders  [MX-24].  The  MX-64  motors  are  located  in  the  arms  and  head,
and  the  XH540  in  the  knees.  The  rest  of  the  actuators  are  MX-106.  A  Basler
acA2040-35gc on the robot provides images. Two MPU6500 internal measurement

5

units are placed on the head and in the body to obtain information on the robot’s
acceleration, which is useful for fall detection. There are also four strain gauge-
based foot pressure sensors on each foot to detect ground contact.

As this robot is mainly used to participate in the RoboCup Humanoid League,
some custom changes have been made to improve performance for this use case.
Because  robots  frequently  fall  during  matches,  elastic  elements  in  the  shoulder
actuators and neck are added, as well as bumpers to the front and back of the
torso. The robot usually stands or walks, which means there is much weight on
the knee’s actuator. A torsion spring is integrated to reduce this torque.

Figure 3: Wolfgang and a
schematic representation of its kinematic
chain. Source: [Bes+21]

Figure 4: The Webots model of Wolf-
gang.

A Webots model of Wolfgang exists, which was reﬁned when the Hamburg Bit-
Bots  participated  in  the  2021  RoboCup  worldwide  and  the  Humanoid  League
Virtual Season.

In this thesis, we work with forward kinematics and mention a few speciﬁed links
of the robot, which are the base link in the body and the left and right feet. They
are depicted in Figure 5.

6

Figure 5: The sole frames are located at the bottom of the feet, and the base link is located in
the robot’s body. For forward kinematics, the chain of links in between needs to be traversed for
that, so these are also visualized.

Due to the platform’s inexpensive hardware and use of 3D-printed parts, inaccu-
racies in the geometric model are introduced, which should be accounted for. By
using the robot’s proprioceptive sensors, a neural network-based odometry can be
developed to address these imprecisions.

2.3 Odometry

As mentioned in Chapter 1, odometry in robotics integrates motion estimations
to  compute  the  current  pose  in  relation  to  an  origin.  It  can  be  used  for  naive
self-localization or as a starting reference for more computationally expensive lo-
calization  algorithms  [BM18].  Usually,  information  from  proprioceptive  sensors,
like joint encoders and IMUs, are used to measure the distance traversed in com-
parison to a starting point. However, there are also approaches in which data from
exteroceptive sensors is taken into consideration.

2.3.1 Rigid Body Motion

We want to describe how the 3-dimensional movement of a rigid body, which is a
non-deformable object, can be expressed mathematically because this is how we
can represent the movement of a robot and, thus, odometry on a computer. For
this, we refer to Chapter 4 of Modern Robotics by Lynch et al. [LP17]. Then, we

7

show how this can be applied to a robot that moves in relation to a ﬁxed reference
frame, which is the origin of the odometry.
We focus on translation on the x and y-axis and a rotation around the z-axis as
most mobile robots move on a 2-dimensional plane, which is true for the soccer
ﬁeld in the RoboCup. However, some moving objects like drones can translate and
rotate along all three spatial axes.

A rotation by 𝜃 around the z-axis can be represented by the following matrix:

𝑅𝑧 =

cos(𝜃)
sin(𝜃)
0
0

⎜⎜⎜⎜⎜⎛

⎝

− sin(𝜃)
cos(𝜃)
0
0

0
0
1
0

⎟⎟⎟⎟⎟⎞

0
0
0
1⎠

(1)

Translation by n on the x-axis and m on the y-axis is represented by a 4x4 matrix:

𝑇 =

1
0
0
0

⎜⎜⎜⎜⎛

⎝

0
1
0
0

0
0
1
0

⎟⎟⎟⎟⎞

𝑛
𝑚
0
1 ⎠

(2)

The extra dimension is added so that the transformation distinguishes between
points and vectors. Points can be scaled, but vectors cannot.

If a robot moves n units along its x-axis and m units along its y-axis and turns
by 𝜃, then the transformation can be expressed by a single matrix:

𝑇 ⋅ 𝑅𝑧 =

1
0
0
0

⎜⎜⎜⎜⎛

⎝

0
1
0
0

0
0
1
0

⎟⎟⎟⎟⎞

𝑛
𝑚
0
1 ⎠

⎜⎜⎜⎜⎜⎛

⋅

cos(𝜃)
sin(𝜃)
0
0

− sin(𝜃)
cos(𝜃)
0
0

0
0
1
0

⎟⎟⎟⎟⎟⎞

0
0
0
1⎠

=

cos(𝜃)
sin(𝜃)
0
0

⎜⎜⎜⎜⎜⎛

⎝

⎝
− sin(𝜃)
cos(𝜃)
0
0

0
0
1
0

⎟⎟⎟⎟⎟⎞

𝑛
𝑚
0
1 ⎠

(3)

We want to express the movement of a robot in comparison to a ﬁxed reference
frame, so we deﬁne two frames: the ﬁxed world frame {𝑤} and the robot’s base
link frame {𝑏}. By knowing where the robot initially stands, we know how the

8

base link and world frame relate: 𝑇WB. Thus, we can express any point 𝑝 speciﬁed
in the base link frame in the world frame:

𝑝𝑤 = 𝑇WB ⋅ 𝑝

(4)

It is easier to detect one’s movement than to relate it to a global coordinate sys-
tem. That is why when the robot moves, the odometry estimates the change of
position 𝑇BB' based on the base link and not the world frame. For the odometry,
′, which can be
we want to know the robot’s new pose in the world frame 𝑇WB
calculated by:

𝑇WB′ = 𝑇WB ⋅ 𝑇𝐵 ⋅ 𝑇BB′

(5)

𝑇WB is updated to the values of 𝑇WB′, and the process is repeated for the next
steps to always mirror the robot’s pose in the world.

2.3.2 Proprioceptive Odometry

In  this  thesis,  we  are  working  with  a  low-cost  bipedal  robot  with  limited  com-
putational resources in the RoboCup Humanoid League, in which many sensors
are prohibited, as explained in Section 2.1. That is why we present a method of
calculating proprioceptive odometry (PO) for legged robots and brieﬂy describe
frequently used sensors.
PO only relies on information gained from the robot itself and not the environ-
ment to estimate the positional displacement of the robot. This data is usually
consistently available and published in high frequency. It is also computationally
eﬃcient compared to algorithms that rely on visual information as the data is low-
dimensional, which is important for systems with limited resources.

For wheeled robots, estimating this movement can be straightforward, provided
the wheel model is accurate. Through the usage of wheel encoders, which measure
how much the wheel’s actuator is spinning, and the knowledge of wheel circumfer-
ence, the distance laid back can be calculated by multiplying the number of wheel
rotations by the circumference [BM18]. In the following, the focus is on legged
robots.

Measuring the actuators’ velocities would not be enough to estimate the robot’s
position as the geometric model is more complex.
A simple approach is to deﬁne a link in each of the robot’s feet and a base link
in its torso. We know how the feet and the base link relate to each other through
forward kinematics [SK16] [p. 28]. A kinematic chain between the links needs to
be deﬁned, then we can calculate the transformation between its frames by matrix

9

multiplication.
One foot is always on the ground, and we assume that it has zero velocity, which
means that it is not slipping. This foot is called a support foot. When another
foot comes into ground contact, meaning that a step is ﬁnished, it becomes the
new support foot. Using forward kinematics, we can calculate the transformation
from the previous to the current support foot.
When calculating the odometry, we deﬁne a frame {𝑠} and the reference frame
{𝑤} to align in the beginning at step 0, meaning 𝑇WS⁰ = I. After the 𝑖th step is
taken, we use the transformation from the previous to the current support foot
𝑇 𝑖
SS' and calculate the following:

WS = 𝑇 𝑖−1
𝑇 𝑖

WS ⋅ 𝑇 𝑖
SS'

(6)

Assuming the robot has taken 𝑘 steps so far, to obtain the current position of
the robot, we use the transformation 𝑇SB from the support foot to the base and
compute:

𝑇WB = 𝑇 𝑘

WS ⋅ 𝑇SB

(7)

This approach is prone to errors due to inaccurate modeling of the links and incor-
rect angle measurements. Additionally, walking in general is less stable, increasing
the risk of stumbling and slipping.

In the following, we now explain frequently used proprioceptive sensors [Ble+18,
Blo+15, Cam+20, Har+18, Yan+23].
Motor encoders, usually integrated within an actuator, provide information about
the joint positions and angles. By adding knowledge about the distances between
actuators, they can be used to calculate the transformation between adjacent joint
frames through forward kinematics [SK16] [p. 28]. For humanoid robots, the links
of interest are the left and right foot and the base frame, which is usually located in
the robot’s body. Their transformations can be computed by matrix multiplication
because they can be viewed as a serial chain. If the robot’s model is inaccurate,
the transformation is oﬀ and less useful.
Inertial measurement units (IMUs) can sense linear acceleration and angular ve-
locity [SK16] [p.743]. The IMU’s angular velocity can be integrated to obtain the
orientation.  The  linear  acceleration  needs  to  be  integrated  twice  to  obtain  the
translation. This leads to large errors, especially on cheap and noisy IMUs.
Foot pressure sensors can be used to detect ground contact.

10

2.3.3 Exteroceptive Odometry

PO  can  be  augmented  by  using  a  variety  of  other  sensors.  This  leads  to  more
accurate results, but also more complex algorithms with more computational and
hardware expenses. We only brieﬂy mention them here for completeness, as this
thesis focuses on proprioceptive odometry.
An example of using external information is tracking key features in the camera’s
image to detect positional changes and using this information to deduct to one’s
position [Aqe+16].
If only visual information is used, the approach is called Visual Odometry (VO). If
it is an addition to the IMU, it is called Visual-Inertial-odometry (VIO) [Blo+15].
Other feasible sensors for extending the odometry are lasers, sonar scanners, or
GPS [SK16] [p.744].
Sometimes, many diﬀerent sensors are fused to create a robust model [WCF22].

2.4 Supervised Learning

As legged odometry usually suﬀers from unbounded drift, as mentioned in Sec-
tion 2.3.2, we want to use supervised learning to mitigate this error by learning a
corrected step size.
Supervised learning aims to infer a target value from observable information. A
mapping from input to output can be approximated through the usage of anno-
tated data, which means that the target values of given input features are known.
The  following  explanation  is  based  on  the  notation  used  in  Chapter  6  of  Data
Science: An Introduction to Statistics and Machine Learning by Matthias Plaue
[Pla23].
An n-dimensional input can be represented as a vector:

𝑋 = (𝑥1, 𝑥2, …, 𝑥𝑛)

(8)

If all input features are continuous, then 𝑋 ∈ ℝ𝑛. The set of all feature vectors
can be called 𝚾.
Similarly, the target value can be deﬁned as :

𝑌 = (𝑦)

(9)

If y is continuous, namely 𝑦 ∈ ℝ, it is called a regression problem. The set of all
output vectors is 𝚼. 𝚼 can have multi-dimensional elements as well, but they are
treated as one-dimensional from now on for simplicity.

As mentioned above, we have annotated data which can be represented as pairs:

11

{(𝑋𝑖, 𝑌𝑖)| 𝑋𝑖 ∈ 𝚾 ∧ 𝑌𝑖 ∈ 𝚼} ⊂ 𝚾 × 𝚼

The set of all possible mappings from 𝚾 to 𝚼 is deﬁned as:

Φ ≔ {𝑓 : 𝚾 → 𝚼}

(10)

(11)

We want to ﬁnd the mapping 𝑓 ∈ Φ, which captures the relationship between in-
put and output vectors by fulﬁlling 𝑓(𝑋𝑖) = 𝑌𝑖 for all pairs in the dataset.
For that, we choose a model which can represent several mappings of a subset
of Φ:

𝜑 ≔ {𝑓(⋅, Θ) : 𝚾 → 𝚼 | Θ ∈ 𝑃 } ⊂ Φ

(12)

The model can take on diﬀerent conﬁgurations of parameters 𝑃 .
It is unlikely that we can ﬁnd the exact mapping, so the goal is to ﬁnd a conﬁgu-
̂Θ) a good approximation. If the mapping is good,
ration  ̂Θ ∈ 𝑃  which makes 𝑓(⋅,
then for any input features 𝑋* and the belonging output 𝑌 * and a prediction 𝑌 ′:

𝑓(𝑋*,

̂Θ) = 𝑌 ′~𝑌 *

(13)

As we can only sample the input and output space most of the time, we create
a dataset by doing so. In a dataset 𝐷 of size 𝑁 , we have N tuples (𝑋𝑖, 𝑌𝑖), 𝑖 ∈
{1, …, 𝑁 }. Assuming that the dataset reﬂects the actual relation of input to output
features reasonably well, the model makes good predictions on unseen data. If it
does not, the prediction will be biased, which happens if datasets are imbalanced
or too small.
How good a mapping approximates the relationship of input to output, can be
measured by calculating the distance between the prediction on input 𝑋𝑖 and the
label 𝑌𝑖 with (𝑋𝑖, 𝑌𝑖) ∈ 𝐷. This is called a loss function:

𝜆 : 𝚼 × 𝚼 → [0, ∞[ ,   (𝑌 ,

̂𝑌 ) ↦ 𝜆(𝑌 ,

̂𝑌 )

(14)

We want the model to predict well on the whole dataset. Thus, we minimize the
following function with respect to Θ:

Λ(Θ) =

1
𝑁

𝑁
∑
𝑛=1

𝜆(𝑌𝑛, 𝑓(𝑋𝑛, Θ))

(15)

The loss depends on the distance metric chosen in Equation 14. For regression
problems, feasible loss functions include the mean-squared and the mean absolute
errors, which are calculated by taking the mean of the (squared) diﬀerence from
label to function output.

12

MSE =

MAE =

1
𝑛

1
𝑛

𝑛
∑
𝑖=1

(𝑌 ′ − 𝑌 *)²

𝑛
∑
𝑖=1

|(𝑌 ′ − 𝑌 *)|

(16)

(17)

There are several approaches to ﬁnding a local or global minimum for Λ by adapt-
ing Θ. This method depends on the model chosen. Approaches for neural networks
are discussed in Section 2.4.1.

2.4.1 Neural Networks

One method to implement supervised learning is the training of artiﬁcial neural
networks.  Conceptually,  they  emulate  the  human  brain’s  neurons  [Agg18].  The
most  basic  neural  network  is  called  perceptron  and  consists  of  𝑛  input  nodes,
which  correspond  to  each  dimension  in  the  input  vector,  and  one  output  node.
This is depicted in Figure 6. The input nodes are connected to the output node
by n distinct edges with weights 𝑤1, …, 𝑤𝑛. The output node computes (∑𝑛
=
𝑤𝑖𝑥𝑖) + 𝑏, with b being an optional bias term, and then passes it through an ac-
tivation function, which is the following in the case of a perceptron:

𝑖=1

sign(𝑥) ≔ {

1 if 𝑥 ≥ 0
−1 else

(18)

Figure 6: The ﬁve input features denoted as the 𝑥𝑖, 𝑖 ∈ {1, …, 5} are all put into distinct input
nodes. Then, the input features saved in the input nodes are multiplied by the weights 𝑤𝑖, 𝑖 ∈
{1, …, 5}  and  then  summed  up  with  the  bias  term  𝑏.  Lastly,  the  sum  is  passed  through  the
activation function, which produces the ﬁnal prediction of 𝑦. Source: [Agg18] P.5.

Multiple intermediate layers, which are called hidden layers, can be put between
the in- and output layers. The number of hidden layers and their size can be var-
ied, but the in- and output layers have to stay the same size as the in- and output
features respectively. The nodes of each layer are fully connected to the nodes of

13

the previous and following layers. All these connections have their own weights.
This is called a multi-layer perceptron and can be seen in Figure 7.

Figure 7: We see two hidden layers with size three, which are fully connected to the two adjacent
layers. As mentioned, the in- and output dimensions are not changed. Source: [Agg18] P.18.

The weights and bias terms operate as parameters of the model, like Θ in Equa-
tion 12. In contrast, the set 𝑃  is decided upon by the model architecture, meaning
the size and connection of its layers. We want to ﬁnd a conﬁguration  ̂Θ ∈ 𝑃 , which
minimizes a chosen loss function like in Equation 15. Λ is calculated by passing
the samples of the given dataset through the network and comparing the output
with  the  label  in  Equation 14.  Then,  the  gradient  of  the  function  Λ  given  the
dataset is calculated, pointing in the direction of the steepest ascent. The weights
are updated in the opposite direction of the gradient by a fraction of the actual
value, which is deﬁned by a scalar value called the learning rate. The learning rate
must be suﬃciently big because otherwise, the weights will be updated too slowly.
If it is too big, on the other hand, the local or global minima may not be reached
as it keeps overshooting.
There are variations of this approach: Stochastic gradient descent (SGD) updates
the weights based on many randomly chosen samples, instead of deriving Λ. If a
batch of samples is used instead of the whole dataset, it is called mini-batch gra-
dient descent. There are also other more sophisticated approaches where the size
of the derivation step is varied dynamically, such as the Adam optimizer [KB14],
which uses momentum.
We still need to determine which node contributed to which part of the error to
update the weights accordingly. This can be done by using an algorithm called
backpropagation, which, after passing the input data through the network and
computing the loss, recursively computes the gradient with respect to the para-
meters, i.e., weights and biases, starting at the output layer. This can then be
used to update the weights according to the gradient.

We want the activation function to map values into narrow ranges like −1 and
1, as this way, big values do not have proportionally smaller weights. Due to the
backpropagation approach, it should also be diﬀerentiable. Additionally, the func-
tion should be non-linear. Otherwise, the model can only learn linear relations.
The tanh and sigmoid functions are frequently used and suﬃce these criteria.

14

sig(𝑥) =

sig′(𝑥) =

1
1 + 𝑒⁻𝑥

1
1 + 𝑒⁻𝑥

⋅ (1 −

1
1 + 𝑒⁻𝑥

)

tanh(𝑥) =

𝑒²𝑥 − 1
𝑒²𝑥 + 1

tanh′(𝑥) = 1 − (

𝑒²𝑥 − 1
𝑒²𝑥 + 1

)²

(19)

(20)

The non-diﬀerentiable ReLU function can also be used by setting its derivative to
zero at its undiﬀerentiable point.

ReLU(𝑥) = max(𝑥, 0)

ReLU′(𝑥) = {

1 if 𝑥 > 0
0 else

(21)

Now, we present approaches to ensure the model performs well on unseen data.
To force the model to rely not only on speciﬁc neurons encoding some features,
they  are  randomly  set  to  0  with  a  speciﬁc  probability.  This  approach  is  called
dropout.
Overﬁtting occurs when complex models are trained on small data sets, as pre-
sented in Section 2.4.2. The model remembers the dataset’s samples instead of
learning the proper relationship between input and output. Unseen inputs passed
through the mapping are poorly predicted. This can be counteracted by using a
simpler model or stopping the training early enough.
To determine the latter, the dataset is split into two parts. The ﬁrst part is used to
optimize the parameters. The samples in the second part are not used for training
and thus show how well the model generalizes to unseen data. This part is also
used to decide on the model architecture, the optimizer, the loss function, and
other hyperparameters.

2.4.2 Recurrent Neural Networks

When a bipedal robot takes a step, the previous steps might be inﬂuencing the
current  one.  Thus,  information  on  preceding  steps  should  be  considered  when
training a neural network to predict the step size. If the order of input samples
gives useful context, e.g. for time series, recurrent neural networks can be used.

15

They have hidden layers that have cycled connections between nodes. That means
the values of previous input sent through the model aﬀect the current prediction
as seen in Figure 8.

Figure 8:  A neural network with a recurrent layer and its unrolled representation. In (a), we see
that some edge weights represented by the edge 𝑤hh are fed back into the hidden layers. This
way, the network can remember information from previous inputs. In (b), we see that it does
not have any cycles. Source: [Agg18] P.275

When optimizing the parameters, the network needs to be unrolled over time to
have the same structure as a normal multi-layer perceptron, as seen in (b) of Fig-
ure 8. This unrolling can get very long for sequences with many input steps.
This way, the vanishing, and exploding gradient problems might occur when op-
timizing  through  backpropagation  as  the  update  rates  for  the  weights  between
layers get very small or very big. The gradient usually vanishes for the weights
between the ﬁrst layers, almost not altering them at all and thus making learning
impossible.  On  the  other  hand,  the  exploding  gradient  has  huge  update  steps,
which means the loss function probably does not converge.

To counter this, there is long-short-term memory [HS97], which can also remember
the context of previous inputs but with fewer weights. It contains two diﬀerent
states. The cell state functions as a long-term memory as it can retain information
from the whole input sequence. A hidden state, which is the output of the LSTM
at  the  previous  time  step,  realizes  the  short-term  memory.  The  two  states  are
managed using three diﬀerent gates, which can be seen in Figure 9. The forget
gate decides which information should be removed from the cell state, whereas
the input gate checks which information should be forwarded to it. The output
gate selects which information from the short- and long-term memory should be
passed to the next layer and output.

16

Figure 9: Depiction of an LSTM. The input vector at time 𝑡 is denoted as 𝑋𝑡 and the hidden state
of the previous time step as ℎ𝑡−1. They are concatenated and ﬁrst passed through the forget gate,
which consists of the ﬁrst sigmoid and the combination of its output with the previous cell state
𝑐𝑡−1. The input gate comprises the second sigmoid and the tanh function, which are combined
and added to the cell state. The output gate combines the previous hidden state passing through
the third sigmoid and the cell state 𝑐𝑡 passing through the tanh. The output is ℎ𝑡, which also
functions as the hidden state for input 𝑥𝑡+1. Source: [Lon24]

2.4.3 PyTorch

To implement the neural network for the odometry, we use PyTorch [Pas+19], a
machine-learning library for Python. It has commonly used optimizers, loss func-
tions, and components of neural networks like fully connected or recurrent layers
already implemented and can be used modularly.
The underlying data structure used is called a tensor, which is the multi-dimen-
sional extension of one-dimensional vectors and two-dimensional matrices. These
tensors  store  values  including  edge  weights  between  nodes  and  in-  and  output
features. Tensor operations can be calculated on accelerating hardware such as
GPUs, which can be used through the Nvidia CUDA framework.
When training a neural network, we usually want the data to come in batches
and  be  shuﬄed.  By  inheriting  from  PyTorch’s  Dataset  class,  a  dataset  can  be
implemented that can be used by a PyTorch Dataloader, which automates tasks
such as batching, shuﬄing, and multi-threaded loading, thereby streamlining the
training process and improving eﬃciency.

17

2.5 ROS 2

The software run on Wolfang presented in Section 2.2 when participating in the
RoboCup is mostly written using ROS 2 [Mac+22]. Therefore, it is used to imple-
ment neural network-based odometry.
ROS, standing for robot operating system, is an open-source middleware for us-
age in robotics and enables communication of otherwise independent components.
There are two distinct frameworks named ROS 1, whose latest distribution reaches
the end of life in May 2025 [Dis24], and ROS 2, with new distributions still released
yearly [ROS24]. The underlying concepts and implementations diﬀer, and in the
following, the focus is on ROS 2.
The fundamental units of the software are called nodes. They have diﬀerent func-
tionalities  and  their  own  context  and  thus  need  to  share  data  explicitly.  The
framework provides means of n-to-m communication via so-called topics. On these
topics, standardized messages can be passed asynchronously through a publisher-
subscriber mechanism seen in Figure 10. Custom messages can be deﬁned by spec-
ifying their format following a given semantic.
Other means of communication are services that provide a request-response com-
munication when the assurance of receiving and completion of a task is wanted,
and actions that are similar to services but can provide continuous feedback are
non-blocking and cancellable.

Figure 10: Node A and Node B subscribe to a topic on which Node C publishes messages.
Node A provides an action server. Node C has an action client which can send requests to the
server. The service follows a similar principle, with Node C providing it and Node B requesting
it. Source: [Mac+22]

ROS 2 is implemented to provide a more secure and time-constraint reliable com-
munication compared to ROS 1 by using DDS, a middleware for data exchange.
It uses a decentralized peer-to-peer approach for every node to detect the others
instead of a centralized node that handles the registration and opens the commu-
nication channels between other nodes.

18

ROS 2 is written in C but supports diﬀerent languages, foremost C++ and Python,
that  implement  the  ROS  client  library  (rcl).  As  ros  nodes  are  structured  into
packages, reuse of existing implementations from other users is possible. Several
tools enable visualization of data like plotjuggler [Fac24] for time series, Rviz [RVi]
for  general  visualization,  and  rqt  [ROS24]  running  graphical  user  interfaces  as
plugins. There is also a tool called rosbag, which enables recording, saving, and
playing back messages published on given topics. They are stored as .mcap, which
is a container format for time-stamped data. This way, data can be serialized and
stored eﬃciently. Later, it can be deserialized again, and all the information about
topics, messages, and their times of reception is kept. Another useful package is
tf2, which provides geometric transformations between frames deﬁned in a tree
structure to given time stamps.

2.6 Simulation

In  this  thesis,  we  want  to  generate  data  for  neural  network-based  odometry  in
simulation, as it is easier to obtain and does not pose a risk to the robot compared
to  the  real  world.  Moreover,  this  simulation-based  approach  serves  as  a  proof-
of-concept for sim-to-real transfer, showing whether training neural networks in
simulation and deploying them on physical robots is viable.
A system or objective can be investigated by building a model that behaves sim-
ilarly  but  is  easier  to  observe.  Robots  and  their  environment  can  be  modeled
digitally on a computer. There usually is a need for an accurate physical repre-
sentation of the real world and thus mathematical models have to be implemented
to compute the behavior of objects. Even if this is done well, there will be inac-
curacies as a physics engine can only approximate real-world properties and does
not consider all of them.

This means there is always a gap between soft- and hardware working in simula-
tion and transferring it to the real world. The models are ﬂawed as sensors underly
diﬀerent noise due to production errors. It is also diﬃcult to model the materials
used and inertia correctly. Additionally, the simulator does not run in continuous
but discrete time steps and thus can only approximate continuous systems.
To minimize this diﬀerence, the model has to be either very accurate to the real
world, which is diﬃcult to obtain, or depend very little on the implementation de-
tails of the simulation software by focusing on modeling only the most important
characteristics of the system. An example of that is the simulation of a robot’s
sensor used to detect an event and the diﬃculty of modeling the sensor readings
and noise. To obtain good results, we either need to take special care during the
modeling  of  the  sensor  to  make  it  as  realistic  as  possible  or  we  only  focus  on
whether the sensor detects the event or not and work with this information, dis-

19

regarding the concrete readings.
Nevertheless,  simulation  can  be  very  useful  for  developing  and  testing  robotic
systems, especially when acquiring real-world data is challenging or impractical.
The simulation keeps track of detailed information about objects in the world and
their properties to properly simulate. This means obtaining this information does
not  pose  an  additional  cost.  In  addition,  it  is  usually  cheaper,  and  there  is  no
risk of damaging hardware or causing other harm during experiments. Simulation
can also accelerate the development process as changes to the model can be made
quicker than those to the hardware.

2.6.1 Webots

The  simulation  software  Webots  [Web24]  has  been  used  for  the  RoboCup  Hu-
manoid League Virtual Season and thus is an established environment for simu-
lating humanoid robots. As mentioned in Section 2.1 and Section 2.2, there exist
digital models of the robots and the ﬁeld, which we use.
Webots is a simulation software for the physical simulation of mobile robots de-
veloped by Cyberbotics Ltd and has been open-source since 2019. Simulation of
various sensors and actuators is supported, enabling users to model diﬀerent hard-
ware platforms.

Figure 11: The model of a six times nine meters soccer ﬁeld. The grass is an unstiﬀ plane.

It is also possible to create a so-called Supervisor, which can edit the scene and
also obtain information about every other object in the simulation, except internal
measurements and computations made by the robot [Sup24]. Webots also provides
an interface for implementation with ROS nodes, making running software written
in it, using visualization tools, and rosbags for data collection possible.

There are some disadvantages of simulating robots in Webots due to the underly-
ing physics engine, the Open Dynamics Engine (ODE) library developed by Russel
Smith, which is used to simulate rigid bodies composed of many interconnected
parts. Most legged robots have many joints, and the joint-dampening approach
appears to not model the real-world counterpart well [Dru+10]. The friction mod-

20

eling has artifacts, meaning that movements diﬀer from the real robot and joint
constraints may be overstepped if a solver cannot ﬁnd another way.

In this thesis, we want to generate data in simulation to leverage the advantages
mentioned above. As the robot software uses ROS 2 and a model of the ﬁeld and
robot exists, Webots is a feasible simulator.

21

3 Related Work

Key problems in legged odometry are the inaccuracies of sensor measurements and
the detection and modeling of slippages. There are several existing approaches that
tackle these problems which can be roughly divided into two categories. The ﬁrst
consists of traditional approaches, which mostly use diﬀerent models of Kalman
Filters (KF) described in Section 3.1, and the second one uses machine learning
on data from diﬀerent sensors shown in Section 3.2.

3.1 Traditional Approaches

Because  of  noisy  sensor  information,  many  of  the  following  approaches  use  a
Kalman Filter, which can estimate a robot’s position by making an initial guess
about its starting position and velocity. Then, it can use its sensors to obtain a
measured position. Afterwards, the predicted position is calculated by applying
a  weighted  diﬀerence  between  the  initial  guess  and  the  measured  velocity  and
adding it to the initial guess [WBo95]. The same is done for the velocity. The next
state estimation, which will replace the initial guess from then on, is calculated by
adding the predicted velocity to the predicted position. The advantages are that it
is comparatively easy to compute and returns the optimal linear solution. Often,
we need to estimate non-linear relationships, which the Kalman Filter cannot do.
For that, an Extended Kalman Filter (EKF) can be used, which linearizes all the
non-linear components [JU97]. Drawbacks to this approach are that sometimes
unstable ﬁlters are created and that the calculation the linearization is based on
can be diﬃcult to implement. These problems can be solved by using an Unscented
Kalman Filter (UKF) that estimates the current state from a random variable
whose  mean  and  covariance  are  set  based  on  deterministically  chosen  samples
passed through the motion model.

Bloesch et al. model the odometry for legged robots using IMU measurements and
kinematics in an Extended Kalman Filter [Blo+13]. They try to keep the model
simple  and  independent  of  the  robot  platform.  Their  state  vector  is  composed
of  the  position  of  the  center  main  body,  its  velocity  and  a  rotation  in  relation
to  the  internal  coordinate  frame  to  the  body.  Adding  to  that  are  the  absolute
position of its feet, an accelerometer bias, and a gyroscope bias. Their measure-
ment model consists of the transformation from world to body frame, a negative
velocity of the body in the body frame, and the rotation and bias terms for the
IMU. Using a motion capture setup, their approach is evaluated on a quadruped
robot on uneven and slippery ground. They conclude that they can estimate the
robot’s roll, pitch, and velocity well but not its general position or yaw. This is
because when one foot is in ground contact, these values can be fully observed

22

through IMU measurements. To obtain the absolute position though, the linear
acceleration measurements need to be integrated twice leading to accumulation of
large errors. Computing the yaw is diﬃcult as gravity has no vertical translation
reference.
Following  the  previous  approach,  Rotella  et  al.  make  changes  to  it  to  ﬁt  a  hu-
manoid robot [Rot+14]. As humanoid robots usually have ﬂat feet instead of a
quadruped’s point feet, there is less possibility for tilting, making the geometric
model and thus computations simpler. This approach is again independent of the
exact humanoid robot platform used. They tested their implementation in simu-
lation and compared it to the ﬁlter implemented by Bloesch et al. They ﬁnd that
the ﬁlters behave mostly similarly but that the velocity estimation for ﬂat-foot
robots diverges less.

Bledt  et  al.  [Ble+18]  implement  odometry  on  the  quadruped  MIT  Cheetah  3,
which can use a normal Kalman Filter instead of the extended version. They split
the pose estimation into ﬁrst computing the robot’s body orientation and second
using a KF to predict the linear position.

Camurri et al. provide a legged robot state estimation framework with velocity
correction,  which  at  its  core  consists  of  an  Extended  Kalman  Filter  that  fuses
IMU and leg odometry [Cam+20]. They can also fuse additional information from
exteroceptive sensors like stereo image cameras and lidar scanners. They evaluated
their approach on several robotic platforms, which are both biped and quadruped,
and it showed a deviation of less than 35 centimeters on ten meters traveled in
diﬃcult environments. The robot’s walking speed ranged up to half a meter per
second.

Yang et al. [Yan+23] explain that normal odometry usually assumes zero velocity
when  there  is  feet-to-ground  contact,  which  is  not  true  in  some  terrains.  They
hope to detect slippages by placing one IMU on each of the robot’s calves and
using their measurements, joint encoders, and a body IMU. Because they only use
proprioceptive sensors, their computations are lightweight because of the low di-
mension of their data. Their evaluation showed that their approach outperformed
standard PO.

Approaches, that use other mathematical models, are presented in the following.
Wisth et al. use stereo vision and IMU measurements, joint encoders and torque
sensors to incorporate a velocity bias term into a factor graph, which models slip-
pages in the leg odometry of a four-legged ANYmal robot [WCF20]. They assume
that there is an almost constant velocity bias in their Inertial state estimator when
walking. They do not want to further model the dynamics of non-rigid terrains as
this can be robot-speciﬁc and does not abstract well. The Bias term consists of
the IMU’s gyro and accelerometer biases and the new angular and linear velocity

23

biases proposed by the researchers. Additionally to the robot state, the position of
all visual landmarks is estimated. They model their factor graph by preintegrat-
ing their IMU measurements between two consecutive time steps. Their approach
showed improvements to their previous work and to other proprioceptive odome-
try approaches.
Wisth et al. use factor graphs to fuse four diﬀerent sensors [WCF22]. As visual
information was used, they extensively tested their approach in an environment
that was dark and dusty. Their evaluation showed an improvement to other state-
of-the-art approaches.

3.2 Neural Network-based Odometry

Wang et al. train a deep recurrent neural network that directly infers position from
raw image data which can represent the sequential dependencies between images,
which are diﬃcult to model explicitly [Wan+17]. Their architecture consists of a
convolutional neural network to extract the features followed by a multi-layered
LSTM to encapsulate relations of the CNN’s outputs. The ﬁnal output is the pose.
Their approach showed stable outputs, although they had some trouble evaluating
them as overﬁtting was hard for them to detect.

Chen et al. trained a recurrrent neural network on sequences of raw IMU data
to output the location transformations in 2D coordinates, learning the positional
displacement directly from IMU data [Che+18].
Liu et al. trained a regression model on IMU data, which outputs a 3D displace-
ment [Liu+20]. Then, it was integrated into an EKF, which takes the net’s output
and predicts the transform, the velocity, and an IMU bias.

Buchanan et al. train a 1D ResNet18 architecture, which is a convolutional net-
work, to predict the positional increment from gravity-aligned IMU measurements
generated on a quadruped robot [Buc+22]. The network also outputs its uncer-
tainty. The model is evaluated by integrating it into a Kalman Filter and a factor
graph.
Following that, the same authors train an LSTM and a transformer, which are
both recurrent neural networks, to predict a device-speciﬁc IMU bias, which is
later used in a factor graph [Buc+22]. The data is not necessarily collected on
the robot. They take a slice of their IMU measures and previous bias estimates
as input for their model to output the current bias term. As the model is device-
speciﬁc, it can be used not only on legged robots but also on drones or any vehicle
that uses these IMUs. They show that this improves the performance of odometry,
especially in environments where visual information cannot be obtained.

24

Rouxel et al. want to compute the transformation of the head pose of a humanoid
after a walk cycle, which consists of two consecutive steps and trains two locally
weighted projection regression models [Rou+16]. The ﬁrst takes the last two steps,
which are calculated based on motor goals and a variable deﬁning what foot is
swapped. This approach can also be used for planning purposes, as no sensory
data has to be measured. The second model predicts based on the latest two steps
calculated by using sensor information from the IMU, foot pressure sensors, and
motor positions. It also takes the step duration of the steps as input in addition to
the binary variable because these steps are not periodic. Both models output the
foot displacement for the current step. They only used a translation on the x and
y axis and a rotation 𝜃 around the z-axis for input displacements and the output.
This shows improvements on carpet and artiﬁcial grass, on which the humanoid
is prone to slippage.

Looking at state-of-the-art legged odometry, we see many approaches for odome-
try regarding quadruped high-end robots that can infer their position from IMU
data  and  their  kinematics  model,  often  aided  through  supervised  learning  and
recurrent models. This is mostly used to estimate a velocity factor, which is then
accompanied by the usage of additional sensors to determine the ﬁnal robot pose.
This causes computational constraints as the velocity factor has to be assessed at
a relatively high frequency, and additional sensors pose high-dimensional data.
Additionally, there seems to be a gap in using data gained in simulation, which
poses fewer constraints on human and ﬁnancial resources, and transferring it to
the real world.

25

4 Approach

As described in Chapter 3, many state-of-the-art approaches use data from IMUs
or joint angles as input to train a neural network, which is used to calculate the
odometry of a robot. Similarly, our approach involves training a neural network
on input derived from such sensors. However, to save computational resources, we
predict a transformation from one foot to the other when a step is taken instead
of estimating a velocity directly, which has to be done at a high frequency.
Furthermore, we mainly collect data in simulation, enabling us to generate a large
dataset quickly and without concerns regarding damaged hardware. Nonetheless,
we also conduct real-world data collection for model training and subsequent eval-
uation purposes.

The speciﬁcs of our data generation setup are explained in Section 4.1. Following
that, Section 4.2 outlines our data processing pipeline. Afterwards, the train and
test procedure to determine the best-performing neural network is shown in Sec-
tion 4.3. Lastly, in Section 4.4, the integration into the existing software stack of
the Hamburg Bit-Bots is depicted.

4.1 Data Collection

Our data collection process aims to gather information on the robot’s movement
and sensory input to train a neural network. We conduct controlled walks at var-
ious velocities to achieve this, recording sensor data and ground truth measure-
ments. Speciﬁcally, we track the positions of the right and left soles, as well as the
base link, in a global coordinate system.
The robot can receive walk commands at time 𝑡, which are comprised of three
velocity components: Forward/backward movement (represented by the x-compo-
nent
̇𝑦𝑡), and rotation
around the z-axis (represented by the z-component
̇𝑤𝑡). To decide on the velocities
to use, diﬀerent sampling strategies are presented.
Our strategies for data collection diﬀer between simulated and real-world environ-
ments. Thus, we provide separate explanations for each of them.

̇𝑥𝑡), left/right movement (represented by the y-component

To cover the velocity space, we want to sample from the space of all feasible ve-
locities:

𝑉 = {( ̇𝑥𝑖,

̇𝑦𝑖,

̇𝑤𝑖)| 𝑖 ∈ {1, …, 𝑛}}

(22)

We also want the dataset to contain transitions of walking velocities and deﬁne
a delta:

26

Δ = {(𝛿 ̇𝑥𝑖

, 𝛿 ̇𝑦𝑖

, 𝛿 ̇𝑤𝑖

)| 𝑖 ∈ {1, …, 𝑛}}

Our sampling space is the image of the function:

𝑠 : 𝑉 × Δ → ℝ³ × ℝ³,

(( ̇𝑥𝑖,

̇𝑦𝑖,

̇𝑤𝑖), (𝛿 ̇𝑥𝑖

, 𝛿 ̇𝑦𝑖

, 𝛿 ̇𝑤𝑖

)) ↦ (( ̇𝑥𝑖,

̇𝑦𝑖,

̇𝑤𝑖), ( ̇𝑥𝑖 + 𝛿 ̇𝑥𝑖

,

̇𝑦𝑖 + 𝛿 ̇𝑦𝑖

,

̇𝑤𝑖 + 𝛿 ̇𝑤𝑖

))

(23)

(24)

4.1.1 Simulation

To generate data in simulation, we use the Webots simulator as described in Sec-
tion 2.6.1 and collect rosbags of the robot’s movement and sensor data.

First, we need to decide on a sampling strategy for simulation. It is easier to obtain
a well-balanced dataset in simulation than in the real world as we do not have to
worry about hardware breaking and are less limited by human resources.
The following sampling intervals are found empirically by testing the boundaries
of walkable combinations in Webots:

̇𝑥𝑖 ∈ [−0.4, 0.3],

̇𝑦𝑖 ∈ [−0.2, 0.2],

̇𝑤𝑖 ∈ [−0.8, 0.8]

(25)

The ﬁrst strategy is sampling the space in a grid. This means choosing 𝑛 points
that are equally spaced to one another in the range of the intervals in Equation 25.
Then, we combine each of them to obtain all possible combinations.
Thus, we get

𝑉grid = {(𝑥1, 𝑦1, 𝑤1), (𝑥2, 𝑦1, 𝑤1), …, (𝑥𝑛, 𝑦𝑛, 𝑤𝑛−1), (𝑥𝑛, 𝑦𝑛, 𝑤𝑛)}

(26)

We can sample a total of 𝑚 diﬀerent transitions for grid sampling.

Δgrid = {(𝛿 ̇𝑥𝑖

, 𝛿 ̇𝑦𝑖

, 𝛿 ̇𝑤𝑖

)| 𝑖 ∈ {1, …, 𝑚} ∧ 𝛿 ̇𝑥𝑖

⊕ 𝛿 ̇𝑦𝑖

⊕ 𝛿 ̇𝑤𝑖

≠ 0}

(27)

We put Δgrid and 𝑉grid into Equation 24 to obtain the sampling space.

The other sampling strategy is randomly sampling all feasible walking velocities
𝑛 times. Then, we combine them to obtain:

𝑉rand = {(𝑥1, 𝑦1, 𝑤1), (𝑥2, 𝑦2, 𝑤2), …, (𝑥𝑛, 𝑦𝑛, 𝑤𝑛)}

(28)

27

Then, each sample gets its own randomly generated transition, which is within 25
percent of the size of the interval of feasible velocities.
Although the ﬁrst strategy ensures that the whole space is covered at least punc-
tually,  we  chose  the  second  one  because  it  can  create  a  more  diverse  sampling
space. As we can collect enough samples in simulation of diﬀerent walking veloc-
ities, more advanced sampling strategies like Brownian motion are not used.

We simulated 10.000 runs, which take about seven days on a computer with an
Nvidia GeForce RTX 2080 Ti with 24 CPU cores. The robot’s model is the Wolf-
gang OP speciﬁed in a .proto ﬁle [Bes+21], which is generated from CAD ﬁles
that do not contain manufacturing tolerances or deformations and, thus, are po-
tentially inaccurate to some extent. The environment in which the robot walks is
the digital soccer ﬁeld seen in Figure 11.
The simulator runs in discrete time steps of which its step size is a tradeoﬀ be-
tween computational expense and accuracy. It is set to eight milliseconds.
We use the Webots Supervisor [Sup24] to obtain the position of the robot’s feet
and base link. This is used to compute the label for the samples of the dataset in
Section 4.2.
To collect the actual data, we record 14-second rosbags. To ensure obstacles like
the goalposts do not inﬂuence the robot, it is always reset to the side of the playing
ﬁeld after the recording is ﬁnished.

4.1.2 Real world

We  record  data  in  the  real  world  for  training  a  neural  network  because,  as  ex-
plained in Section 2.6, simulating the environment has disadvantages like overﬁt-
ting on the simulator. Additionally, we also use it to evaluate how well the odom-
etry using a neural network trained on data from simulation can perform in the
real world.

A motion capture system is used to record the robot’s position. Our setup con-
sists of Qualisys’ Miqus M3 cameras [Qua20] placed at diﬀerent points in a room,
as seen in Figure 12. The cameras have LED rings around them, which emit in-
frared light that is reﬂected well by small spheres. Using a program called Qualisys
Tracking Manager (QTM), we can calculate the positions of the spheres seen by
the cameras after they have been calibrated.

28

Figure 12: Motion capture set up with the robot and the artiﬁcial grass soccer ﬁeld. The cameras
are marked in magenta and the reﬂective spheres on the robot in orange. The cameras are placed
in the same way for both sides of the ﬁeld.

To capture the robots’ position, we record the location of the robots’ feet and head
by placing reﬂective spheres in unique constellations on them, which are deﬁned
as rigid bodies in QTM. We record the head instead of the base link because the
markers are more visible, and it is important that enough spheres can be detected.
If there is too much occlusion, the rigid bodies cannot be located, rendering the
recording useless.

Figure 13: Reﬂective spheres on the robot’s feet. The sphere constellations for the left and right
foot diﬀer so that their rigid body deﬁnitions can be distinguished.

As data collection in the real world is more diﬃcult with robot breakages and
limited time for recording, we do not have the option to record a plethora of data,
and thus, we need to be more selective of the velocity space we sample.
Looking at the navigation used by the Hamburg Bit-Bots [Bit24], which sends the
command velocities, we obtain diﬀerent sampling intervals:

̇𝑥𝑖 ∈ [−0.05, 0.1],

̇𝑦𝑖 ∈ [−0.04, 0.04],

̇𝑤𝑖 ∈ [−0.3, 0.3]

(29)

29

̇𝑥𝑖 and

We also see that the maximum linear velocity is 0.15 m/s in total, which we do
not want to overstep. We add an extra condition that caps the summed velocity
of
We ﬁrst sample the x velocity from the deﬁned space, which means for a randomly
̇𝑦𝑖 the following
̇𝑤𝑖 from the interval from Equation 29, we choose
chosen
way:

̇𝑥𝑖 and

̇𝑦𝑖.

̇𝑦𝑖 ∈ [−0.05 + ̇𝑥𝑖, 0.1] if 𝑥 ≥ 0
̇𝑦𝑖 ∈ [−0.05, 0.1 + ̇𝑥𝑖] else

(30)

The angular velocity is handled separately as we found it to be less destabilizing
and thus has no such constraint.
Similar to the simulated dataset, we want to include velocity changes. The path-
planning  transitions  smoothly  between  velocities,  and  we  want  to  emulate  this
by keeping 𝛿 relatively small. Additionally, walking on the artiﬁcial grass is less
stable than in simulation and we do not want the robot to fall and break. Thus
we choose a sample 𝛿 = (𝛿𝑥, 𝛿𝑦, 𝛿𝑤) randomly from the following spaces:

𝛿𝑥 ∈ [−0.025, 0.05], 𝛿𝑦 ∈ [0.02, 0.02], 𝛿𝑤 ∈ [−0.1, 0.1]

(31)

Over 40 minutes of walking are recorded.
To perform these measurements we let the robot presented in Section 2.2 walk
on a patch of artiﬁcial grass and record the information published by the robot’s
sensors in rosbags and the global pose by the motion capture system. After the
recording, the global pose of the deﬁned rigid bodies described by a rotation ma-
trix and a position vector can be calculated and exported as a .tsv by QTM.

We brieﬂy describe the workﬂow of recording the data in the real world:
1. A QTM recording and the sampling script are started.
2. The robot is placed on the ﬁeld where it is visible to the motion capture system

to avoid occlusions.

3. After pressing a button on the robot’s shoulder, the robot walks with two dif-

ferent velocities. After it ﬁnishes, we continue with 2.

Some peculiarities of recording the data in the real world are mentioned in the
following: First, we needed to make sure the time stamps of the ros messages and
the recorded poses align and thus synced the clocks of the robot’s and QTM’s
computer. To the best of our knowledge, the clocks had very similar times. Sec-
ond, the robot never fell, as one person always followed the robot to stabilize it
when it stumbled. These runs were noted down, but are still used for learning,
as the dataset is small. Third, we also encountered hardware issues. The robot’s
actuators  heated  up  during  the  recording,  and  the  3D-printed  parts  started  to

30

deform, which led to worse walking performance. This was counteracted by taking
breaks in between the recordings and letting them cool down. At the end of the
recording session, the robot had problems with the hip actuators, and thus the
quality of the data decreased.

Overall, we still think that the real-world data is valuable, as it can show how well
the simulation-based odometry generalizes to the real world.

4.2 Data Processing

Before training the neural network, we preprocess the data. This involves reading
information  from  the  .mcap  binary  ﬁle,  removing  invalid  data,  selecting  useful
input features, and aligning the data with step times to predict step size. Finally,
we implement the data in a format that can be used to train a neural network.

To remove invalid data, we check each for a fall detection. If a fall is detected, we
discard data after the fall as it contains no useful information regarding the step
size. In simulation, we detected 270 falls in 10,000 runs. Forty-ﬁve rosbags were
rendered useless due to the robot falling at the start.
We select input features based on sensors mentioned in Section 2.3 and Chapter
3. We extract IMU data and forward kinematics data of tf2 transformations from
rosbags. The transformation between the robot’s soles best represents the actual
step size as they are closest to the ground.
For simulated data, we extract ground truth pose from the simulation interface.
For real-world data, we use poses calculated by the motion capture system, ad-
justing the head frame to approximate the base link.

We organized the data in pandas data frames[Mo10], which are a tabular data
structure and enable fast data processing in Python. The Python subprocess li-
brary [Pyt24] was used to speed up the process of deserialization of data. In the
end,  the  data  frames  of  all  processes  are  combined  and  saved  as  .feather  ﬁles,
which enable fast reading and writing [Gut].
Reading out 10,000 rosbags from simulation takes approximately 58 minutes on
24 CPU cores, while real-world data processing time is negligible.

With  the  data  formatted,  we narrowed the  dataset  to  include  only  step  times,
which are deﬁned as the switch of the current support foot, which is assumed to
be the one closest to the ground, as shown in Figure 14.

31

Figure 14: The height of the soles taken from ground truth is plotted while the robot walked. A
right-to-left switch (Phase of −1) is shown as a blue dot, and a left-to-right switch (Phase of 1)
is shown as a red dot. When the support foot switches, indicating both feet brieﬂy made ground
contact, a step has been taken.

We merge tables and resample data based on the step changes, addressing invalid
data points through forward-ﬁlling interpolation. This ensures that the data at
each time stamp contains the latest information, which was available at that point
in time.
We deﬁne a phase for each step, which is saved based on whether the step was
one from left to right (1) or right to left (-1).

For each step, we calculate the transformation from the previous support foot to
the current one. Given the ground truth data containing transformations from the
world frame to each foot frame (𝑇WL and 𝑇WR), we derive the transformations
from right to left foot (𝑇LR) and left to right foot (𝑇RL) as follows:

𝑇LR = 𝑇WL⁻¹ ⋅ 𝑇WR  and 𝑇RL = 𝑇WR⁻¹ ⋅ 𝑇WL

(32)

Based  on  the  computed  phase,  we  retain  either  the  left-to-right  or  right-to-left
transformation and discard the other.

To simplify learning for the neural network, we convert rotation from quaternion
to  Euler  angles,  focusing  solely  on  the  yaw  component,  representing  rotation
around the z-axis for the transformation between soles for tf and the ground truth
[Zho+19].

The resulting data frame comprises input features and corresponding labels for
each row, saved to a feather ﬁle for use in the dataset outlined in Section 4.2.2.
We can see that the data correlates as shown in Figure 15.

32

Figure 15: The x part of the ground-truth transform’s translation from right to left sole and
the angular velocity on the y axis measured by the IMU insimulationare depicted. They are
normalized to make their correlation more visible. The data is taken from simulation.

The preprocessing parts also need to be done only once. For simulation, we cannot
process all of the 10.000 rosbags at once, as the data is too large to ﬁt into the
RAM. From now on, we only use a quarter of the values for the simulation train
dataset and another for the test dataset.

4.2.1 Normalization

Before  implementing  a  dataset  and  training  a  neural  network,  we  want  to  nor-
malize the data to improve training speed [Agg18]. We use z-score normalization,
which means for each input feature and label entry 𝑥 in the dataset, we calculate
the mean 𝜇 and the standard deviation 𝜎 and then use the normalized value 𝑧 to
pass into the neural network instead:

𝑧 =

𝑥 − 𝜇
𝜎

(33)

We  precompute  the  𝜇  and  𝜎  for  each  feature  and  label  and  save  them  for  the
normalization  of  the  train-  and  test  dataset.  The  same  values  are  also  used  in
Section 4.4 to normalize the data when calculating the odometry on the robot.

4.2.2 PyTorch Dataset

For easier integration with PyTorch, a dataset is implemented as this can be used
by a data loader, which batches and shuﬄes the data as explained in Section 2.4.
We  normalize  the  data  using  previously  computed  𝜎  and  𝜇  from  Section 4.2.1.
To accommodate recurrent neural networks, we introduce the option to consider
𝑁  subsequent features, grouping them into sequences using a sliding window ap-

33

proach.  Each  sample  from  the  original  data  can  be  part  of  up  to  𝑁   sequences.
To maintain context integrity, we avoid grouping data from diﬀerent rosbags, en-
suring sequences remain within the same walking context. The labels and input
features are presented in Table 1 and Table 2.

Label

x

y

Description

The translation in x-direction of the transformation between the feet.

The translation in y-direction of the transformation between the feet.

yaw

The rotation around the z-axis of the transformation between the feet.

Table 1: The labels contain the x, y, and yaw of a transformation between the robot’s feet from
either left to right or right to left.

Feature

Description

IMU’s angular velocity x

IMU’s angular velocity y

Angular velocity around the x-axis measured by the
IMU.

Same as above for y-axis, an example can be seen in
Figure 15.

IMU’s angular velocity z

Same as above for z-axis.

IMU’s linear acceleration x

IMU’s linear acceleration y

IMU’s linear acceleration z

IMU’s orientation x

IMU’s orientation y

IMU’s orientation z

IMU’s orientation w

Linear  acceleration  in  x-direction  measured  by  the
IMU.

Same as above for y-axis.

Same as above for z-axis.

The x component of a quaternion of the orientation
calculated from IMU data. A quaternion is a mathe-
matical concept used to represent rotations in three-
dimensional space.

Same as above for y.

Same as above for z.

Same as above for w.

tf2transformof left to right sole x

tf2 transfrom of left to right sole y

tf2 transfrom of left to right sole yaw

Translation inx-directionof the tf2 transform between
the left and right sole.

Translation in y-direction of the tf2 transform between
the left and right sole.

Rotation  around  the  z-axis  of  the  tf2  transform  be-
tween the left and right sole.

phase

The phase of the step, which is either −1 or 1.

Table 2: The 14 diﬀerent input features for training a neural network with short descriptions.
It is low dimensional compared to other problems like image recognition where neural networks
are also commonly used

34

4.3 Neural Networks

We aim to predict the odometry of a humanoid robot by integrating neural net-
work predictions of its step sizes. Our approach involves exploring diﬀerent archi-
tectures, searching their corresponding hyperparameter space, and presenting the
results of the best-performing network for this purpose.

4.3.1 Neural Network Architectures

We train various neural network architectures to determine their suitability for the
problem domain. We consider standard multi-layer perceptrons (MLP), recurrent
neural networks (RNN), and long short-term memory (LSTM) networks. MLPs
are expected to learn static errors present in the transformation data and poten-
tially obtain insights from IMU inputs. Recurrent architectures, stacked behind
MLP layers, should capture temporal dependencies between steps as well.
The variation of the other parameters might also have an unforeseen positive ef-
fect on how well the trained model can predict, and thus, we try diﬀerent options
presented in Table 3 to further investigate which conﬁguration of parameters from
this subset learns the labels best.

Parameter

Architecture

Optimizer

Loss Function

Values

MLP, RNN, LSTM

Adam, SGD

MSE, MAE

Acitvaton Function

ReLU, tanh, sigmoid

Learning Rate

Dropout

Epochs

Number of Hidden Layers

Layer Size

Recurrent Size (LSTM/RNN only)

Recurrent Depth (LSTM/RNN only)

[0.0001, 0.1]

[0.01, 0.15]

[10, 50]

[1, 5]

[4, 128]

[4, 64]

[1, 16]

Batch Size

[128, 512]

Table 3: The hyperparameters used for the neural network architectures of which many are de-
scribed in Section 2.4. The values presented in [⋅] are intervals.

PyTorch provides already implemented modules like recurrent layers to build a
neural  network,  but  the  activation  functions  and  optimizers  are  also  shown  in
Table 3.

35

In the training process, after creating a neural network and using the desired hy-
perparameters, we proceed as follows:
1. We split our data into training and test sets using an 80/20 random split. For
recurrent architectures, each sample consists of a sequence of ﬁve steps. The
number of sequences varies based on the dataset. Insimulationfor recurrent ar-
chitectures, we use 116,821 5-step sequences for the train dataset and 29,205 for
the test dataset. For MLPs, we use 120,301 and 41.325 samples, respectively.
For real-world data, we use 6994 5-step sequences for the train dataset and 1748
for the test dataset. For MLPs, we use 7174 and 1794 steps in each dataset.
2. We train the model to make predictions on input features and compute loss
compared to the label. We employ a learning rate reduction strategy to adjust
learning rates during training.

3. The model is then evaluated on the unseen test dataset to prevent overﬁtting.
4. Model weights and biases are periodically saved to a .pth ﬁle, and hyperpara-

meters are stored in a yaml ﬁle for future reference.

The training and evaluation process is visualized using wandb [Bie20].

To ﬁnd the best hyperparameter set, we use Optuna [Aki+19], which is a parame-
ter optimization framework which can minimize an objective function. For that,
a so-called study is created, which consists of running several trials in which we
sample from the parameter set, which in our case is shown in Table 3. Optuna
does  not  have  to  sample  randomly  but  can  apply  more  eﬀective  strategies  like
the Tree-structured Parzen Estimator [Oza+22], which we used. Our results are
summarized in Table 4 in Section 5.2.

4.4 Integration

For the neural network that predicts the step sizes to be used in the RoboCup
competition, it has to be integrated into the existing software stack of the Ham-
burg Bit-Bots. It can be used to compute a naive localization, which can function
as the base for the particle ﬁlter in the RoboCup competition.
For that, we orient ourselves on the approach presented in Section 2.3 and call
it Model Odometry. We implement a ROS node that takes the IMU data, the tf2
transformations from the robot’s joints, and a walk support state as input and
publishes a transformation from the origin to the base link.
A key challenge is accurate step detection, which is detailed in Section 4.4.1.

Upon starting the node, the speciﬁed model and its parameters containing archi-
tecture, as well as the normalization factors for input and output, are loaded.
A priority queue-like data structure is deﬁned, which can return the closest mes-

36

sage to a time stamp given as a parameter and delete all older messages. We create
subscribers for all the topics that publish the data we use as input to the model,
as  seen  in  Figure 16.  This  way,  we  can  keep  track  of  the  current  support  foot
and the IMU data at the time of the step. We also create a tf-listener to get the
transformations between the left and right foot on a given time stamp.

Figure 16: The model odometry takes input from the foot pressure state detector, IMU and the
kinematics from TF2. The ﬁrst two have callback functions in which we append the messages to
the priority queue.  It broadcasts a transformation from origin to base link on TF2 and publishes
onto a topic that might be subscribed by components like localization.

When a step is detected, for which two approaches are presented in Section 4.4.1,
the model predicts the step size and orientation. This is then used to update the
transformation from the origin to the current support foot similar to Equation 6.
The odometry should publish the transformation from the origin to the base link
as in Equation 7. We approximate the transformation from the current support
foot to the base link by using the tf2. For the locations of the links, refer to Fig-
ure 5.

4.4.1 Foot Pressure Step Detection

The  model  odometry  depends  on  detecting  steps  accurately.  The  current  node
publishing the walk support state is not reliable due to its lack of sensory data
integration, as evident in Figure 17.

37

Figure 17: The walk support state and the height of the soles from Webots are visualized. We
see the support state depicted in red alternating between the diﬀerent states: right (0), left (1),
and double support (2). The height of the left and right soles are depicted in blue and orange,
respectively. It is plausible that the double support phase only happens for a short amount of
time, but we see that it does not correlate with when both feet are on the ground (having a
low height).

To address this, step detection based on foot pressure measurements is proposed.
Each of the four cleats per foot publishes how much load they detect.
In Figure 18, we see that the summed pressure detected by the cleats of one foot
is very high when the foot rises.

38

Figure 18: The cleats of the right foot are all depicted in brown and the cleats of the left foot
in a dark blue. The height of the left foot is shown in blue, and the right foot in orange.  For
the time stamp 400, we see the right cleats detect high values as the left foot starts rising. On
the other hand, when the cleats detect a very low load, we know that the other foot is currently
in ground contact. If we can detect these maxima of pressure, we can reliably detect the double
support phase and the switches. Data is taken from simulation.

Unfortunately, raw values from cleats diﬀer in the real world, requiring calibration
to ensure consistency.  This calibration measures load absence and predeﬁned load
conditions to establish oﬀsets and factors for ﬁltering foot pressure.
A simple approach to detect the maxima is to sum the outputs of the cleats of
each foot and threshold them. Before doing so, a low-pass ﬁlter, which keeps low-
frequency components like the overall pressure detected when the foot is in ground
contact but attenuates high frequencies like measurement noise, is applied.
However, determining an appropriate threshold for step detection proves challeng-
ing due to pressure variation with robot movement, especially in real-world sce-
narios.

An alternative approach is to use the information that the local minima of the
pressure  of  one  foot  coincides  with  the  ground  contact  of  the  other  foot.  We
calculate  the  derivatives  and  identify  the  roots  of  the  low-pass  ﬁltered  sum  of
the cleats, which we assume to be a support foot switch. Though susceptible to
noise, this approach oﬀers improved accuracy compared to the original method,
as demonstrated in Figure 19. We do not detect a double support phase anymore
but implicitly assume them to be in between foot swap times.

39

Figure 19: The walk support state is depicted in green. The right foot height in orange and the
left foot height in blue. We see that the switch of phase happens when both feet are on the
ground as at time 200. Sometimes it is a bit too early or late, as around time 400.

The  foot  pressure  walk  support  state  detector  is  implemented  in  C++  and
launched with the bitbots motion.
We did not use this approach for label generation but to fully integrate the model
odometry into the existing software stack.

40

5 Evaluation

In this Chapter, we want to evaluate the approach presented in Chapter 4. Firstly,
we introduce two existing implementations of odometry utilized by the Hamburg
Bit-Bots  in  the  RoboCup  domain,  detailing  their  underlying  models.  Then,  we
describe  the  experiments  conducted  to  assess  the  performance  of  our  approach
compared to these baselines.  Finally, we present and discuss the results obtained
from these experiments.

5.1 Baseline

We compare our odometry with two existing approaches used by the Hamburg
Bit-Bots in the RoboCup Humanoid Soccer League. The two methods of odom-
etry  follow  the  same  principle  as  laid  out  in  Section 2.3  with  Equation 6  and
Equation 7.

The Walk Engine Odometry is calculated based on splines generated by the walk
engine [BZ22]. To do so, it assumes the commanded end-eﬀector poses for the feet
to be reached at the time the step transitions are calculated in its internal model.
The odometry itself is computed by the walk node, which handles the components
needed for walking. It obtains the position of the support foot from the walk en-
gine, which keeps track of the transformation from an origin for both feet. After
every step, a calculated oﬀset is added to the foot that took the step which rep-
resents Equation 6.
The robot’s trunk functions as the base link. The support-foot-to-trunk transfor-
mation  is  also  speciﬁed  by  the  walk  node’s  internal  model.  Then,  odometry  to
base is computed as in Equation 7.
This odometry method does not use external measurements but only relies on the
calculated splines for walking. It does not consider diﬀerent step lengths or wig-
gling caused by the environment. The ground contact time is also not measured
but computed and thus less accurate, but it ﬁts this odometry from the timing.

The Motion Odometry is based on joint encoder measurements and IMU data at
step transitions calculated by the walk engine.  It uses transformations from sole
to sole and from sole to base link obtained from the tf2 buﬀer.  An odometry fuser
node adjusts for tilting by calculating transformations from IMU measurements,
aﬀecting step lengths.  At the node’s initialization, the transformation from the
origin to the support foot is set to the identity matrix and iteratively updated
after  each  step,  like  in  Equation 6.  It  continuously  updates  and  publishes  the
transformation from origin to base link, as in Equation 7.
 Despite similarities in step detection mechanism, simulation reveals issues with

41

this approach, as evident in Figure 20. However, both methods prove usable in
real-world scenarios.

Figure 20: The walk engine and motion odometry plotted against the ground truth from simu-
lation data. The base link of the walk engine odometry and the ground truth show sinusoidal
movement due to the robot’s walking pattern. The motion odometry performs very badly as
the double support phases are detected without regard to the actual step taken, as described in
Section 4.4.1. However, it works for model-based walk engine odometry.

5.2 Hyperparameters

In Section 4.3, we optimized various architectures and hyperparameters to develop
a neural network capable of accurately predicting step sizes.  Now, we present the
best-performing architecture and hyperparameters for the neural network trained
on simulation data with the one trained on real-world data and compare the two.

42

Parameter

Architecture

Optimizer

Loss Function

Acitvaton Function

Learning Rate

Dropout

Number of Hidden Layers

Layer Size

Recurrent Size (LSTM/RNN only)

Recurrent Depth (LSTM/RNN only)

Epochs

Batch Size

SimNet RealWorldNet

LSTM

Adam

MAE

relu

0.007

0.0688

1

87

52

3

81

512

LSTM

Adam

MSE

tanh

0.0261

0.1224

1

125

63

2

85

497

Table 4: The table displays the best-performing sets of hyperparameters after 1000 trials. SimNet
is trained on simulation data, and RealWorldNet is trained on real-world data. These parameters
will be used for experiments in Section 5.3

As shown in Table 4, both the best-performing networks are LSTMs, indicating
the importance of considering information from previous steps in predicting step
sizes.  Interestingly, they have similar numbers of epochs and batch sizes, possibly
due to the LSTM’s requirement for suﬃcient samples to adjust weights and biases
eﬀectively. On the other hand, this might not be the case as the real-world data
was trained on a much smaller dataset and has a higher learning rate, which we
will further discuss in the following.
The real-world network has a learning rate that is almost four times as high as the
one of the simulation net. This might be due to the real-world dataset containing
fewer samples and thus needing a higher learning rate to update its weights and
biases. The dropout is also twice as high for the real-world net, which might be
due to the real-world data being more noisy, and thus, the network can rely less
on single input features.

Both neural networks feature a single fully connected linear layer preceding the
LSTM layers, possibly indicating a nearly linear relationship between step sizes
and input features. This alignment is supported by the similarity between tf trans-
formations of soles and ground truth, as depicted in Figure 21.

43

Figure 21: The plot illustrates values of the transform between soles according to tf and computed
from simulation data. The red line represents the ground truth transform, ideally alternating
between the right-to-left and left-to-right transform. While some deviation exists, particularly
visible in the x-component, the overall similarity is evident.

The similarity in recurrent size and depth, as well as batch size and number of
epochs, suggests comparable complexities in the models.  However, diﬀerences in
loss and activation functions may stem from variations in the datasets, but we
cannot be sure of this.
Interestingly, the higher layer size and recurrent size in the real-world network may
reﬂect the noisier nature of the real-world data, necessitating a greater number of
neurons to eﬀectively learn labels.

As LSTM models show the most promising results, the importance of previous
steps  in  both  simulation  and  real-world  scenarios  is  shown.  Despite  the  model
trained on real-world data showing signs to account for more noisy input data,
there is still a similarity in the architecture of the best-performing networks espe-
cially regarding the linear layers. This shows potential for a successful simulation-
to-real transfer

5.3 Experiments

We want to assess the performance of the model odometry and the approaches
presented in Section 5.1 relative to the ground truth over a speciﬁc timeframe. We

44

measure odometry drift over 5 seconds of walking, focusing on this short duration
due  to  the  disproportionate  impact  of  incorrect  rotations  on  overall  estimation
accuracy.
To evaluate our approach, referred to as Model Odometry, we select the best-per-
forming neural networks based on Section 4.3.1 and test it on walk trajectories,
which were not used in the Optuna optimization process.
We test RealWorldNet shown in Table 4 on real-world data and SimNet on both
simulation and real-world data, as it is interesting to assess generalization to real-
world scenarios.

We  input  the  unseen  prerecorded  data  into  the  neural  network  for  predictions
to obtain the model odometry estimate of the robot’s pose after each step.  We
iteratively apply the transformation in Equation 6, resetting it at the start of each
new run. To ensure a continuous transformation from an origin to the base link,
we use the tf2 transformations from support sole to base to interpolate, similar to
Section 4.4 and Equation 7.
Afterward, we load the Motion and Walk Engine Odometry and the ground truth,
which  all  have  ﬁtting  time  stamps  and  bag  numbers  after  the  preprocessing  in
Section 4.2 and merge them.
We apply a sliding window with a 5-second size over the data, excluding sequences
that involve a bag change.  To ensure comparability, we align the pose estimations
to start at the same position and angle.  We then calculate the mean absolute
deviation from x, y, yaw, and the Euclidean distance between each odometry es-
timate  and  the  ground  truth  of  the  last  pose  of  the  sequence.   This  approach
mitigates the inﬂuence of base link oscillations during the walk sequence on the
results.

5.4 Results

We  present  the  experiment  results  by  assessing  the  total  deviation  relative  to
ground truth after 5 seconds of walking.  Additionally, we showcase example tra-
jectories  and  illustrate  the  distribution  of  deviation.   Further  analysis  includes
examining the median, spread of deviation, and identiﬁcation of outliers.

5.4.1 SimNet on Simulation Data

First,  we  assess  the  Model  Odometry  using  the  SimNet  on  simulation  data.  A
total of 15643 5-second sequences were utilized for evaluation purposes. The re-
sults of this evaluation are presented in the Table 5. There, we see that the model
odometry outperforms both existing approaches. Speciﬁcally, the total deviation

45

in comparison to the walk engine odometry is reduced by over 80%, and compared
to the motion odometry, it’s decreased by almost 90%. Our approach exhibits only
a 5-centimeter drift after 5 seconds, whereas the walk engine odometry displays
a drift of over 27 centimeters. However, the motion odometry performs poorly in
simulation  due  to  discrepancies  in  the  walk  support  phase  and  the  actual  step
taken, as mentioned in Section 5.1 and Section 4.4.1, and is thus not a good com-
parison.

SimNet on sim data

Motion
Odometry

Walk Engine
Odometry

Model
Odometry

total deviation in m after 5sec

x deviation in m after 5sec

y deviation in m after 5sec

yaw deviation in rad after 5sec

0.4887

0.3428

0.2789

1.1851

0.2761

0.1794

0.1716

1.3609

0.0506

0.0308

0.0334

0.125

Table 5: Performance of the model odometry using the SimNet on simulated data in comparison
to the motion and walk engine odometry on unseen walk trajectories. The error is rounded to
four decimal places. The best values are marked bold.

Example trajectories are illustrated in Figure 22 and Figure 24. The walk engine
odometry tends to overestimate, possibly due to not considering current sensor
measurements and external factors like friction. In contrast, our model odometry
accurately predicts step lengths, resulting in closer proximity to the ground truth.

Figure 22: The diﬀerent odometry approaches plotted against the ground truth. One box is 0.1
time 0.1 meters. The network used is SimNet, and it is evaluated on simulation data.

46

Figure 23: Quiver plot of the odometries compared with the ground truth. The model used is
the SimNet. Here, we can see that the walk engine odometry aligns quite well with the ground
truth. For the last pose, they happen to be orientated in diﬀerent directions.

Very noticeable in Table 5 is the big diﬀerence in the rotational yaw component.
The motion and walk engine odometry diﬀer over one radiant from the ground
truth, which is almost 60 degrees. Despite this, the walk engine odometry tends
to be oriented correctly during walk sequences, as observed in Figure 22 and Fig-
ure 24. This discrepancy in the yaw component may stem from variations in base
link deﬁnitions or step transition timings.
Figure 23  highlights  discrepancies  in  the  last  pose  orientation,  indicating  that
yaw might not be the most reliable metric for assessing odometry performance in
simulation. Therefore, we focus on the Euclidean distance to the ground truth in
subsequent analyses.

47

Figure 24: Walk trajectories of the diﬀerent odometry approaches on simulation data using the
SimNet.

Figure 25  presents  the  distribution  of  the  distance  to  the  ground  truth  after  5
seconds of walking. The model odometry exhibits a deviation of less than 10 cen-
timeters in nearly all cases, with a median of around 5 centimeters. In contrast,
the walk engine odometry has a median deviation of around 28 centimeters and
shows more variability. The motion odometry tends to estimate the robot to stay
close to the origin, which is often inaccurate.

Figure 25: Histogram of the frequency of Euclidean distance to the ground truth from the dif-
ferent odometry approaches. The model used is the SimNet, and the data tested on is from
simulation.

48

In Figure 26, the same data is depicted as a boxplot. For the model odometry, we
see that there are indeed many outliers, but almost all values still lie in the normal
estimation range of the walk engine odometry. The model odometry has a narrow
interquartile range, and the median is close to the ground truth. This is a desirable
property as it shows that the model odometry is reliable in its estimation.

Figure 26: Boxplots of the diﬀerent odometry approaches. The model used is the SimNet and
the data evaluated on is from simulation.

In conclusion, employing a neural network to compute odometry based on pre-
dicted step sizes appears to be eﬀective for simulation scenarios. The model odom-
etry shows better performance than the existing approaches, which means more
reliability and accuracy in estimation. In the context of the RoboCup Humanoid
League Virtual Season, using the model odometry might improve the overall play-
ing of the robots.

5.4.2 RealWorldNet on Real-World Data

Now, the performance of Real WorldNet on real-world data is shown. We again
present  the  deviations  of  ﬁve-second  sequences  in  Table 6,  for  which  the  Real-
WorldNet  was  tested  on  775  5-second  sequences  of  unseen  data  from  the  real
world. The relatively small size of this unseen data must be considered, potentially
limiting the representativeness of the results. While the total duration of these
sequences exceeds 64 minutes, it’s important to note that they were created using
a sliding window approach, which means one second might appear in up to ﬁve
diﬀerent sequences. The unique sequences amount to roughly 13 minutes.

49

The model odometry still outperforms the other two approaches in terms of total
deviation, although not as signiﬁcantly as in simulation. It shows an increase in
accuracy on the total deviation of almost 21% and 14.8% compared to the motion
odometry and the walk engine odometry, respectively.

RealNet on real data

Motion
Odometry

Walk Engine
Odometry

Model
Odometry

total deviation in m after 5sec

x deviation in m after 5sec

y deviation in m after 5sec

yaw deviation in rad after 5sec

0.2269

0.16

0.1258

0.29

0.2107

0.1328

0.1321

0.4961

0.1795

0.097

0.1285

0.287

Table 6: Performance of the model odometry using the RealWorldNet on real-world data in
comparison to the motion and walk engine odometry on unseen walk trajectories. The error is
rounded to four decimal places. The best values are marked in bold.

Both baseline approaches perform better in the real world compared to simulation,
which could be attributed to the software initially being developed for the actual
robot rather than for simulation purposes. Particularly, the motion odometry per-
forms notably better than in simulation, likely because the estimation of the walk
support phase aligns more closely with actual steps in the real world.

Figure 27 shows an example trajectory in which the model odometry ends close
to the ground truth, although the path the base link walks along is less ﬁtting
than, for example, the motion odometry. This is probably due to the way we ap-
proximate transformation from sole to base link as described in Section 5.3. The
current position is still based on the summation of the steps. We approximated
the actual position of the base link in the ground truth data by the position of the
head and then transformed it downwards, as mentioned Section 4.2. This might
also be why the head is oscillating more than the actual base link would and might
lead to the big oscillations.

50

Figure 27: Walk trajectories using the RealWorldNet on real-world data in comparison to the
motion and walk engine odometry on unseen data. We see that all odometry approaches can
perform well on the left. Maybe due to slippages on the grass, the baselines overestimate, as seen
on the right.

Again, we visualize the distribution of deviation in Figure 28. The model odome-
try still performs best but is less accurate than in simulation, as seen in Figure 25.
This is probably at least partially due to the small dataset. The motion and walk
engine odometry perform similarly to each other. They have very small deviations
from the ground truth than the model odometry, but they also have more inaccu-
rate estimations.

Figure 28: Histogram of the frequency of Euclidean distance to the ground from the odometry
approaches in the real world. The model used is the RealWorldNet.

51

Looking at Figure 29, the model odometry’s median is closer to the ground truth
than the other two, with a slightly narrower interquartile range, indicating slightly
better reliability. However, all odometry approaches exhibit some outliers.

Figure 29: Boxplots of the diﬀerent odometry approaches in the real world. The model used is
the RealWorldNet.

In  summary,  despite  being  trained  on  a  small  dataset,  the  model  odometry  re-
mains the best-performing approach in the real world, oﬀering improved accuracy
and  reliability  compared  to  the  other  two  approaches,  even  though  the  motion
odometry performs better in real-world conditions than in simulation.

5.4.3 SimNet on Real-World Data

In the following, we assess the performance of the model odometry using the Sim-
Net on real-world data. This analysis is interesting as it provides insights into the
model’s transfer from simulation to the real world.
As all the data generated in the real world is unseen to this model, we have more
samples we can evaluate and thus use 3235 5-second sequences in this comparison.
Observations from Table 7 mirror those from Table 6, highlighting that despite the
real-world setting, the model odometry performs best in total deviation compared
to both motion and walk engine odometry. Notably, the model odometry shows an
improvement of at least 12% compared to the motion odometry and 3% compared
to the walk engine odometry.

52

SimNet on real data

Motion
Odometry

Walk Engine
Odometry

Model
Odometry

total deviation in m after 5sec

x deviation in m after 5sec

y deviation in m after 5sec

yaw deviation in rad after 5sec

0.2041

0.1433

0.1144

0.3067

0.1849

0.1214

0.1142

0.4921

0.1794

0.1276

0.0989

0.3427

Table 7: Performance of the model odometry using the SimNet in comparison to the motion and
walk engine odometry on unseen walk trajectories in the real world. The error is rounded to four
decimal places. The best values are marked in bold.

Additionally, Table 8 showcases the comparison between the dataset used in Sec-
tion 5.4.2 and the network trained on real-world data. The model odometry em-
ploying the RealWorldNet outperforms its counterpart trained on simulation data.
This diﬀerence likely stems from the RealWorldNet being trained on a more rep-
resentative dataset. The sensor measurements collected in simulation might not
align with the actual sensors. Additionally, as noted in Section 4.1, potential hard-
ware malfunctions in the robot toward the end of data collection could further
amplify the disparities between simulation and real-world performance.

SimNet and RealWorldNet
on real data

Motion
Odometry

Walk
Engine
Odometry

[SimNet]
Odometry

[RealWorld-
Net]
Odometry

total deviation in m after 5sec

x deviation in m after 5sec

y deviation in m after 5sec

yaw deviation in rad after 5sec

0.2269

0.16

0.1258

0.29

0.2107

0.1328

0.1321

0.4961

0.2062

0.1369

0.1221

0.4524

0.1795

0.097

0.1285

0.287

Table 8: Performance of the model odometry using the SimNet and RealWorldNet on real-world
data. The error is rounded to four decimal places. The best values are marked in bold.

The histogram in Figure 30 and the boxplot in Figure 31 look similar to Figure 28
and Figure 29 respectively with regards to the relation of estimation diﬀerences
between the diﬀerent odometry approaches. We do notice the trends from Table 7
in less overall accuracy for the model odometry compared to simulation, probably
due to sensor measurement values not aligning.

53

Figure 30: Histogram of the frequency of Euclidean distance to the ground from the odometry
approaches in the real world. The model used is the SimNet.

Figure 31 illustrates that while the distribution remains similar, the model odom-
etry’s  interquartile  range  is  larger,  and  the  median  is  further  from  the  ground
truth, indicating reduced accuracy and reliability compared to simulation and the
RealWorldNet.

Figure 31: Boxplots of the diﬀerent odometry approaches tested on real-world data. The model
used is the SimNet.

Figure 32 illustrates instances where the model odometry estimates reasonably
well, while other approaches, the walk engine odometry in this case, perform worse.

54

Figure 32: Trajectory of the three odometry approaches compared to the ground truth on real-
world data. The SimNet is used.

In the real world, the model odometry using the SimNet is still the best-performing
odometry approach, but only marginally. This indicates the feasibility of trans-
ferring insights from simulation-trained models to real-world scenarios. However,
further research has to be conducted to fully leverage the possibilities depicted in
Section 5.4.1, where the model odometry reaches very accurate results.

55

6 Conclusion

In  this  thesis,  we  proposed  a  lightweight  odometry  based  on  a  neural  network
called model odometry, which uses proprioceptive sensor data to predict step sizes
and orientations, which are then integrated to obtain the robot’s pose.
For  that,  we  ﬁrst  generated  simulation  and  the  real  world  data  and  processed
them ﬁtting our needs. Afterwards, we performed optimization to ﬁnd the best
conﬁguration of hyperparameters for a neural network based on our problem. We
integrated  the  neural  network  into  the  existing  software  stack  of  the  Hamburg
Bit-Bots and proposed a new step-detection mechanism based on foot pressure
measurements to make the odometry reliable.
Finally, we evaluated our approach on 5-second walking sequences with two ap-
proaches  currently  used  by  the  Hamburg  Bit-Bots.  We  demonstrated  that  the
model odometry can be trained on simulation data, transferred to the real world
without adjustment, and still outperform existing methods. For a RoboCup Hu-
manoid Soccer match, the model odometry could be used to improve the robots’
playing as it enables better positioning.
Notably, the model odometry demonstrates high accuracy when utilized in sim-
ulation  scenarios,  making  it  feasible  to  use  in  the  RoboCup  Humanoid  Soccer
League Virtual Season.

There are several directions for future work.
First, many approaches, as seen in Chapter 3, calculate velocity factors to estimate
directional  velocity  but  are  typically  designed  for  quadruped  robots.  Adapting
such an approach to a biped robot and evaluating the computational expense and
performance could be a viable next step.
Second, we chose the input features for the network based on what seemed rea-
sonable to us. The next step involves conducting an ablation study to identify the
most inﬂuential features for network performance.
Third, as we only used IMU data from one point in time in the input vector for
our neural network, we should try to incorporate data over larger time frames to
estimate slippages better.
Furthermore, as the real-world performance of the walk engine and motion odom-
etry  was  good,  we  could  use  their  estimate  as  input  for  the  neural  network  to
improve the model odometry. Even for simulation, the walk engine odometry over-
scaled the data but usually estimated decently.
Moreover,  we  also  showed  that  the  network  trained  on  data  in  simulation  also
makes good estimations in the real world but lacks in comparison to its perfor-
mance in simulation. It could be tried to pre-train a model on data from simulation
and then slightly adjust the weights by training on data from the real world with
a low learning rate. Another possibility would be to adjust the model odometry’s

56

parameters online.
Lastly, to get a stable odometry on the real robot, the model odometry, together
with the footstep detection, should be tested thoroughly as it highly depends on
how well steps are detected.

57

Bibliography

[HD99]

S. Huang and G. Dissanayake, “Robot localization: An introduction,”
Wiley Encyclopedia of Electrical and Electronics Engineering, pp. 1–
10, 1999.

[Bit24]

“Bit-Bots  Website.”  Available:  https://bit-bots.de/en/.  [Accessed:
Apr. 25, 2024]

[SK16]

B. Siciliano and O. Khatib, Robotics and the Handbook. Springer, 2016.

[Del+99] F. Dellaert, D. Fox, W. Burgard, and S. Thrun, “Monte carlo localiza-
tion for mobile robots,” in Proceedings 1999 IEEE international con-
ference  on  robotics  and  automation  (Cat.  No.  99CH36288C),    1999,
pp. 1322–1328.

[Thr+01] S. Thrun, D. Fox, W. Burgard, and F. Dellaert, “Robust Monte Carlo
localization for mobile robots,” Artiﬁcial intelligence, vol. 128, no. 1–
2, pp. 99–141, 2001.

[Fed24]

[Fed23]

R. Federation, “A Brief History of RoboCup,” 2024. Available: https://
www.robocup.org/a_brief_history_of_robocup.  [Accessed:  Jan.  18,
2024]

R.  Federation,  “RoboCup  Humanoid  League  2023  Rules,”
2023.  Available:  http://humanoid.robocup.org/wp-content/uploads/
RC-HL-2023-Rules.pdf. [Accessed: Jan. 18, 2024]

[Bes+21] M. Bestmann, J. Güldenstein, F. Vahl, and J. Zhang, “Wolfgang-op:
a robust humanoid robot platform for research and competitions,” in
2020 IEEE-RAS 20th International Conference on Humanoid Robots
(Humanoids),  2021, pp. 90–97.

[MX-24]

“MX-64  DYNAMIXEL.”  Available:  https://emanual.robotis.com/
docs/en/dxl/mx/mx-64/. [Accessed: Feb. 24, 2024]

[BM18]

[LP17]

M.  Ben-Ari  and  F.  Mondada,  “Robotic  motion  and  odometry,”
Springer, 2018, pp. 63–93.

K. M. Lynch and F. C. Park, Modern robotics. Cambridge University
Press, 2017.

[Ble+18] G.  Bledt,  M.  J.  Powell,  B.  Katz,  J.  Di  Carlo,  P.  M.  Wensing,  and
S.  Kim,  “Mit  cheetah  3:  Design  and  control  of  a  robust,  dynamic
quadruped  robot,”  in  2018  IEEE/RSJ  International  Conference  on
Intelligent Robots and Systems (IROS),  2018, pp. 2245–2252.

58

[Blo+15] M.  Bloesch,  S.  Omari,  M.  Hutter,  and  R.  Siegwart,  “Robust  visual
inertial odometry using a direct EKF-based approach,” in 2015 IEEE/
RSJ international conference on intelligent robots and systems (IROS),
2015, pp. 298–304.

[Cam+20] M. Camurri, M. Ramezani, S. Nobili, and M. Fallon, “Pronto: A multi-
sensor state estimator for legged robots in real-world scenarios,” Fron-
tiers in Robotics and AI, vol. 7, p. 68–69, 2020.

[Har+18] R. Hartley, M. G. Jadidi, J. W. Grizzle, and R. M. Eustice, “Contact-
aided invariant extended Kalman ﬁltering for legged robot state esti-
mation,” arXiv preprint arXiv:1805.10410, 2018.

[Yan+23] S. Yang, Z. Zhang, B. Bokser, and Z. Manchester, “Multi-IMU Pro-
prioceptive Odometry for Legged Robots,” in 2023 IEEE/RSJ Inter-
national Conference on Intelligent Robots and Systems (IROS),  2023,
pp. 774–779.

[Aqe+16] M. O. Aqel, M. H. Marhaban, M. I. Saripan, and N. B. Ismail, “Review
of visual odometry: types, approaches, challenges, and applications,”
SpringerPlus, vol. 5, pp. 1–26, 2016.

[WCF22] D. Wisth, M. Camurri, and M. Fallon, “VILENS: Visual, inertial, lidar,
and leg odometry for all-terrain legged robots,” IEEE Transactions on
Robotics, vol. 39, no. 1, pp. 309–326, 2022.

[Pla23]

M.  Plaue,  Data  Science:  An  Introduction  to  Statistics  and  Machine
Learning. Springer Nature, 2023.

[Agg18]

C. C. Aggarwal, “Neural networks and deep learning.” Springer, 2018.

[KB14]

[HS97]

[Lon24]

D. P. Kingma and J. Ba, “Adam: A method for stochastic optimiza-
tion,” arXiv preprint arXiv:1412.6980, 2014.

S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
computation, vol. 9, no. 8, pp. 1735–1780, 1997.

“Long short-term memory.” Available: https://en.wikipedia.org/wiki/
Long_short-term_memory. [Accessed: May 01, 2024]

[Pas+19] A. Paszke et al., “Pytorch: An imperative style, high-performance deep

learning library,” vol. 32. 2019.

[Mac+22] S.  Macenski,  T.  Foote,  B.  Gerkey,  C.  Lalancette,  and  W.  Woodall,
“Robot Operating System 2: Design, architecture, and uses in the wild.
Science  Robotics  7,  66  (2022),  eabm6074,”  Jin  Seob  Kim  (Member,
IEEE) received ysis, 2022.

59

[Dis24]

“Distributions  ROS.”  Available:  http://wiki.ros.org/Distributions,.
[Accessed: Jan. 18, 2024]

[ROS24]

“ROS  Rolling  Release  Documentation.”  Available:  https://docs.ros.
org/en/rolling/Releases.html. [Accessed: Jan. 18, 2024]

[Fac24]

[RVi]

[ROS24]

D.  Faconti,  “PlotJuggler,”  2024.  Available:  https://github.com/
facontidavide/PlotJuggler.git. [Accessed: Feb. 04, 2024]

“RViz:  3D  Visualization  Tool  for  ROS  2.”  Available:  https://github.
com/ros2/rviz

“ROS 2 Foxy Fitzroy - RQt Overview.” Available: https://docs.ros.org/
en/foxy/Concepts/About-RQt.html#overview.  [Accessed:  Jan.  18,
2024]

[Web24] Webots, “Open-source Mobile Robot Simulation Software.” Available:
http://www.cyberbotics.com/. [Accessed: Jan. 15, 2024]

[Sup24]

“Supervisor  Node  Webots.”  Available:
https://cyberbotics.
com/doc/reference/supervisor#wb_supervisor_node_get_root.  [Ac-
cessed: Feb. 23, 2024]

[Dru+10] E. Drumwright, J. Hsu, N. Koenig, and D. Shell, “Extending open dy-
namics engine for robotics simulation,” in Simulation, Modeling, and
Programming  for  Autonomous  Robots:  Second  International  Confer-
ence,  SIMPAR  2010,  Darmstadt,  Germany,  November  15-18,  2010.
Proceedings 2,  2010, pp. 38–50.

[WBo95] G.  Welch,  G.  Bishop,  and  others,  “An  introduction  to  the  Kalman

ﬁlter,” 1995.

[JU97]

S. J. Julier and J. K. Uhlmann, “New extension of the Kalman ﬁlter
to nonlinear systems,” in Signal processing, sensor fusion, and target
recognition VI,  1997, pp. 182–193.

[Blo+13] M. Bloesch et al., “State estimation for legged robots-consistent fusion

of leg kinematics and IMU,” Robotics, vol. 17, pp. 17–24, 2013.

[Rot+14] N. Rotella, M. Bloesch, L. Righetti, and S. Schaal, “State estimation
for a humanoid robot,” in 2014 IEEE/RSJ International Conference
on Intelligent Robots and Systems,  2014, pp. 952–958.

[WCF20] D. Wisth, M. Camurri, and M. Fallon, “Preintegrated velocity bias es-
timation to overcome contact nonlinearities in legged robot odometry,”
in 2020 IEEE International Conference on Robotics and Automation
(ICRA),  2020, pp. 392–398.

60

[Wan+17] S. Wang, R. Clark, H. Wen, and N. Trigoni, “Deepvo: Towards end-
to-end visual odometry with deep recurrent convolutional neural net-
works,”  in  2017  IEEE  international  conference  on  robotics  and  au-
tomation (ICRA),  2017, pp. 2043–2050.

[Che+18] C. Chen, X. Lu, A. Markham, and N. Trigoni, “Ionet: Learning to cure
the curse of drift in inertial odometry,” in Proceedings of the AAAI
Conference on Artiﬁcial Intelligence,  2018.

[Liu+20] W. Liu et al., “Tlio: Tight learned inertial odometry,” IEEE Robotics
and Automation Letters, vol. 5, no. 4, pp. 5653–5660, 2020.

[Buc+22] R. Buchanan, M. Camurri, F. Dellaert, and M. Fallon, “Learning in-
ertial odometry for dynamic legged robot state estimation,” in Con-
ference on robot learning,  2022, pp. 1575–1584.

[Buc+22] R.  Buchanan,  V.  Agrawal,  M.  Camurri,  F.  Dellaert,  and  M.  Fallon,
“Deep imu bias inference for robust visual-inertial odometry with fac-
tor graphs,” IEEE Robotics and Automation Letters, vol. 8, no. 1, pp.
41–48, 2022.

[Rou+16] Q. Rouxel, G. Passault, L. Hofer, S. N'Guyen, and O. Ly, “Learning
the odometry on a small humanoid robot,” in 2016 IEEE International
Conference  on  Robotics  and  Automation  (ICRA),    2016,  pp.  1810–
1816.

[Qua20]

[Bit24]

[Mo10]

[Pyt24]

“Qualisys  Miqus  cameras,”  2020.  Available:  https://cdn-content.
qualisys.com/2020/01/PI_Miqus.pdf. [Accessed: Mar. 16, 2024]

Bit-Bots, “Path Planning Conﬁguration Bit-Bots.” Available: https://
github.com/bit-bots/bitbots_main/blob/main/bitbots_navigation/
bitbots_path_planning/conﬁg/path_planning.yaml.  [Accessed:  Mar.
15, 2024]

W. McKinney and others, “Data structures for statistical computing
in Python.,” in SciPy,  2010, pp. 51–56.

subprocess

“asyncio
asyn-
cio.” Available: https://docs.python.org/3/library/asyncio-subprocess.
html. [Accessed: Jan. 19, 2024]

Subprocess

support

for

-

[Gut]

J. Gutsche, “Quantifying Player Performance in Simulated Humanoid
Robot Soccer Games.”

[Zho+19] Y.  Zhou,  C.  Barnes,  J.  Lu,  J.  Yang,  and  H.  Li,  “On  the  continuity
of rotation representations in neural networks,” in Proceedings of the
IEEE/CVF  conference  on  computer  vision  and  pattern  recognition,
2019, pp. 5745–5753.

61

[Bie20]

L.  Biewald,  “Experiment  Tracking  with  Weights  and  Biases,”  2020.
Available: https://www.wandb.com/. [Accessed: Feb. 04, 2024]

[Aki+19] T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama, “Optuna: A
next-generation hyperparameter optimization framework,” in Proceed-
ings of the 25th ACM SIGKDD international conference on knowledge
discovery & data mining,  2019, pp. 2623–2631.

[Oza+22] Y.  Ozaki,  Y.  Tanigaki,  S.  Watanabe,  M.  Nomura,  and  M.  Onishi,
“Multiobjective tree-structured Parzen estimator,” Journal  of  Artiﬁ-
cial Intelligence Research, vol. 73, pp. 1209–1250, 2022.

[BZ22]

M.  Bestmann  and  J.  Zhang,  “Bipedal  walking  on  humanoid  robots
through  parameter  optimization,”  Robot  World  Cup.  Springer,  pp.
164–176, 2022.

62

