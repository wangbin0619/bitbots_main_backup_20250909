Application from Hamburg Bit-Bots for
Robocup 2013

Timon Giese, Maxim Holand, Robert Keßler, Maike Paetzel, Martin Poppinga,
Nils Rokita, Robert Schmidt, Heye V¨ocking

Department of Informatics, University of Hamburg info@bit-bots.de

Abstract. Hamburg Bit-Bots is a highly motivated team interested in
the wide ﬁelds of robotics. Over the last two years we have developed
our own software for the RoboCup tournament and gathered much ex-
perience. Our goal is not only to score, but to share this knowledge with
like-minded people from all over the world.
Last year we were able to learn from the experiences gathered during that
time and improved our software based on that. We are doing research in
many diﬀerent ﬁelds, among other things and globally unique topics as
team communication based on natural language.

1 Our Team

The team Hamburg Bit-Bots consists of a group of students from the Department
of Informatics at the University of Hamburg, Germany. The team is ﬁnancially
supported by the department and the university. Apart from that Hamburg Bit-
Bots are an independent work group lead and organised by students.

We are using the Darwin OP robots produced by Robotics and Mechanisms
Laboratory. All team members are currently studying computer science or Com-
puting in Science and are working on their bachelor’s or master’s degrees.

2 Research

2.1 Research until now

We will give a short draft of the published work by some of our group members.
Due to the fact that our team consists only of students, the published works so
far are mostly bachelor theses.

Evolving Locomotion for the DARwIn-OP Is a bachelor thesis work-in-
progress where walking with neural networks is learned using evolution on a
Darwin model in Webots. In the future we consider to transfer a successful
and stable walk to the real Darwin.

Team coordination in RoboCup soccer based on natural language Maike
Paetzel is currently writing her Bachelor thesis about a new strategy for
robot to robot communication during RoboCup games. In the last years the

2

coordination based on the wireless network was error-prone because of the
unstable network hardware during the championships. Particularly with re-
gard to the aim in 2050 the solution is a new communication protocol that is
adapted to natural language. Robots should exchange their most important
information via speech production and language processing.

Ball recognition based on probability distribution of shapes Sandra Schr¨oder

developed a process to determine whether a given shape would match the
soccer ball or not. She uses an elaborate edge detection algorithm in combi-
nation with the probability distribution of the position of edges to calculate
the possibility of a given shape in the presented image.

Behaviour based coordination of a multi robot scenario realized by BDI-agents

Group member Anja Richter wrote her Bachelor thesis on the modelling of
a behaviour for a logistic scenario. The behaviour is realized by software
agents according to the believe-intention-desire model and then transferred
to a multi robot system.

Estimation of optical-ﬂow ﬁelds in multispectral images is a ﬁnished bach-
elor thesis written by Oliver Bestmann in the ﬁeld of cognitive science. The
developed algorithm is able to robustly estimate the optical-ﬂow in an image
sequence using additional information provided by color gradients. It can be
used for better tracking of the ball once it is located.

Ball veriﬁcation The group members Lasse Einig and Anja Richter wrote an
article about the ball veriﬁcation they developed for the object recognition
tool for the NAO robot in the Standard Platform League 2011.

2.2 Current research

We will give you are short overview of our current research topics.

Construction design of new feet and heads for the new cameras As
the DarwinOP has some problems with parts of its hardware we are working on
our hardware, too. We tried to build our behaviour in parts on the distance to
the ball. This distance was calculated with the angle of the head and the size of
the ball on the picture. The camera in the Darwins head is ﬁxed on the plastic
and this is ﬁxed to the body with a connector. That means the camera is very
shaky and for that the angle is useless for calculating. That was the reason for
us to design new heads and plot it with a 3D plotter. In this new heads will be
enough space for our new cameras with higher resolution.
The second building area are the feet of the Darwins. Because humans are not
walking with ﬂat feet but doing a roll motion we try to design feet that make
this roll motion possible, too. By now we have a prototype made of wood and
try to make our new walk stable.

Evolving Locomotion for the DARwIn-OP The purpose of the bachelor
thesis is the evolution of artiﬁcial neural networks to develop locomotion for the
Darwin robot. The main problem in robot soccer is a robust and fast locomotion.

3

Since a humanoid robot is a very complex system, it is diﬃcult to hand craft a
robust walking algorithm. Furthermore it needs to be adjusted by hand if the
ﬂoor or the weight distribution of the robot itself is changed. An approach to
automatically develop a walking algorithm is the biologically inspired evolution
in which a gradual improvement of individual solutions can be achieved over
many generations. Advantage of the evolution is that the problem itself doesn’t
need to be solved, but one only needs a so-called ﬁtness function, which rates the
quality of a solution. But evolution has also certain diﬃculties which have to be
overcome. The ﬁtness function has to be designed very carefully in order to get
good results. We are using a realistic model of the DARwIn-OP in the Webots
simulator for the experiments so the ﬁnal solution can eventually be transferred
to the real Darwin. Because of the promising results we had so far we are now
trying to optimize the evolution to develop a more robust solution.

Pointcloud-based self-calibrating vision Our vision is based on point clouds.
These point clouds are pre-generated sets of points that we use for image pro-
cessing. The point clouds are generated at start-up. Generating means creating
and sorting random points and reference to each of them an array of their near-
est neighbours including the distances. Using this point clouds enables us to
gain higher resolution on certain areas of the image. So in particular we use
three diﬀerent point clouds according to our input and the resolution we want
to achieve in a particular area of the input image. Another topic on vision is the
ﬁeld recognition. We implemented a self-calibrating model to recognize the ﬁeld
colour even if it is diﬀerent under changing lightning conditions. This helps us
in achieving a fast set-up in a new environment which is certainly necessary for
future robotics research.

Localisation on the ﬁeld At the moment we are using no complete localisa-
tion. The robot just knows where the ball is and where the goals are. But we are
going to rewrite the localisation started in October 2012. The new localisation
will be based on Kalman Filter line tracking to localise the robot. To support
the visual localisation process, we aim at a motion tracking system. This sys-
tem will record the movement of the robot and ﬁgure out the rough position
and direction of the robot. This can be used to reduce the computing time and
increase the precision of the localisation .

Robot/Team Communication based on natural language The goal of
RoboCup is playing soccer as similar to humans as possible. To get a step closer
to that goal we try to convert our robot to robot communication from wireless
communication to natural language. We are currently developing a new com-
munication protocol that is optimized to the requirements of natural language.
Every robot can transport their own data to the other robots via speech synthesis
and gets data from them via language processing.

4

Continuous simulation and evaluation of tryouts To test our robot be-
haviour we plan to set-up a continuous integration system which is simulating
nightly our source code in a virtual environment. Therefore we are just evaluat-
ing simulation frameworks which can be used. With this set-up we would like to
raise our software quality and give it a measurement.

Complex behaviour The behaviour is modelled with ﬁnite automata. This
means that every abstract state like ”Search for Ball” is capsuled in such a state
executing the piece of code that is particular assigned to this situation. In each
such a state there are conditions which when met make a transition to another
state happen. In future we want to improve that model and maybe add a state
machine in which a state could be a state machine itself. Furthermore we want
to improve testability of the behaviour software part due to it complexity. This
means ﬁnding a way to make it at least a bit more possible to design such a
complex behavioural system.

Robot recognition One of the common problems in our ﬁeld is to recognise
the shape of a robot, regardless of the robot type. This has to be done in a very
time and space eﬃcient way. We are testing a new kind of algorithm to segment
a binary image really fast (O(n)) , and check objects for their “limbs” in order
to classify an object on the ﬁeld as a robot.

Sound Source Localisation To check where a player is we plan to use sound
source localisation. This is useful at least from the point where the robots are
talking to each other with natural language. Diﬀerent voice types can be used
to identify diﬀerent robots. This would give a major beneﬁt in localizing in a
multidimensional way.

3 Prior performance in RoboCup

The Hamburg Bit-Bots team was founded in 2011 as a group of former par-
ticipants of the oﬃcial robocup bachelor project. The aim of the team was to
enlarge the experience won during the project time. Cooperation with the SPL
team RFC St. Ellingen is limited to the sharing of the laboratory. The cur-
rent team was explicitly founded for the participation in the humanoid league
and thus started from the beginning with new robots and a newly developed
codebase.

In 2011 we started our working group and were busy recruiting students and

setting up our robots.

Last year we participated in RoboCup German Open and were placed third.
Furthermore, we took part in the world championship in Mexico City and were
dropped out in second round robin, but successfully ﬁnished the Throw-In chal-
lenge. Apart from that we joined the Robow 12.1, 12.2 and 12.3 in Berlin to
push the interconnectedness between the european robocup teams and take part
in a research exchange.

5

4 Further dedication in RoboCup

Beyond the participation in the championship we do have many projects to
make robotics and RoboCup accessible to people. For example we are going to
participate in ”Robots on tour” in Zurich 2013 and in the German Protestant
Kirchentag.

5 Code from other Teams

Right now all of our codebase is written by members or former members of our
team. We do not use any code from other teams.

6 Statements

6.1 Participate

We assure to participate in the RoboCup 2013 Humanoid League.

6.2 Referee

We assure that we have a person with suﬃcient knowledge of the rules. We assure
that this person will be available as referee during the competition.

7 Conclusion

We achieved a lot experience in last years RoboCup season and are working much
to improve our software for next year. We managed to correct our software in
many aspects, for example we are now able to walk stable and do localisation
on the ﬁeld.

We are looking forward to see how our robots acquit themselves on the cham-
pionships with the new software. We see the RoboCup World Championships as
an opportunity to exchange our experiences with other students and researchers
from all over the world and to improve and communicate our knowledge.
We sincerely hope to get the chance to be part of this great event.

