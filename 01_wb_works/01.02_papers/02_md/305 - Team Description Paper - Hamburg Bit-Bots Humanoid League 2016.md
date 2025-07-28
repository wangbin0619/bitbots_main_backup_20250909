Application from Hamburg Bit-Bots for
RoboCup 2016

Marc Bestmann, Juliane B¨odeker, Fabian Fiedler, Timon Giese, Judith
Hartﬁll, Marcel Hellwig, Maxim Holand, Jessica Jobski, Wiebke Koll, Amrei
Mueller, Maike Paetzel, Martin Poppinga, Dennis Reher, Bente Reichardt,
Robin Riebesehl, Nils Rokita, Robert Schmidt, Oliver Sengpiel, Daniel Speck,
Lars Thoms, and Felix Wiedemann

Department of Informatics, Universit¨at Hamburg,
Vogt-K¨olln-Straße 30, 22527 Hamburg, Germany
info@bit-bots.de

Abstract. This Team Description Paper describes the humanoid robot
team Hamburg Bit-Bots, from its history over currently used software
and hardware to the research interests and achievements in RoboCup.
We currently focus our development on hardware to have robots capable
of playing on artiﬁcial turf. Therefore, we enhanced our open-source plat-
form Hambot and developed a second one named Minibot (cf. Chapter
4). We especially research hardware features for the robots, like diﬀerent
types of joints or pressure sensors for the feet (cf. Chapter 2).

1

Introduction

The team Hamburg Bit-Bots consists of students from the Department of In-
formatics at the University of Hamburg, Germany. The team is ﬁnancially sup-
ported by the University of Hamburg and its Department of Informatics. Apart
from that Hamburg Bit-Bots are an independent work group led and organized
solely by students.

1.1 Prior performance in RoboCup

Since 2012 our team participated in the GermanOpen (2nd place in 2013, 3rd
place in 2012 and 2014). Moreover, our participation in the WorldCup since
2012 allowed us to connect with other teams and gave us the possibility to
show our latest developments in hardware and exchange research ideas with the
international RoboCup community. In 2014 we participated in the IranOpen for
the ﬁrst time. Following this rewarding experience we participated in 2015 again
and achieved a 3rd place.

1.2 Further dedication to RoboCup

We have many further projects to push interconnectedness between teams and
support the accessibility of robotics and RoboCup to the general public. In 2014

2

we established close collaboration with another RoboCup Team from our home
town which competes in the SPL. This gave us the opportunity to host the
RoHOW1 jointly with them in 2014 and 2015. We also organized this years
RoHOW in Dresden, which was a satellite event of the German KI conference.
Moreover, we participated in “Robots on Tour” in Zurich 2013, in the “Hamburg
Night of Knowledge” and “Berlin Night of Knowledge”. In cooperation with a
school we created a yearly course in robotics for high school students which is
very successful since 2013. Furthermore, in 2014, we started to provide practical
lectures in robotics at our university which are highly attended by students.

2 Current Research

After our experiences during the German Open and World Championship in
2015, the focus of our research for 2016 was the development of hardware which
can face the challenge of walking on artiﬁcial grass. With regard to the roadmap
we shifted the focus from optimizing the Darwin OP in general to the develop-
ment of larger robots.

2.1 Walking

With larger robots the complexity of estimating the eﬀects of movements on
the stability of the robot is increased. With pressure sensors in the feet and the
IMU we assume to get suﬃcient feedback of the robot’s stability. We currently
research on an algorithm using this feedback to enhance the stability of the
walking in combination with the currently used ZMP algorithm. We want to
do this by automatically learning the eﬀects of the ZMP Walking rather than
approximating them.

2.2 Construction of new feet

In contrast to human feet robot’s feet in the HKSL are ﬂat and stiﬀ. The sole of
human feet has a structure so that only some parts touch the ground and other
parts do not. This renders the standing more stable. Human feet are also ﬂexible
in themselves which helps to adapt to the surface a foot is standing on. We’d
like to develop more human-like feet to stabilize our walking on artiﬁcial turf.

2.3 Joints, muscles and tendons

While the human body contains a hard skeleton and a lot of muscles that are used
to move the skeleton, the construction of our robots is diﬀerent. The motors work
as muscles and are a part of the robot’s skeleton. This causes much pressure on
the motors. Therefore we try to add ribbons with motors working like muscles
and tendons similar to the human joints. We hope that the pressure on our

1 Robotics Hamburg Open Workshop, www.rohow.de/en/

motors will decrease and the joints themselves will become smaller without losing
any degree of freedom. A bachelors thesis[1] about this topic has been written
by one of our team members but it showed that its diﬃcult to determine the
strain on the tendons and therefore it is not yet applicable for humanoid robots.

3

3 Hardware

3.1 Mechanical structure

For RoboCup 2012 and 2013 a standard Darwin-OP robot was used by our
team. Learning from the ﬂaws in the Darwin-OP, a modiﬁed Darwin-OP was
used for the RoboCup 2014 competition. The main change was the new head
construction, which provides a better camera protection and more reliable image
data.

In addition, the team worked on a new robot platform named GOAL, which
is a 24 DOF robot and was brought for inspection to the RoboCup 2014, but was
not used during the competitions because of software issues. Main diﬀerences to
the Darwin-OP robot are the increased height of 86 cm, pitch and roll servos for
the torso and a yaw servo for the shoulder to provide more human-like movement.
In 2015 the project was renamed to Hambot and due to the new possibility
of 3D printing at our university we were able to completely build two Hambot
robots as well as produce spare parts ourselves. The project is open source and
can be found at GitHub [8]. As it turned out walking was yet diﬃcult for the
rather heavy Hambot robots, the smaller platform Minibot could be developed
in a rather short time due to the experience with the Hambot platform. Minibot
is not only smaller than Hambot, but it has also a very similar kinematic to the
Darwins and is therefore able to walk with the old Darwin walking.

3.2 The modiﬁed Darwin-OP

The Darwin-OP robot has the following electronic components:

– Actuators: The Robotis Dynamixel MX-28 servos have Hall sensors to mea-
sure the position of the joint and measurement of voltage, current and the
temperature inside the servo.

– IMU: The CM 730 board provides a 3 axis accelerometer and a 3 axis

gyroscope that is used for the stabilization of the robot.

– Camera: The robot is equipped with a “Logitech HD Pro Webcam B910”.

A resolution of 800x600 is used at 20 frames per second.

– Computer: The main computing board is a “Fit Pc 2i”, providing a sin-
glecore Intel Atom process which runs at 1.6 Ghz. The subcontroller is the
CM730 board by Robotis.

4

Fig. 1. From left to right: Minibot, Hambot, modiﬁed Darwin-OP

3.3 Hambot

Hambot has the following electronic components:

– Actuators: The Robotis Dynamixel MX-28, MX-64 and MX-106 servos
have Hall sensors to measure the position of the joint and measurement of
voltage, current and the temperature inside the servo.

– IMU: Hambot has 2 MPU6050 chips with 3 axis gyroscope and accelerom-
eter per chip. It has more accuracy than the one built in the Darwin-OP
robot and enhances the stability of the robot.

– Camera: The robot is equipped with a “Logitech HD Pro Webcam B910”.

A resolution of 800x600 is used at 20 frames per second.

– Computer: The main computing board is an Odroid XU3 Lite, with an
ARM octacore processor. The subcontroller is a selfmade board with three
independent buses for the servo communication and a direct UART commu-
nication between the ARM Cortex M4 and the Odroid board.

3.4 Minibot

Minibot has the following electronic components:

– Actuators: The Robotis Dynamixel MX-28, MX-64 and MX-106 servos
have hall sensors to measure the position of the joint and measurement of
voltage, current and the temperature inside the servo.

– IMU: The CM 730 board provides a 3 axis accelerometer and a 3 axis

gyroscope that is used for the robots stabilization.

– Camera: The robot is equipped with a “Logitech HD Pro Webcam B910”.

A resolution of 800x600 is used at 20 frames per second.

– Computer: The main computing board is an Odroid XU3 Lite, with an
ARM octacore processor. The subcontroller is the CM730 board by Robotis.

5

4 Software

4.1 General Architecture

Our software framework (released, [7]) is split into two main parts: a cogni-
tion part for the behaviour and a motion part. The cognition part consists of a
decision making behaviour which is described below and a set of basic modules
which perform the preprocessing and the calculations required by the behaviour.
Among other things this set of basic modules contains the vision, team commu-
nication and localization as described below. The motion part is a complex state
machine acting as a service for the behaviour and can take commands for anima-
tions, positioning of motors and furthermore encapsulates the walking algorithm.
We use Python for high level programming of behaviour and Cython as well as
C++ for low level sensor/motor control and optimized implementations of algo-
rithms.

4.2 Team communication

For team communication we use a shared protocol with other teams. The so
called mitecom library was developed by the FUmanoids and is used in drop-in-
games at the Worldcup and local events. For example we played successfully in
demo-games together with the ”Bold-Hearts” in WorldCup 2014 in Brazil and
IranOpen in Tehran. Information received by the team communication is mainly
used in decision-making processes.

4.3 Localization

In the last seasons we were working on diﬀerent approaches for the localization
to adapt to the new diﬃculties. Especially because of the goals being white now
and the often hardly recognizable ﬁeld markings caused by the artiﬁcial grass, we
are working on a more robust approach. Our Monte-Carlo-Localization/ particle-
ﬁlter based approach uses a variety of features from the ﬁeld. We are also trying
to adapt SLAM-like approaches for landmarks outside the ﬁeld and using the
team communication for further improvement. Thus, we try to further improve
the result-based techniques like a Rat-SLAM based approach we used before [4].

4.4 Behaviour

Currently we are using a self written behaviour framework based on hierar-
chical state machines and decision trees. For the decision-making we are using
information obtained from several other modules, such as vision and team com-
munication, on a blackboard. We communicate abstract movement tasks like
walking slowly forward or performing a kick in the same way.

In our behaviour tree we start with more general decisions like determining
which role the robot has to perform. We distinguish three diﬀerent roles: goal-
keeper, defender and striker. Finished decisions are pushed on a stack and, if

6

needed, registered for occasionally recomputing. Decisions deeper in the tree are
more on a task level, e.g. attack and stay away. The leaves of the tree perform
certain tasks, e.g. going to the ball.

For pathﬁnding and aligning to the ball we use an oﬄine trained neural

network based on ball and goal positions [5].

4.5 Vision

Camera setup: The image processing is independent from the image sources
due to our modularized vision framework. The images can either be retrieved
from the webcam or an alternative source like the simulator or recorded images.
We implemented converters to be able to use several image formats like YUYV,
RGB and BGR.

Colour detection: A subset of the pixels are assigned to one or more cate-
gories. This is done via lookup tables. Currently we use this technique to classify
white pixels, turf, obstacles and team markers. The green of the turf is adapted
during runtime because it highly depends on the angle at which we look at the
ﬁeld.

Vision basis: Our image processing is based on randomly pre-generated
point clouds. The point clouds diﬀer in density functions of the pixels, so that
we can choose the area of highest considered pixel density depending on an
image. This makes it easier to recognize small objects like the ball even when it
is far away and reduces the number of pixels representing near objects.

Field contours: Due to the carpet being green we assume green to be the
most represented colour. This assumption is utilized for determining the ﬁeld’s
contours. Any feature detected outside this contour can be ignored. We use
vertical scan lines to calculate a convex hull of the ﬁeld contour. Furthermore
we are able to feed additional information into the vision framework based on
knowledge of the camera position when taking an image. Therefore the number
of considered pixels is reduced if the corresponding areas do not belong to any
feature on the ﬁeld.

Object recognition: For the object recognition we use colour separation.
Considering only pixels of a given colour we perform shape recognition to extract
the ball, the goal or the ﬁeld lines. To detect huge obstacles we look for dents in
the horizon line.

Test data: To further improve our algorithms we need the ability to simu-
late or replay realistic boundary conditions. Because a simulated environment
is not always lifelike, we implemented a mode in which the robot can record
images as well as kinematic information for the triangulation of positions on the
ﬁled and localization of the horizon. For quick tests which don’t need kinematic
information, the vision can be run with graphical output on a laptop.

4.6 Code from other teams

Right now our code base is fully written by members or former members of our
team. We include a cross-team developed C communication libary named mite-

com which is also used by many other teams. Our walking is heavily inﬂuenced
by the Team DARwIn.

7

5 Publications

Design and Control of Biologically Inspired Joints

In this thesis a biologically inspired joint operating with tendons and the
controlling of such with neural networks is developed. Joints operated by
tendons have some advantages over motors directly in the joint, e.g. the
elastic properties of the joint can protect the motor from the forces if the
robot falls down.[1]

Development of a user-interface for realtime editing of robot anima-

tions
This work covers the design and implementation of a user-friendly applica-
tion to generate and edit static robot-animations (or motions) in realtime
directly on a robot via an arbitrary text-terminal.[2]

Hambot: An Open Source Robot for RoboCup Soccer

In this paper we present our newly developed soccer robot platform Hambot.
Hambot can be produced entirely using 3D-printing. [9]

Development of a stable robot walking algorithm using center-of-

gravity control
Bachelor thesis of the implementation of a walking algorithm, which is based
on capture steps, as described in [10]. This thesis concludes, that the cap-
ture steps are not applicable for our robot hardware [3]. In this context, we
also improved our inverse kinematics, which is conceptually inspired by the
FUmanoids.

Estimation of optical-ﬂow ﬁelds in multispectral images

Bachelor thesis in which an algorithm was developed to robustly estimate
the optical-ﬂow in an image sequence using additional information provided
by color gradients [6]. The algorithm can be used for better tracking of the
ball once it is located.

6 Statements

Participate

We assure to participate in the RoboCup 2016 Humanoid League.

Referee

We further assure that we have a person with suﬃcient knowledge of the rules
and that this person will be available as referee during the competition.

8

7 Video & website

The following resources provide access to our team application video for the tour-
nament: http://data.bit-bots.de/applications/application2016.mp4 . Further ma-
terial can be found at our oﬃcal homepage: http://www.bit-bots.de.

8 Conclusion

We gained a lot of experience during the last RoboCup seasons and are working
hard on improving our hardware and software for the upcoming years. Further-
more we started many cooperations with other teams participating in our league.
We consider the possibility of developing custom platforms one of the most excit-
ing aspects of our league. Hence we recently invested a lot of time and resources
into hardware development.

We are looking forward to see how our robots compete at this year’s WorldCup
in Germany, which is also another opportunity to exchange our experiences with
other students and researchers from all over the world and improve our coopera-
tion with other teams as well as contribute to the success of humanoid robotics.
We sincerely hope to again become part of this great event.

References

1. Rokita, N.; Design and Control of Biologically Inspired Joints. Bachelor thesis, Uni-

versit¨at Hamburg, Department of Informatics, Germany (2015)

2. Giese, Timon.: Development of a user-interface for realtime editing of robot anima-
tions. Bachelor thesis, Universit¨at Hamburg, Department of Informatics, Germany
(2015)

3. Schmidt, R.: Development of a stable robot walking algorithm using center-of-
gravity control. Bachelor thesis, Universit¨at Hamburg, Department of Informatics,
Germany (2015)

4. Bestmann, M.: Biologically Inspired Localization On Humanoid Soccer Playing
Robots. Bachelor thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2014)

5. Poppinga, M.: Intelligente Wegﬁndung humanoider Roboter am Beispiel des
RoboCup. Bachelor thesis, Universit¨at Hamburg, Department of Informatics, Ger-
many (2014)

6. Bestmann, O.: Konzeption und Implementierung eines Verfahrens zur Messung von
Verschiebungsvektoren in Multispektralbildern. Bachelor thesis, Universit¨at Ham-
burg, Department of Informatics, Germany (2012)

7. Hamburg Bit-Bots. Hamburg Bit-Bots Coderelease 2015. Available online at:

http://data.bit-bots.de/CodeReleaseHamburgBitBots2015.tar.gz

8. The mechanical parts of the open source robot Hambot are available at

https://github.com/bit-bots/hambot

9. Marc Bestmann, Bente Reichardt, Florens Wasserfall. Hambot: An open source
robot for robocup soccer. 19’th RoboCup international Symposium, Hefei, 2015
10. Marcell Missura and Sven Behnke. Balanced walking with capture steps. 18’th

RoboCup international Symposium, Joao Pessoa, 2014

