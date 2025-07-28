WF Wolves & Hamburg Bit-Bots
Team Description for RoboCup 2018
– Humanoid TeenSize –

Marc Bestmann1, Niklas Fiedler1, Alexander Gabel2, Jasper G¨uldenstein1,
Niklas Hamann2, Judith Hartﬁll1, Tanja Heuer2, Jessica Jobski1, Tom Lorenz2,
Maike Paetzel1, Martin Poppinga1, Dennis Reher1, Bente Reichardt1, Nils
Rokita1, Ivan David Ria˜no Salamanca2, Oliver Sengpiel1, Daniel Speck1,
Sebastian Stelter1, Frank Stiddien2, and Natasza Szczypien2

1 Department of Informatics, Universit¨at Hamburg,
Vogt-K¨olln-Straße 30, 22527 Hamburg, Germany
info@bit-bots.de
www.bit-bots.de
2 Ostfalia University of Applied Sciences, Wolfenb¨uttel, Germany
robo-wm@ostfalia.de
https://www.wf-wolves.de

Abstract. In this team description paper the joint team WF Wolves &
Hamburg Bit-Bots, their robots, and current research status are intro-
duced. With the collaborative work for a standardized software frame-
work for humanoid robots based on a ROS framework, a joint team
should show advantages of using this framework. As a new research topic,
the Bit-Bots focused on Neural Networks for bio-inspired image process-
ing which was adopted by the WF Wolves. Additionally, the hardware
and software of the robots are speciﬁed in detail for the robots. Hereby
the joint team Bit-Bots and WF Wolves apply for participation at the
RoboCup 2018 for Team Competition in Montreal, Canada.

This Paper is similar to [1] except that the later intodruced Minibot
is not viable for the TeenSize League. Although this team is a joined
team, each sub team will participate with 4 robots each.

1

Introduction

WF Wolves & Hamburg Bit-Bots want to participate as a joint robot team. The
team integrates WF Wolves from Germany, Wolfenb¨uttel and Bit-Bots from
Germany, Hamburg. The Hamburg Bit-Bots is supported by the Department
of Informatics at the University of Hamburg. They are an independent working
group and Bachelor, Master and Ph.D. students are part of the group. Their
robot platform Minibot will participate in the KidSize competition, whereas
their two new Nimbro-based robots are allowed to participate in KidSize and
TeenSize competitions. The WF Wolves are located at the Faculty of Computer

Science at the Ostfalia - University of Applied Sciences. Besides computer sci-
ence students also students from electrical and mechanical engineering are part
of the team. Like the Bit-Bots the team is an independent working group, ﬁnan-
cially supported by the University. While WF Wolves changed to a NimbRo-OP
based platform (usable in Kid- and TeenSize) in 2014, they already have some
years of experience in TeenSize RoboCup competitions, the Hamburg Bit-Bots
concentrate on playing with a self-designed KidSize platform called ”Minibot” .
Since the WF Wolves robots are also valid for KidSize, we are concentrating on
a common framework platform. Together we want to concentrate manpower at
the research of humanoid robots. The teams started working together in 2017
building a common ROS framework. At the Iran Open 2017, the teams ﬁrst
participated as a joint team and got the 5th place in the TeenSize competition.
In Hefei (KidSize/TeenSize) and in Leipzig (TeenSize) WF Wolves made the
second place in the category Technical Challenge. In 2017 they won the third
prize at the German Open, Magdeburg and the second prize in the new category
Drop-In Challenge at the RoboCup World Championship in Nagoya, Japan.

Besides, the Hamburg Bit-Bots have some further projects for a better in-
terconnectedness between humanoid robot teams and to support a more general
public presence and availability. Since 2014, the Bit-Bots are actively part of the
RoboCup Federation supporting the organization of the RoboCup world cham-
pionship and participating in the enhancement of the rules. For this year, we
want to adapt the GameController to support the new rule changes. Apart from
that, the annual RoHOW3 is hosted by us together with another RoboCup Team
(SPL league) from Hamburg.

2 Research Overview

This section gives an overview of the focused research topics for the following
RoboCup competition.

2.1 Motion Robustness

Although the artiﬁcial grass is used for two years now it is still a hard challenge
for stabilization and robustness of the robots motions. Therefore we worked on
weight cells under the foot plates. Additionally, we introduced a diﬀerent kind of
studs for a better grip on the ﬁeld and we continued improving the sequences and
the closed-loop controllers. With these techniques we achieved less falls during a
kick motion and a more stable walk. Besides the WF Wolves have built a robot
with a series knee. That fact improves a faster walk and a higher kick range.
With those aspects, we improve the robustness of walking and kicking of the
robots. The Hamburg Bit-Bots are currently working on using a neural network
to learn the gait based on inputs from the new weight cells and the information
about the current eﬀorts and positions in the joints.

3 Robotics Hamburg Open Workshop, www.rohow.de/en/

2.2 Tensorﬂow & Convolutional Neural Network

Until now we worked with the haar ball ﬁnder to localize the ﬁeld, the ball, and
the goal. Because of an expansion of the football ﬁeld, the problem of detection
over a longer distance occurred. As an advantage, we are working with Tensorﬂow
and a Convolutional Neural Network (CNN) now to recognize all important parts
on the ﬁeld, especially over a longer distance. This is based on our award-winning
publication [14]. As already mentioned, the neural networks can also be used for
a lot of things, like operating behavior.

2.3 Interteam Collaboration

We researched and developed tools to accelerate the research and ease collabo-
ration. One result is a common ROS interface and a tool set for the Humanoid
League [15]. Another tool, called ”Imagetagger” was developed to enable col-
laborative online labeling and exchange of vision training data sets [17]. This
is increasingly important since many teams use deep learning in their object
recognition and therefore need large amounts of data. Furthermore, it makes it
easy to compare diﬀerent algorithms with each other.

3 Hardware

Fig. 1. NimbRo-OP based robot (left) and the Minibot (right).

3.1 WF Wolves Robots: Detlef & Hans & Gambi

The size of all robots is valid for the TeenSize and KidSize league. They based on
the NimbRo-OP platform. In the legs, Dynamixel MX-106 are used. Dynamixel
MX-64 are used for the arms and the head. In our university’s mechanical work-
shop we milled the aluminum and carbon parts. With our 3D printer, we can
create plastic parts like the head with ABS. Gambi as a reﬁned robot has series
knee (see Fig. 3). It is a modiﬁed knee with two Dynamixel MX-106 servos in a
row. Hans is the robot with weight cells under the foot plates. Every robot has
an Intel NUC computer with Core i5 in addition to 4 GB DDR3 RAM, USB
3.0 and wireless LAN. As a new part, we built in a body board from Rhoban,
connected to an adaptive shield board. This board also serves power supply for
our Jetson boards. The Nvidia Jetson board was added to the robot to be able to
get a higher performance in running neural networks which are now used in ob-
ject detection and motion. The power is supplied by lithium polymer batteries.
To regulate the voltage, the robots have a separate board as voltage regulator
included. All the parts are located in the torso of the robots. Our software was
adapted to the new hardware and works properly. We used these boards for the
ﬁrst time at the competition in Nagoya. The used camera for the WF Wolves
robots is the Logitech C920 HD Pro Webcam as a visual sensor. The camera
runs up to a 1.920 x 1.080 resolution at 30 FPS.

3.2 Bit-Bots Robots: Minibot

The Hamburg Bit-Bots experimented over a long period of time with diﬀerent
robot platforms in diﬀerent sizes. The Minibot is a compromise in hight, which
ensures stability and low weight, while still being big enough for a fast walk and a
strong kick. It is made of simple aluminum sheet metal and uses the Dynamixel
MX servos of all sizes. It is controlled via an Odroid XU-4 with an octa-core
ARM processor and a CM730 for the servo control.

3.3 Studs & Weight Cells

Since the introduction of the artiﬁcial grass, we are printing diﬀerent kinds of
studs with our 3D printer from ABS. By mounting them, we achieve a more
stable walk on the ﬁeld [11]. One of the best working studs is shown in Fig. 3.
Additionally, we assumed the weight cells from the Kid Size Team Rhoban from
France and integrated them under the foot plates. This integration of the weight
cells can is shown in Fig. 2.

4 Software

4.1 Framework Architecture

Since 2016 the WF Wolves are using a ROS based framework for our software
architecture which was adopted by the Hamburg Bit-Bots in 2017. Since last

Fig. 2. The Weight Cells

Fig. 3. Studs and Series Knee

year we revised the framework together. The main advantage of the now used
framework is the modularity that enables code exchanges in an easier way among
each other. Therefore, we (WF Wolves & Hamburg Bit-Bots) can develop soft-
ware modules independently from each other but still share and compare them.
Since ROS is being used more often in RoboCup, cooperation with other teams
is also getting easier. Our code is open source and available online 4.

4.2 Team Communication

Communication between robots is getting more important since last years Drop-
In challenges. Therefore a shared protocol was developed by team FUmanoids[9].It
is the so-called Mixed team communication protocol (mitecom). With the use of
this protocol, our robots are capable of communication with other robots of the
own or another team. Especially in a drop-In challenge where robots from dif-
ferent teams play together, a communication is useful. This was already tested
during previous championships. What’s more, with this protocol it is much easier
for our teams to play together in a joint team.

4.3 Localization

Our vision consists of three parts. We worked on the ball detection using tensor-
ﬂow and a neural network. With the introduction of artiﬁcial grass, the problem
of reﬂections on the ﬁeld occurred. For that reason, we developed some ap-
proaches on ﬁnding the right ﬁeld color and ﬁeld-lines for basic localization [12].
Additionally, a particle-ﬁlter based approach to recognize various features on the
ﬁeld. Finally, we created a goal detection so that the robot kicks the ball in the
right direction.

4 https://github.com/Bit-Bots

4.4 Motions

For movement, such as walking forward, backward, sideways and turning, an
omni-directional walk engine is used. Servo positions are calculated in real time.
This allows us to control the body via high-level commands instead of using a
combination of predeﬁned sets of key-frame motions. Even though the inferior
control method proves to be static motions, some are too complex to be gener-
ated in an easy way. Therefore the robots use predeﬁned key-frame motions e.g.
for goalkeeper motions and getting up. Besides this, it is suﬃciently abstract to
allow running the same behavior on diﬀerent robots without the need for sophis-
ticated calibration [3]. A kick motion generator was developed by WF Wolves
to allow the robots to kick in nearly every direction [4]. With two vectors, one
for the current ball and one for the target position, the required movements are
calculated in real time. For more stabilization, a closed-loop control was added
and the sequence was improved [11].

The walking is now based on more data than before. The foot pressure force
is measured by the weight cells. The eﬀort values are based on the current of the
motors and available due to the new ﬁrmware version of the MX Dynamixels.
These information are used by a neural network, which continuously computes
spline points for the motion of both feet. The goal position of the joints is then
computed by the spline interpolation. The network uses online learning to update
its own weights based on the stability of the robots walking. Therefore manual
tuning of parameters is not necessary.

4.5 Vision

The vision is the new part we are working on together to get a common status of
the vision software. The WF Wolves used a cascade classiﬁer for ball detection
implemented in OpenCV until last year. With the cooperation with the Hamburg
Bit-Bots we started to work on ball recognition with the help of neural networks.
With the installed Jetson it can be calculated well and the recognition works
better. Because of reﬂections on the artiﬁcial gras some new approaches on ﬁeld
colour and ﬁeld-lines for basic localization [12] were introduced. Additionally to
that we try to localize the goal, to be able to kick to the right direction. The
Hamburg Bit-Bots started on fundamental research in the ﬁeld of deep learning.
By doing that they contribute bio-inspired neural architectures which enhance
the visual perception of complex scenarios. The neural network is able to learn
substantial features on the ﬁeld during a match [14, 16]. This technique should
be improved with the cooperation.

4.6 Behaviour

A hierarchical state machine is the base of the behavior framework. Therefore it
is necessary that the robot knows it’s role, like goal keeper, striker or defender.
Depending on the vision and calculations the robot can fulﬁll tasks like going to
the ball, searching the ball, kicking. Attacking or defending are more high-level
tasks. For path-ﬁnding an oﬄine trained neural network is used [2].

5 Conclusions

Our changes in robot hardware and software provide improvements in compari-
son to the previous year. A better robustness for the motions and upgrades for
vision and localization show promise results. WF Wolves & Bit Bots is looking
forward to participating in the RoboCup 2018 for the Team Competition in
Montreal, Canada.

References

1. Lorenz, T.; Heuer; T, Bestmann, M.; et al.: WF Wolves & Hamburg Bit-Bots Team
Descirption for RoboCup 2018 - Humanoid Kidsize; Ostfalia - University of applied
Sciences, Wolfenbuettel, Germany & Universit¨at Hamburg, Department of Infor-
matics, Germany (2018)

2. Poppinga, M.: Intelligente Wegﬁndung humanoider Roboter am Beispiel des
RoboCup. Bachelor thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2014)

3. Michalik, S.: Dynamisches Laufen von humanoiden Robotern. Bachelorthesis, Ost-

falia - University of applied Sciences, 2010.

4. Krebs, O.; Gerndt, R.: Dynamic Ball Kicking for Humanoid Robots. In: First Brazil-

ian Workshop on Service Robotics, Santa Maria, 2013.

5. Martins, L. T.; Gerndt, R.; Guerra, R. S.: Series Elastic Actuator and Its Application
For Humanoid Platform. In: First Brazilian Workshop on Service Robotics, Santa
Maria, 2013.

6. Martins, L. T.; de Mendon¸ca Pretto, R.; Gerndt, R.; da Silva Guerra, R.: Design
of a modular series elastic upgrade to a robotics actuator. In Robot Soccer World
Cup (pp. 701-708). Springer International Publishing, 2014

7. Martins, L. T.; Tatsch, C.; Maciel, E. H.; Henriques, R. V. B.; Gerndt, R.; da Guerra,
R. S.: Polyurethane-based modular series elastic upgrade to a robotics actuator. In
Robot Soccer World Cup (pp. 347-355). Springer International Publishing, 2015
8. Martins, L. T.; Tatsch, C. A. A.; Maciel, E. H.; Gerndt, R.; da Silva Guerra, R. : A
polyurethane-based compliant element for upgrading conventional servos into series
elastic actuators. IFAC-PapersOnLine, 48(19), 112-117, 2015

9. FUmanoids, Mixed Team Communication protocol, 2014. Available online at

https://github.com/fumanoids/mitecom.

10. Krebs, O.; Bolze, T.; Gerndt, R.: Bumblebee Stereo Camera for Robotic Soccer -

A Case Study. In: RoboCup Humanoid Open Workshop, Dresden, 2015.

11. Krebs, O.: Closed-Loop Kinematic Scheme for Kicking Motion of Humanoid Soccer

Robots. Bachelorthesis, Ostfalia - University of applied Sciences, 2015.

12. Lorenz, T.: Visuelle Lokalisierung eines humanoiden Roboters anhand von Feldlin-

ien. Bachelorthesis, Ostfalia - University of applied Sciences, 2016.

13. Missura, Marcell, and Sven Behnke.: Balanced walking with capture steps.
RoboCup 2014: Robot World Cup XVIII. Springer International Publishing, 2014.
3-15.

14. Speck, D., Barros, P., Weber, C., Wermter, S.: Ball Localization for Robocup Soc-
cer using Convolutional Neural Networks. 20’th RoboCup International Symposium,
Leipzig, 2016

15. Bestmann, Marc.: Towards Using ROS in the RoboCup Humanoid Soccer League.

Masterthesis, University Hamburg, 2017.

16. Speck, D.; Balltracking for Robocup Soccer using Deep Neural Networks. Bachelor

thesis, University of Hamburg, Department of Informatics, Germany (2016)

17. imagetagger.bit-bots.de

