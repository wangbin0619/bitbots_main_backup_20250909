Application from Hamburg Bit-Bots for
RoboCup 2015

Marc Bestmann, Juliane B¨odeker, Fabian Fiedler, Timon Giese, Judith
Hartﬁll, Marcel Hellwig, Maxim Holand, Jessica Jobski, Robert Keßler, Maike
Paetzel, Martin Poppinga, Dennis Reher, Bente Reichardt, Nils Rokita, Robert
Schmidt, Oliver Sengpiel, Daniel Speck, and Lars Thoms

Department of Informatics, Universit¨at Hamburg,
Vogt-K¨olln-Straße 30, 22527 Hamburg, Germany
info@bit-bots.de

Abstract. This Team Description Paper describes the humanoid robot
team Hamburg Bit-Bots, from its history over currently used software
and hardware to the research interests and achievements in RoboCup.

1

Introduction

The team Hamburg Bit-Bots consists of a group of students from the Department
of Informatics at the University of Hamburg, Germany. It was founded in 2011
as a group of former participants of the oﬃcial RoboCup bachelor project par-
ticipating as RFC St. Ellingen in the SPL league. The new team was founded
with the goal to integrate knowledge from diﬀerent ﬁelds of our studies in a
more practical approach. It was explicitly created for the participation in the
humanoid league and thus started from scratch with new robots and a newly
developed codebase.

The team is ﬁnancially supported by the university and its Department of In-
formatics. Apart from that Hamburg Bit-Bots are an independent work group
led and organised solely by students. All team members are currently computer
science related students and are working on their bachelor’s or master’s degrees.

1.1 Prior performance in RoboCup

In 2012 we participated in the German Open and were placed third. Furthermore,
we took part in the WorldCup in Mexico City and were dropped out in the
second round robin, but successfully ﬁnished the Throw-In Challenge. Apart
from that we joined the RoBOW 12.1, 12.2 and 12.3 in Berlin to push the
interconnectedness between the European RoboCup teams and to take part in
a research exchange.
In 2013 we participated in the German Open (second place) and organized a
Mini RoBOW in Hamburg. The WorldCup in the Netherlands was a good view
of our ongoing development progress and despite the fact that we missed the

2

quarter ﬁnals, we were very pleased with In 2014 we participated in the German
Open (placed third), the IranOpen and the WorldCup in Brazil. We were able
to show our latest developments in hardware in Brazil and furthermore made
close contact to another RoboCup Team from our home town which competes in
the SPL. This gave us the opportunity to host the RoHOW1 jointly with them
that brought together twelve international teams from the RoboCup SPL and
humanoid leagues.

1.2 Further dedication in RoboCup

Apart from the participation during championships we have many projects to
make robotics and RoboCup accessible to people. For example we participated
in “Robots on Tour” in Zurich 2013, in the “Hamburg Night of Knowledge” and
“Berlin Night of Knowledge”. In cooperation with a school we created a yearly
course in robotics for high school students which is a great success since 2013.
Furthermore, in 2014, we started to provide practical lectures in robotics at our
university which are highly attended by students.

2 Current Research

2.1 Construction of new feet

The feet of the robots in the HKSL are ﬂat and stiﬀ. Humans don’t have ﬂat
and stiﬀ feet. The sole of the human foot has a structure that only in some
parts touches the ground and others parts that don’t. This makes the standing
more stable. The human foot is also ﬂexible in itself which helps to adapt to the
surface the foot is standing on. Regarding the change from carpet to artiﬁcial
grass, more stability in the walking and the foot’s adaption to the ground will
be necessary.

2.2 Joints, muscles and tendons

In the human body there exists a hard skeleton and a lot of muscels that are used
to move the skeleton. The construction of our robots is diﬀerent. The motors
work as muscles and are a part of the robot’s skeleton. This causes much pressure
on the motors. Therefore we try to add ribbons with motors working like muscles
and tendons similar to the human joints. We hope that the load on our motors
will decrease and the joints themselves will become smaller without losing any
degree of freedom.

2.3 Localisation with Rat-SLAM

To enable the localisation in the RoboCup Soccer context, the algorithm Rat-
SLAM, which does simultaneous localisation and mapping, was ported into an

1 Robotics Hamburg Open Workshop, www.rohow.de/en/

existing RoboCup framework. The algorithm was extended to use data from the
existing image processing and to improve thereby the position matching. The
use of the distances to the goal posts and of the lines in relation to the robot were
examined. It was shown that these additional data can improve the matching of
the RatSLAM algorithm. [1]

3

2.4 Bioinspired Pathﬁnding of Humanoid Robots

We are testing an approach of combining classic potential ﬁelds and bio-inspired
learning algorithms for robot navigation to perform eﬃcient path planning to
the ball while aligning to the enemy goal [2]. With evolutionary training we
create neuronal networks and use them as a dynamic layer of a potential ﬁeld.
We expect better results in contrast to the often used hard coded pathﬁnding.

2.5 Continuous simulation and evaluation of tryouts

To test our robot’s behaviour we plan to set-up a continuous integration system
which is simulating our source code in a virtual environment on nightly basis.
Currently we are adapting the vrep simulation framework for our needs. With
this set-up we would like to raise our software quality and give it a measurement.

3 Software

3.1 General Architecture

The software framework (released, [3]) in general is a cyclic program with several
modules performing diﬀerent tasks. In general we have developed a set of basic
modules which does the general tasks which are necessary when a new frame
from the camera is available or if there is new input from the team communi-
cation network stream. Those general modules have dependencies and produce
data which is necessary for the behaviour. The behaviour itself is described be-
low.
Next to the high level module based structure we have a diﬀerent piece of soft-
ware which provides a motion control architecture. The motion software is acting
as a service to the high level module structure and can take commands for anima-
tions, positioning of motors and furthermore encapsulates the walking algorithm.
We are using python and cython as well as C++ ranked from high level pro-
gramming of behaviour down to low level sensor/motor control and fast imple-
mentations of algorithms.

3.2 Team Communication

For the Team Communication we use the mitecom library developed by the
team FUmanoids. The shared protokoll of mitecom enables us to build mixed
teams with other teams from the Humanoid League. We have already played a
successful test game together with the team Bold Hearts in a mixed team at the
WorldCup in Brazil.

4

3.3 Localisation

We had rewritten our localisation in 2012 to be based on the Kalman Filter
and line tracking to localise the robot. However the results did not satisfy us, so
another rewrite is scheduled. This time we are working on some artiﬁcial learning
algorithm [1].

3.4 Behaviour

Based on the data from a world model and information of the mitecom (inter
robot communication) we use a decision tree-like structure to determine the
robots behaviour. We use elements of actions and decisions which we put on a
stack-like structure which holds the current path in the decision-tree. These leafs
of the tree are the actions, which determine the robots actions of movements.
This leafs are on top of the stack. Elements on top of the stack are called in each
iteration of the framework and remove themselves when done. Further other
elements in the stack have the ability to register themselves for recalculation, so
they will also be called to check the presumptions and if necessary remove parts
of the current stack.

With this structure in the one hand we deﬁne diﬀerent roles of players like
defender, striker or goalie, which are able to change dynamically. So each role
has their own part of the decision tree for their behaviour so they can switch
roles with other players who might be in a better position. On the other hand
the structure also determines the roles behaviour like moving to the ball, going
to a speciﬁc position or passing the ball to another player. Because we look
at information from the mitecom it is possible to create actions which involve
multiple robots.

3.5 Vision

Camera setup: The camera is set up independently from our vision framework.
The framework is connectable to various “camera” types. Usually we use a USB
camera but we can also use a simulator as image source or a prepared set of
test images. The camera conﬁguration is mostly done by hand but the camera
exposure is adjustable at runtime. We avoid the auto exposure to keep our colour
lookup tables relatively stable for the green detection.

Colour detection: To decide the colour of a pixel we use a lookup table for
the main RoboCup soccer ﬁeld colours green, yellow, magenta, cyan and red.
The calibration of the green colour mask is done dynamically at runtime, the
remaining colours need to be pre conﬁgured.

Field contours: We use the assumption of the green carpet as mostly present
colour to determine the ﬁeld contours. Any feature detected outside this contour
can be ignored. We use vertical scan lines to calculate a convex hull of the ﬁeld
contour. Furthermore we are able to give additional information into the vision
framework based on knowledge of the camera position when taking the image.

5

This way we can reduce the number of considered pixels for case we know they
can’t belong to any feature on the ﬁeld.

Object recognition: For the object recognition we use colour separation.
Considering only pixels of a given colour we do some shape recognition to extract
the ball, the goal or the ﬁeld lines out of the image. To determine huge obstacles
we use out layers of the calculated horizon convex hull.

Vision basis: Our image processing image access is based on randomly pre
generated point clouds. The point clouds diﬀer in the density functions of the
pixels. So we can choose the area of highest considered pixel density depending
on an image. This makes it easier to recognize small objects like the ball even
when it’s far away and reduces the number of pixels seen on a ball very close to
the robot.

3.6 Code from other Teams

Right now all of our code base is written by members or former members of
our team. We include a shared developed c team communication libary named
mitecom which is also used by other teams. Our Walking is heavily inﬂuenced
by the Team DARwIn.

4 Hardware

4.1 Mechanical Structure

For RoboCup 2012 and 2013 a standard Darwin-OP robot was used by the Ham-
burg Bit-Bots. Learning from the ﬂaws in the Darwin-OP, a modiﬁed Darwin-OP
was used for the RoboCup 2014 competition. The main change is the new head
construction, that provides a better camera protection and more reliable image
data.

In addition the team worked on a new robot platform, named GOAL, a 24
DOF robot which was brought for inspection to the RoboCup 2014, but was not
used because of software issues during the competitions.

Main diﬀerences to the Darwin-OP robot are the increased height of 86cm,
pitch and roll servos for the torso and a yaw servo for the shoulder to provide
more human like movement.

4.2 The modiﬁed Darwin-OP

The Darwin-OP robot has the following electronics:

– Actuators: The Robotis Dynamixel MX-28 servos have hall sensors to mea-
sure the position of the joint and measurement of voltage, current and the
temperature inside the servo.

– IMU: The CM 730 board provides a 3 axis accelerometer and a 3 axis

gyroscope that is used for the robots stabilization.

6

Fig. 1. One the left: GOAL standing Upright. On the right: The modiﬁed Darwin-OP
head.

– Camera: The robot is equipped with a “Logitech HD Pro Webcam B910”.

A resolution of 800x600 is used at 20 frames per second.

– Computer: The main computing board is a “Fit Pc 2i”, providing a sin-
glecore Intel Atom process which runs at 1.6 Ghz. The subcontroller is the
CM730 board by Robotis.

4.3 GOAL

GOAL has the following electronics:

– Actuators: The Robotis Dynamixel MX-28 and MX-64 servos have hall
sensors to measure the position of the joint and measurement of voltage,
current and the temperature inside the servo.

– IMU: GOAL has 2 MPU6050 chips with 3 axis gyroscope and accelerometer
per chip. It has more accuracy than the one built in the Darwin-OP robot
and enhances the stability of the robot.

– Camera: The robot is equipped with a “Logitech HD Pro Webcam B910”.

A resolution of 800x600 is used at 20 frames per second.

– Computer: The main computing board is a Odroid XU3 Lite, with an
octacore processor by Samsung, this helps with the rising requirements due
to the new environment with white goals and white ball in RoboCup 2015.
The subcontroller is a selfmade board with three independent buses for the
servo communication and a direct UART communication between the ARM
Cortex M4 with 168Mhz processor on it and the Odroid board.

7

5 Publications

Team coordination in RoboCup soccer based on natural language

Bachelor thesis about a new strategy for robot to robot communication dur-
ing RoboCup games [4]. In the last years the coordination based on the
wireless network was error-prone because of the unstable network during
the championships. Particularly with regard to ”2050” the solution is a new
communication protocol that is adapted to natural language. Robots should
exchange their most important information via speech production and lan-
guage processing.

Ball recognition based on probability distribution of shapes

Bachelor thesis in which a process was developed to determine whether a
given shape would match the soccer ball or not. It uses an elaborate edge
detection algorithm in combination with the probability distribution of the
position of edges to calculate the possibility of a given shape in the presented
image [5].

Behaviour based coordination of a multi robot scenario realized by

BDI-agents
Bachelor thesis on the modelling of a behaviour for a logistic scenario [6]. The
behaviour is realized by software agents according to the believe-intention-
desire model and then transferred to a multi robot system.

Estimation of optical-ﬂow ﬁelds in multispectral images

Bachelor thesis in which an algorithm was developed, to robustly estimate
the optical-ﬂow in an image sequence using additional information provided
by color gradients.[7] The algorithm can be used for better tracking of the
ball once it is located.

Ball veriﬁcation

Article about a ball veriﬁcation, developed for the object recognition tool
for the NAO robot in the Standard Platform League 2011 [8].

6 Statements

We assure to participate in the RoboCup 2015 Humanoid League. We further
assure that we have a person with suﬃcient knowledge of the rules and that this
person will be available as referee during the competition.

7 Video & Website

The following resources provide access to our team application video for the
tournament:

8

– http://data.bit-bots.de/application2015WC.mp4
– http://youtu.be/1Keofpf7LxA

Further material can be found at our oﬃcal homepage http://www.bit-bots.de.

8 Conclusion

We gained a lot of experience in last RoboCup seasons and are working hard
to improve our software for the coming years. We were able to begin lot of co-
operations with other teams participating in our league as well as managed to
improve our software in many aspects. Next to the software we focused on the
main aspect of our league and invested a lot of time and resources into the hard-
ware development. We hope that we can provide our ﬁrst self designed humanoid
robot to participate as a goal keeper in the tournament.
We are looking forward to see how our robots acquit themself on this years
WorldCup in China, which is also another opportunity to exchange our experi-
ences with other students and researchers from all over the world and improve
our cooperation with other teams as well as contribute to the success of hu-
manoid robotics.
We sincerely hope to again become part of this great event.

References

1. Bestmann, M.: Biologically Inspired Localization On Humanoid Soccer Playing
Robots. Bachelor’s thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2014)

2. Poppinga, M.: Intelligente Wegﬁndung humanoider Roboter am Beispiel des
RoboCup. Bachelor’s thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2014)

3. Hamburg Bit-Bots. Hamburg Bit-Bots Coderelease 2013, 2014. Available online at:

http://data.bit-bots.de/Hamburg Bit-Bots Release V2.9.3 2013.tar.gz

4. Paetzel, M.: Spielerkoordination in RoboCup-Fußballspielen mittels gesprochener
Sprache. Bachelor’s thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2013)

5. Schr¨oder, S.: Ball recognition based on probability distribution of shapes. Bachelor’s

thesis, Universit¨at Hamburg, Department of Informatics, Germany (2012)

6. Richter, A.: Verhaltensbasierte Koordination eines Multi-Roboter-Szenarios mittels
BDI-Agenten. Bachelor’s thesis, Universit¨at Hamburg, Department of Informatics,
Germany (2012)

7. Bestmann, O.: Konzeption und Implementierung eines Verfahrens zur Messung von
Verschiebungsvektoren in Multispektralbildern. Bachelor’s thesis, Universit¨at Ham-
burg, Department of Informatics, Germany (2012)

8. Einig, L., Peikert, K., Richter, A.: Ballveriﬁkation. Projektbericht, Universit¨at Ham-

burg, Department of Informatics, Germany (2012)

