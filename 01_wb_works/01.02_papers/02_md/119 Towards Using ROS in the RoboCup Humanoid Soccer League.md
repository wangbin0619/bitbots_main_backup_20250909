MASTERTHESISTowardsUsingROSintheRoboCupHumanoidSoccerLeaguevorgelegtvonMarcBestmannMIN-FakultätFachbereichInformatikTechnischeAspekteMultimodalerSystemeStudiengang:InformatikMatrikelnummer:6209584Erstgutachter:Prof.Dr.JianweiZhangZweitgutachter:Dr.NormanHendrichAbstract

Sharing software modules between teams in the RoboCup Humanoid League is dif-
ﬁcult since all teams use diﬀerent frameworks. This leads to reimplementation of
software which slows the research process. A common framework for the league
would resolve this. Therefore, this thesis proposes a ROS-based architecture which
is deﬁned by a set of ROS messages. The teams can decide on the speciﬁc implemen-
tation of nodes since the messages provide the interfaces. Diﬀerent tools, especially
for visualization, are implemented to be used in conjunction with this architecture.
Furthermore, the robot control module of the team Hamburg Bit-Bots is transferred
into the new framework to show its usability. The architecture is compared to others
and its performance is evaluated.

The presented architecture makes sharing software modules easier and can thereby
accelerate the research in the RoboCup Humanoid League. Furthermore, the entry
of new teams is simpliﬁed, due to the availability of shared modules.

Zusammenfassung

Der Austausch von Softwaremodulen zwischen Teams der RoboCup Humanoid
League ist schwierig, da alle Teams unterschiedliche Frameworks benutzen. Dies
f¨uhrt zu Neuimplementation von Software, wodurch der Forschungsprozess ver-
langsamt wird. Ein gemeinsames Framework f¨ur die Liga k¨onnte dieses Problem
l¨osen. Daher stellt diese Masterarbeit eine auf ROS basierte Architektur vor, welche
durch einen Satz von ROS Nachrichten deﬁniert ist. Verschiedene Werkzeuge die in
Verbindung mit dieser Architektur benutzt werden k¨onnen, besonders f¨ur Visual-
isierungen, wurden implementiert. Außerdem wurde das ”robot control module” der
Hamburg Bit-Bots in das neue Framework transferiert um dessen Benutzbarkeit zu
zeigen. Die Architektur wurde mit anderen verglichen und ihre Leistungsf¨ahigkeit
wurde evaluiert.

Die pr¨asentierte Architektur erleichtert den Austausch von Softwaremodulen und
kann dadurch die Forschung in der RoboCup Humanoid League beschleunigen.
Außerdem wird der Einstieg f¨ur neue Teams in die Liga erleichter, da sie die geteilten
Module benutzen k¨onnen.

Contents

1 Introduction

1
1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
3
1.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Thesis Goals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

2 Fundamentals

13
2.1 RoboCup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.2 Humanoid Robots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.3 Robot Operating System . . . . . . . . . . . . . . . . . . . . . . . . . 17

3 Hardware and Software

27
3.1 Minibot
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2 Bit-Bots Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

4 Architecture

33
4.1 Basic Concept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.3 Message Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

5 Implementation

45
. . . . . . . . . . . . . . . . . . . . . . . 45
5.1 Humanoid League Packages
5.2 Hamburg Bit-Bots Packages . . . . . . . . . . . . . . . . . . . . . . . 48

6 Evaluation

59
6.1 Architecture Comparison . . . . . . . . . . . . . . . . . . . . . . . . . 59
6.2 Transfer process to ROS . . . . . . . . . . . . . . . . . . . . . . . . . 65
6.3 Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
6.4 Community Building . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
. . . . . . . . . . . . . . . . . . . . . . . . . 68
6.5

Inﬂuence on the League

7 Conclusion

69
7.1 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.2 Further Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

8 Appendix

Bibliography

71

83

iii

Contents

iv

List of Figures

4
1.1 Statistic of publications regarding ROS and RoboCup . . . . . . . . .
5
1.2 Example of an architecture using the B-Human framework . . . . . .
6
1.3 Example of a RoboGram . . . . . . . . . . . . . . . . . . . . . . . . .
8
1.4 The three primitives in robotics . . . . . . . . . . . . . . . . . . . . .
1.5 The three paradigms in robotics . . . . . . . . . . . . . . . . . . . . .
9
1.6 Statistic of ROS usage in RoboCup . . . . . . . . . . . . . . . . . . . 11

2.1 List of all RoboCup Leagues . . . . . . . . . . . . . . . . . . . . . . . 13
2.2 Picture of a Humanoid League soccer ﬁeld . . . . . . . . . . . . . . . 15
2.3 Picture of the Asimo robot . . . . . . . . . . . . . . . . . . . . . . . . 16
2.4 Example ROS architecture for a simple wheeled robot . . . . . . . . . 18
2.5 Example ROS messages
. . . . . . . . . . . . . . . . . . . . . . . . . 18
2.6 Connection procedure between nodes . . . . . . . . . . . . . . . . . . 20
2.7 Example of a package.xml
. . . . . . . . . . . . . . . . . . . . . . . . 21
2.8 Screenshot of the rqt interface . . . . . . . . . . . . . . . . . . . . . . 24
2.9 Screenshot of the RViz interface . . . . . . . . . . . . . . . . . . . . . 24

3.1 Picture of the Minibot . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2 Picture of the Dynamixel servo motors . . . . . . . . . . . . . . . . . 28
3.3 Presentation of the daisy chained TTL bus . . . . . . . . . . . . . . . 29
3.4 Overview of the original Hamburg Bit-Bots architecture . . . . . . . . 30
3.5 Example of the module architecture . . . . . . . . . . . . . . . . . . . 31

4.1 The basic concept of the proposed architecture . . . . . . . . . . . . . 34
4.2 Simpliﬁed overview of the tasks and information ﬂow . . . . . . . . . 35
4.3 Overview of the deﬁned messages in context . . . . . . . . . . . . . . 37
4.4 High granulated example implementation . . . . . . . . . . . . . . . . 38
4.5 Low granulated example implementation . . . . . . . . . . . . . . . . 39

5.1 Screenshot of the implemented visualization tools
. . . . . . . . . . . 47
5.2 Simulated RoboCup Soccer environment
. . . . . . . . . . . . . . . . 49
Implementation of robot control and hardware communication . . . . 50
5.3
5.4 UML state diagram of the HCM state machine . . . . . . . . . . . . . 51
5.5 UML sequence diagram of the HCM main thread . . . . . . . . . . . 52
. . . . . . . . . . . . 53
5.6 UML class diagram of the bitbots hcm package
5.7 Visualization of the state machine . . . . . . . . . . . . . . . . . . . . 54
. . . . . . . . . . 56
5.8 UML activity diagram for an animation action call
. . . . . . 57
5.9 Three diﬀerent visualizations of the Minibot URDF model

v

List of Figures

6.1 The architecture of the NimbRo robot
. . . . . . . . . . . . . . . . . 60
6.2 Nodes of the NimbRo architecture . . . . . . . . . . . . . . . . . . . . 61
6.3 Comparison of standard and NimbRo messages
. . . . . . . . . . . . 62
6.4 The ROS nodes and topics of the team WF Wolves . . . . . . . . . . 64
6.5 CPU loads of the nodes . . . . . . . . . . . . . . . . . . . . . . . . . . 66
. . . . . . . . . 67
6.6 Latencies between sending and receiving of messages
. . . . . . . . . . . . . . . . . . . . . . . . . 67
6.7 Comparison of latencies

vi

1 Introduction

The RoboCup Foundation was founded to enhance the progress in autonomous
robotics by proposing competitions with standard scenarios for research. The most
important league is the humanoid soccer league, where robots compete in a modiﬁed
rule set of human soccer to achieve the goal of winning against the FIFA world cup
champions with a team of robots in the year 2050. This goal gives the competing
teams a motivation and the game is a basis for comparison of diﬀerent approaches.
Even though RoboCup is a competition, most of the teams publish their code
and hardware to accelerate the research process. But due to the complex software
systems running on the robots, the eﬀective transfer of code between teams is al-
most nonexistent. Therefore this thesis proposes a way to ease code exchange by
a transition to the Robot Operating System (ROS), an open source framework for
robot programming. Furthermore, standard messages will be proposed for the spe-
ciﬁc ﬁeld of robot soccer. To validate the eﬀectiveness of this approach, the current
software of the Hamburg Bit-Bots will be transferred to ROS and its performance
will be tested.

The structure of the thesis is as following: First, the topic is motivated in section
1.1, related work is discussed in section 1.2 and the concrete goals are stated in
section 1.3. Then the fundamentals are explained in section 2. Afterward, the used
hardware and software components are explained in section 3. The approach is
explained in section 4 and its implementation examined in section 5. An evaluated
of this implementation is presented in section 6. Finally, the thesis is concluded in
section 7.

1.1 Motivation

While the idea of RoboCup Soccer, with a mixture of competitions and exchange,
is a good approach in theory to accelerate the research, some problems still remain.
One of the biggest is the sharing of software. Many teams share their code base using
services like GitHub, but due to their monolithic architectures, specialized frame-
works and hardware speciﬁc code, actually using parts of other team’s software is
diﬃcult. The resulting barriers lead to a waste of time due to reprogramming of ex-
isting software. An example is the de facto standard motor, the Robotis Dynamixel,
which is used by almost all teams, but every team has its own code for control.

The lack of usable modules generates a high entry threshold for new teams because
they have to implement many algorithms from scratch in order to be able to perform
the basic tasks needed to participate. Therefore the RoboCup Federation is trying
to solve these problems [Gerndt et al., 2015].

1

1 Introduction

One way to simplify code exchange is using a common framework or middleware.
The Robot Operating System (ROS) [Quigley et al., 2009] is a good choice because
it has a large community, is already widely used in research and supports many
diﬀerent robots [Gerkey, 2015]. It also provides a large set of standard libraries and
message types, as well as simulation and debug tools.

In other RoboCup leagues, especially RoboCup Rescue, this is already more
widespread (see section 1.2). There are also a few teams in the Humanoid Soc-
cer League which are already using it (cp. 1.2.1). This is a ﬁrst step in the right
direction because the structure is less monolithic due to the split into diﬀerent ROS-
nodes, but the problem of sharing code still persists. Even if two teams have each
one node for the same task, e.g. ball detection, the subscribed and published mes-
sages are most likely not the same. This is understandable because there exist no
standards for these messages. The messages speciﬁed by ROS are mostly regarding
general sensor input, actuator control, and navigation. In RoboCup Soccer exist
diﬀerent kinds of information that are not commonly communicated in other con-
texts. Therefore no messages exist which are standardized by ROS. Proposing an
additional set of messages can be useful to make nodes substitutable with others. It
would also increase the ability to compare the performance of two nodes with each
other.

Another point, which will increase its importance in the future, is the collaboration
of robots of diﬀerent teams. The road map of the RoboCup Humanoid League [11]
shows that the number of playing robots will increase in the future from currently
four to the normal player count for soccer, eleven. An even higher number of robots
is needed when counting substitute players. This will force teams to join their
robots into a mixed team. Doing this with completely diﬀerent software frameworks
is theoretically possible, but not practical.

The Hamburg Bit-Bots are a team of students which has been participating in the
RoboCup Humanoid League since 2011. Until now they did not use ROS or any other
framework for their software and based everything on a self-programmed mixture
of shared memory inter process communication (IPC) and a modiﬁed blackboard
system. Transferring their software to an ROS architecture does not only serve
as an example and test for the proposed use of ROS in the humanoid league, but
also results in a collection of open source packages which can be used by other
teams. Last but not least, the architecture change will also ease the work of the
Hamburg Bit-Bots, because a modular system is simpler to maintain. Especially
in the context of having only students working on the software, who don’t have
a ﬁnished education and who are working on this project for a comparably short
time. The modularization enables them to work on one part of the software without
having knowledge about the others.

The robots that are currently used by the Hamburg Bit-Bots, shall be used to
validate the proposed architecture in terms of usability and performance. The Mini-
bot, created by the Hamburg Bit-Bots, is an upscaled version of the Darwin-OP
[Ha et al., 2011]. It was needed because the Darwin-OP will soon no longer be al-

2

1.2 Related Work

lowed to participate due to an increase of the minimal robot size in the league’s
rules [11]. The Minibot is a good example platform as it is similar to most robots
in the league. To put it in a nutshell, the transfer to a ROS-based architecture shall
modularize and parallelize the software, ease the exchange between teams, lower the
entry diﬃculties of new teams and enable the use of standard messages, libraries, and
simulators. Together with the open source hardware of the Minibot, the software
framework shall provide an easy to access platform.

1.2 Related Work

When looking at the number of publications corresponding to RoboCup and ROS,
it is clear to see that ROS is becoming more and more popular. The ﬁrst paper
about ROS was written in 2009 [Quigley et al., 2009], since then its popularity in-
creased enormously [Gerkey, 2015]. While the RoboCup-related publications were
stagnating during this time, the number of ROS-related ones already excelled them
in 2015 (see ﬁg 1.1).

1.2.1 Publications in RoboCup

The ﬁrst publication in the RoboCup proceedings concerning ROS, about an exter-
nal system for ﬁnding a ground truth, was in 2011 [Khandelwal and Stone, 2011].
The year after, only one other paper was using ROS and only for comparison with
their result [Ruiz et al., 2013]. In 2013, the number rose to 13 including more im-
pacting papers. But until 2016, the number dropped back to zero. This doesn’t
mean, that the teams stopped using ROS again. It shows that there was a wave
when teams started to use ROS in diﬀerent leagues which resulted in publications
about this integration. Afterward, no further papers were written about it, but the
usage was still high in 2016 (cp. ﬁgure 1.6).

Rescue League

The Rescue League started early to advertise the use of ROS with the goal of an
easier exchange between teams. In 2010 and 2011, they organized workshops for the
league and in 2012 even a complete summer school [Kohlbrecher et al., 2012]. This
resulted in a release of a corresponding ROS meta package [Kohlbrecher et al., 2013]
by team Hector. A package which was used and kept up to date. Additionally, in
2013, the ROS support for the ”Uniﬁed System for Automation and Robot Simula-
tion” (USARSim), was added by a RoboCup team [Kootbally et al., 2013]. In 2014,
team Hector stated that using open source software and ROS helped to achieve
reliable autonomy in search and rescue [Kohlbrecher et al., 2014].

3

1 Introduction

Figure 1.1: Distribution of publications containing the three terms: ”robot operat-
ing system”, robocup, robocup ”robot operating system”. The data is
based on Google Scholar and was generated by an external tool [1]. The
graph shows a steadily increasing number of publications per year using
the term ”Robot Operating System”. Publication numbers concerning
RoboCup in general were relatively stable over the last ten years but
publications concerning ROS and RoboCup have risen. This indicates
an increasing interest in ROS inside the RoboCup community.

Standard Platform League (SPL)

The most used framework in the Standard Platform League is based on the code
of the B-Human team which is published annually since 2008. This is possible
because all teams use the same robot, the NAO [Gouaillier et al., 2008]. B-Humans
architecture consists of modules which perform computations based on data which
is provided by representations, see ﬁgure 1.2. These are C++ classes that are stored
in a blackboard. Each process has its own blackboard and representations can be
shared between processes.

This architecture was compared to ROS in 2013 [R¨ofer and Laue, 2013]. The
authors stated that the parallel architecture of ROS was not useful on the single-core
NAO robot. As the custom B-Human framework was already spread in the league,
they saw no need for changing towards ROS. In the same year, another paper was
published about the transfer towards ROS in the SPL [Forero et al., 2013]. The
authors wrote that it is too hard for new teams to adapt the code from B-Human,
leading to a reuse of the software stack with almost no own modiﬁcations.

4

 0 500 1000 1500 2000 2500 2000 2002 2004 2006 2008 2010 2012 2014 2016number of publicationsyear"robot operating system"robocuprobocup "robot operating system"1.2 Related Work

Figure 1.2: Example of an architecture for a robots vision using the B-Human frame-
work [R¨ofer and Laue, 2013]. The ellipses are representations which pro-
vide data and the rectangles are modules which perform computations.
The architecture looks similar to ROS but the representations are not
handled peer-to-peer but using a blackboard system.

The authors stated that the use of ROS could allow:

• ”to share easily software module between teams,
• to encourage the development of very specialized solutions which can be shared

among the teams,

• to facilitate the incorporation of new teams in the league,
• to attract new students and new researchers to the leagues teams,
• to encourage the specialization of some teams in some robot control areas (e.g.

motion control or perception), and
the

• to facilitate

comparison and benchmarking of

speciﬁc

software

modules.”[Forero et al., 2013]

Furthermore, the authors deﬁned messages for the migrated motion component
of B-Human. Unfortunately, they did not deﬁne general messages which would be
typically used in RoboCup.

a

In

2014

proposed
the
[Mamantov et al., 2014].
The authors compared it to frameworks used at
this point in the SPL, stating that most of the teams are using a modiﬁed

new non-ROS-architecture

SPL was

for

5

1 Introduction

Figure 1.3: Example of a RoboGram with four modules [Mamantov et al., 2014].
Each module can specify OutPortals and InPortals which can con-
nect to other modules synchronously or asynchronously to transfer data.
Each RoboGram is run in one thread of execution and calls its modules
successively.

blackboard design. They wanted to change this but not by using ROS due to the
complications of running it on the NAO robot. Similar to the mentioned paper
by B-Human, the reason for not using ROS was mainly the hardware of the NAO
robot. Their proposed architecture was very close to the publisher-subscriber model
of ROS. They are using OutPortals and InPortals which form synchronous or
asynchronous connections between modules, as shown in ﬁgure 1.3. The transferred
data is also speciﬁed by messages. Multiple modules form together a RoboGram
which has one thread of execution and is sequentially calling a run() method on
its modules, in an order depending on their connections.

Humanoid League

The humanoid league has no commonly used robot platform like the SPL, but dur-
ing the last years, many teams in the Kid-Size used the Darwin-OP. Therefore a
framework for this robot, made by Team DARwIn and UPennalizers, was relatively
widespread [McGill et al., 2013]. But as the use of the Darwin-OP decreased and
Team DARwIn stopped participating in the league, the framework was not further
maintained.

6

1.2 Related Work

In 2013, the NimbRo-OP was released, ﬁrst with a framework based on the Dar-
win, but later with full ROS support [Schwarz et al., 2013]. This was the beginning
of a development towards bigger robots in the Kid-Size and the ﬁrst step towards
using ROS. Unfortunately this robot still had some ﬂaws in hard- and software.
While the framework was released on GitHub [12] and further updates were promised
[Allgeuer et al., 2013], there were no further commits after one month. Furthermore,
the package infrastructure was done badly. The package.xml ﬁles are not completed,
the packages are not registered in the ROS wiki and all packages are placed in one
GitHub repository. This hinders contributions to speciﬁc packages. Also, the fact
that there were no new commits to the git, is not inviting for contribution.

On the hardware side, the robot was diﬃcult to build by yourself, mainly due to
the used carbon ﬁber which is diﬃcult to manufacture but also due to the lack of
documentation. The CAD ﬁles were published as .step in another GitHub repos-
itory [12], but similar to the software git, there were no further commits after one
month, no documentation and only a promise that it will be added later. These
problems lead to the fact that no other teams used the NimbRo-OP in RoboCup.
But it greatly inﬂuenced the design of other platforms with a ROS framework. The
team WF Wolves used it as a base to build an own robot with another ROS-based
architecture [Anders et al., ]. Furthermore, the NimbRo-OP inspired the MU-L8,
a robot for RoboCup with a ROS framework [Stroud et al., 2013] [Stroud et al., ].
Unfortunately, neither the CAD ﬁles nor the software can be found on the Internet.
The corresponding page of the university was not updated since 2014 [13].

In 2015, Robotis released an ROS based framework [14] for the Robotis-OP (for-
merly known as Darwin-OP). Fortunately, they split the code into diﬀerent packages,
but they didn’t put it on the ROS wiki. Furthermore, the release came too late to
be used in RoboCup, since teams already started to use other robots.

In 2015, the igus Humanoid-OP was released by the constructors of the NimbRo-
OP. Based on the same skeleton and mostly the same hardware, it is principally a
change in manufacturing method towards 3D printing [Allgeuer et al., 2016]. Un-
fortunately, the same mistakes already done with the NimbRo-OP were made again.
The CAD ﬁles are only available as .step without documentation [15], the software
is not documented in the ROS wiki and only in one GitHub repository [16]. Like in
the NimbRo-OP repository, no active development or contribution can be observed.
All these robots in the humanoid league are using the same motors (Robotis Dy-
namixel Line), the same motor communication protocol, the same motor controller
board and ROS, but still, no common code is used. There exists even an open source
ROS package for controlling the Dynamixel motors, which is also not used.

1.2.2 Publications Outside RoboCup

Naturally, there was work done on the subject of humanoid robot control using
ROS outside the RoboCup. Still, most publications are rather concerning wheeled
robots. While certain problems, e.g. computer vision, remain the same and results

7

1 Introduction

from wheeled robots can be transferred, some problems are completely humanoid
speciﬁc. One example for this is the bipedal gait. There are not many papers related
to ROS on this topic since the researchers are trying to ﬁnd a solution for a certain
problem which doesn’t need integration into a full architecture and therefore they
don’t need to use ROS.

There are alternative middlewares

to ROS. The most known are Play-
er/Stage project [Gerkey et al., 2003], YARP [Metta et al., 2006] and OROCOS
[Bruyninckx, 2001]. All of them are designed for all types of robots but none oﬀers
special advantages for humanoid robots. Since they have no advantage over ROS,
which is most widespread, there is no gain in using one of them.

Three general paradigms are currently present for robot control architectures:
hierarchical, reactive, and hybrid deliberative/reactive [Murphy, 2000]. These are
presented in ﬁgure 1.5. They are all based on three commonly accepted primitives
of robotics: Sense, Plan, Act. The primitives can be deﬁned based on their input
and output, cp. ﬁgure 1.4.

The hierarchical paradigm is the oldest one. It strictly follows the three steps of
sensing, planning and acting sequentially in a loop. It often collects all information
in a global world model which is then used to make decisions in the planning step.
The advantage of this paradigm is that it can use elaborated plans, but it can be
diﬃcult aggregate a good model, depending on the environment.

A more biologically inspired paradigm is the reactive one.

It has no planning
step but directly maps sensor information to an action. Multiple of these reactive
behaviors are run in parallel to achieve an overall behavior of the robot. It has a fast
execution time, but, due to the missing planning phase, the complexity of achievable
behaviors are limited.

The third paradigm, hybrid deliberative/reactive, tries to solve this problem by
adding another kind of planning to the reactive paradigm. The robot planning
consists of a decomposition of the task into subtasks. These subtasks are then
executed by reactive behaviors. To be able to do this, the sensed data has to be
available to the planner, as well as to the behaviors.

Robot Primitives
Sense
Plan
Act

Input
Sensor data
Information (sensed and/or cognitive) Directives
Sensed information or directives

Output
Sensed information

Actuator commands

Figure 1.4: The three commonly accepted primitives in robotics with their in- and
output [Murphy, 2000]. Sense extracts information from the sensor data.
Plan decides on directives based on the available information. Act moves
the actuators based on sensed information or directives.

8

1.2 Related Work

Figure 1.5: The three general paradigms in robotics [Murphy, 2000]. The hierarchi-
cal paradigm uses a loop of sense-plan-act which often includes a global
model. The reactive paradigm has multiple parallel behaviors without
planning phase. In the hybrid paradigm, the planning is done by de-
composition of the task into subtasks which are executed by reactive
behaviors.

1.2.3 ROS Usage in RoboCup

Every RoboCup team has to write a technical report about the teams’ hard- and
software in order to participate in the championships. These are called team de-
scription paper (TDP). It is thereby possible to get a good estimation of the number
of teams which were using ROS in the last year by looking at these papers. It is
often diﬃcult to see how far the team is using ROS since the description of the
architecture is often rather short. Furthermore, it can happen that a team is using
ROS but not mentioning it in the TDP. Thereby the statistic in ﬁgure 1.6 is a lower
boundary for teams that use ROS at least in some part.

The distribution of ROS in the diﬀerent leagues is very heterogeneous. For some
leagues, it is clear that using ROS would not be possible due to limited hardware,
e.g. Standard Platform League. In others, the tasks are not controlling an actual
robot, e.g. Rescue Agent Simulation, and therefore it is not useful to use ROS. ROS
is used the most outside of RoboCup Soccer. This is due to the fact that these
robots have wheels and have to do navigation using SLAM. Therefore the standard
ROS navigation stack is often used. In the soccer leagues, the area is clearly deﬁned
and simple enough to be abstracted to a 2D plane. Creating maps is not needed
and localization can be done using simple transforms to recognized ﬁeld features.

In the Humanoid League, ROS is more used in the taller sub-leagues. This is
probably connected to the fact, that the Kid-Size League was mostly using Darwin-

9

SensePlanActHierarchical/Deliberative ParadigmReactive ParadigmSenseActHybrid Deliberative/Reactive ParadigmSenseActPlan1 Introduction

OPs and similar small robots which had not enough computing power or multiple
cores to run ROS eﬀectively. In the last years, a growth in robot size and thereby also
a growth in computational performance was observable, removing the limitations of
using ROS for many teams.

1.2.4 Summary

The RoboCup Foundation tries to encourage the sharing of code and therefore the
use of a suitable software architecture. The most common candidate for a middle-
ware is ROS. Other leagues are already widely using it, leading to an acceleration of
progress inside RoboCup but also to an impact in general research. Only the ﬁrst
steps have been made in the humanoid league for now, but the possibilities look
promising.

1.3 Thesis Goals

The main goal of this thesis is building a general software framework for diﬀerent
humanoid robots. It should provide an architecture adapted to the RoboCup con-
text, but also usable in general research. While it will be based on the existing code
of the Hamburg Bit-Bots, the ROS paradigms and mechanisms should be used as
far as possible. The architecture should be modular enough to enable exchange and
comparison of nodes with other teams. This includes also using the standard ROS
libraries, e.g. “tf”, for expanding compatibility with other ROS nodes. To ease the
exchange further, a set of standard messages which apply to the RoboCup Soccer
context shall be deﬁned. Also, a set of nodes for the basic abilities, e.g. commu-
nicating between team member robots, shall be released as packages and shared
between teams.

The parallelism of the code shall be increased from using currently two cores
to using at least eight cores, which are currently available on the Minibot. Other
teams should be included in this process to ensure, that the resulting architecture
actually works for other teams. After ﬁnishing, the architecture shall be tested on
the Minibot of the Hamburg Bit-Bots in terms of performance and compared to the
existing architecture.

10

1.3 Thesis Goals

Figure 1.6: Lower boundary of teams using ROS at least in a part of their software
in the championship 2016. The data was collected by examining the
team description papers [17]. Therefore only teams are counted which
wrote that they are using ROS. The chart shows that the overall use
of ROS is high in RoboCup, especially if the simulated leagues are not
counted. The percentage of usage in the leagues with humanoid robots
(ﬁrst four) is less than in the rest, where wheeled robots are used. It is
possible that this is connected to the available computing power, which
was signiﬁcantly lower on humanoid robots in the last years. Since us-
ing ROS results in a performance overhead, most teams with humanoid
robots wrote their own performance oriented frameworks.

11

Humanoid Kid SizeHumanoid Teen SizeHumanoid Adult SizeStandard PlattformMiddle SizeSmall SizeSimulation 2DSimulation 3DRescue RobotRescue Agent SimulationRescue Virtual Robot Simulation@home@WorkLogistics05101520250510152025132317522831925106201985723Teams not using ROSTeams using ROS1 Introduction

12

2 Fundamentals

In this chapter, the fundamentals for understanding the thesis’ topic will be ex-
plained. First, the RoboCup environment will be presented in 2.1. Then humanoid
robots will be described in section 2.2. In the end, the Robot Operating System
(ROS) will be explained in section 2.3.

2.1 RoboCup

The RoboCup is an initiative to make
robotic research more comparable and to
increase its visibility to the public. It was
founded in 1992 with the oﬃcial goal to win
against the human soccer world champion
with a team of robots by the year 2050 [18].
To achieve this, every year a world champi-
onship is held, where teams of researchers
from all over the world let their robots com-
pete against each other. Over the years also
diﬀerent local events, e.g. German Open
and Iran Open, have evolved to give more
chances for comparison. The RoboCup con-
sists of diﬀerent leagues, which do not all
play soccer. There are also leagues for in-
dustrial operation, home robotics, and res-
cue robots, see ﬁgure 2.1. As this thesis is
focused on humanoid robots, both concern-
ing leagues are presented in the following.

2.1.1 Standard Platform League

RoboCupSoccer

RoboCupRescue

RoboCup@Home

Humanoid
SPL
Middle Size
Small Size
Simulation
Robot
Simulation
Open Platform
Domestic SP
Social SP

RoboCupIndustial @Work

RoboCupJunior

Logistics
Soccer
OnStage
Rescue

Figure 2.1: The RoboCup Leagues
and their categories
for
2017. SP means standard
platform.

The Standard Platform League (SPL) was introduced with the goal to let the re-
searchers only focus on the software. Therefore all teams use the same robot, a NAO
from the company Aldebaran [Gouaillier et al., 2008]. This does not only make the
software more comparable but also more exchangeable due to the same hardware
platform. As the developers can focus on the software, the speed of the development
progress is high and games in this league are already quite ﬂuent.

13

2 Fundamentals

2.1.2 Humanoid League

The Humanoid League (HL) gives every team the freedom to buy or build their
own humanoid robot, which only has to ﬁt in a set of measurements to ensure that
it’s humanoid enough. All non human sensors, e.g. depth cameras or laser-range
ﬁnders, are forbidden. The robots are divided in three size classes: Kid-, Teen- and
Adult-Size. Although some de facto standards for the basic layout of the robots have
evolved, most teams have very diﬀerent robots. This makes exchanging code more
diﬃcult since it has to be abstracted from the hardware. Therefore, the progress of
the HL is not as far as the SPL, where no abstraction from the hardware is needed.
Most teams in the HL have still problems with basic control of their robots, e.g.
walking.

2.1.3 The Game

Both leagues play with almost the same rules and in almost the same environment.
It consists of a 9m x 6m ﬁeld made of carpet (SPL) or artiﬁcial grass (HL), two goals
and soccer line markings. Robots can communicate with each other via WiFi and get
the current state of the game from an external computer also via WiFi. All robots
have to act autonomously and can therefore only use the data of their sensors and the
communicated data of their teammates for decision making. The most important
information are the position of the ball relative to the robot and the robot’s position
on the ﬁeld which is mostly determined by the goals and line markings. Additional
data are the positions of team mates and opponents. Based on this the robots try
to kick the ball in direction of the opponent goal to eventually score a goal. Passes
and more complex team behavior are rarely used for the moment, especially in the
HL.

The referee team consists of two normal referees and one referee sitting at a
computer next to the ﬁeld. This computer runs a software called game controller
which is transmitting the current status of the game, e.g. goals and remaining time,
to the robots. It also tells robots when they get a penalty. These robots have to
listen to this command and are not allowed to move while having a penalty.

2.2 Humanoid Robots

”A humanoid robot is a robot that has a human-like shape.” [Kajita et al., 2014]
Humanoid robots should be able to interact with the world like humans. This is
necessary to prevent eﬀorts for making the world robot friendly. Robots which
strongly resemble humans in appearance and behavior are called androids.

The development of humanoid robots follows two main goals. First, for achieving
an artiﬁcial intelligence similar to the human one, a learning process is needed
which is also similar to the human one. Therefore the robot has to have comparable
capabilities in sensing and actuation. The second goal is related to the integration

14

2.2 Humanoid Robots

Figure 2.2: A Humanoid Soccer League ﬁeld which is 9m x 6m in size and consists
of an artiﬁcial turf. While the ﬁeld is clearly speciﬁed, the outsides are
not, which can be challenging for vision algorithms. The picture was
taken during the Iran Open 2016.

of robots in our environment. Since everything humans use is adapted to them, a
robot which should work in this environment, e.g. helping old people at home, must
be able to interact with this environment. Otherwise, the environment would have
to be adapted to the robot, for example by replacing stairs with ramps for wheeled
robots, which would be more cost intensive.

In the following, humanoid robots are further described in the three typical sec-

tions sensing, computing and actuating.

2.2.1 Sensing

Sensing on humanoid robots is more diﬃcult than on other types of robots since the
movement of the robot leads to noise in the sensors. For example, camera images
get blurry if the shutter speed is too slow or if it is a rolling shutter sensor. Also,
odometry data is less certain than on wheeled robots. Furthermore, the position
of sensors in relation to the world is not stable. On a wheeled robot, the camera
is usually a ﬁxed hight above the ground. A humanoid robot has to do forward
kinematics from its support feet to the camera to get the position and orientation.
This also requires knowing which leg is the supporting leg and if the robot is standing
at all. For this an inertia measurement unit (IMU) and position encoders in the joints
are crucial. These are described in the following.

The IMU is a combination of a gyroscope and an accelerometer.

It measures
angular velocities and linear accelerations. It is normally installed inside the torso
near the center of mass. The sensor values can be used to detect falls and to identify
the side on which the robot landed after a fall.

15

2 Fundamentals

Figure 2.3: The Asimo robot walking on a ﬂight of stairs [2]. The algorithm was
adapted to this speciﬁc stair size, therefore it is not applicable in the
real world. This transfer from the lab environment to the real world is
tried to be achieved in RoboCup by enforcing realistic testing conditions
in which teams have to prove their performance.

Furthermore, the positions of the robot’s joints have to be measured. This is
usually realized by a combination of a magnet on the end of the outermost gear
and a hall sensor [Ramsden, 2011]. When the gear rotates, the magnet ﬁeld rotates
accordingly. The hall sensor measures this and a microcontroller can compute the
position of the servo based on this data.

2.2.2 Computing

In the early days of humanoid robots, having enough computational power was
diﬃcult because the space and mass for the computational unit are very limited.
Today, single-board computers, e.g. Raspberry Pi [Upton and Halfacree, 2014], and
Intel NUCs [Perico et al., 2014] are mostly used, depending on the size of the robot.
All these boards provide GPUs and multiple CPU cores. Therefore the interest in
parallelizing software and outsourcing computation to the GPU, especially for neural
networks and computer vision, rose in the last years. Sometimes multiple cheap
single-board computers are installed and connected using an Ethernet network, to
get a high performance for low cost. This comes with the disadvantage that the
software has to be able to run in parallel on a distributed system.

16

2.3 Robot Operating System

2.2.3 Actuating

A humanoid robot is typically composed of multiple joints. Each joint has to be
actuated which can be done in two diﬀerent ways. Either the joint can be moved
by tendons, similar to the human movement, or a motor can be placed directly into
the joint axis. The later approach is used more often in smaller robots, since it
needs less space. Using tendons makes exact positioning of the joint more diﬃcult,
but also enables to use bigger and linear motors, since they don’t have to be placed
inside the joint.

Actuators need a high strength in relation to their weight, since they have to carry
themselves. Multiple actuators are typically needed for one limb, resulting in a high
number of cables, which have to be laid over multiple joints. Therefore a bus system
is often used to limit the number of cables. The bus requires the motors to have a
micro controller, to receive goal positions and to send the current position. Micro
controller, motor and a gearbox are usually grouped together in a case and called
servo. For reaching the goal position and for holding it, a controller is required in
the ﬁrmware of the servo. This is usually a PID controller [Wescott, 2000].

2.3 Robot Operating System

The Robot Operating System (ROS) was developed by Willow Garage, originally
for the PR2 robot in 2007 [Quigley et al., 2009]. It is an open source framework
for developing software in robotics with a focus on the ability to run parallel on
distributed computer systems.
It can be run on diﬀerent operating systems, but
only Ubuntu and Debian are oﬃcially supported. Its main advantage is a big library
of available software modules for common robotics tasks. These are developed,
maintained and documented by the ROS community and adding further modules is
easy. Using ROS decreases the time for developing software as most of the parts can
be taken from the library. In the following section, a short overview of the concepts
of ROS is provided. A deeper insight can be found in the online documentation [3].

2.3.1 Nodes

A node is a process in the ROS system. It can communicate with other ROS nodes
via topics or services.
In doing so, all nodes form a computational graph. Each
node has typically a clearly deﬁned subtask. For example one node gets the camera
image, a second node detects balls on this image, and a third node computes the
ball positions. Nodes can be easily reused in diﬀerent tasks, for example the node
which gets the camera image can be reused in a diﬀerent task that detects goals.

Open source implementations of nodes for most standard subtasks, especially
hardware controlling, already exist. Thereby the eﬀort in implementing a new task
is drastically decreased. The most important packages used for this thesis are men-
tioned in section 2.3.7.

17

2 Fundamentals

Figure 2.4: Example ROS architecture for a simple wheeled robot with the task to
follow a line until it ﬁnds a stop marker. The nodes are displayed as
ellipses with a name and the topics are shown as rectangles with name
and message type. First, an image is provided from the camera. Lines
and stop markers are detected on this image. Based on this information,
a navigation node computes the necessary movement of the robot and
publishes it. The robot control node is then controlling the motors of
the robot accordingly.

Twist.msg
geometry msgs/Vector3
geometry msgs/Vector3

Stop.msg
linear
uint8
angular uint8
uint8
ﬂoat32

RED = 0
GREEN = 1
color
distance

Figure 2.5: Two example messages. The Twist message (left) is already deﬁned in
ROS. The Stop message (right) is newly deﬁned for the special applica-
tion case of ﬁgure 2.4.

18

/imagesensor_msgs/Image.msgline_detectionimage_provider/lineexample_msgs/Line.msgnavigation/cmd_velgeometry_msgs/Twist.msgrobot_controlstop_detection/stopexample_msgs/Stop.msg2.3 Robot Operating System

2.3.2 Topics and Messages

Messages are the main communication method between ROS nodes. Messages are
always published on a topic, which is identiﬁed by a name and can only transmit
one type of message. A node can subscribe to a topic and will get the messages
other nodes publish to it. Each node can subscribe to and publish on any number
of topics and will not know with whom it communicates.

Communication can happen between nodes running on the same computer as well
as nodes distributed over diﬀerent computers, as long as they are connected with
an TCP/IP network. This is not only useful for parallelization but also eases the
visualization of the robots state on a separate desktop computer. Each message has
a type which is either predeﬁned in the ROS system or deﬁned by a user package.
The interface of a node is mainly deﬁned by the types of the messages it subscribes
and publishes. These types can be either predeﬁned in ROS or be newly created by
a developer, cp. ﬁgure 2.5.

2.3.3 roscore

The roscore is the most central part of a running ROS system. It consists of the
rosmaster, the ROS parameter server and the rosout logging node. The ROS
master is registering which topics are published by the nodes and on which topics
nodes want to subscribe. If one node wants to subscribe to a topic which another
node is publishing, a peer-to-peer connection is established from one node to the
other. Thereby the master does not become a bottleneck since it only connects the
nodes but does not need to handle the messages. To do this, a subscribing node asks
the master for a list of nodes which publish on this named topic. The master holds
It also
a table of all publishers and sends their names to the subscribing nodes.
remembers which nodes are subscribing to this topic, if a new publisher is started
later. This process is shown in ﬁgure 2.6.

The ROS parameter server is a global key-value store. It is mainly designed to
be used for static conﬁguration parameters. Transmission of data between nodes
should be done via topics to prevent making the parameter server a bottleneck. All
parameters are globally visible. If a parameter should be able to be changed during
runtime, dynamic reconﬁgure can be used. It provides the possibility to state on
compile time which parameter values should be changeable and provides an rqt
plug-in for it, see section 2.3.9. The rosout logging node subscribes to the /rosout
topic which is the standard topic for logging. ROS has built in methods to send
data to this topic which are displayed on runtime and written in a log ﬁle.

2.3.4 Services

Services can be seen as remote procedure calls (RPC). In contrast to messages
which are an unidirectional stream of data, service calls are blocking and waiting
for a response. They have deﬁned types which consist of a request and a response

19

2 Fundamentals

Figure 2.6: Procedure for establishing a peer-to-peer connection via the ROS master.
First, one node advertises the topic it wants to publish. The master
remembers by whom this topic is published. When another node tries
to subscribe to this topic, the master informs both nodes about each
other, so that they can start a communication.

message. The node providing the service is called server and the node calling the
service is called client. Services are useful for fast tasks, but should not be used
when getting the result can take a long time, because the calling node is blocked
until completion. For longer tasks, actions should be used (section 2.3.5). A possible
service for the example described in ﬁgure 2.4 would be a manual stop service. It
would be advertised by the navigation node and would stop the robot even without
markers. As this would take not a lot of time, basically just alternating the state of
the navigation node, this would be possible to do with a blocking service call.

2.3.5 Actions

Actions are used when a task which takes a long time should be called asyn-
chronously, in contrast to the synchronous service calls. Each action has a speciﬁed
type which consists of three messages: goal, feedback, and result. A node providing
the action, the action server, is called by another node, the action client, by sending
a goal. The action server will now try to achieve this goal, while the action client is
not blocked and can perform other tasks. The server will constantly send feedback
messages to the client to inform it about the status of the process towards the goal.
The server will send a result message when the goal was reached or if the action was
interrupted. Actions can be interrupted by sending new goals which the server con-
siders more important or by request of the action client, for example, if the sent goal
is not useful anymore. A possible action for the example described in 2.4 would be
driving a certain distance on the line. This needs some time because the robot has
to move. Therefore a blocking call is not feasible. The action runs asynchronously
and can also be interrupted, for example, if the line ends before reaching the desired
distance.

20

line_detectionimage_providerMasterAdvertise(/image)/imagesensor_msgs/Image.msgline_detectionimage_providerMasterSubscribe(/image)/imagesensor_msgs/Image.msgline_detectionimage_providerMaster2.3 Robot Operating System

<package>

<name>example_package</name>
<version>1.0.0</version>
<description>Short example for a package.xml.</description>

<maintainer email="ex@ample.org">Jane Doe</maintainer>

<license>BSD</license>

<buildtool_depend>catkin</buildtool_depend>
<build_depend>example_2</build_depend>
<run_depend>std_msgs</run_depend>

</package>

Figure 2.7: Example of a package.xml. Diﬀerent tags can be used to specify meta-
data of the package. These are necessary to state the owner of this
package and its license. The listed dependencies are used by catkin for
compiling.

2.3.6 Code Organization

The smallest and main unit for organizing software for ROS is a package. A package
has a package.xml (cp. ﬁgure 2.7) which describes diﬀerent metadata of this package,
e.g. the package name, the author, the license and dependencies on other packages.
A package can build on its own if all dependencies are met. The content can, among
other things, be ROS nodes, visualization plug ins, libraries or datasets. It can be
distinguished between dependencies on build and runtime. Diﬀerent packages can
be grouped in meta-packages, which hold no content of their own but only collect
packages which belong together.

2.3.7 Code Distribution

The idea of reusing nodes can only be utilized if the nodes are shared. Therefore
a wiki is provided with documentation to the packages. Usually the packages are
hosted in GitHub repositories which are linked in the wiki. A description of the
package and its documentation is provided in the wiki. Since the package depen-
dencies are clearly speciﬁed in the package.xml, it is easy to install them. Further
development, e.g. bug ﬁxes, of packages is usually done in the GitHub repository
by creating pull requests or issues.

2.3.8 ROS Packages Used in This Thesis

In the following a short description of the ROS standard packages which were used
in this thesis is provided.

21

2 Fundamentals

rosbag

rosbag is a package which can record the messages of a ROS system during
runtime and save them into a ﬁle. This ﬁle, also called rosbag, can later be
further investigated or replayed. This allows easier debugging and testing of
nodes without the need to bring up the whole ROS graph. It is also particularly
helpful to compare performance of diﬀerent algorithms on the same dataset.

tf2

tf2 keeps track of the diﬀerent coordinate transforms and provides informa-
tion of relations between them. One example would be the position of the
foot tip in relation to the camera. The robot state publisher package sub-
scribes to JointState messages to get the current joint positions and provides
these information to tf2. tf2 can be called by any node to get coordinate
transforms, not only at the current time but also for past positions.

URDF

The Uniﬁed Robot Description Format (URDF) is an XML format for describ-
ing robots. The urdf ROS package provides a parser which can read these
ﬁles, enabling other packages, e.g. tf2, to use this to abstract from the robots
structure. When creating a new robot, only creating a corresponding URDF
is needed to make ROS software run on it. The URDF is therefore crucial for
hardware abstraction.

xacro

xacro provides macros to xml documents. This is especially useful in the ROS
context to make URDF ﬁles, since they are often symmetric. By using xacro,
it is possible to deﬁne, for example, an arm just once and then use a macro to
generate a left and a right arm out of it. The xacro ﬁles are expanded to xml
ﬁles by running the xacro ROS package.

2.3.9 Visualization

One of ROS’ core strengths is providing diﬀerent tools for visualization. Due to its
publisher-subscriber architecture, it is very easy to establish a data stream from the
program to the visualization. Either the visualization can subscribe on topics that
are already being in use or additional topics can be provided from the software to
deliver more information to the visualization. Messages in ROS are only published
if there is a subscriber on the topic, therefore publishing additional topics for visu-
alization reasons does not cost performance when the visualization is not running.
ROS provides two main tools for visualization which can be extended by plug-ins.
It is also possible to implement own tools which are independent from these.

22

2.3 Robot Operating System

rqt

rqt is a QT based interface with ROS connection (ﬁgure 2.8). Plug-ins can be
launched and provide a QtWidget. Multiple widgets can be displayed at the same
time. They can be resized and positioned by drag and drop. ROS provides a set
of plug-ins but writing an own plug-in is possible too. These plug-ins can be used
to visualize data in 2D but also to provide a controlling interface. In the following,
some examples of important plug-ins are shown.

The node graph plug-in shows all currently running nodes and topics. Published
and subscribed topics are connected to their nodes and thereby it is easy to see the
ﬂow of data. This plug-in is especially helpful to get an overview of the running
software and to ﬁnd misconnected nodes.

The topic monitor lists all current topics. It is possible to subscribe to them and
to get the current transmitted values. Further on, statistics about the publishing
rate and the used bandwidth can be shown for each topic.

The rqt plot plug-in enables live plotting of data, using matplotlib. The
dynamic reconfigure plug-in provides an interface to change parameter values pre-
viously deﬁned to be reconﬁgurable. This is useful when tuning parameter values,
because changing it is possible on the ﬂy and does not require a restart of the
software.

RViz

RViz provides a 3D visualization of the robots state and its environment. The
standardized URDF format is used to get a visual robot model, which is then used
to show the current positions of the robots joints. Furthermore, sensor data can
be displayed using marker messages. These messages can be published by any node
and deﬁne three dimensional states which are displayed in RViz. This is for example
helpful to get a visualization of recognized objects. Furthermore, a lot of diﬀerent
standard ROS messages can directly be visualized in RViz, e.g. camera images,
depth clouds, laser scans and point clouds. Thereby RViz provides visualization
without additional eﬀort, if the standard messages are used. It is especially used for
localization and mapping, because it is possible to see the current sensor inputs of
the robot as well as its map in the same window (c.p. ﬁgure 2.9).

2.3.10 Simulation

Simulation is a crucial part when developing robot software, since it gives the devel-
oper the possibility to run his software without using hardware. This can prevent
hardware damages because bugs can be found before running it on the robot and
it can be used to accelerate development, e.g. by testing in faster than real time.
While ROS can generally use any simulator, Gazebo is normally preferred, since it
has a good ROS integration and was also originally developed for ROS. In order to
use Gazebo, an URDF of the robot is required.

23

2 Fundamentals

Figure 2.8: The rqt interface with diﬀerent plug-ins started. rosbag is opened (top
left), it publishes values, which is visible by the edges in the node graph
(top right). The data is plotted using rqt plot (bottom right). The
topic monitor lists the current topics (bottom left).

Figure 2.9: Example visualization with RViz. In this case a wheeled robot is map-

ping its surroundings using depth data from a Kinect [4].

24

2.3 Robot Operating System

This URDF is used to display the robot in the simulator and to compute its
collisions with itself and the environment. The simulator can provide sensor data
in the corresponding standard messages. To actuate the servos of the robot, dif-
ferent controllers are available which work with the corresponding messages, e.g.
JointTrajectory.

25

2 Fundamentals

26

3 Hardware and Software

In this chapter, the used hard- and software are explained in detail. First the used
Minibot robot platform is described in section 3.1. Afterward, the previous software
architecture is investigated in section 3.2.

3.1 Minibot

The Minibot was designed by the Hamburg Bit-Bots because their previous robot
platform, the Darwin-OP, became too small to eﬀectively participate against the
other robots in the league. Furthermore, the computational power of the Darwin-
OP was low and newer boards could not be installed easily due to the restricted
space. Therefore an upscaled platform was constructed with the same composition
of joints. The computational unit was replaced by an Odroid XU3 with eight cores
[10].

Figure 3.1: The Minibot in its walking position.

27

3 Hardware and Software

The robot has two degrees of freedom (DOF) in the head, two in each shoulder,
one in each elbow, three in each hip, one in each knee and two in each ankle. This
leads to overall 20 joints. These joints are connected with bended sheet aluminum
parts. The size of the robot is 0,7 m and the weight 5 kg. Since most sensor types
are forbidden in the HL, it only has a camera, an IMU and the position encoders of
the servos. Lately, an experimental set of pressure sensors was installed under the
feet, to stabilize the robots walking.

In the following, the used servo motors and the motor controller board are further

investigated.

3.1.1 Dynamixel Servos

Dynamixel is a series of servo motors by the South Korean company Robotis [5]
which are designed for the use in robotics. They are widespread in humanoid robotics
and especially in the RoboCup Humanoid League. Diﬀerent models are available
but all share the property that they are daisy-chainable and communicate using a
bus protocol.
In this thesis, three diﬀerent models from the M series were used,
the MX-28, MX-64 and MX-106, see ﬁgure 3.2. They all use the TTL protocol and
diﬀer only in size and torque. The TTL bus is used with 1 megabaud.

The M series can communicate using single read and write packages as well as
bulk read and sync write, which are used to access all motors at the same time. Since
accessing all motors at once requires less packages on the TTL bus and therefore
the update rate can be increased, it is commonly used in RoboCup. Regardless
which of these methods is used, only a single goal position can be transfered. Since
it would often be more interesting to send joint trajectories an eﬀort was made to
implement an alternative framework for these servos [Fabre et al., 2016]. For the
moment, almost all teams are still using the standard ﬁrmware, therefore being able
to accept only one goal position.

Figure 3.2: The MX-28T, MX-64T and MX-106T servos [6]. All three are controlled
by the same TTL bus protocol. The only diﬀerence is the maximal
torque.

28

3.2 Bit-Bots Framework

Figure 3.3: Communication between controller board and motors via a daisy chained

TTL bus system [7].

3.1.2 CM730

The CM730 is a motor controller board also produced by Robotis. It was originally
used in the Darwin-OP [Ha et al., 2011] but is now widely used in the Humanoid
League. It is connected to a computer via USB2.0. It provides ﬁve connected TTL
sockets for ﬁve chains of Dynamixel motors. Therefore it is easy to make a chain for
both arms, both legs, and the head. Unfortunately, all chains are on the same TTL
bus. Therefore all communication with the motors has to be done via one bus. This
limits the communication rate to each motor by the count of the connected motors.
Furthermore, the CM730 provides an on board accelerometer and gyroscope, as well
as two general purpose buttons and a reset button.

3.2 Bit-Bots Framework

The old architecture of the Hamburg Bit-Bots was designed to run in two processes
because the originally used Darwin-OP robot had a single core processor with two
In the ﬁrst
hyper-threads. Therefore the software was split into two processes.
one, all software closely related to the hardware (motion, walking, animation) was
integrated. The vision processing and the behavior were included in the second one.
Those two processes use a shared memory IPC to communicate with each other.

3.2.1 Module Architecture

The main part of the software is divided in modules. Each of them is providing an
update method. All modules are executed together in a loop by calling their update
methods. The main work of a module should be done in this method, but a module
can also deﬁne a pre- or post-method, which is called before or after the loop.

29

3 Hardware and Software

Figure 3.4: Overview of the original Hamburg Bit-Bots architecture. The top half
shows the behavior process, which is connected via the shared memory
IPC to the motion process. The modules exchange information via the
data dictionary and the connector collects all of them to provide it to
the behavior. Additionally, events are used to inform software parts
about pressed buttons and changes of the game controller. In the motion
process, a pose object is exchanged via function calls. It includes current
and goal positions for all motors.

30

Behavior processMotion processLegendTeam CommunicationBehaviorHeadBehaviorConnectorUnitData ﬂow via function callMotionCamera ModuleModuleFilteringGamecontroller ModuleAnimation ModuleData ﬂow via eventData ﬂow via datadictonaryShared Memory IPCWalkingWalkingWorld ModelButtonsLocalizationNetworkAnimatorPenalizeCM730PosePoseObjectGoal RecognitionBall RecognitionPose3.2 Bit-Bots Framework

Module
Camera
Ball Recognition
Goal Recognition

Requires

RAW IMAGE
RAW IMAGE

Provides
RAW IMAGE
BALL INFO
GOAL INFO

Vision Visualization BALL INFO, GOAL INFO

Figure 3.5: Example of the module architecture with two possible orders of modules.
The modules would be run either in the displayed order or with ball and
goal recognition switched.

The order of the method calls is deﬁned by the input and output data of a module.
Each module deﬁnes provided and required data by named strings. The architecture
makes sure that a module is only executed after the required data was provided in
this cycle. If a module is started which requires data that no other started module
is providing, an error is given directly at the start.

The data is shared between the modules by a shared dictionary which is passed as
an argument to each update method. This architecture can be seen as a blackboard
architecture, in which the data dictionary is the blackboard, the modules are the
knowledge sources and the control is done by providing a ﬁxed running order due
to the required and provided data [Nii, 1986]. Threaded modules are possible, but
they are only useful for I/O-operations because Python can not actually run them
in parallel. An advantage of this architecture is, that it makes sure that all modules
are called sequentially, which simpliﬁes some algorithm. For example, the behavior
module gets all aggregated recognition information from the vision for each image.
Disadvantages are that it is not generally parallel, very adapted to a speciﬁc system
and the framework is not used outside of the team.

3.2.2 Motion

It is
The motion is responsible for all tasks regarding the control of the robot.
handling the communication to the motors and the IMU, provides the current pose
to the IPC and gets motor goals via the IPC, for example from the animation
module. The motion also takes care of falling and getting up. Therefore it plays
also animation by itself by using the animator class. Furthermore, the motion holds a
walking object for computing the next walking pose, if necessary. There are diﬀerent
parts of the software that want to set the motor positions of the robot: animations
from the behavior, head positions from the head behavior, walking, falling and
standing up. Therefore the motion has to decide which part of the software gets
control over the motors. In summary, the motion acts like a state machine, without
having its structure.

31

3 Hardware and Software

3.2.3 Visualization

To show the status of all robots during a game, a graphical user interface was
implemented for GTK+ called debug ui. It receives data from the robots via UDP,
since the robots are not allowed to use any TCP during the game. In the source
code, ﬁrst a scope was deﬁned, e.g. ball detection. Then data could be transmitted
for this scope, e.g. the balls position. This gave a structure to the data which was
used by the debug ui to order it. Diﬀerent widgets could be started to display
data. There were implementations for a tree-like view of the raw data, an image
viewer with markings for detected objects, an overview of the motors temperatures,
a visualization of relative object positions to the robot and an overview of the ﬁeld.
The program was not used frequently because it had to be compiled additionally
and it was not stable.

32

4 Architecture

Diﬀerent objectives for the software architecture were listed in section 1.3. First and
most of all, it should be usable on diﬀerent robots, as well as by diﬀerent teams.
Therefore an architecture is presented which tries to ensure a maximum of ﬂexibility.
The structure of this chapter is as following: First, the basic approach is presented
in section 4.1. Afterward, an overview of the architecture and the used names is
provided (section 4.2). Finally, the chapter is concluded with the deﬁnition of the
ROS messages in section 4.3.

4.1 Basic Concept

The goal of the architecture is to be ﬂexible, so that teams can adapt it to their
implementation. Still, it has to allow an easy exchange of modules. To achieve this,
only ROS messages and their topic names were deﬁned. It is also not necessary to
publish all deﬁned topics. This leads to the possibility of diﬀerent implementations of
nodes that are still exchangeable and comparable, cp. ﬁgure 4.1. Thereby, semantic
parts, but not necessarily single nodes, are exchangeable.

It’s crucial to give the teams freedom in design, since not all their architectures can
be exactly the same. As RoboCup is a research competition, methods and algorithms
change often. New concepts have to be compared to the old ones to see if there is
an improvement. Comparing is also simpler using this common architecture since
input and output of diﬀerent implementations stay the same.

4.2 Overview

There are diﬀerent tasks that a robot architecture has to perform. The most basic
is to communicate with the robots hardware, e.g. via the TTL bus to the servos. In
the proposed architecture this is called hardware communication. It also abstracts
from the concrete hardware by providing a ROS interface to get its sensor data and
to control it.

Above that, there is a part of software that controls the robot’s hardware by doing
meaningful actions. In the case of a humanoid robot this is walking for generating
motor positions in order to achieve a gait and animation to play predeﬁned sequences
of positions. Since there are potentially multiple users of the robot’s joints, there
has to be a managing unit which controls the access, the hardware control manager
(HCM). It acts similar to the biological cerebellum which handles motor functions
in the human brain.

33

4 Architecture

Figure 4.1: This ﬁgure presents the basic concept of the architecture. Three diﬀerent
possible implementations for the vision are shown. On the left, the
ball and goal detection are implemented in diﬀerent steps. First, the
candidates for balls and goal posts are chosen and then the actual result
is computed in a second step. In the center, everything is done in one
node, e.g. because the code was transferred from an old framework and
was not modular. On the right, one node is used again, but it has an
internal modular structure, thus allowing to publish additional data for
visualization. All three have implementations have diﬀerent nodes but
can be exchanged easily and their results can be compared.

The HCM detects falling, interrupts animations or walking if needed and plays
standing up animations when the robot fell down. In the special case of RoboCup
Soccer, it makes sure that the robot completely stops to move if it is penalized, by
using the information provided trough the gamecontroller client.

Above this HCM, there is a higher decision taking part, the behavior. It controls
the robot on a more abstract level, deciding for example to kick and where to go.
This can be split into a body and a head behavior, where the head is only controlled
by sending goals to look for, e.g. tracking the ball. Finding a path to the navigation
goal is done by the path planning. It decides on a path and generates the necessary
walking commands.

In order to know where to go, the robot needs information about its surroundings.
Since only humanoid sensors are allowed in the HL, the robot has to rely on its cam-
era. The image acquisition gets the image from the camera and removes distortion
from it. The vision uses this image to detect features of the ﬁeld and to get visual
odometry. The positions of the detected objects in relation to the robot have to be
computed from the position on the image, also known as transferring from image
space to relative space, which is done in the pixel to position transformation (PPT).
The absolute position of the robot on the ﬁeld is computed by the localization by
using odometry and ﬁeld features.

34

ball_detection/ball_in_imageBallInImage.msg/ball_candidatesBallsInImage.msgball_candidate_chooser/imagesensor_msgs/Image.msgmonolithicvisionnode/imagesensor_msgs/Image.msg/ball_in_imageBallInImage.msgpost_detection/goal_in_imageGoalInImage.msggoal_detection/postsPostsInImage.msg/goal_in_imageGoalInImage.msgmodularvisionnode/imagesensor_msgs/Image.msg/ball_in_imageBallInImage.msg/goal_in_imageGoalInImage.msg/postsPostsInImage.msgball_detect.post_detect.goal_detect.All vision information are aggregated
to a personal model (PM) which can
ﬁlter them over time. The robot can
exchange information with other team
players, using the team communication.
The personal model can be updated to
a team updated model (TUM) by using
these information.

Overall, this architecture is mostly
similar to the hierarchical paradigm, cp.
section 1.2.2. Mainly, the camera is
used for sensing. The resulting informa-
tion are aggregated into a global model
which is used by the behavior to plan
the actions, e.g. walking. The main
diﬀerence to the classical hierarchical
paradigm are the HCM and the head
behavior. The HCM acts more like a
reactive behavior, since it transfers di-
rectly from sensing, i.e. the IMU, to ac-
tions, i.e. animations. It takes no direc-
tives from the behavior to do so, which
would be the case in a hybrid deliber-
ative/reactive paradigm. But it would
be possible to add a directive to tell the
HCM if it should stand up or not. This
was not done, since it is obligatory to
directly stand up in RoboCup Soccer.
The head behavior is a more clear deﬁ-
nition of a reactive behavior. It takes a
directive from the body behavior, spec-
ifying the searched object, and controls
the motors afterwards by itself.

4.3 Message Deﬁnitions

Following the basic concept, described
in section 4.1, a set of messages were
deﬁned for all tasks, described in section
4.2. These messages are shown in their
data ﬂow context in ﬁgure 4.3. Since the
nodes are not deﬁned, there are multiple

4.3 Message Deﬁnitions

Figure 4.2: Very simpliﬁed representation
of the diﬀerent task and the in-
formation ﬂow in the proposed
architecture.

35

Image AcquisitionVisionPixel to PositionPersonal ModelLocalizationTeam ModelBody BehaviourTeam Comm.AnimationPath PlanningWalkingHCMHardware Comm.Gamecontr. Cl.Head Behaviour4 Architecture

ways to implement an actual architecture based on these messages. Two examples
are shown in ﬁgure 4.4 and 4.5, with diﬀerent degrees of granulation. The exact
deﬁnition of all messages is included in the appendix (section 8).

The deﬁnition for the necessary topics and messages should not be done by only
one person or one team, as it would be too speciﬁc and ”over ﬁts” on their current
architecture. At the same time, developing the architecture with all teams in the
Humanoid League together is also not practical. Therefore the development was
done in three steps. First developing a prototype only inside the Hamburg Bit-Bots
team. This resulted in the basic principle of deﬁning only messages and topics. In
a second step, this prototype was introduced to two other teams (WF Wolves and
Rhoban FC) of which one was using ROS already and one wasn’t. The prototype
was changed based on their feedback and was already very near to the end result.
During the actual implementation of nodes, new arising changes were discussed
between the teams. In a ﬁnal step, the architecture will be presented at the RoboCup
Symposium 2017 to the other teams. In the next subsections, the diﬀerent parts of
the architecture are further investigated.

4.3.1 Image Acquisition

The image acquisition uses only standard ROS messages
(Image.msg and
CameraInfo.msg), as it is already well deﬁned in ROS. Cameras are the only al-
lowed optical sensor in the league, therefore we don’t have to take care about depth
cameras or laser-range-ﬁnders. Stereo cameras are allowed but currently not used
by any team, as they often decalibrate during falling. Therefore they were not taken
into account by the architecture for the moment.

4.3.2 Vision

The image can be used to extract visual odometry for the localization. No message
has to be specialized for this since ROS already provides an odometry message
(Odometry.msg). A less sophisticated approach for getting localization information
is the visual compass. It is often used in RoboCup since the symmetry of the ﬁeld is a
problem for the localization. As compass sensors are not humanoid, this distinction
can only be done visually. One common approach is to look for ﬂamboyant markers
outside of the ﬁeld. Another approach is looking at the ceiling and comparing it
with images that were recorded before the game. In any case, this results in an angle
of orientation on the ﬁeld. A simple message with an angle and a conﬁdence are
speciﬁed to transfer this data to the localization (VisualCompassRotation.msg).

Furthermore, there are four deﬁned classes of objects to be recognized in RoboCup
Soccer: ball, goals, obstacles and lines. Therefore it is simple to deﬁne four diﬀerent
pipelines, one for each of the classes. While theoretically, one message would be
enough for each one of these, some extra messages for intermediate results have
been deﬁned, based on the current recognition algorithms in use.

36

4.3 Message Deﬁnitions

Figure 4.3: Proposed and ROS standard messages (rectangles) form together the
data ﬂow. The nodes (ellipses) are only shown for clariﬁcation and don’t
have to be implemented in this way. Actions are dotted and services
dashed. Grey colored messages are ROS standard messages. The mes-
sages are grouped into diﬀerent categories (colors). The vision pipeline
(ﬁrst three sections) transfers sensor data to information (Sense). These
are provided to the localization and the world model. The model is used
by the behavior to decide on the directives (Plan), which are handled by
the robot control (Act). The hardware communication abstracts from
the used robot platform.

37

/imageImage.msg/ball_in_imageBallInImage.msg/goal_in_imageGoalInImage.msg/obstacles_in_imageObstaclesInImage.msg/lines_in_imageLineInformationInImage.msgbehaviorhardware_control_manager/joint_statesJointState.msg/walking_motor_goalsJointTrajectory.msg/cmd_velTwist.msg/team_dataTeamData.msg/head_modeHeadMode.msg/ball_relativeBallRelativ.msg/obstacles_relativObstaclesRelative.msg/goal_relativeGoalRelative.msg/lines_relativeLineInformationRelative.msgNetwork/robot_stateRobotState.msg/motor_goalsJointTrajectory.msg/imuImu.msg/servo_dataAdditionalServoData.msg/gamestateGameState.msg/strategyStrategy.msg/odomnav_msgs/Odometry.msg/pathPath.msg/ball_candidatesBallsInImage.msg/goal_part_candidatesGoalPartsInImage.msg/global_modelModel.msg/pausedbool/head_motor_goalsJointTrajectory.msg/local_modelModel.msg/animationAnimation.msg/vc_rotationVisualCompassRotation.msghardware_communication/line_points_in_imagePointCloud2.msg/positionPosition2D.msg/batteryBatteryState.msg/visual_odomOdometry.msg/navigation_goalPoseStamped.msg/play_animationPlayAnimation.action/kickKick.actionmanual_penalizeswitch_motorpowerImage AcquisitionVisionPixel to PositionFilteringLocalizationNetwork Com.BehaviorRobot ControlHardware Com.Path Planning4 Architecture

Figure 4.4: In this example, all messages are used. While this would allow an ex-
change of very small parts, it is probably not going to be implemented
like this in reality. The real number of used nodes is lower, e.g. because
some algorithms can not provide an intermediate result or a recognition
of goals is not necessary for some localizations.

38

/image_rawImage.msgimage_acquisitionball_detectionpost_detection/ball_in_imageBallInImage.msg/goal_in_imageGoalInImage.msgobstacle_detectline_detection/obstacles_in_imageObstaclesInImage.msg/lines_in_imageLineInformationInImage.msgbody_behavioranimation_serverhardware_control_manager/joint_statesJointState.msg/walking_motor_goalsJointTrajectory.msgwalking/cmd_velTwist.msgpath_planingteam_communication/team_dataTeamData.msghead_behaviour/head_modeHeadMode.msggamecontroller_clientimage_procball_position_tfopp_position_tf/ball_relativeBallRelativ.msg/obstacles_relativObstaclesRelative.msggoal_position_tfline_position_tf/goal_relativeGoalRelative.msg/lines_relativeLineInformationRelative.msgNetwork/robot_stateRobotState.msg/motor_goalsJointTrajectory.msg/imuImu.msg/servo_dataAdditionalServoData.msg/gamestateGameState.msg/strategyStrategy.msg/odomOdometry.msgpersonal_model/pathPath.msgpath_execution/ball_candidatesBallsInImage.msg/goal_part_candidatesGoalPartsInImage.msgball_choosergoal_detection/ball_ROIsRegionOfInterest[]team_updated_model/global_modelModel.msg/obstacle_ROIsRegionOfInterest[]/goal_ROIsRegionOfInterest[]/line_ROIsRegionOfInterest[]ball_ROIobstacle_ROIgoal_ROIline_ROI/camera_infoCameraInfo.msgpause/pausedbool/head_motor_goalsJointTrajectory.msglocalization/local_modelModel.msg/animationAnimation.msgvisual_compass/vc_rotationVisualCompassRotation.msghardware_communication/image_rect_colorImage.msg/line_points_in_imagePointCloud2.msgline_points_tf/line_points_relativePointCloud2.msgvisual_odom/positionPosition2D.msgkick_server/batteryBatteryState.msg/visual_odomOdometry.msgmanual_penalizeswitch_motorpower/navigation_goalPoseStamped.msg/play_animationPlayAnimation.action/kickKick.action4.3 Message Deﬁnitions

Figure 4.5: This is a more typical example of how the architecture would look when
it is used by a team. The vision can’t detect obstacles or lines. Further-
more, it directly outputs the relative positions. The positions in image
space are only published for visualization. The localization is only based
on detected goals and the visual compass. Filtering is done in only one
node. The path planning is integrated into the behavior. Animations
and kicks are handled by the same node.

39

/cmd_velTwist.msg/image_rawImage.msgcamera_driver/ball_in_imageBallInImage.msg/goal_in_imageGoalInImage.msgbody_behaviourrobot_control/joint_statesJointState.msgteam_communication/team_dataTeamData.msghead_behaviour/head_modeHeadMode.msggamecontroller_client/ball_relativeBallRelativ.msg/goal_relativeGoalRelative.msgNetwork/robot_stateRobotState.msg/motor_goalsJointTrajectory.msg/imuImu.msg/gamestateGameState.msg/strategyStrategy.msgﬁlter/team_updated_modelModel.msgobject_recognitionpause/pausedbool/head_motor_goalsJointTrajectory.msglocalizationvisual_compass/vc_rotationVisualCompassRotation.msghardware_communication/positionPosition2D.msg/play_animationPlayAnimation.actio/kickKick.actionmanual_penalizeswitch_motorpower4 Architecture

Most of the teams have multiple steps in their vision algorithm. First regions
of interest (ROI) are deﬁned, for example the ball is usually expected below the
horizon, as it stays usually on the ground in RoboCup Humanoid Soccer. Therefore
computation time can be saved and false positives can be reduced by using ROIs,
which is already a deﬁned message in ROS (RegionOfInterest.msg).

Ball

For the ball, a message was deﬁned specifying the center position, the size
on the image and a conﬁdence value (BallInImage.msg). If wanted, an in-
termediate result can be provided by publishing an array of ball candidates
(BallsInImage.msg).

Obstacles

can be of diﬀerent kinds.

The obstacles
the message
(ObstaclesInImage.msg) includes an enumeration to tell if it’s a team robot,
an opponent robot, a human leg or something not recognized. Furthermore,
the position on the image is deﬁned with a rectangle. As in all speciﬁed vision
messages, a conﬁdence value is included.

Therefore

In order to detect goals, parts of them have to be identiﬁed, this can be
goal posts or bars. A ﬁrst message (GoalPartsInImage.msg) was deﬁned for
publishing information about these goal parts. The result of the goal detection
can be published using a second message (GoalInImage.msg), which can also
be used to transmit information about not completely discovered goals. When
viewing only one goal post, it is not clear on which side the center of the goal
lies. Sometimes, educated guesses can be done, for example if the post was
near the boarder of the frame, implicating that the other one lies probably
outside the image. To enable this, a goal center position was added to the
message.

Goal

Lines

There are two diﬀerent ways to detect ﬁeld lines. One is to detect only line
points and to generate a point cloud out of it, for which a ROS message
already exists (PointCloud2.msg). The other one is to identify crossings,
line segments and the center circle as features. To enable this, a message
(LineInformationInImage.msg) was deﬁned.

4.3.3 Pixel to Position Transformation

To get the position of the objects in relation to the robot, a transformation from
the image space to the relative space has to be done. To publish the results, mes-
sages for all objects were deﬁned (BallRelative.msg, ObstaclesRelative.msg,
GoalRelative.msg and LineInformationRelative.msg). They deﬁne the objects

40

4.3 Message Deﬁnitions

positions in relative space and a conﬁdence value. The position is usually computed
in ROS by using tf, but there are diﬀerent other approaches in RoboCup, e.g. using
the diameter of the ball on the image.

4.3.4 Localization

The localization uses the information about the detected goals and lines, as well
as the visual compass and the odometry to compute the position. ROS already
speciﬁes a position message with covariance matrix, but still a new one was created
(Position2D.msg). It consists of a position without covariance, a conﬁdence value
and a description of the standard for displaying absolute positions. Thereby teams
that can not provide the complex covariance matrix, can use the easier conﬁdence
value. Furthermore, the standard for the absolute position ensures, that all teams
use the center point of the ﬁeld as a reference with the same directions for positive
and negative values.

4.3.5 Filtering

The absolute position of the robot and the relative positions of the ball and obsta-
cles are forming the personal model. This model is used to ﬁlter the obstacle and
ball data over time, preventing the behavior to make decisions based on a single
falsely detected objects. This model can be updated by the information from the
team communication and published on a diﬀerent topic. One message is deﬁned
(Model.msg) which consists of a BallRelative.msg, a ObstaclesRelative.msg
and a Position2d.msg. This eases the comparison between ﬁltered and non-ﬁltered
data. Furthermore, relative positions were chosen for the case where the robot does
not know its absolute position on the ﬁeld.

4.3.6 Behavior

The behavior consists often of two parts in RoboCup, a main behavior for the
body and a subbehavior for the head. This partitioning lowers the complexity of
each behavior. Usually, the body behavior decides where the robot should go and
starts animations and kicks. It also provides its current action and role to the team
communication, so that the other robots can be informed. Therefore a message
was deﬁned to publish the current strategic information (Strategy.msg). The head
behavior only controls the position of the head due to its current mode which is set
by the body behavior using a newly deﬁned message (HeadMode.msg). The modes
can be searching for ball, goal, localization features on and oﬀ the ﬁeld, looking in a
direction and don’t move. Teams are not forced to split their behavior in two parts,
but since this is a de facto standard, the HeadMode message was include.

41

4 Architecture

4.3.7 Path Planning

ROS provides messages for path planning. The navigation goal is set by an action
(using PoseStamped.msg). Other messages specify the path (Path.msg) and the re-
sulting movement commands (Twist.msg). These messages were originally designed
to be used by wheeled robots but are applicable in this context too, because it is
possible to abstract from the movement of the motor joints to an abstract planar
movement using a walking algorithm. This has not only the advantages that no
further messages have to be deﬁned, but also that it is possible to use a variety of
ROS tools without further work. For example setting of navigation goals and visu-
alization of the computed path can be done in RViz. Furthermore, already available
navigation algorithms can be used.

4.3.8 Network Communication

The network is used for communication with the game controller and other robots in
the team. The software tells the game controller that the robot is online and receives
the data from it, which is published using a deﬁned message (GameState.msg). It
can be used by the behavior for strategy but also by the HCM to stop the robot
during penalty. Furthermore, data from vision and behavior of other robots is shared
using another message (TeamData.msg). This data can be used in the ﬁltering for
updating the model.

4.3.9 Robot Control

The robot control provides all necessary parts for controlling the joints of the robot.
Communication in this part is mainly done by using the ROS standard message,
to be able to use ROS functionalities, e.g. tf2 and RViz. An additional message
(RobotState.msg) was deﬁned to inform the rest of the software about the state of
the HCM. This is for example important for the localization, as it needs to know if
the robot fell down, in order to adapt its model.

For a humanoid robot there are diﬀerent canonical and artiﬁcial states which
can be published by a HCM. Each state is named with an identiﬁer which is also
used in the deﬁnition of the RobotControlState message, cp.
section 8. The
most basic states are related to the position of the robot. It can stand correctly
(CONTROLABLE), it can be walking (WALKING), it can be on the way to fall (FALLING),
it can be lying on the ﬂoor (FALLEN) and it can be on the way to get back up
(GETTING UP). Furthermore, there are two states related to starting and stopping of
the robots software. The robot can just be started and still occupied on initialization
(STARTUP) or on the way to shut down (SHUTDOWN). The last send status of the HCM
before turning oﬀ is HCM OFF. There are two RoboCup speciﬁc states, namely being
penalized by the game controller (PENALIZED) or getting into and out of the penalty
position (PENALTY ANIMATION).

42

4.3 Message Deﬁnitions

a message

The robot can also play animations (ANIMATION RUNNING) or record animations
(RECORD). Another state, which is utile outside the game is when all the motors are
turned of, for example when only the camera is used (MOTOR OFF).
has

deﬁned
Furthermore,
(Animation.msg).
It provides the motor positions and information if the an-
imation is ﬁnished or if a new one is started. To start animations, two actions
were deﬁned. One to start statical animations (PlayAnimation.action) and one
explicitly for the kick, where a dynamic goal can be deﬁned. The kick uses a new
message (Kick.action) which consists of two Vector3.msg for the ball position
and the target.

animations

playing

been

for

The requested speeds, which are transmitted to the walking, are a Twist message.
This is the normal ROS standard, originally used for wheeled robots, but it can also
be applied here. Using this standard enables the use of other ROS packages, e.g.
the joy package for remote controlling the robot. The walking can also listen to the
robot control state in order to know when it has to stop walking, because the robot
fell down.

4.3.10 Hardware Communication

A good abstraction from the used hardware is necessary to make the proposed
architecture run on any robot. At this point it is crucial to use the ROS deﬁned
standards to enable the use of tools like RViz and MoveIt!. Therefore the node that
is controlling the hardware has to publish the current motor values in a JointState
message.

For accepting new motor goals, two message types would have been possible.
Either a JointState message, which would allow one set of position, velocity and
eﬀort values, or a JointTrajectory message which describes a complete trajectory
based on multiple points. Each point consists of position, velocity and eﬀort. The
Dynamixel servos, which are commonly used, are not able to accept a trajectory but
only one goal point. However, there is an alternative ﬁrmware which can do it, cp.
section 3.1.1. If the servo can accept only one goal position it is also possible to send
the diﬀerent points of the trajectory message one after another from the hardware
node to the motor. The JointTrajectory message is the more powerful interface
and was therefore chosen.

The Dynamixel servos are providing information about their temperature and
voltage, which cannot be transmitted via the JointState message. Since this motor
is widespread in the league, an additional message (AdditionalServoData) was
deﬁned to publish these values. The hardware communication also has to publish
all other sensor data, except the camera image. The possible sensor types are very
restricted due to the rules. Therefore it can only be an IMU. There is already
a well deﬁned ROS message (Imu.msg) for the IMU which is also used. Further
information on the robot are more speciﬁc and can be implemented by every team
itself, for example, information about pressed buttons.

43

4 Architecture

44

5 Implementation

The parts of the architecture which are expected to be used by all teams, were
implemented as packages, so that other teams switching to ROS would not have to
reimplement these. They can take these packages and will get all necessary basic
capabilities, on top of which they can implement their own vision and behavior
algorithms. Obviously it is also possible to use only parts of these packages and
reimplement others, for example the walking. The nodes were written in rospy as
far as possible, since it has a good readability [Sanner et al., 1999]. The intention is
to rather sacriﬁce performance than having code which can not be easily understood
or reused by others. Furthermore, ROS makes it very simple to distribute the code on
diﬀerent computers. For example, by installing an additional single-board computer.
Thereby, performance is less an issue.

The packages for the whole HL are presented ﬁrst (section 5.1). Afterwards the
packages which were implemented especially for the Hamburg Bit-Bots are examined
in section 5.2.

5.1 Humanoid League Packages

All package that are presented in this section were implemented to be usable by
any team in the Humanoid League. They are all fully compatible to the deﬁned
architecture.

5.1.1 Messages Package

All the deﬁned messages were put in one package. Thereby this package has very
few dependencies, only to message generation and ROS deﬁned message packages.
This allows easy use of this package, even for teams who don’t want to completely
follow the proposed architecture. The complete list of all message deﬁnitions can be
found in chapter 8.

5.1.2 Game State Receiver

For the implementation of the game state receiver, the already existing package
from the WF Wolves was used. Only small adaptions were needed. The message
was changed to the deﬁnition in the humanoid league msgs package and the team
and robot IDs were changed to parameters.

45

5 Implementation

5.1.3 Team Communication

During the last years, the team FUmanoids established a communication standard
in the league called Mixed Team Communication protocol (Mitecom) [8]. This is
important because robots need the ability to communicate with robots from other
teams. Beginning this year, this ability is mandatory to participate in a drop-
in challenge, where robots from diﬀerent teams play together [9]. Furthermore,
the player count will increase in the future up to eleven [11], forcing teams which
can not eﬀort so many robots to build joint teams. Therefore having a standard
for communication is important. The existing Mitecom was expanded to provide
additional information about positions of other robots on the ﬁeld and to add the
ability to share simple strategies between diﬀerent robots.

5.1.4 Speaker

The speaker package provides an easy way to use the Linux text-to-speech program
espeak in ROS. Vocal output is needed for two reasons: First, as a way to provide
information to the robot user. Either for telling the robot’s next action, or to get
a humans attention to a problem, for example, an emergency shut down. Secondly,
the RoboCup wants to use natural team communication in the future. While this
package is not sophisticated enough for team communication, it can still be used
for ﬁrst tests in this area. The implementation is done by a simple node which has
three queues with diﬀerent priorities. Messages can be send to the node, including a
text and a priority. The node executes espeak with the texts, in an order depending
on their priority. Diﬀerent options, e.g. volume, can be adjusted using dynamic
reconﬁgure.

5.1.5 RoboCup Visualization

ROS already provides two powerful tools for visualization, e.g. RViz. Still, there are
special use cases in RoboCup which are not provided directly by ROS. For some of
them, plug-ins were implemented during this thesis, to provide the most important
functions from the start and to motivate others to provide additional plug-ins in the
future. The implemented plug-ins are described in the following.

rviz marker

On of the most important features is to visualize the beliefs of a robot related to
its position on the ﬁeld and the recognized objects, like ball and lines. These can
be displayed in RViz via markers. To do this, messages of type Marker have to be
published. A node was implemented which subscribes on the relative positions of
objects and publishes the corresponding marker messages. Thereby, only this node
have to be started and the position of ball, goal posts and obstacles are visualized
in RViz (ﬁgure 5.1).

46

5.1 Humanoid League Packages

Figure 5.1: The screenshot shows the diﬀerent visualization tools compared to each
other. The field rqt plug-in (top left) shows the absolute position of
the robot on the ﬁeld. Relative positions of objects are visualized in the
relative rqt plug-in (bottom left) and in RViz (right), using markers
generated by rviz marker.

ﬁeld rqt

While using Rviz to visualize the recognized objects provides a nice interface, often
a more simplistic interface is better to get a fast overview. Therefore a rqt plug-in
was written, which displays a 2D image of the ﬁeld (ﬁgure 5.1). On this, shapes
are painted, which show the beliefs of the positions of the robots itself, the ball and
other robots. It can be displayed together with other rqt widgets at the same time
and needs only a small display space.

relative rqt

This rqt plug-in provides the same data as the rviz marker package but in a 2D
top down view (ﬁgure 5.1). It has the advantage of a clearer interface and it takes
less display space when used.

47

5 Implementation

image marker

While the ﬁrst two plug-ins, described above, are useful to visualize the beliefs which
result from the object recognition, this plug-in is for the object recognition itself.
Displaying the camera image is already possible in RViz and therefore it would be
a feasible solution to provide an image to RViz where all recognized objects are
already marked. Still, the use case is often to display only certain information of the
object recognition. This can be achieved without implementing an additional plug-
in by using dynamic reconﬁgure to activate and deactivate markings. Thereby only
one node is needed which subscribes to the camera image, draws shapes depending
on the current parameters and provides this image on another topic which is then
displayed in the standard image viewer plugin.

5.1.6 Simulator

ROS already has a well connected simulator: Gazebo. The communication works
directly with the standard messages, therefore no additional work has to be done to
interface the simulator. Still, a Gazebo world with a ﬁeld, goals and a ball is needed
in order to simulate a RoboCup Soccer game. Team NimbRo already created such
a world for their ROS architecture and released it open source. Unfortunately, the
package included some NimbRo speciﬁc ﬁles and had dependencies. Therefore the
world and object ﬁles were extracted and put together in a new package. Every team
using the architecture needs only to provide an URDF for their robot platform and
will get complete simulator support (ﬁgure 5.2).

5.2 Hamburg Bit-Bots Packages

In this section, the packages are presented which were especially written for the
Hamburg Bit-Bots. Nevertheless, these packages can be used by other teams. A
graph of the implemented nodes is shown in ﬁgure 5.3.

5.2.1 Robot Control

The tasks for controlling the basic robot abilities was described in section 4.2. These
tasks were implemented into three diﬀerent nodes for HCM, walking and animation.
Their realization is further investigate in the following.

Hardware Control Manager

The main task of the HCM is to evaluate the current state of the robot and to decide
what actions should be taken. A set of general useful states were already deﬁned in
the RobotControlState message, section 4.3.9. A common approach to implement
them is using a state machine. Given that the number of states is low, a hierarchical
state machine is not needed.

48

5.2 Hamburg Bit-Bots Packages

Figure 5.2: The Humanoid League environment which was extracted from the Nim-
bRo code base. The Minibot robot was integrated using the modeled
URDF, cp section 5.2.3. The lines in front of its head visualize the
robot’s ﬁeld of view.

The resulting state machine is shown in ﬁgure 5.4.

In the following, names of
states in the message are written in upper case, e.g. GETTING UP, and concrete
implementations are written in camel case, e.g. GettingUp. Methods are lower
case, for example entry().

We

states

create the

following additional

to make the state machine
more understandable and closer to the previous functionalities of the Bit-
PENALTY ANIMANTION is divided into PenaltyAnimationIn and
Bots motion:
PenaltyAnimationOut, to easier diﬀerentiate between them. GETTING UP is divided
into GettingUp and GettingUpSecond, because the getting up procedures of the Bit-
Bots consists of two parts. WALKING is divided into Walking and WalkingStopping
to show the fact that the walking tries to stop, for example to play an animation.
The walking has always to do a few steps to come to a safe stop. SHUTDOWN is divided
into ShutDown and ShutDownAnimation, which is showing that the motion is on the
way to shut down by playing a sit down animation.

49

5 Implementation

Figure 5.3: The implemented nodes for the robot control and hardware communi-
cation of the Hamburg Bit-Bots. All functionalities from the previous
motion process were transfered but restructured in single independent
packages.

To implement this state machine, ﬁrst the classes AbstractStateMachine and
AbstractState were deﬁned. The AbstractState class deﬁnes three main methods:
entry(), evaluate(), exit(). The entry() method is called once when the state
machine transitions to this state, to instantiate this state. The evaluate() method
checks if the state should change and returns the state to which the state machine
should transition. Finally, the exit() method is called on leaving this state.

the

The AbstractStateMachine deﬁnes

two methods evaluate() and
set state(state). When evaluate is called, it ﬁrst checks if it should shut down
and acts accordingly by going to state ShutDownAnimation. If this is not the case,
the current active state is evaluated by calling the state’s evaluate() method.
This returns either a state to which the state machine should switch or None if it
should stay in this state. If the state machine should switch, the set state(state)
method is called. In set state(state), ﬁrst the exit() method of the current state
is called, the current state is changed to the new state, the current state is published
and the entry method of the current state is called. This process is visualized in
ﬁgure 5.5.

50

animation_serverhardware_control_manager/joint_statesJointState.msg/walking_motor_goalsJointTrajectory.msgwalking/cmd_velTwist.msg/robot_stateRobotState.msg/motor_goalsJointTrajectory.msg/imuImu.msg/gamestateGameState.msgpause/pausedbool/head_motor_goalsJointTrajectory.msg/animationAnimation.msghardware_communicationmanual_penalizeswitch_motorpower/play_animationPlayAnimation.msg5.2 Hamburg Bit-Bots Packages

Figure 5.4: UML state diagram of the HCM state machine, without shutdown con-
nections for better readability. Conditions for state transitions are writ-
ten on the arrows. Each state is deﬁned by a name (top) and its actions
(bottom) which can be done in the entry, exit or evalutation (tagged
with do) method.

The AbstractStateMachine is implemented by a HcmStateMachine class and
the AbstractState class is implemented by a set of classes representing the states
of the state machine. To share information between these classes a singleton is
introduced which holds all the necessary data, e.g. the gyro and accel values, and
has some utility methods. Furthermore, it holds an object of type FallChecker,
which provides methods to know if the robot is fallen or falling.

This completes the state machine, but a connection to the other ROS nodes is
necessary to get information and to publish the current HCM state. Therefore the
class HardwareControlManager initiates a ROS node. It creates an object of type
HcmStateMachine and calls its evaluate method periodically. To get the current
servo positions and IMU values, it subscribes to the related topics.

51

5 Implementation

Figure 5.5: UML sequence diagram of the HCM main thread. CurrentState and
NextState represent any unequal subclasses of the AbstractState. The
evaluate() method of the current state returns the next state or None
if the state should not be changed. If a new state is returned, the current
exit() method is called. Afterwards the entry() method of the new
state is called.

In the callback methods, the information is written into the VALUES object and
is thereby accessible by the states of the state machine. When the node receives
motor goals from the walking, animation or the head, it decides directly inside the
callback function if these goals can be applied in the current state. Furthermore,
the values in VALUES are updated correspondingly, e.g. to tell the state machine
that an animation is playing or the walking is active.

hcm visualization

In some cases it is diﬃcult to recognize in which state the HCM state machine is
at the moment, especially if the states are changing often. An additional plug-
in provides a visualization of the states, the state transitions and a history of the
previous states (ﬁgure 5.7).
It is loosely based on the node graph plug-in which
provides a similar GUI. The InteractiveGraphicsView class of QT is used to have
a sort of canvas on which geometrical shapes can be drawn. To easily draw the state
machine, a similar approach as in the node graph plug-in is used. First, the dot
code which represents this state machine is generated and then built in methods to

52

5.2 Hamburg Bit-Bots Packages

Figure 5.6: Simpliﬁed UML class diagram of the bitbots hcm package.

The
HardwareControlManager implements the node and provides callback
methods.
It has an object of the type HcmStateMachine. This state
machine consists of diﬀerent states which all have a class which extends
AbstractState. All states, the state machine, and the ROS node are
using a singleton called Values to exchange information. This singleton
also has an object of type FallChecker, to examine if the robot is falling
or fallen.

53

5 Implementation

Figure 5.7: The graph shows the diﬀerent states of the state machine and their
transitions. The current state is colored and a history of the active
states is provided on the right.

draw this dot code are used. The current state is colored in orange and it is possible
to hover over a state with the mouse to color the states which have transition to or
from this state. Additionally a list is displayed on the right side which lists the last
active states. This is very useful since states might change fast.

Walking

The walking was already capsuled in the old framework.
It is provided by the
ZMPWalkingEngine which allows to set the walking velocities, start and stop the
walking and to get the next goal pose for the robot with the process() method.
Around this, a ROS wrapper has been written which holds an object of this type and
calls its process() method periodically. The resulting motor goals are published
afterwards. The current motor positions and the IMU values are provided in class
variables from the call back function of their subscribers. The walking engine itself
is based on the ZMP walking [Vukobratovi´c and Borovac, 2004]. Its core is written
in C++ and it provides a Python interface via Cython. The functionalities of the
walking engine itself were not changed.

54

5.2 Hamburg Bit-Bots Packages

Animation

The animation is done in a simple action server which can cancel running animations
if needed. Therefore the animation node has an object of type SimpleActionServer.
A method execute cb() is deﬁned, which is called in a diﬀerent thread by the
SimpleActionServer whenever a new goal is received.
In this method, the cor-
responding motor goal values for the animation are generated in a loop. At each
generation point, it is checked if a new goal is available on the action server. If this
is the case, the thread decides if the current goal should be canceled or not.

The generation of motor goals for a given animation is done by an interpolation
over saved keyframes. To do this, ﬁrst an interpolation method is chosen, e.g. lin-
ear or cubic hermite [De Boor et al., 1978]. Then the keyframes are used as splines
and the curve for each motor is interpolated. This is strongly based on the pre-
existing code. The animations are saved in yaml ﬁles, which are recorded either
by an external tool or are written by hand. Such a ﬁle consists of a header and a
ﬁnite number of keyframes. Each keyframe has a duration, pause, and motor goal
positions for a set of motors. These ﬁles can be parsed into objects of the class
Animation. To get smooth trajectories for the motor goals, the Animator class
provides a update() function. This function has to be called periodically until the
animation is completed.

Pause

The pause node subscribes to the information of the game controller client and
provides a service to penalize the robot manually. These two sources of penalties
are merged into one and published on the /paused topic. The manual penalize can
overwrite the penalty from the game controller, but not the other way around. This
is useful to reset penalty states if the wiﬁ connection is distorted during a game.

5.2.2 Hardware Communication

The most common board for controlling the motors in the Humanoid League is the
CM-730 (cp. section 3.1.2). It is also used in the Minibot and thereby it is a good
choice to implement the hardware abstraction for this board, as it can be used both
for this thesis and by other teams. In the old framework, code for accessing the board
was already present but mixed with code for animation and hardware control. The
related parts of the code were extracted and put together in one package. A Cython
class for the CM-730 was written which provides an interface for the diﬀerent classes
which are used for the low-level communication.

55

5 Implementation

Figure 5.8: UML activity diagram showing how a call of the PlayAnimation action
is handled. First, the current robot state is evaluated, to see if an anima-
tion can be run. If this is the case, the animation is loaded and parsed.
Then the animation function is called in a loop to get the next motor
goals, which are then published. This loop can be intersected by a new
goal that comes from the HCM. If this is the case, the old animation is
aborted and the new one is started.

56

5.2 Hamburg Bit-Bots Packages

5.2.3 Minibot URDF

Many ROS built in features like RViz or tf require an URDF model of the robot. The
robot that was used in this thesis, Minibot, was constructed by the Hamburg Bit-
Bots themselves. Therefore an URDF had to be made (ﬁgure 5.9). The construction
of the robot was done in the CAD program Autodesk Inventor. This program
allows assembling multiple parts together inside the program. Thereby it was easy
to export a single mesh for each joint, which consists of multiple real parts. This
makes the URDF simpler, as only one visual ﬁle per link is needed. Two versions
of meshes were provided to the URDF per link. One high-resolution ﬁle for the
visual representation and a second low-quality version for the collision model. The
second version was modiﬁed using Meshlab to reduce the number of polygons and
to replace parts of the object with bounding boxes. This increases the performance
of the model during simulation. Additionally to the tf links for the movable parts of
the robot, some fake links were provided. These point to the position of the camera,
the end of the arms and the tips of the feet. This increases the usability of this
model.

Figure 5.9: Three diﬀerent visualizations of the Minibot URDF model. The visual
representation (left) is used for displaying the robot in RViz or Gazebo
since it resembles it the most. The collision model (center) is a down-
sampled version of the visual model. It is used by Gazebo for the collision
detection since it has fewer vertexes which accelerates the detection of
collisions. The tf structure (right) shows the coordinates systems of all
joints and the parent-child relationship between them.

57

5 Implementation

58

6 Evaluation

In this chapter, the previously presented approach and its implementation are eval-
uated to investigate if it is feasible. First, the architecture is compared to others in
section 6.1. Then, the transfer process is investigated in section 6.2 and the per-
formance is tested in section 6.3. Afterwards, the building of a community around
this architecture is investigated in section 6.4. Finally, the inﬂuence on the league
is examined in section 6.5.

6.1 Architecture Comparison

The two other frameworks from the HL, which are open source and based on ROS,
are chosen, for comparison. These frameworks are from the teams NimbRo and
WF Wolves, which were already mentioned in section 1.2. First, the architecture of
NimbRo is examined and compared. Afterward, the one of the WF Wolves. Finally,
another comparison with the old architecture of the Hamburg Bit-Bots is done in
order to investigate if an improvement can be observed.

6.1.1 NimbRo

robot and its

same between both robots

software architecture stayed basically
The NimbRo / igus
[Schwarz et al., 2013]
the
[Allgeuer et al., 2016]. Therefore only one comparison was made with the newest
version. An overview of the architecture can be seen in ﬁgure 6.1.

[Allgeuer et al., 2013]

While this ﬁgure gives a nice overview of the present software parts, it does not
actually show the present nodes and topics. Therefore a second diagram, ﬁgure 6.2,
was created based on the available code. This shows that the number of actual ROS
nodes is lower than one would expect after seeing ﬁgure 6.1. This is due to the
fact that the motion modules are part of the robot control node, the localization
is actually part of the vision node, and tool nodes are not displayed in the second
ﬁgure.

This low granulation leads to the problem that only large pieces of the NimbRo
architecture could be exchanged, e.g. the complete vision, not only the ball recog-
nition. The same problem persists with the motion modules which are representing
the diﬀerent direct controls of the robot, e.g. walking and fall protection. These are
modularized but use a particular plug-in system with a shared robot model object
which is also following no standard. Thereby these parts are modular but can only
be used in this specialized context and not with arbitrary ROS software. This is a
disadvantage compared to the proposed architecture, which has a high granulation

59

6 Evaluation

Figure 6.1: The

of

architecture

the NimbRo/igus

as described in
[Allgeuer et al., 2016]. The software is split into diﬀerent modules which
are grouped in categories. Unfortunately, these modules are not one to
one represented by a ROS node, cp. ﬁgure 6.2

robot

of nodes which can be used with arbitrary ROS code. A potential advantage of this
software is the performance, since the number of message transfers is far lower than
in the proposed architecture, especially in the motion section.

The low number of nodes also leads to a low parallelism, since every node is a
process. Still, a node can implement multiple threads to increase the parallelism.
This was not done for the robot control node, since all plug-ins get called one after
another in a loop.

The hardware abstraction of the NimbRo architecture is on a high level. This
means, parts like behavior and vision could run on diﬀerent robot but lower parts,
like walking or head control doesn’t. This results also from the use of the motion
plug-in system with the robot model. In the proposed architecture, only the lowest
node needs to be exchanged and all other still work if they are implemented properly.

60

6.1 Architecture Comparison

Figure 6.2: The ROS nodes and topics of the NimbRo architecture based on the code,
without displaying tools. Three main nodes are present: vision module,
walk and kick and robotcontrol. The vision module node does
the object recognition and the localization. Decisions are taken by
the walk and kick node. The robotcontrol node provides all meth-
ods to control the robots joints.
It is split up into diﬀerent mo-
tion plugins that share a common RobotModel. The team communica-
tion is done using nimbro topic transport which transports the local
TeamCommsData message to the team mates and provides the received
data to walk and kick.

61

Legend/gaitCommandGaitCommand.msgwalk_and_kick/robotcontrol/headcontrol/targetLookAtTarget.msg/ledLEDCommand.msg/walk_and_kick/teamPacketTeamCommsData.msg/game_controller/dataGCData.msg/buttonButton.msg/vision/outputsvision_outputs.msg/robotcontrol/diagnosticsDiagnostics.msgvision_module/gait/odometryGaitOdom.msgrcup_game_controllerrobotcontrol/joint_statesJointState.msg/joint_commandsJointCommands.msg/robotcontrol/stateState.msg/robotmodel/robot_headingrobot_heading.msgnimbro_topic_transportnetwork/remote/ROBOTID/walk_and_kick/teamPacketTeamCommsData.msgCM730cameraRobotModelgaitlimb_controlmotion_playerfall_protectionnimbro_op_interfacehead_controlmotion pluginnodetopicobjectplayMotionplayCommandsstd. messageservice6 Evaluation

NimbRo

GaitOdom.msg
Header
uint32
Pose
Pose2D
GaitCommand.msg
ﬂoat32
ﬂoat32
ﬂoat32
bool
uint8

ROS

Odometry.msg
Header
string
PoseWithCovariance

header
ID
odom
odom2D TwistWithCovariance
Twist.msg
Vector3
Vector3

gcvX
gcvY
gcvZ
walk
motion

header
child frame id
pose
twist

linear
angular

Figure 6.3: Comparison of messages deﬁned and used in the NimbRo software and
the standard message deﬁned by ROS which should be used in this case.
Odometry is used to provide information about the walked distance from
the walking algorithm to the localization and Twist is normally used to
provide a directive of velocities to the walking.

The used messages are almost completely not ROS standard. This can be very
reasonable in some cases but messages were implemented, for which standards al-
ready exist, see ﬁgure 6.1.1. This makes modules not compatible with other ROS
packages.
In the presented example, the walking uses diﬀerent messages for ac-
cepting commands and providing odometry information. Thereby the normal ROS
navigation stack would not be usable. In the proposed architecture, ROS standards
were used as far as possible and messages were only deﬁned for RoboCup Soccer
speciﬁc information. Thereby this architecture would also be able to use for example
the ROS navigation stack.

In addition to the specialized messages, some of the ROS internal structures were
reimplemented. Normally, parameters are handled in ROS using the parameter
server and dynamic reconﬁgure, see section 2.3.3. Team NimbRo implemented their
own parameter server because the dynamic reconfigure package ”was insuﬃcient
for the task as it did not allow the reconﬁgurable parameters to be shared globally
between the various nodes of the system.”[Allgeuer et al., 2013]

They did not state any examples for these parameters and therefore it remains
unclear which parameters have to be conﬁgurable at runtime and are used by more
than one of their nodes. Even if this feature is necessary, it should have been
added to the dynamic reconfigure package rather than implementing a complete
new package for this. The resulting problem is that all NimbRo packages have a
dependency on this specialized parameter server. Using one of their nodes would
also mean to use the parameter node and ending up with two diﬀerent parameter
systems. This is a high barrier in using their code, since it would result in having two

62

6.1 Architecture Comparison

diﬀerent systems for handling parameters. Furthermore, a user needs to learn how
In the proposed architecture this problem
to use the NimbRo parameter server.
does not arise as only the standard parameter handling methods are used. All
reconﬁgurable parameters are also node speciﬁc. For visualization RViz and rqt
were used, in relation with programmed plug-ins. This is good since the standard
tools are used and their functionalities are expanded.

In summary, the main advantage of the proposed architecture in comparison to
the NimbRo’s is that using single packages of it is easier as there are fewer inter-
dependencies and ROS standards are used. The NimbRo architecture could have a
higher performance since there are fewer messages transferred and it is completely
written in C++. On the other hand, it is less parallel and therefore only has an
advantage on CPUs with a low core number.

6.1.2 WF Wolves

The WF Wolves developed their software completely independently from the Nim-
bRo architecture, even though they are using a modiﬁed version of their robot plat-
form. No papers were released about this platform, thereby all following analysis is
only based upon their open source code. An overview of their nodes and topics is
given in ﬁgure 6.4.

The number of nodes is higher in comparison to the NimbRo code but less than
in the proposed architecture. The level of hardware abstraction is basically the
same as in the NimbRo architecture. The moveit humanoid node handles all direct
control of the robot, e.g. walking. Thereby changing the robot would also mean
that all these functionalities would have to be changed. Some of these algorithms
are outsourced to the body board which makes it hard to reuse them. Furthermore,
the node’s name is confusing, since MoveIt! is a software for robotic manipulation,
which is also integrated in ROS, but the node does not have anything to do with it.
The used messages are ROS standard where it is applicable, e.g. Twist.msg
for walking commands. The new deﬁned messages are all grouped in one package,
making it easy to use them, since only one additional dependency on a package
without further dependencies is necessary.

The packages of this architecture are easier to use than the NimbRo ones since
they have less special dependencies or messages. The main disadvantage is the use
of the body board which makes transferring of robot control algorithms, e.g. walking,
diﬃcult.

6.1.3 Hamburg Bit-Bots

The previous architecture of the Hamburg Bit-Bots was star-shaped due to the use of
the shared memory IPC and the connector, cp. ﬁgure 3.4. Star-shaped architectures
are prone to have a bottleneck. The new architecture is more homogeneous, since
all data is transfered peer-to-peer.

63

6 Evaluation

Figure 6.4: The ROS nodes and topics of the team WF Wolves based on the code,
without displaying tools. The vision process is distributed over multi-
ple nodes. The behavior consists of two nodes (decision maker and
head control). The robots joints are controlled by an external body
board which is accessed via the moveit humanoid node.

64

body boardmoveit_humanoid/cmd_velTwist.msg/head_movement_vectorVector3.msg/kick_testVector3/ball_relativeVector3/poles_relavtivePolesRelative/GameStateGameState.msg/head_modeHeadMode.msgdecision maker/raw_imageImage.msghaar_ball_ﬁnder/ball_candidatesObjectsInImage.msg/goal_candidatesObjectsInImage.msggame_controllerimage_provider_v4l/ball_in_imageObjectInImage.msghead_controlvisual_compass/vc_rotationFloat64local_localisation/poles_in_imageObjectsInImage.msgpole_ﬁlterball_ﬁltercameranetworkLegendnodetopicstd. message6.2 Transfer process to ROS

Furthermore, the new architecture is far more parallel than the old one. This is
especially important because the new used robot platform has at least eight CPU
cores. In the old architecture only two processes were used, one for the motion and
one for all higher level computing. This was appropriate at that time, since the
used robot had only two hyper threads. The old module structure was not able to
run in parallel, except for IO, because it used Python which has a global interpreter
lock. This means all threads of one process can not be run in parallel, when using
Python. The new architecture still uses Python, but each node is a single process.
Thereby the global interpreter lock only aﬀects threads in the scope of one node.

The old architecture had a custom made interface for displaying information about
the status of the robot. While it was theoretically possible to implement diﬀerent
visualizations, it had some problems, see section 3.2.3, which lead to a low usage
and little eﬀort on implementing plug-ins. The new architecture can proﬁt from the
available ROS tools. Especially useful was the new possibility to plot values using
rqt plot.

6.2 Transfer process to ROS

After ﬁnishing the deﬁnition of the architecture and the messages, it was easy to
develop the diﬀerent parts of the software with multiple developers, due to the clear
deﬁnition of interfaces and low dependencies between the nodes.

ROS also enables to easily test a package with mockup data, thereby not requiring
a complete implementation of all packages to run basic tests. This is especially
important for the behavior, since it has the most dependencies on data from other
packages. In the past, testing the behavior before the competitions was normally
not possible due to problems with other modules.

The needed time for transferring parts of the software to the new framework
depended highly on the previous degree of modularization. The walking port, which
was already modular in the old framework, took around three hours with testing.
Only a small class had to be written which accepts the goal velocities, calls the
computation method and publishes the results on a ROS topic. The implementation
of the HCM and CM730 nodes took much longer since they were not modular and
a large part of them had to be reimplemented to get clean modules.

6.3 Performance

All ROS nodes were written using rospy with the intention of making it easy to
understand for users. It would have been possible to achieve a higher performance
using roscpp. Still, an eﬀort was made to ensure a usable performance of all nodes.
During programming, it became clear that three major factors played a role in
increasing the performance of a rospy node: First, message objects should be only
generated once and then be reused. This prevents time consuming object generation.

65

6 Evaluation

cm730
joint state publisher
hcm
walking
animation
pause
buttons
Sum of all nodes
previous motion

Standing Animation Walking
58%
4%
20%
40%
7%
0%
0%
129%
60%

58%
4%
20%
12%
46%
0%
0%
140%
50%

58%
4%
10%
12%
7%
0%
0%
91%
45%

Figure 6.5: CPU loads of diﬀerent nodes and the previous motion process (left) in
three cases of robot action (top), measured on the Minibot. The highest
load is generated by the cm730 node which has to communicate with the
servos at all time. Therefore the load generated by it does not change.
The loads of animation and walking are only high when they have
to act, but they have a ground load which comes from their callback
methods. This is about 6 to 7% per subscription on a 100Hz topic, i.e.
/imu, /joint states and /motor goals.

Second, parameters should completely be read from the parameter server at the start
and saved locally. Communication with the distant parameter server is not only
time consuming, the server can also become a bottle neck, since it is a centralized
facility. Third, using rospy.Time.now() for the generation of message stamps is
more expensive than time.time(), since it synchronizes the clock via the network.
This is not necessary in this case, since all nodes are currently run on the same
machine.

The CPU load is shown in ﬁgure 6.5 and compared to the previous motion process.
All values for the imu, the current joint positions, and the joint goals are being
published at around 100Hz. More is not possible due to the limitations of the TTL
bus which was the same in the previous motion process.

Due to the split into diﬀerent nodes, a new inter process communication was intro-
duced by the publisher-subscriber relation using ROS messages. Thereby latencies
are introduced into the software. These have to be as low as possible to achieve a
high reactivity of the robot. The resulting latencies are shown in ﬁgure 6.6. They
are higher than expected, therefore a simple test publisher and subscriber was imple-
mented and tested on the Minibot as well as on a desktop computer (i5-2400 CPU
@ 3.10GHz). For this, an empty imu message with a time stamp was transferred at
100Hz, cp. ﬁgure 6.7. It is observable that the ARM board of the Minibot produces
more and higher peaks. It remains uncertain why this is the case, but it is possible
that the Linux kernel version (3.10) on the Odroid is linked to this. Unfortunately,
there are no newer kernels available for the board and therefore it was not possible

66

6.3 Performance

From
cm730
animation
walking

Message Type
To
Imu.msg
hcm
hcm
Animation.msg
hcm JointTrajectory.msg
hcm cm730 JointTrajectory.msg

Latency
7.45 ms
17.74 ms
16.90 ms
32.51 ms

Figure 6.6: Latencies between sending and receiving of messages. The Imu.msg has a
lower latency since its size is smaller. The JointTrajectory.msg which
are received by the cm730 node have a doubled latency because they are
passed through the hcm node. The stamp is done by the creating node,
i.e. walking or animation, therefore two transmissions are counted.

to validate this. Still, achieving lower latencies would be possible by using other
hardware and maybe newer kernel versions.

The highest latency is observed in the cm730 node on the motor goal topic, because
these message have passed by the hcm node. Thereby their latency is doubled, since
they are transfered two times. It would also be possible to pass the messages directly
to the cm730 node, but this would make it more complex to ensure that only one
node is writing motor goals at the same time.

When running this software on the Minibot, no diﬀerence to the previous archi-
tecture could be observed optically, e.g. while walking. This is a very subjective
perception, but no other objective method for comparing the performances could be
found in the scope of this thesis.

Figure 6.7: Comparison of latencies between the used Odroid XU-3 and the desktop
computer. An empty but stamped Imu.msg was sent and received at
100Hz. The Odroid shows a general higher latency and higher spikes.
This is possibly related to its outdated kernel version.

67

 0 0.5 1 1.5 2 2.5 3 3.5 0 500 1000 1500 2000 2500Latency [ms]MessageOdroid XU-3Desktop i5-24006 Evaluation

6.4 Community Building

Bringing others to use and further develop the implemented packages is crucial for
having an impact on the league and thereby on the research.
In order to make
this happen, there has to be a motivation for others to do so. This is normally
achieved by providing a gain which is higher than the necessary eﬀort when using
this architecture. The gain was already described in the sections 1.1, 6.1 and 6.3.
The eﬀort will be investigated later in this section. Furthermore, others have to
know about the existence of these packages and a community has to be formed
around them.

First the code has to be easily accessible for everybody. By providing it on GitHub,
it is not only easy to get the code but also to contribute, since diﬀerent ways, e.g.
making pull request or stating issues, are available on the platform.

The packages have to be included in the existing communities which are the ROS
and the RoboCup community. Pages in the ROS wiki were created, which describe
the packages and provide links to the repository and further documentation. For
RoboCup, it is more necessary to search a direct contact to the teams, since it is a
smaller community. Some teams were directly involved in the development process.
On releasing the ﬁrst version, a mail to the leagues mailing list will be send, providing
information and inviting other teams to use it. A paper was submitted to the
RoboCup symposium and the architecture will be presented there. Furthermore,
the software will be listed in the open source section of the HL website after its
release.

The code has to be understandable so that others can use and further develop
it. Therefore most of the parts were written in Python, as it provides a good
readability, even if this costs performance. The modularization and the compliance
of ROS standards helps understanding the code. Another important role is played by
the documentation. Therefore the code was commented in English and an overview
documentation was provided for every package in form of a readme ﬁle. Furthermore,
general documentation can be found in the submitted paper and this thesis.

6.5 Inﬂuence on the League

The inﬂuence of the league is not clear yet, since the proposed architecture will be
presented in the future. Still, some indicators look promising. First, the RoboCup
Foundation supported this framework ﬁnancially. This shows a general interest in
it. Furthermore, two other teams were involved in the development process and
they will change to this architecture until the next year. This means that for the
ﬁrst time an architecture will actually be shared by multiple teams in the Humanoid
League.

68

7 Conclusion

This chapter concludes the thesis in section 7.1 and provides a perspective for further
work on this topic in 7.2.

7.1 Conclusion

In this thesis, a ROS based architecture was proposed with the goal of sharing
software modules between teams in the RoboCup Humanoid League. A ﬂexible
approach of deﬁning only messages was chosen for this architecture. Furthermore,
additional packages with visualization tools and utilities were provided, so that they
can be used by all participating teams. Other teams were integrated in the process
of deﬁning these messages.

The resulting architecture was compared to two previously existing ROS based
architectures in the league. It was shown that the proposed architecture is more
ﬂexible, easier to adapt by diﬀerent teams and closer to the ROS standards. Fur-
thermore, a comparison was made to the previous architecture of the Hamburg
Bit-Bots and it was shown that the proposed architecture is easier to use and can
make better use of the new robot Minibot.

This new robot was modeled for RViz and Gazebo and integrated into a simulated
RoboCup environment. ROS nodes for the communication with the hardware and
the control of the joints, i.e. walking and keyframe animations, were written for the
Minibot. These nodes were successfully tested and the robot is now usable with the
proposed architecture.

While the impact on the league can only be observed in the future, it was already
shown that the approach is feasible by exchanging nodes between the Hamburg
Bit-Bots and the WF Wolves. The usage of ROS and this architecture oﬀers the
possibility for a better transfer of software between RoboCup and general research.

7.2 Further Work

The 2017 season of RoboCup will show the ﬁrst results of the proposed architecture,
since the Hamburg Bit-Bots and the WF Wolves will each participate in three com-
petitions with it. The experiences that will be made during them can then be used
for further reﬁning of messages or for adding additional ones. After the RoboCup
world championship, the architecture will be presented to the league.

Further work will be mostly necessary on the visualization tools. Their features
can still be improved and further packages can be added. One example would

69

7 Conclusion

be showing the status of the team communication which is necessary because the
wireless connections are very instable during competition due to a high amount of
networks. Another important aspect for the visualization is to enable data transfer
via UDP, for example by ROSUDP. Only a unidirectional UDP connection is allowed
during matches to prevent human control. Therefore the implemented visualization
tools are currently not allowed during competition.

The performance of the implemented robot control for the team Hamburg Bit-
Bots could be further increased, especially regarding the latencies. It should also be
tested on other robot platforms to ensure its general usability.

70

8 Appendix

# This message p r o v i d e s a d d i t i o n a l data from t h e s e r v o s , which i s not

i n c l u d e d i n J o i n t S t a t e . msg

AdditionalServoData.msg

# Should mainly used f o r m o n i t o r i n g and debug p u r p o s e s
# S e t t i n g t h e v a l u e t o −1 means t h e r e
float32 [ ] v o l t a g e
sensor msgs /Temperature [ ]

t e m p e r a t u r e

i s no data from t h i s motor

Animation.msg

t o make HCM c o n t r o l l a b l e , e . g .

s t o p w a l k i n g

i s a r e q u e s t

t h i s a n i m a t i o n

Header h e a d e r
# This
bool
r e q u e s t
# F i r s t message o f
f i r s t
bool
# Last message o f
bool
# I s
bool hcm
# J o i n t g o a l s
trajectory msgs / JointTrajectory p o s i t i o n

t h i s a n i m a t i o n

l a s t
t h i s a n i m a t i o n comming from t h e hardware c o n t r o l manager

BallInImage.msg

i n t h e image

i n c l u d e d t o g e t

# P r o v i d i n g a ( p o s s i b l e ) b a l l
# The h e a d e r
i s
std msgs/Header h e a d e r
# Center p o i n t o f
geometry msgs/Point c e n t e r
# Diameter o f
float6 4 d i a m e t e r
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
# 0 means no b a l l was found
floa t3 2 c o n f i d e n c e

( i n p i x e l )

t h e z−a x i s

t h e b a l l ,

t h e b a l l

t h e time stamp f o r

l a t e r u s e i n t f

s h o u l d be i g n o r e d ( i n p i x e l )

t h e s u r e s t .

BallRelative.msg

t h e b a l l

t h e time stamp

i s

t h e r e l a t i v e p o s i t i o n o f
i n c l u d e d t o g e t

# P r o v i d e s
# The h e a d e r
std msgs/Header h e a d e r
# x t o f r o n t
# y t o l e f t
# z h e i g h t
# E v e r y t h i n g i s measured i n me te rs

( s h o u l d n o r m a l l y be 0 ,

i f b a l l was not h i g h k i c k e d )

71

8 Appendix

geometry msgs/Point b a l l r e l a t i v e
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
# 0 means no b a l l was found
float32 c o n f i d e n c e

t h e s u r e s t .

# C on ta i ns m u l t i p l e b a l l s on an image . Should be mainly used t o p r o v i d e

BallsInImage.msg

b a l l c a n d i d a t e s
f i r s t

( f o r example round s h a p e s )
t h e v i s i o n p i p e l i n e .

s t e p o f

# i n t h e
# The h e a d e r
std msgs/Header h e a d e r
# An empty a r r a y means no b a l l s have been found .
humanoid league msgs/ B a l l I n I m a g e [ ]

i n c l u d e d t o g e t

c a n d i d a t e s

t h e time stamp f o r

i s

l a t e r u s e i n t f

# A ( p o s s i b l e ) g o a l bar
p o i n t s and a width .

i n t h e image .

I t

i s d e f i n e d by t h e two end

BarInImage.msg

t h e time stamp f o r

l a t e r u s e i n t f

i s

i n c l u d e d t o g e t

# The h e a d e r
std msgs/Header h e a d e r
# Two p o i n t s d e f i n i n g t h e s i g n i f i c a n t a x i s o f
geometry msgs/Point l e f t p o i n t
geometry msgs/Point r i g h t p o i n t
# Orthogonal
float32 width
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

t o s i g n i f i c a n t v e c t o r

( i n p i x e l )

t h e p o s t

t h e s u r e s t .

GameState.msg

i n f o r m a t i o n from t h e game c o n t r o l l e r

i n f o r m a t i o n s e e documentation o f

t h e game c o n t r o l l e r

# This message p r o v i d e s a l l
# f o r a d d i t i o n a l
# h t t p s : / / g i t h u b . com/bhuman/ GameController
std msgs/Header h e a d e r
uint8 GAMESTATE INITAL=0
uint8 GAMESTATE READY=1
uint8 GAMESTATE SET=2
uint8 GAMESTATE PLAYING=3
uint8 GAMESTATE FINISHED=4
uint8 gameState
uint8 STATE NORMAL = 0
uint8 STATE PENALTYSHOOT = 1
uint8 STATE OVERTIME = 2
uint8 STATE TIMEOUT = 3
uint8 s e c o n d a r y S t a t e
bool
f i r s t H a l f
uint8 ownScore
uint8 r i v a l S c o r e
# Seconds
int16 secondsRemaining
# Seconds

t h e game h a l f

r e m a i n i n g f o r

r e m a i n i n g f o r

t h i n g s

l i k e k i c k o f f

72

uint16 s e c o n d a r y s e c o n d s r e m a i n i n g
bool h a s K i c k O f f
bool p e n a l i z e d
uint16 s e c o n d s T i l l U n p e n a l i z e d
# Allowed t o move i s d i f f e r e n t
# You can f o r example be not a l l o w e d t o move due t o t h e c u r r e n t

from p e n a l i z e d .

s t a t e

o f

t h e game

bool allowedToMove
bool dropInTeam
uint16 dropInTime
uint8 p e n a l t y S h o t
uint16 s i n g l e S h o t s
string c o a c h m e s s a g e

i s

i n c l u d e d t o g e t

GoalInImage.msg
# A g o a l on t h e image . Should be e x t r a c t e d from t h e s e e n p o s t s and b a r s
# The h e a d e r
std msgs/Header h e a d e r
# L e f t p o s t
humanoid league msgs/PostInImage l e f t p o s t
# Right post , o r n u l l
humanoid league msgs/PostInImage r i g h t p o s t
# Vector p o i n t i n g t o t h e ( p r o b a b l e ) c e n t e r o f
# Should o n l y be used i f o n l y one g o a l p o s t

t h e g o a l .
i s v i s i b l e .

i f o n l y one p o s t o f

t h e o n l y s e e n one )

t h e time stamp f o r

l a t e r u s e i n t f

I f both a r e

t h e g o a l

s e e n

( o r

i s

v i s i b l e

t h i s

s h o u l d be none .

# This

i s n o r m a l l y an e d u c a t e d g u e s s , u s i n g t h e g o a l bar o r

t h e

p o s i t i o n o f

t h e p o s t on t h e image

# The p o i n t can a l s o be o u t s i d e o f
geometry msgs/Point c e n t e r d i r e c t i o n
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
# 0 means no g o a l was found .
float32 c o n f i d e n c e

t h e image

t h e s u r e s t .

GoalPartsInImage.msg

i n c l u d e d t o g e t

i s

# The h e a d e r
std msgs/Header h e a d e r
PostInImage [ ] p o s t s
BarInImage [ ] b a r s

t h e time stamp f o r

l a t e r u s e i n t f

GoalRelative.msg

t h e time stamp f o r

l a t e r u s e i n t f

i n c l u d e d t o g e t

# R e l a t i v e p o s i t i o n t o a g o a l
# The h e a d e r
i s
std msgs/Header h e a d e r
# P o s i t i o n o f
geometry msgs/Point l e f t p o s t
# P o s i t i o n o f
geometry msgs/Point r i g h t p o s t
# Vector p o i n t i n g t o t h e ( p r o b a b l e ) c e n t e r o f
# Should o n l y be used i f o n l y one g o a l p o s t

t h e r i g h t post , n u l l

l e f t g o a l p o s t

f e e t

t h e

( i n meter )

v i s i b l e

t h i s

s h o u l d be none .

t h e g o a l
i s v i s i b l e .

i f o n l y one p o s t was s e e n

( i n m et ers ) .
I f both a r e

73

8 Appendix

# This

i s n o r m a l l y an e d u c a t e d g u e s s , u s i n g t h e g o a l bar o r

t h e

p o s i t i o n o f

t h e p o s t on t h e image
geometry msgs/Point c e n t e r d i r e c t i o n
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
# 0 means no g o a l was found
float32 c o n f i d e n c e

t h e s u r e s t .

HeadMode.msg
# This message i s used f o r communicating between t h e body b e h a v i o u r and

t h e head b e h a v i o u r

t h e head by t h i s message what
i f

# The body t e l l s
# S e a r c h f o r B a l l and t r a c k i t
uint8 BALL MODE=0
# S e a r c h f o r g o a l p o s t s , mainly t o l o c a t e t h e r o b o t on t h e
uint8 POST MODE=1
# Track b a l l and g o a l by c o n s t a n t l y s w i t c h i n g between both
uint8 BALL GOAL TRACKING=2
# Look g e n e r a l l y f o r a l l

f e a t u r e s on t h e

s h a l l do

found

i t

f i e l d

f i e l d ( b a l l , g o a l s , c o r n e r s ,

c e n t e r p o i n t )

uint8 FIELD FEATURES=3
# Look f o r
e t c ) .

f e a t u r e s o u t s i d e o f

t h e

f i e l d ( p e r i m e t e r a d v e r t i s i n g , w a l l s ,

l o c a l i z a t i o n u s i n g f e a t u r e s on t h e c e i l i n g .

f e e t .

# Can be used f o r
uint8 NON FIELD FEATURES=4
# Simply l o o k down t o i t s
uint8 LOOK DOWN=5
# Simply l o o k d i r e c t l y f o r w a r d
uint8 LOOK FORWARD=7
#Don ’ t move t h e head
uint8 DONT MOVE=8
# Look t o t h e c e i l i n g ,
uint8 LOOK UP=9
uint8 headMode

f o r example f o r v i s u a l compas

geometry msgs/ Vector3 b a l l p o s
geometry msgs/ Vector3 t a r g e t

Kick.action

LineCircleInImage.msg
i n image space ,

i . e .

t h e c e n t e r

c i r c l e

c i r c l e

# D e f i n e s a l i n e
std msgs/Header h e a d e r
# The c i r c l e
p o i n t

i s d e f i n e d by an a r c with l e f t and r i g h t end p o i n t s and a

i n t h e middle f o r g e t t i n g t h e r a d i u s

geometry msgs/Point l e f t
geometry msgs/Point middle
geometry msgs/Point r i g h t

# D e f i n e s a l i n e

c i r c l e

LineCircleRelative.msg
i . e .
i n r e l a t i v e space ,

t h e c e n t e r

c i r c l e

74

i s d e f i n e d by an a r c with l e f t and r i g h t end p o i n t s and a

std msgs/Header h e a d e r
# The c i r c l e
p o i n t

i n t h e middle f o r g e t t i n g t h e r a d i u s

geometry msgs/Point l e f t
geometry msgs/Point middle
geometry msgs/Point r i g h t

LineInformationInImage.msg

r e l a t e d i n f o r m a t i o n on t h e image

i t s e l f

i n c l u d e d t o g e t

t h e time stamp f o r

l a t e r u s e i n t f

i s

l i n e

# C on ta i ns a l l
# The h e a d e r
std msgs/Header h e a d e r
LineIntersectionInImage [ ]
LineSegmentInImage [ ]
LineCircleInImage [ ]

segments

c i r c l e s

i n t e r s e c t i o n s

LineInformationRelative.msg

i s

r e l a t i v e

i n c l u d e d t o g e t

# C on ta i ns a l l
# The h e a d e r
std msgs/Header h e a d e r
LineSegmentRelative [ ]
LineIntersectionRelative [ ] markings
LineCircleRelative [ ]

segments

c i r c l e s

i n f o r m a t i o n about

l i n e

f e a t u r e s on t h e

f i e l d

t h e time stamp f o r

l a t e r u s e i n t f

LineIntersectionInImage.msg

i n t e r s e c t i o n i s p r e s e n t

i n t e r s e c t i o n f e a t u r e i n t h e image

# A l i n e
std msgs/Header h e a d e r
# The type d e f i n e s which kind o f
uint8 UNDEFINED=0
uint8 L=1
uint8 T=2
uint8 X=3
uint8 type
# The l i n e segments
humanoid league msgs/LineSegmentInImage segments
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

r e l a t e d t o t h i s

c r o s s i n g

t h e s u r e s t .

LineIntersectionRelative.msg

l i n e

f e a t u r e on t h e

f i e l d

t h e time stamp f o r

l a t e r u s e i n t f

i n t e r s e c t i o n i s p r e s e n t

i n c l u d e d t o g e t

# I n f o r m a t i o n about a s p e c i a l
# The h e a d e r
i s
std msgs/Header h e a d e r
# The type d e f i n e s which kind o f
uint8 UNDEFINED=0
uint8 L=1
uint8 T=2
uint8 X=3
uint8 type
# The l i n e segments

r e l a t e d t o t h i s

c r o s s i n g

75

8 Appendix

humanoid league msgs/LineSegmentRelative segments
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

t h e s u r e s t .

LineSegmentInImage.msg

l i n e segment

# A normal
# The h e a d e r
std msgs/Header h e a d e r
# Two p o i n t s d e f i n i n g t h e v e c t o r o f
o r t h o g o n a l l y i n t h e middle o f

i n c l u d e d t o g e t

i n t h e image

i s

t h e l i n e

t h e time stamp f o r

l a t e r u s e i n t f

t h e l i n e . The c e n t e r

i s

geometry msgs/Point s t a r t
geometry msgs/Point end
# Orthogonal
float3 2 s t a r t w i d t h
float3 2 e n d w i t h
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float3 2 c o n f i d e n c e

t o t h e s i g n i f i c a n t v e c t o r

t h e s u r e s t .

LineSegmentRelative.msg

t h e l i n e

t h e r o b o t

r e l a t i v e t o t h e r o b o t

# A l i n e segment
std msgs/Header h e a d e r
# S t a r t and end p o s i t i o n o f
# x i n f r o n t o f
# y t o t h e
l e f t
# z s h o u l d be 0
geometry msgs/Point s t a r t
geometry msgs/Point end
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float3 2 c o n f i d e n c e

t h e s u r e s t .

Model.msg

# The model message c o n t a i n s a l l

i n f o r m a t i o n from t h e o b j e c t

r e c o g n i t i o n a f t e r

f i l t e r i n g

BallRelative b a l l
ObstaclesRelative o b s t a c l e s
geometry msgs/ PoseWithCovarianceStamped p o s i t i o n

# An o b s t a c l e i n t h e image , which can be a robot , a human o r

something

ObstacleInImage.msg

i n c l u d e d t o g e t

t h e time stamp f o r

l a t e r u s e i n t f

t h e o b s t a c l e ,

t o d i f f e r e n t i a t e between r o b o t s and o t h e r

e l s e
# The h e a d e r
std msgs/Header h e a d e r
# Main c o l o r o f
t h i n g s

i s

l i k e human l e g s

# Something we c a n t c l a s s i f y
uint8 UNDEFINED = 0
# Robot w i t h o u t known c o l o r
uint8 ROBOT UNDEFINED = 1

76

uint8 ROBOT MAGENTA = 2
uint8 ROBOT CYAN = 3
# A human l e g s , e . g .
uint8 HUMAN = 4
# Black p o l e s which a r e n o r m a l l y used f o r
uint8 POLE = 5
uint8 c o l o r
# The number o f

from t h e r e f e r e e

t h e robot ,

i t

i f

t e c h n i c a l

c h a l l e n g e s

i s a r o b o t and i f

i t can be r e a d . Put

i n −1 i f not known

uint8 playerNumber
# The c o r r e s p o n d i n g s e c t i o n i n t h e image
geometry msgs/Point t o p l e f t
uint8 h e i g h t
uint8 width
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

t h e s u r e s t .

ObstacleRelative.msg

i n c l u d e d t o g e t

t h e time stamp f o r

l a t e r u s e i n t f

t h e o b s t a c l e ,

t o d i f f e r e n t i a t e between r o b o t s and o t h e r

r e l a t i v e t o t h e r o b o t

# An o b s t a c l e
# The h e a d e r
std msgs/Header h e a d e r
# Main c o l o r o f
t h i n g s

i s

l i k e human l e g s

# Something we c a n t c l a s s i f y
uint8 UNDEFINED = 0
# r o b o t w i t h o u t known c o l o r
uint8 ROBOT UNDEFINED = 1
uint8 ROBOT MAGENTA = 2
uint8 ROBOT CYAN = 3
# A human l e g s , e . g .
uint8 HUMAN = 4
# Black p o l e s which a r e n o r m a l l y used f o r
uint8 POLE = 5
uint8 c o l o r
# The number o f

from t h e r e f e r e e

t h e robot ,

i t

i f

t e c h n i c a l

c h a l l e n g e s

i s a r o b o t and i f

i t can be r e a d . Put

i n −1 i f not known

uint8 playerNumber
# P o s i t i o n ( i n m et er s )
geometry msgs/Point p o s i t i o n
# Educated g u e s s o f
floa t3 2 width
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float 32 c o n f i d e n c e

t h e width ( i n m et e rs )

t h e s u r e s t .

ObstaclesInImage.msg

# The h e a d e r
std msgs/Header h e a d e r
ObstacleInImage [ ] o b s t a c l e s

i s

i n c l u d e d t o g e t

t h e time stamp f o r

l a t e r u s e i n t f

77

8 Appendix

ObstaclesRelative.msg

# The h e a d e r
std msgs/Header h e a d e r
ObstacleRelative [ ] o b s t a c l e s

i n c l u d e d t o g e t

i s

t h e time stamp f o r

l a t e r u s e i n t f

PlayAnimation.action

# g o a l d e f i n i t i o n
# name o f
string a n i m a t i o n
# i f

t h e a n i m a t i o n

t h e a n i m a t i o n commes from t h e hardware c o n t r o l manager ,

i t

s h o u l d

i n t e r r u p t i n g o t h e r a n i m a t i o n s and w a l k i n g

s t a n d i n g up

be p l a y e d d i r e c t l y ,
# i t ’ s p r o p a b l y f a l l i n g o r
bool hcm
−−−
#r e s u l t d e f i n i t i o n
bool
−−−
#f e e d b a c k
uint8 p e r c e n t d o n e

s u c c e s s f u l

Position2D.msg

# The p o s i t i o n system i s

t h e same a s mitecom . The f o l l o w i n g p a r t

i s

taken from t h e mitecom documentation :

# h t t p s : / / g i t h u b . com/ fumanoids / mitecom
# The o r i g i n o f

t h e a b s o l u t e c o o r d i n a t e c e n t e r

middle

i s

t h e c e n t e r o f

t h e

( c e n t e r o f

f i e l d ) . The x a x i s p o i n t s

towards

t h e opponent g o a l

t o t h e

# c i r c l e
t h e
,
# y a x i s
#
#
#
#
#
#
# 0
#
#
#
#
#
#
#
# The 0 v a l u e o f

l e f t .

|
|
|

x , y

M |
Y | −x , y
|
G |
|
O |
A |
|
L

y
ˆ
|
|
|
+
|
|
|
|
+−−−−−−−−−−−−−−−−−−+−−−−−−−−−−−−−−> x

| O
| P
| P
| G
| O
| A
L
|

| −x,−y
|

x,−y

|
|
|

|
|
|

(

)

0

t h e o r i e n t a t i o n i s p o i n t i n g t o t h e opponent

s i d e (

r i g h t

s i d e i n t h e image ) .
# The v a l u e i n c r e a s e s c o u n t e r c l o c k w i s e
# E v e r y t h i n g i n m et ers
# The h e a d e r
std msgs/Header h e a d e r
geometry msgs/Pose2D p o s e

i n c l u d e d t o g e t

( b e c a u s e i t

i s

i s

t h e ROS s t a n d a r d )

t h e time stamp f o r

l a t e r u s e i n t f

78

# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float3 2 c o n f i d e n c e

t h e s u r e s t .

# A ( p o s s i b l e ) g o a l p o s t

i n t h e image .

I t

i s d e f i n e d by two end p o i n t s

PostInImage.msg

t h e time stamp f o r

l a t e r u s e i n t f

and a width .
i s

i n c l u d e d t o g e t

# The h e a d e r
std msgs/Header h e a d e r
# Two p o i n t s d e f i n i n g t h e s i g n i f i c a n t a x i s o f
geometry msgs/Point f o o t p o i n t
geometry msgs/Point t o p p o i n t
# Orthogonal
float32 width
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

t o s i g n i f i c a n t v e c t o r

( i n p i x e l )

t h e p o s t

t h e s u r e s t .

RobotControlState.msg

# This message p r o v i d e s

s t a t e o f
manager (HCM) , which i s h a n d l i n g f a l l i n g ,
d e c i s i o n

t h e c u r r e n t

t h e hardware c o n t r o l
s t a n d i n g up and t h e

# between p l a y i n g a n i m a t i o n s and w a l k i n g
# Robot can be c o n t r o l l e d from a h i g h e r
uint8 CONTROLABLE=0
# Robot
i s
# i t can not be c o n t r o l l e d and s h o u l d go t o a p o s i t i o n t h a t m i n i m i z e s

c u r r e n t l y f a l l i n g

l e v e l

t h e damage d u r i n g a f a l l

i s

r u n n i n g

l y i n g on t h e f l o o r

f u r t h e r a n i m a t i o n s p o s s i b l e

t h e s t a t e s h o u l d be un su re now

c u r r e n t l y t r y i n g t o g e t up a g a i n

uint8 FALLING=1
# Robot
# maybe r e s e t your world model , a s
uint8 FALLEN=2
# Robot
i s
uint8 GETTING UP=3
# An a n i m a t i o n i s
# no w a l k i n g o r
# F a l l i n g d e t e c t i o n i s d e a c t i v a t e d
uint8 ANIMATION RUNNING=4
# The hardware c o n t r o l manager
uint8 STARTUP=5
# The hardware c o n t r o l manager
uint8 SHUTDOWN=6
# The r o b o t
i s
# I t can not be c o n t r o l l e d
uint8 PENALTY=7
# The r o b o t
uint8 PENALTY ANIMANTION=8
# The r o b o t
# Reserved a l l
# No f a l l i n g d e t e c t i o n i s p r o c e s s e d and no s t a n d ups w i l l be done
uint8 RECORD=9
# The r o b o t

i s g e t t i n g i n o r out o f p e n a l t y p o s i t i o n

c o n t r o l i n g t o a r e c o r d i n g p r o c e s s

r e c o r d i n g a n i m a t i o n s

i n p e n a l t y p o s i t i o n

s h u t t i n g down

i s used f o r

i s w a l k i n g

i s b o o t i n g

i s

79

8 Appendix

i s
# i f a move commando comes
uint8 MOTOR OFF=11
# Last
uint8 HCM OFF=12
uint8 s t a t e

s t a t u s

uint8 WALKING=10
# A s t a t e where t h e motors a r e t u r n e d o f f , but t h e hardware c o n t r o l
t h e motors on ,
s t i l l w a i t i n g f o r commandos and t u r n s

manager

send by t h e hardware c o n t r o l manager a f t e r

s h u t t i n g down

# This message i s used t o a c t i v a t e t h e a u d i o output o f
# This can be used f o r debug p ro p o se d but a l s o f o r n a t u r a l

t h e r o b o t

l a n g u a g e

team communication

Speak.msg

# The t e x t w i l l o n l y be outputed i f ” f i l e n a m e ” i s empty
string t e x t
uint8 LOW PRIORITY=0
uint8 MID PRIORITY=1
uint8 HIGH PRIORITY=2
uint8 p r i o r i t y
# I f a f i l e

s h o u l d be read ,

t h e path has
s t r i n g s h o u l d be n u l l

Ot herw ise t h i s

string f i l e n a m e

t o be s p e c i f i e d h e r e .

# This message p r o v i d e s

i n f o r m a t i o n about

r o b o t

t o t h e team communication s o t h a t

t h e c u r r e n t
i t can be

s t r a t e g y o f

t h e

Strategy.msg

# s h a r e d with o t h e r team r o b o t s
# Which r o l e t h e r o b o t has c u r r e n t l y
uint8 ROLE IDLING=0
uint8 ROLE OTHER=1
uint8 ROLE STRIKER=2
uint8 ROLE SUPPORTER=3
uint8 ROLE DEFENDER=4
uint8 ROLE GOALIE=5
uint8 r o l e
# The c u r r e n t a c t i o n o f
uint8 ACTION UNDEFINED=0
uint8 ACTION POSITIONING=1
uint8 ACTION GOING TO BALL=2
uint8 ACTION TRYING TO SCORE=3
uint8 ACTION WAITING=4
uint8 a c t i o n
# O f f e n s i v e s t r a t e g y
uint8 SIDE LEFT = 0
uint8 SIDE MIDDLE = 1
uint8 SIDE RIGHT = 2
uint8 o f f e n s i v e s i d e

t h e r o b o t

80

# This message c o n t a i n s a l l

i n f o r m a t i o n p r o v i d e d by t h e mitecom

TeamData.msg

team communication .
i n m ete rs
( mitecom s t a n d a r d ) !

s t a n d a r d f o r
# E v e r y t h i n g i s
m i l l i m e t e r s
t o 0 i f o b j e c t was not
# S e t b e l i e f v a l u e s
# More i n f o r m a t i o n h e r e : h t t p s : / / g i t h u b . com/ fumanoids / mitecom
std msgs/Header h e a d e r
# Every v a l u e

i s an a r r a y b e c a u s e we can have m u l t i p l e r o b o t s

(ROS s t a n d a r d ) not

r e c o g n i z e d .

t o be c o n f u s e d with

communicating with us .

i d s

r o b o t i d s

# The v a l u e s match with t h e r o b o t
uint8 [ ]
uint8 ROLE IDLING=0
uint8 ROLE OTHER=1
uint8 ROLE STRIKER=2
uint8 ROLE SUPPORTER=3
uint8 ROLE DEFENDER=4
uint8 ROLE GOALIE=5
uint8 [ ]
r o l e
uint8 ACTION UNDEFINED=0
uint8 ACTION POSITIONING=1
uint8 ACTION GOING TO BALL=2
uint8 ACTION TRYING TO SCORE=3
uint8 ACTION WAITING=4
uint8 [ ] a c t i o n
uint8 STATE INACTIVE=0
uint8 STATE ACTIVE=1
uint8 STATE PENALIZED=2
uint8 [ ]
# A b s o l u t e p o s i t i o n v a l u e s
geometry msgs/Pose2D [ ]
# R e l a t i v e b a l l p o s i t i o n ,
Position2D [ ] b a l l r e l a t i v e
# R e l a t i v e p o s i t i o n o f
# This

i s h e l p f u l

s t a t e

i f

r o b o t p o s i t i o n s

t h e t a o f Pose2D i s not used

t h e opponent g o a l ,

t h e t a o f Pose2D i s not used

t h e r o b o t has no g l o b a l p o s i t i o n , but

s e e s

t h e

g o a l

Position2D [ ] o p p g o a l r e l a t i v e
# P o s i t i o n s o f opponent
# The l e t t e r o f

t h e r o b o t

r o b o t s ,

i f
i s a r b i t r a r y a s

they a r e r e c o g n i z e d

t h e s e n d i n g r o b o t d o e s not

know t h e i d o f a s e e n r o b o t

Position2D [ ] o p p o n e n t r o b o t a
Position2D [ ] o p p o n e n t r o b o t b
Position2D [ ] o p p o n e n t r o b o t c
Position2D [ ] o p p o n e n t r o b o t d
# P o s i t i o n s o f
# The l e t t e r o f

team r o b o t s ,
t h e r o b o t

know t h e i d o f a s e e n r o b o t

Position2D [ ]
Position2D [ ]
Position2D [ ]
float32 [ ] a v g w a l k i n g s p e e d

t e a m r o b o t a
t e a m r o b o t b
t e a m r o b o t c

i f

they a r e r e c o g n i z e d

i s a r b i t r a r y a s

t h e s e n d i n g r o b o t d o e s not

81

8 Appendix

t i m e t o p o s i t i o n a t b a l l

float3 2 [ ]
float32 [ ] m a x k i c k i n g d i s t a n c e
# S t r a t e g y o v e r which s i d e t h e team t r i e s
# E s p e c i a l l y u s e f u l d u r i n g a k i c k o f f
uint8 UNSPECIFIED=0
uint8 LEFT=1
uint8 RIGHT=2
uint8 CENTER=3
uint8 [ ] o f f e n s i v e s i d e

t o a t t a c k

VisualCompassRotation.msg

# This message i s used t o s p e c i f y t h e o r i e n t a t i o n o f

t h e v i s u a l compass

i n r e l a t i o n t o a RoboCup S o c c e r

f i e l d

t o t h e opponent g o a l

# 0 p o i n t s
float32 o r i e n t a t i o n
# A c e r t a i n t y r a t i n g between 0 and 1 , where 1 i s
float32 c o n f i d e n c e

l i n e , 3 . 1 4 t o t h e own g o a l

l i n e

t h e s u r e s t .

82

Bibliography

[Allgeuer et al., 2016] Allgeuer, P., Farazi, H., Ficht, G., Schreiber, M., and Behnke,
S. (2016). The igus Humanoid Open Platform. KI-K¨unstliche Intelligenz, pages
1–5.

[Allgeuer et al., 2013] Allgeuer, P., Schwarz, M., Pastrana, J., Schueller, S., Mis-
sura, M., and Behnke, S. (2013). A ROS-based software framework for the
NimbRo-OP humanoid open platform. In Proceedings of 8th Workshop on Hu-
manoid Soccer Robots, IEEE-RAS Int. Conference on Humanoid Robots, Atlanta,
USA.

[Anders et al., ] Anders, B., Stiddien, F., Krebs, O., Gerndt, R., Bolze, T., Lorenz,
T., Chen, X., Londero, F. T., et al. WF Wolves & Taura Bots–Humanoid Teen
Size Team Description for RoboCup 2016.

[Bruyninckx, 2001] Bruyninckx, H. (2001). Open robot control software: the ORO-
COS project. In Robotics and Automation, 2001. Proceedings 2001 ICRA. IEEE
International Conference on, volume 3, pages 2523–2528. IEEE.

[De Boor et al., 1978] De Boor, C., De Boor, C., Math´ematicien, E.-U., De Boor,
C., and De Boor, C. (1978). A practical guide to splines, volume 27. Springer-
Verlag New York.

[Fabre et al., 2016] Fabre, R., Rouxel, Q., Passault, G., N’Guyen, S., and Ly, O.
(2016). Dynaban, an Open-Source Alternative Firmware for Dynamixel Servo-
Motors. In Symposium RoboCup.

[Forero et al., 2013] Forero, L. L., Y´anez, J. M., and Ruiz-del Solar, J. (2013). Inte-
gration of the ROS framework in soccer robotics: the NAO case. In Robot Soccer
World Cup, pages 664–671. Springer.

[Gerkey, 2015] Gerkey, B. (2015). ROS, the Robot Operating System, Is Grow-
Retrieved from IEEE Spec-
http://spectrum.ieee.org/automaton/robotics/roboticssoftware/ros-robot-

ing Faster Than Ever, Celebrates 8 Years.
trum:
operating-system-celebrates-8-years.

[Gerkey et al., 2003] Gerkey, B., Vaughan, R. T., and Howard, A. (2003). The
player/stage project: Tools for multi-robot and distributed sensor systems.
In
Proceedings of the 11th international conference on advanced robotics, volume 1,
pages 317–323.

83

Bibliography

[Gerndt et al., 2015] Gerndt, R., Seifert, D., Baltes, J. H., Sadeghnejad, S., and
Behnke, S. (2015). Humanoid robots in soccer: Robots versus humans in RoboCup
2050. IEEE Robotics & Automation Magazine, 22(3):147–154.

[Gouaillier et al., 2008] Gouaillier, D., Hugel, V., Blazevic, P., Kilner, C., Mon-
ceaux, J., Lafourcade, P., Marnier, B., Serre, J., and Maisonnier, B. (2008).
The nao humanoid: a combination of performance and aﬀordability. CoRR
abs/0807.3223.

[Ha et al., 2011] Ha, I., Tamura, Y., Asama, H., Han, J., and Hong, D. W. (2011).
Development of open humanoid platform DARwIn-OP. In SICE Annual Confer-
ence (SICE), 2011 Proceedings of, pages 2178–2181. IEEE.

[Kajita et al., 2014] Kajita, S., Hirukawa, H., Harada, K., and Yokoi, K. (2014).

Introduction to humanoid robotics, volume 101. Springer.

[Khandelwal and Stone, 2011] Khandelwal, P. and Stone, P. (2011). A low cost
ground truth detection system for RoboCup using the Kinect. In Robot Soccer
World Cup, pages 515–527. Springer.

[Kohlbrecher et al., 2014] Kohlbrecher, S., Kunz, F., Koert, D., Rose, C., Manns,
P., Daun, K., Schubert, J., Stumpf, A., and von Stryk, O. (2014). Towards Highly
Reliable Autonomy for Urban Search and Rescue Robots. In Robot Soccer World
Cup, pages 118–129. Springer.

[Kohlbrecher et al., 2013] Kohlbrecher, S., Meyer, J., Graber, T., Petersen, K.,
Klingauf, U., and von Stryk, O. (2013). Hector open source modules for au-
In Robot Soccer World
tonomous mapping and navigation with rescue robots.
Cup, pages 624–631. Springer.

[Kohlbrecher et al., 2012] Kohlbrecher, S., Petersen, K., Steinbauer, G., Maurer,
J., Lepej, P., Uran, S., Ventura, R., Dornhege, C., Hertle, A., Sheh, R., et al.
(2012). Community-driven development of standard software modules for search
and rescue robots. In SSRR, pages 1–2.

[Kootbally et al., 2013] Kootbally, Z., Balakirsky, S., and Visser, A. (2013). En-
abling codesharing in rescue simulation with usarsim/ros. In Robot Soccer World
Cup, pages 592–599. Springer.

[Mamantov et al., 2014] Mamantov, E., Silver, W., Dawson, W., and Chown, E.
(2014). Robograms: A lightweight message passing architecture for robocup soc-
cer. In Robot Soccer World Cup, pages 306–317. Springer.

[McGill et al., 2013] McGill, S. G., Yi, S.-J., Zhang, Y., and Lee, D. D. (2013).
Extensions of a robocup soccer software framework. In Robot Soccer World Cup,
pages 608–615. Springer.

84

Bibliography

[Metta et al., 2006] Metta, G., Fitzpatrick, P., and Natale, L. (2006). Yarp: Yet an-
other robot platform. International Journal of Advanced Robotic Systems, 3(1):8.

[Murphy, 2000] Murphy, R. (2000). Introduction to AI robotics. MIT press.

[Nii, 1986] Nii, H. P. (1986). Blackboard application systems, blackboard systems

and a knowledge engineering perspective. AI magazine, 7(3):82.

[Perico et al., 2014] Perico, D. H., Silva, I. J., Vil˜ao, C. O., Homem, T. P., De-
stro, R. C., Tonidandel, F., and Bianchi, R. A. (2014). Hardware and software
aspects of the design and assembly of a new humanoid robot for robocup soc-
cer. In Robotics: SBR-LARS Robotics Symposium and Robocontrol (SBR LARS
Robocontrol), 2014 Joint Conference on, pages 73–78. IEEE.

[Quigley et al., 2009] Quigley, M., Conley, K., Gerkey, B., Faust, J., Foote, T.,
Leibs, J., Wheeler, R., and Ng, A. Y. (2009). ROS: an open-source Robot Op-
erating System. In ICRA workshop on open source software, volume 3, page 5.
Kobe, Japan.

[Ramsden, 2011] Ramsden, E. (2011). Hall-eﬀect sensors: theory and application.

Newnes.

[R¨ofer and Laue, 2013] R¨ofer, T. and Laue, T. (2013). On B-human’s code releases
in the standard platform league–software architecture and impact. In Robot Soccer
World Cup, pages 648–655. Springer.

[Ruiz et al., 2013] Ruiz, J. A. ´A., Pl¨oger, P., and Kraetzschmar, G. K. (2013). Ac-
tive scene text recognition for a domestic service robot. In RoboCup 2012: Robot
Soccer World Cup XVI, pages 249–260. Springer.

[Sanner et al., 1999] Sanner, M. F. et al. (1999). Python: a programming language

for software integration and development. J Mol Graph Model, 17(1):57–61.

[Schwarz et al., 2013] Schwarz, M., Pastrana, J., Allgeuer, P., Schreiber, M.,
Schueller, S., Missura, M., and Behnke, S. (2013). Humanoid teensize open plat-
form nimbro-op. In Robot Soccer World Cup, pages 568–575. Springer.

[Stroud et al., ] Stroud, A., Carey, K., Chinang, R., Gibson, N., Panka, J., Ali,
W., Brucato, M., Procak, C., and Morris, M. Team MU-L8 Humanoid League–
TeenSize Team Description Paper 2014.

[Stroud et al., 2013] Stroud, A. B., Morris, M., Carey, K., Williams, J. C., Ran-
dolph, C., and Williams, A. B. (2013). MU-L8: The Design Architecture and
3D Printing of a Teen-Sized Humanoid Soccer Robot. In 8th Workshop on Hu-
manoid Soccer Robots, IEEE-RAS International Conference on Humanoid Robots,
Atlanta, GA.

85

Bibliography

[Upton and Halfacree, 2014] Upton, E. and Halfacree, G. (2014). Raspberry Pi user

guide. John Wiley & Sons.

[Vukobratovi´c and Borovac, 2004] Vukobratovi´c, M. and Borovac, B. (2004). Zero-
moment point—thirty ﬁve years of its life. International Journal of Humanoid
Robotics, 1(01):157–173.

[Wescott, 2000] Wescott, T. (2000). Pid without a phd. Embedded Systems Pro-

gramming, 13(11):1–7.

86

Internet Sources

[1] https://github.com/Pold87/academic-keyword-occurrence.

[2] http://www.b92.net/zivot/nauka.php?yyyy=2012&mm=09&dd=07&nav_id=

641200.

[3] wiki.ros.org.

[4] http://www.pirobot.org/blog/0025/.

[5] http://en.robotis.com.

[6] http://support.robotis.com/en/techsupport_eng.htm.

[7] http://en.robotis.com/index/product.php?cate_code=101010.

[8] https://github.com/fumanoids/mitecom.

[9] https://www.robocuphumanoid.org/materials/rules/.

[10] http://www.hardkernel.com/main/products/prdt_info.php?g_code=

G140448267127.

[11] https://www.robocuphumanoid.org/wp-content/uploads/

\HumanoidLeagueProposedRoadmap.pdf.

[12] https://github.com/NimbRo/.

[13] http://www.eng.mu.edu/abwilliams/heirlab/index.html.

[14] https://github.com/ROBOTIS-OP.

[15] https://github.com/igusGmbH/HumanoidOpenPlatform.

[16] https://github.com/AIS-Bonn/humanoid_op_ros.

[17] http://www.robocup2016.org/de/symposium/team-description-papers/.

[18] http://www.robocup.org/about-robocup/a-brief-history-of-robocup.

87

Internet Sources

88

Eidesstattliche Erkl¨arung

Hiermit versichere ich an Eides statt, dass ich die vorliegende Arbeit im Masterstudi-
engang Informatik selbstst¨andig verfasst und keine anderen als die angegebenen Hilf-
smittel – insbesondere keine im Quellenverzeichnis nicht benannten Internet-Quellen
– benutzt habe. Alle Stellen, die w¨ortlich oder sinngem¨aß aus Ver¨oﬀentlichungen
entnommen wurden, sind als solche kenntlich gemacht.
Ich versichere weiterhin,
dass ich die Arbeit vorher nicht in einem anderen Pr¨ufungsverfahren eingereicht
habe und die eingereichte schriftliche Fassung der auf dem elektronischen Speicher-
medium entspricht.

Hamburg, den 06.04.2017

Marc Bestmann

Ver¨oﬀentlichung

Ich stimme der Einstellung der Arbeit in die Bibliothek des Fachbereichs Informatik
zu.

Hamburg, den 06.04.2017

Marc Bestmann

