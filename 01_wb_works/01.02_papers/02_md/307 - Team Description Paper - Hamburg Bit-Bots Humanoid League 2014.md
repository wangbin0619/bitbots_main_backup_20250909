Application from Hamburg Bit-Bots for
Robocup Worldcup 2014

Marc Bestmann, Juliane B¨odeker, Timon Giese, Maxim Holand, Jessica Jobski,
Robert Keßler, Maike Paetzel, Martin Poppinga, Dennis Reher, Bente
Reichard, Nils Rokita, Robert Schmidt, Lars Thoms

Department of Informatics, Universit¨at Hamburg, info@bit-bots.de

Abstract. Hamburg Bit-Bots is a highly motivated team interested in
the wide ﬁelds of robotics. Over the last two years we have developed our
own software for the RoboCup tournament and gathered much experi-
ence. Last year we were able to learn from the experiences and improved
our software based on that. Among other topics, we are conducting re-
search in many diﬀerent ﬁelds, from team communication based on nat-
ural language to human-like shaped Darwin-feet

1 Our Team

The team Hamburg Bit-Bots consists of a group of students from the Department
of Informatics at the University of Hamburg, Germany. The team is ﬁnancially
supported by the department and the university. Apart from that Hamburg Bit-
Bots are an independent work group lead and organised solely by students.

We are using modiﬁed Darwin OP robots produced by Robotis. All team
members are currently computer science related students and are working on
their bachelor’s or master’s degrees.

2 Research

2.1 Research until now

We will give a short draft of the published work by some of our group members.
Due to the fact that our team consist only of students, the published work so
far are mostly bachelor thesis.

Team coordination in RoboCup soccer based on natural language

Maike Paetzel has written her bachelor thesis about a new strategy for robot
to robot communication during RoboCup games. In the last years the coordi-
nation based on the wireless network was error-prone because of the unstable
network during the championships. Particularly with regard to ”2050” the
solution is a new communication protocol that is adapted to natural lan-
guage. Robots should exchange their most important information via speech
production and language processing.

2

Ball recognition based on probability distribution of shapes

Sandra Schr¨oder developed a process to determine whether a given shape
would match the soccer ball or not. She uses an elaborate edge detection
algorithm in combination with the probability distribution of the position of
edges to calculate the possibility of a given shape in the presented image.
Behaviour based coordination of a multi robot scenario realized by

BDI-agents
Group member Anja Richter wrote her bachelor thesis on the modelling of
a behaviour for a logistic scenario. The behaviour is realized by software
agents according to the believe-intention-desire model and then transferred
to a multi robot system.

Estimation of optical-ﬂow ﬁelds in multispectral images

This ﬁnished bachelor thesisk was written by Oliver Bestmann in the ﬁeld
of cognitive science. The developed algorithm is able to robustly estimate
the optical-ﬂow in an image sequence using additional information provided
by color gradients. It can be used for better tracking of the ball once it is
located.

Ball veriﬁcation

The group members Lasse Einig and Anja Richter wrote an article about
the ball veriﬁcation they developed for the object recognition tool for the
NAO robot in the Standard Platform League 2011.

Improving the stability and durability of the Darwin Camera Hard-

ware
The Darwin-OP head has some ﬂaws in it’s design. The camera is mounted
directly in the front of the head and is only secured by the plastic peel of
the head. We had several issues with defective contacts of the camera caused
by falling forward. Our decision was to design a new head for our robots to
protect the camera from damage. Now we are using a new camera protected
by a new head, made of aluminium, developed by us.

2.2 Current research

We will give you are short overview of our current research topics.

Construction design of new feet The Darwin-OPs feet are ﬂat and mounted
in their center to the leg. Because humans are not walking with ﬂat feet but doing
a roll motion we try to design feet that make this roll motion possible, too. By
now we have a prototype made of aluminium with a hinge-joint and springs
might render our robots walking more stable.

Pointcloud-based self-calibrating vision Our vision is based on point clouds.
These point clouds are pre-generated sets of points that we use for image pro-
cessing. The point clouds are generated at start-up. Generating means creating
and sorting random points and reference to each of them an array of their near-
est neighbours including the distances. Using this point clouds enables us to

3

gain higher resolution in some areas of the image. In particular we use three
diﬀerent point clouds according to our input and the resolution we want to
achieve in a particular area of the input image. Another topic is the ﬁeld recog-
nition. We implemented a self-calibrating model to recognize the ﬁeld colour
even under changing lighting conditions. Also, we implemented autocalbration
for Ball-colors. This also enables us to play with multi colored balls. This allows
us a fast set-up in a new environment.

Localisation on the ﬁeld We had rewritten our localisation in 2012 to be
based on the Kalman Filter and line tracking to localise the robot. However the
results did not satisfy us, so another rewrite is scheduled. This time we want to
try some artiﬁcial learning algorithm.

Robot/Team Communication based on natural language The goal of
the RoboCup is playing soccer as similar to humans as possible. To get a step
closer to this goal we try to convert our robot to robot communication from
wireless communication to natural language. We are currently developing a new
communication protocol that is optimized to the requirements of natural lan-
guage. Every robot can communicate to the other robots via speech synthesis
and gets information from them via language processing.

Continuous simulation and evaluation of tryouts To test our robot be-
haviour we plan to set-up a continuous integration system which is simulating
our source code in a virtual environment on nightly basis. Currently we are at
adapting the simspark simulation framework for our needs. With this set-up we
would like to raise our software quality and give it a measurement.

Complex behaviour The behaviour is currently modelled with ﬁnite au-
tomata. This means that every abstract state like ”Search for Ball” is capsuled
in such a state executing the piece of code that is particular assigned to this
situation. In each such a state there are conditions which, when met make a
transition to another state happen. In the future we want to improve our model
and possibly add a state machine in which a state could be a state machine itself.
Furthermore we want to improve testability of the behaviour software part.

Robot recognition One of the common problems in our ﬁeld is to recognise
the shape of a robot, regardless of the robot type. This has to be done in a very
time and space eﬃcient way. We are testing a new kind of heuristic algorithm
to segment a binary image really fast (O(n)) into a graph structure, and check
objects for their “limbs” in order to classify an object on the ﬁeld as a robot.
This is going to be a bachelor thesis in the future.

4

Sound Source Localisation To check the player’s position is we plan to use
sound source localisation. This is useful at least from the point where the robots
are talking to each other with natural language. Diﬀerent voice types can be
used to identify diﬀerent robots. This would give a major beneﬁt in localising in
a multidimensional way.

3 Prior performance in RoboCup

The Hamburg Bit-Bots team was founded in 2011 as a group of former partici-
pants of the oﬃcial robocup bachelor project participating as RFC St. Ellingen
in the SPL league. The new team was founded with the goal to integrate know-
ledge from diﬀerent ﬁelds of our studies in a more practical approach. It was
explicitly created for the participation in the humanoid league and thus started
from scratch with new robots and a newly developed codebase.

In 2011 we founded our working group and were busy recruiting students and

setting up our robots.

In 2012 we participated at the German Open and were placed third. Further-
more, we took part at the WorldCup in Mexico City and were dropped out in
the second round robin, but successfully ﬁnished the Throw-In Challenge. Apart
from that we joined the Robow 12.1, 12.2 and 12.3 in Berlin to push the inter-
connectedness between the european robocup teams and took part in a research
exchange.

Last year we participated at the German Open and placed second and hostet

a Mini RoBow. At the WorldCup we missed the quarter ﬁnals.

4 Further dedication in RoboCup

Apart from the participation during championships we have many projects to
make robotics and RoboCup accessible to people. For example we participated
in ”Robots on Tour” in Zurich 2013, in the ”Hamburg Night of Knowledge” and
”Berlin Night of Knowledge”.

In cooperation with a school we created a course in robotics for high school

students which was a great success last year.

5 Code from other Teams

Right now all of our codebase is written by members or former members of our
team. Our Walking is heavily inﬂuenced by the Team-Darwin.

6 Statements

6.1 Participate

We assure to participate in the RoboCup 2014 Humanoid League.

5

6.2 Referee

We assure that we have a person with suﬃcient knowledge of the rules. We assure
that this person will be available as referee during the competition.

7 Conclusion

We gained a lot of experience in last two RoboCup seasons and are working
hard to improve our software for the coming years. We managed to improve our
software in many aspects, for example we are now able to walk reliably stable
and have a partly self-adapting vision.

We are looking forward to see how our robots acquit themself on the World-
cup with the new software. We see the Worldcup as an opportunity to exchange
our experiences with other students and researchers from all over the world and
to improve and communicate our knowledge.

We sincerely hope to become part of this great event.

8 Video

http://data.bit-bots.de/application2014.mp4 or
http://youtu.be/umnWFyavx6s

9 Website

http://bit-bots.de

