Climbing Stairs with DARwIn-OP humanoid
robots using kinematic tasks

Daniel Ahlers, Pamina M. Berg

University of Hamburg, Department of Informatics
http://www.inf.uni-hamburg.de/en.html

Abstract. The walking of biped humanoid robots has been an active re-
search area, whether it is for educational purpose, for supporting armed
forces in diﬃcult terrain or for developing service robots that will act,
communicate and walk in the most human manner possible, as our world
is created for two-legged locomotion. Another aspect is the development
of exoskeletons for the lower limbs, which can beneﬁt from the gait de-
signs for humanoid robots. Especially in the context of developing ser-
vice robots, the climbing of staircases is an essential part of the ability to
move around a real-life environment, such as a two-story apartment or
house. This report focuses on the implementation and design of a simple
stair climbing gait for the DARwIn-OP, using animations and kinematic
tasks.

Key words: Stair Climbing, Humanoid Robot

1 Introduction

Although the human bipedal locomotion is the most elaborate kind of gait, a
large number of computer scientists, phisicists, engineers and other analysts of
a variety of scientiﬁc ﬁelds have been experimenting and developing humanoid
robots to establish an eﬃgy of a human being, capable to move autonomously
on two legs. Despite the large number of robots with four legs or more, or even
those on wheels, that can already provide a reliable help as service robots, there
are numberous aspects that speak in favor of the development of humanoid
robots. First of all, robots have been generated to assist human beings in their
everyday life. Our environment, e.g. apartments, cinemas, streets and stores, has
been built for beings with an upright posture. Especially people with walking
impediments know the kind of challenge that comes with not being able to move
around on two legs. One of the most common barriers are staircases. Therefore,
we need to build robots that are customized for the environment in which they
have to operate. The advancements on this topic are an important part of basic
scientiﬁc research which can be used for artiﬁcial legs that may adapt to the
people’s walking impediments, thus contributing to their well-being.

There have been several approaches to make a biped humanoid climb stairs.
Akhtaruzzaman and Shafie proposed a model of alternating two phases, the

2

Ahlers, Berg

Single Support Phase (SSP), where we have a stance leg and a swing leg, and
the Double Support Phase (DSP). The ascending of the stairs has then been
provided by running through a series of 15 poses for one single step [1]. Choi
et al. used a ZMP motion planning algorithm and described three elementary
phases of stepping up one stair tread – the ascending forward phase, the forward
motion phase and the upward motion phase [2]. Making use of the advances
in stereo vision of robots, Gutmann et al. provided an automatism for stair
recognition, where the control system integrated in the humanoid robot decides
on the next move to climb a staircase [3]. Control algorithms have been the
basis of the approaches made by Kim et al. [5] and Sheng et al. [9] which
focus on the gait optimization and also work on the balance and stability, as
well as minimizing the energy required to achieve these goals. One of the latest
advancements comes from Boston Dynamics, who presented a modiﬁed version
of its humanoid robot PETMAN that established a stable walking up stairs.

Regarding a variety of possibilities to achieve a stable walking gait, the biped
humanoid is often considered to be an open kinematic chain [1]. In our case this
means, that we have rigid bodyparts, that are connected using motors as joints.
For example, the leg of a robot consists of the rigid upper leg, the rigid lower
leg and the foot, connected by motors which we will refer to as the knee and the
ankle. Every joint in the robot has at least one of the three angles of rotation.
These are called roll, pitch and yaw, and as it can be seen in Fig. 1, each one
has a speciﬁc movement in the three-dimensional space. For the DARwIn-OP of
the Hamburg BitBots, we will have a special orientation on the axes x, y and z,
as the x-axis will always direct to the next joint in the kinematic chain. E.g. the
x-axis of the hip joint directs vertically down to the knee, while the x-axis of the
ankle joint directs horizontally toward the front endpoint of the foot.

As we will refer to the concept of [1], now a short introduction into their work.
Referring to the above, Akhtaruzzaman and Shafie assembled a gait for as-
cending stairs using a ’combination of various postures and poses’ [1, p.9]. These
are the two Action Poses at the beginning and the end, where the robot will
stand upright, supporting its weigth with both feet, followed by the Tilt Pose
and the DS-SS Pose, which means, that the robot shifts its weigth support from
two legs (Double Support) to a single one (Single Support), thus we get a stance
and a swing leg. After this, the robot proceeds to the Foot Lifting Pose, the Foot
Forward Pose and the Foot Adjust Pose to lift the swing leg upwards an onto
the tread, hence, concluding the ﬁrst swing phase. In the following SS-DS Pose,
SS-DS Complete Pose and Tilt Pose the foot of the swing leg will be placed onto
the tread, so that the robot will now stand on both of its feet again. Now, ’before
the beginning of the second swing phase with the rear foot’, in the CoM Lifting
Pose, ’the anthropoid moves its Center of Mass (CoM) gradually upwards to ﬁx
its stability by front foot support’ [1, p.9-10]. In the second swing phase, the
robot runs through the DS-SS Pose, the Foot Lifting Pose, the Foot Forward

Climbing Stairs

3

Pose and the SS-DS Pose again, terminating the process with the Action Pose
[1]. (PMB)

Fig. 1. The three angles of rotation [4, p.21]

2 Implementation

2.1 Preliminaries

The ﬁrst step we needed to make was to build a model. We build the staircase
made of wood on a scale of 1 : 4 using the DIN18065 for staircases and it there-
fore has a 45mm height of treads and a depth that is slightly bigger than the foot
of the DARwIn-OP. So the ﬁrst tread has a width of 124mm as we tested with
the ﬁrst one and did not want the robot to fall because of a lack of space an the
tread, followed by three treads with a width of 104mm and a nosing of 8mm each.

The stair climbing module has been developed for and tested with the DARwIn-
OP of the Hamburg BitBots. They have some modiﬁcations compared to the
original version from Robotis, as the head has been replaced by one that will
not be as much aﬀected by an impact on the ground as the former construc-
tion, and some alterations considering the armor of the legs, as well as the feet.
Hence, the Center of Mass is in a diﬀerent position. This has an eﬀect on the
stabilization of the robot during bipedal walking and – in our case – climbing up
stairs, but fortunately our implementation does not rely on calculations based
on the CoM. (DA)

4

Ahlers, Berg

Fig. 2. Staircase model

Fig. 3. Staircase model side view

Climbing Stairs

5

2.2 General Aspects Of The Robotic Bipedal Walking

To understand the diﬃculty of stabilizing a humanoid robot, it is useful to get
an overview of the diﬀerent factors that need to be considered when planning
motions. One of the essential aspects is the stability region, which is the convex
envelope of the feet [4, p.54]. For a robot standing on one leg, the stability region
would be the outer edges of the foot.
The next basic term is the so called Zero Moment Point (ZMP). Sardain and

Fig. 4. Visualization of the Zero Moment Point, [4, p.54]

Bessonnet deﬁne the ZMP as ’the point on the ground, where the tipping mo-
ment acting on the biped, due to gravity and inertia forces, equals zero’ [8, p.2].
In other words, the ZMP is the point of contact on the ground in the stability
region, on which the robot bases its posture on. The ZMP is also an indicator for
the stability of the robot: if the ZMP is in the center of the stability region, the
stability of the robot during its walking is at its maximum. But there is also a
limit of using solely the ZMP for designing a walking gait for a humanoid robot,
as this concept can not be adapted to walk on uneven surfaces [4, p.81].
The Center of Pressure (CoP) is the point where the single force, which is equiv-
alent to the ’ﬁeld of pressure forces (normal to the sole)’ [8, p.1] exerts when the
resultant moment is zero. Ideally, the ZMP and the CoP are in the same spot
within the stability region.

Human locomotion has been translated into bipedal walking of robots in
diﬀerent ways. There are the approaches of the Passive-dynamic Walking, used
by the Cornell Biped, and the Static Walking, where the perpendicular point
of the CoM on the ground never leaves the stability region, thus leading to
enormous feet of the robot. Nowadays, the most common walking concept is the
Dynamic Walking. Using the pattern of a three-dimensional inverted pendulum,
an imitation of the human locomotion can be implemented. For this, a walking
pattern can be described, as well as the ﬂoor trajectory of the feet (Fig. 5) [4].

6

Ahlers, Berg

Fig. 5. Pattern for a straight forward walk with three steps

A relatively new approach in the dynmamic locomotion has been made us-
ing Linear Quadratic Optimal Control. Based on the prior experiences using
optimization-based techniques, made by e.g. Kajita, a new development has
been made by Kuindersma, where a fully actuated robot body system is as-
sumed to be a set of linear dynamics, thus, an optimal walking gait can be
obtained by using linear optimal control [6]. (PMB)

2.3 Motion Design

The general idea consists of running through several poses and stabilizing the
robot at certain points using animations.

Following the concept of [1] as presented in the preceded section, we started
by planning the motion process of one step up stairs. In our project, it consists
of ﬁve diﬀerent phases. After the robot comes to a stable pose on both feet, the
next phase would be that the robot shifts the support of its weight to a single
leg, e.g. the right one, while keeping up its balance. This ﬁrst phase ends with
the robot standing on the right (left) leg with the other leg slightly above the
ground as shown in Fig.6.
In the second phase the robot moves its swing leg onto the tread. For this, the
foot of the swing leg will be raised, then moved forward to hover over the tread
and subsequently set down on the tread (Fig. 7). The robot will then go on to
the next phase where the support will be shifted from the foot on the ground
to the foot on the tread (Fig. 8). The diﬃculty of this phase lies in the height
diﬀerence, as the robot has to overcome it while shifting its weight and Centre of
Mass onto the tread without losing its balance. Before actually standing upright
on the stairs, the robot needs to proceed through the fourth phase, thus lifting

Climbing Stairs

7

Fig. 6. Phase 1

the former stance leg from the ground and onto the tread, similar to phase two.
Now the robot can bring itself to an upright position in phase ﬁve. Because of
the limited power of the motors in the knees, the robot can only stand up from
a kneeling position (e.g. in phase four (Fig. 9)) using both of its legs.

Note, that since balancing the robot, especially during a SSP, is a challenging
task without having a fully developed balance system, we used not only the foot,
leg and hip motors, but created a full body movement. (DA)

2.4 Implementation and Methods

As there is a kinematic for the DARwIn-OP already provided by the framework
of the Hamburg BitBots, our ﬁrst attempt to transfer our ideas into some sort
of code was to use the given kinematic.
Kinematic in general is the ﬁeld of research describing the relationship between
the angles and the alignment of joints. It represents the basis of autonomous
robotic locomotion [4, p.15]. There are diﬀerent approaches for using kinematic
to achieve a stable walking gait for humanoid robots. One is the calculation of

8

Ahlers, Berg

Fig. 7. Phase 2

Fig. 8. Phase 3

Climbing Stairs

9

Fig. 9. Phase 4

joint positions given the joint angles, called forward kinematics, the other one is
the inverse kinematic, where the joint angles will be reckoned from the position
and the pose of the leg and torso [4]. Kajita describes the inverse kinematic
as a necessary element for positioning the leg of a humanoid robot in the right
height for stepping up a tread [4, p.40].

Due to a lack of functionality of one essential method (keep robot stable)
in the kinematic of the Hamburg BitBots framework, we began writing our own
animations for the stabilization of the robot. These animations are, in general,
ﬁxed poses which the robot is told to take in a certain amount of time, using its
motors. In each pose, every joint of the robot has a speciﬁc angle. To make the
robot move, we can change these angles within a given amount of time using ani-
mations. The code for one of our animations is shown in Fig. 10. For keeping our
stair climbing robot stable, we developed four diﬀerent animations, two for bal-
ancing on a single leg (balance left and balance right) and two for changing
the support leg (balance left to right and balance right to left). These
animations are used in Phase 1, where the robot will be told whether to start
with the right or left leg. If we want the robot to climb the tread with the left leg
ﬁrst, it will then use the animation balance right to shift its weight to the right
leg. Since there is a similarity between the motion at the beginning of the stair-
climb and the motion before performing a kick (e.g. on the soccer ﬁeld with the

10

Ahlers, Berg

ball in front of the robot), we used parts of the kick module given in the frame-
work of the Hamburg BitBots for the stabilization in Phase 1. The robot then

Fig. 10. Code for the animation balance right

lifts its leg onto the tread, proceeding to Phase 2. We implemented this by using
kinematic tasks, which we deﬁned as foot up, foot forward and foot down. In
each of these tasks, we needed to deﬁne the angles for an array of joint posi-
tions through the motor ID of each joint. To achieve the optimal joint angles, we
experimented with several diﬀerent options. Although we found good working
values, we made some additional pose updates in the tasks foot forward and
foot down to readjust the balance in the ankle pitches, ankle rolls and the knees.
it will proceed to Phase
After the robot set down its foot on the tread,
3, thus shifting its weight from the right leg on the ground to the left leg
on the tread. For this, we used the animations balance left to right and
balance right to left, depending on which foot is positioned on the tread. So
for the described scenario, we would use the animation balance right to left,
where we deﬁned the goals for the joint angles of both ankle pitches, ankle rolls,

Climbing Stairs

11

elbows, hip pitches, hip rolls, hip yaws, shoulder pitches and shoulder rolls, just
like we did for the animation balance right as it can be seen in (Fig. 10).
In the subsequent Phase 4, where the right leg will be lifted and set down on
the tread, we used our kinematic tasks foot up2, as well as an additional pose
update in the ankle goal, foot forward2 with an adjustment in both hip pitches
and foot down2, correcting the angle values of again both hip pitches as well as
the ankle pitches, due to stability reasons. We obtained these values by trial and
error like we did for the animations in Phase 2.
For the last phase, Phase 5, we modiﬁed the ankle roll joint values using kine-
matic tasks. At last, the robot brings itself into an upright pose using the an-
imation walkready provided by the framework of the Hamburg BitBots, thus
concluding the step up the ﬁrst tread. The whole gait can be illustrated by a
diagram, where the robot would start at the position Walkready (Fig. 11). (DA)

Fig. 11. The diﬀerent phases of the motion sequence

12

Ahlers, Berg

3 Results

We established a stable up-stair motion process for the DARwIn-OP, using an-
imations and kinematic tasks, thus enabling a robot to climb a tread of 45mm
height. The code given in the appendix shows that we provided an implemen-
tation where the user can dynamically change the height of the treads, hence
making this code adaptable to other staircases. Note that we only tested the
code on our model staircase with the measurements as described in Section 2.1.
During the development process for making the robot climb up a staircase, we
discovered some limits in the hardware as well as in the software.
Unfortunately, the motors in the knees do not have enough power to raise the
robot using only one knee. Hence, we had to bring the robot back to a double
support stance after Phase 4 and the robot will get into a stable upright position
on both feet before proceeding to take the next tread.
Another point was that we used the simulation software of the Hamburg BitBots
for testing the angles that had to be deﬁned manually. The disadvantage of this
was that the DARwIn-OP sometimes had a slight diﬀerence in the values, thus
making it hard to decide on an optimal value for the angles. With regard to
this problem, the robot sometimes rotated on one foot during the phases three
to ﬁve, so that it was then impossible for the robot to subsequently proceed to
climb the next tread. Making use of the vision to let the robot recognize the
tread and its position in relation to it and positioning itself correctly before pro-
ceeding to step up the next tread as a result could be a further enhancement to
the software.
The simulation software also does not provide a model staircase, thus we could
only simulate e.g. the motion of the swing leg itself without knowing if it would
ﬁt our staircase properly.
While testing the code on the robot we also noticed a lack of stability of our
staircase model. Since the upper treads are very slim, they would bend down
some millimeters, such that as a consequence, the stability and balance of the
robot will be inﬂuenced once the robot reaches the second tread. Because our
animations are based on ﬁxed joint angle values, the robot is not capable of
adapting to this circumstance.
Unfortunately, we were not able to develop a concept to calculate the required
motion processes dynamically, which would give a solution to the preceded prob-
lem.
Concluding the results, the developed motion process allows the robot to climb
a staircase without falling oﬀ, but can be optimized with regard to the speed.
The project results do not provide a direct enhancement for the soccer playing
DARwIn-OP, but helps to understand the process of movement for humanoid
robots, as it uses very basic elements of the motion (e.g. changing values of the
joint angles to move the foot or leg). This collaborates with the original idea
behind the RoboCup Rescue, which is one of the major competition domains
in the RoboCup tournament in general and has been created as a consequence
of an enormous earthquake in Kobe City in 1995 [7]. With this division that
challenges teams all over the world to develop rescue robots that can act and

move autonomously, the advancements made in the basic scientiﬁc research of
human walking patterns and their adaption due to this challenge did not only
enable the research on robotics to beneﬁt from this but also medical science, e.g.
in the development of exoskeletons. (PMB)

Climbing Stairs

13

4 Conclusion

A simple walking up stairs gait for the DARwIn-OP has been presented, using
kinematic tasks and animations. The stabilization of the robot is made by man-
ually correcting the joint angles after several poses.
As there is a concept by the Hamburg BitBots for building a new humanoid
robot using a 3D printer for the rigid bodyparts, as well as more powerful mo-
tors as joints, the preceded gait for ascending stairs can be enhanced with regard
to the motion speed. For this, a shorter period of time can be chosen to perform
the angle goals in the animations.
Another possibilty for further enhancement is to use the vision of the robot to
recognize not only the staircase, but the height of the treads, following the exam-
ple set by [3]. It could then be considered to make use of the concept provided by
[6] and therefore developing a feedback control loop, in which the sensor data of
the robot will be evaluated and used in the process of calculating the next step.
As this is not only a time-consuming process, but has also great computational
costs, the next generation robot of the Hamburg BitBots will probably not be
able to achieve this kind of dynamic walking gait.
For future academic projects considering the climbing up stairs, there can be
made some changes and improvements in the kinematic of the Hamburg Bit-
Bots framework, e.g. in the method keep robot stable. Using this method, we
could have simulated the human locomotion more eﬃciently because the robot
would have then used the inverse kinematic to perform a task and keep itself
stable during the process. This could lead not only to smoother movements of
the robot, but to a walking gait that is much more gentle to the joints of the
robot, and as a result the motors could be prevented from excessive wear. (PMB)

References

1. Akhtaruzzaman, Md., Shaﬁe, A.: Novel Gait for an anthropoid and Its Joint De-
meanors while Stepping Up and Down Stairs. In: Journal of Mechanical Engineering
and Automation, 1(1):8–16 (2011)

2. Choi, J., Choi, Y., Yi, B.: A Up-Stair Motion Planning Algorithm for a Biped Robot.
In: 5th International Conference on Ubiquitous Robots and Ambient Intelligence,
pp. 681–686. (2008)

3. Gutmann, J.-S., Fukuchi, M., Fujita, M.: Stair Climbing for Humanoid Robots Using
Stereo Vision. In: Proceedings of the 2004 IEEE/RSJ International Vonference on
Intelligent Robots and Systems, pp. 1407–1413. Sendai, Japan (2004)

14

Ahlers, Berg

4. Kajita, S., Hirukawa, H., Yokoi, K., Harada, K.: Humanoide Roboter - Theorie
und Technik des K¨unstlichen Menschen. Ed. Shuji Kajita, Akademische Verlagsge-
sellschaft, Berlin (2007)

5. Kim, J.-Y., Park, I.-W., Oh, J.-H.: Realization of Dynamic Stair Climbing for Biped
Humanoid Robot Using Force/Torque Sensors. In: Journal of Intelligent and Robotic
Systems, Vol. 56, Iss. 4, pp. 389–423. Springer Netherlands (2009)

6. Kuindersma, S., Permenter, F., Tedrake, R.: An Eﬃciently Solvable Quadratic Pro-
gram for Stabilizing Dynamic Locomotion. In: Proceedings of the International Con-
ference on Robotics and Automation (ICRA). Hong Kong, China (2014)

7. RoboCup Rescue Wiki, http://www.robocuprescue.org/wiki/index.php?title=

Main Page

8. Sardain, P., Bessonnet, G.: Forces Acting on a Biped Robot. Center of Pressure -
Zero Moment Point. In: IEEE Trans. Syst. Man Cybern. A., Syst. Humans, Vol. 34,
No. 5, September (2004)

9. Sheng, B. et al.: Multi-Objective Optimiation for a Humanoid Robot Climbing Stairs
based on a Genetiv Algorithm. In: Proceedings of the 2009 IEEE International Con-
ference on Information and Automation, pp. 66–71. Zhuhai/Macau, China (2009)

Appendix

Climbing Stairs

15

2

4

5

7

9

10

11

12

14

15

17

19

20

21

22

23

25

26

28

29

30

31

32

33

34

36

37

38

39

40

41

42

43

44

46

47

# -* - coding : utf -8 -* -

"""
Treppensteigen

Entwickelt im Rahmen des Robocup Projekts im WiSe 14/15

Es soll dem DARwIn - OP ermoeglichen kleine Stufen zu erklimmen .
Die Stufenhoehe kann variiert werden ,
es wurde aber nur mit einer Stufenhoehe von 45 mm Stufen getestet .
Die Stufentiefe sollte in etwa die Tiefe des Fusses des DARwIn - OP haben .

Die Stabilisierung erfolgt ueber Animationen ,
Die Bewegung der Beine ist mit Kinematischen Tasks umgesetzt .

"""

from bitbots . ipc . ipc import *
from bitbots . robot . pypose import *
from bitbots . util . kinematicutil import *
from bitbots . robot . kinematics import *
from bitbots . util . animation import *

import numpy as np
import time

class StairClimb :

# Initialisieren des Roboters
def __init__ ( self ):

self . ipc = SharedMemoryIPC ()
self . pose = PyPose ()
self . robot = Robot ()
self . task = KinematicTask ( self . robot )

# Funktion zum Warten auf eine laufende Animation plus x Sekunden
def wait_for_end ( self , sleeptime =2):

time . sleep (0.1)
# warte auf Animation
while ( not self . ipc . controlable ) or
( self . ipc . get_state () == S TA T E _ AN I M A T IO N _ R UN N I N G :)

time . sleep (0.05)
# warte weitere x Sekunden
time . sleep ( sleeptime )

# schreibt die Pose auf den IPC und
# aktualisiert im Anschluss Pose und robot

16

Ahlers, Berg

48

49

50

52

53

55

56

57

58

59

60

61

63

64

65

66

68

69

70

71

72

73

74

75

76

77

78

79

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

def update_pose ( self , sleeptime =2):
self . ipc . update ( self . pose )
self . wait_for_end ( sleeptime )

self . pose = self . ipc . get_pose ()
self . robot . update ( self . pose )

# spielt eine Animation ab und aktualisiert
# im Anschluss Pose und robot
def animation_play ( self , animation , sleeptime =0.5):

play_animation ( animation , self . ipc )
self . wait_for_end ( sleeptime )
self . pose = self . ipc . get_pose ()
self . robot . update ( self . pose )

# bringt den Roboter in Ausgangsstellung
def walk_init ( self ):

self . wait_for_end (0)
self . animation_play (" walkready " ,0)

# fuehrt einen Kinematischen Task aus
def perform_task ( self , array , i , legnr , speed =1):

if legnr ==1:

# erstes Bein auf der Treppe
self . task . perform (0 , 34+ i , [(1 , 0 , 0) , array ] ,

(1 e -2 , 1) , (0 , 3) , 100 , [15+ i ] , [7+ i ,17+ i ])

else :

# oder zweites
self . task . perform (0 , 35 -i , [(1 , 0 , 0) , array ] ,

(1 e -2 , 1) , (0 , 3) , 100 , [16 - i ] , [8 -i ,18 - i ])

# Winkel auf Roboter schreiben
self . robot . s et_angle s_ to_pose ( self . pose , -1 , speed )

# steigt eine Stufe hoch
def walk_step ( self , height , i ):

i = i %2
if i ==1:

# linkes Bein zuerst
balance =" balance_right "
foot_up = np . array (( -20 , 47 , -265+ height ))
foot_forward = np . array ((120 , 47 , -265+ height ))
foot_down = np . array ((120 , 47 , -275+ height ))
balance_shift =" bala nc e_r ight _to_l eft "
foot_up2 = np . array (( -50 , -47 , -270+ height ))
foot_forward2 = np . array ((35 , -47 , -270+ height ))
foot_down2 = np . array ((60 , -47 , -275+ height ))

else :

# rechtes Bein zuerst
balance =" balance_left "
foot_up = np . array (( -20 , -47 , -285+ height ))

Climbing Stairs

17

foot_forward = np . array ((120 , -47 , -285+ height ))
foot_down = np . array ((120 , -47 , -315+ height ))
balance_shift =" ba la nce_ l ef t_ t o_ r ig ht "
foot_up2 = np . array (( -50 , 47 , -270+ height ))
foot_forward2 = np . array ((35 , 47 , -270+ height ))
foot_down2 = np . array ((60 , 47 , -275+ height ))

# balanciert auf einem Bein
self . animation_play ( balance )

# anderen Fuss heben
self . perform_task ( foot_up ,i ,1)
self . update_pose (1)

# Fuss vor bewegen
self . perform_task ( foot_forward ,i ,1)
# G l e i c h g e w i c h t s k o r r e k t u re n fuer rechts oder links
if i ==1:

self . pose . l_ankle_pitch . goal = -20
self . pose . r_ankle_roll . goal = -12
self . pose . r_knee . goal = 49

else :

self . pose . r_ankle_pitch . goal = 20
self . pose . l_ankle_roll . goal = 12
self . pose . l_knee . goal = -47

self . update_pose (1)

# Fuss absetzten
self . perform_task ( foot_down ,i ,1 ,0.5)
# G l e i c h g e w i c h t s k o r r e k t u re n fuer rechts oder links
if i ==1:

self . pose . l_ankle_pitch . goal = -5
self . pose . l_ankle_roll . goal = -15

else :

self . pose . r_ankle_pitch . goal = -24
self . pose . r_ankle_roll . goal = 15

self . update_pose (0.5)

# Wechsel des Schwerpunktes vom einen auf den anderen Fuss
self . animation_play ( balance_shift )

# hinteren Fuss heben
self . perform_task ( foot_up2 ,i ,2)
## G l e i c h g e w i c h t s k o r r e k t u r e n fuer rechts oder links
if i ==1:

self . pose . l_ankle_roll . goal = 20

else :

self . pose . r_ankle_roll . goal = -20

self . update_pose (1)

98

99

100

101

102

103

105

106

108

109

110

112

113

114

115

116

117

118

119

120

121

122

123

125

126

127

128

129

130

131

132

133

134

136

137

139

140

141

142

143

144

145

146

18

Ahlers, Berg

148

149

150

151

152

153

155

156

157

158

159

160

161

162

163

164

165

166

168

169

170

171

172

173

175

176

178

179

180

181

182

# hinteren Fuss vor bewegen
self . perform_task ( foot_forward2 ,i ,2)
# G l e i c h g e w i c h t s k o r r e k t u re n
self . pose . r_hip_pitch . goal = -100
self . pose . l_hip_pitch . goal = 100
self . update_pose (1)

# hinteren Fuss absetzten
self . perform_task ( foot_down2 ,i ,2 ,0.5)
# G l e i c h g e w i c h t s k o r r e k t u re n fuer rechts oder links
self . pose . r_hip_pitch . goal = -110
self . pose . l_hip_pitch . goal = 110
if i ==1:

self . pose . r_ankle_pitch . goal = 52
self . pose . r_ankle_pitch . speed = 20

else :

self . pose . l_ankle_pitch . goal = -52
self . pose . l_ankle_pitch . speed = 20

self . update_pose (0.5)

# Roboter wieder gerade stellen
self . pose . l_ankle_roll . goal = 0
self . pose . r_ankle_roll . goal = 0
self . pose . l_ankle_roll . speed = 10
self . pose . r_ankle_roll . speed = 10
self . update_pose (1)

# Roboter wieder in Ausgangsstellung bringen
self . animation_play (" walkready ")

# Roboter steigt mehrere Stufen hoch , beginnend mit dem linken Fuss
def walk_stairs ( self , steps =1 , height =45):

self . walk_init ()
for i in range (1 , steps +1):

self . walk_step ( height , i )

