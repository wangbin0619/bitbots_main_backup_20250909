Application for Robocup 2012 by
Hamburg Bit-Bots

Maike Paetzel, Nils Rokita, Anja Richter, Oliver Bestmann, Marc Bestmann

Department of Informatics, Universit¨at Hamburg Germany
robocup-wettbewerb@informatik.uni-hamburg.de

Abstract. Hamburg Bit-Bots is a highly motivated team especially in-
terested in humanoid robotics. Over the last year we have developed our
own software for the RoboCup tournament and gathered much expe-
rience. Our goal is not only scoring, but to share this knowledge with
like-minded people from all over the world.

Fig. 1. Our Logo

1 The Team

The team Hamburg Bit-Bots consists of a group of students from the department
of informatics at the University of Hamburg, Germany. There are no ties to the
oﬃcial robotics projects at our department as we are a student group.

Roughly 20 undergraduate and graduate students studied and worked in our
group during the last year. Because of that we gathered experience in many
diﬀerent ﬁelds of study. We don’t settle for ﬁnding one way to the aim but
trying to ﬁnd more methods, comparing them and discuss the best one for our
team.

As we start from the very scratch each individual has a thorough understand-
ing of every part of the code. A detailed documentation helps new comers to get
along: http://bitbots.mercarion-online.de/html/index.html

2 Research

2.1 Research until now

We will give a short draft of the published work by some of our group members.
Due to the fact that our team consists only of students, the published work so
far are mostly bachelor thesis.

Estimation of optical-ﬂow ﬁelds in multispectral images (2010) is a ﬁ-
nished bachelor thesis written by Oliver Bestmann in the ﬁeld of cognitive
science. The developed algorithm is able to estimate robustly the optical-
ﬂow in an image sequence using additional information provided by color
gradients. It can be used for better tracking the ball once it is located.
Ball veriﬁcation (2011) The group members Lasse Einig and Anja Richter
wrote an article about the ball veriﬁcation they developed for the object
recognition tool for the NAO robot in the Standard Platform League 2011.

Ball recognition based on probability distribution of shapes (2011)

Sandra Schr¨oder developed a process to determine whether a given shape
would match the soccer ball or not. She uses an elaborate edge detection
algorithm in combination with the probability distribution of the position of
edgels to calculate the possibility of a given shape in the presented image.
Sound source localization on a humanoid robot (2011) This work shows
sound source localization in horizontal plane by using cross correlation and
neural networks. Robert Keßler made a contribution not only to the locali-
sation of service robots but also to the localisation of team members during
robot soccer. This concludes that this thesis is ahead of the times because
it deals with the problem of communication on the ﬁeld without using the
wireless network.

Behaviour based coordination of a multi robot scenario realized by
BDI-agents Group member Anja Richter is currently writing her Bachelor the-
sis on the modelling of a behaviour for a logistic scenario. The behaviour is
realized by software agents according to the believe-intention-desire model
and then transfered to a multi robot system.

Furthermore Timon Giese is writing his bachelor thesis on detection of team
members and adversary.

2.2 Actual ﬁelds of research

As our team consists only of students working in their free time, we are not highly
specialized in certain parts of human robotics. In fact every team member has
his or her own area of expertise which is mostly determined by his interests.
Futhermore some of our team members contribute experience gained in oﬃcial
student projects to the group. This mostly comprises of knowledge in the ﬁeld
of image processing, object recognition and experience in self localization using
particle ﬁlters.

We have students doing research in behavior, image recognition, walking

engine, technical challenges and communication on the ﬁeld by now:

Behavior The team studying the behavior of the robotos are discussing the
cooperation of the robots on the ﬁeld. How can a robot decide whether he
should go to the ball himself or wait for another robot to take the ball.
The simple behavior of just one robot on the ﬁeld is already implementated.
Moreover the behavior of the goalie needs to be changed for the better.
Image recognition In Addition to the bachelor thesis of Sandra Schr¨oder other
team members try to recognise the form of the ball and the goal by the
contrast on the picture.

Walking Engine The robots are already able to walk and turn. However they
need to balance unevenness in the ground solider. We are still working on
the adjusment of the parameters.

Technical Challenge We have some problems with the throw-in challenge at
the moment as our robots are not able to keep the ball above their head.
In contrast dribbling around cylinders is still implementated and we are
engaged in the double-pass challenge.

Communication on the ﬁeld Sound source localisation of other robots dur-
ing the match is just one ﬁeld of study in our team. Comunication via the
network is still more trustworthy. However we are still trying to ﬁnd more
methods of comunication on the ﬁeld due to possible future restrictions in
network communication.

Friendly games with other teams are an important part of our study because
the test conditions with just have of the ﬁeld in our lab are inadequate.

3 Prior performance in RoboCup

The Hamburg Bit-Bots team was founded in 2011 as a reaction to our experience
while participating in the RoboCup German Open 2011, where one third of the
current team take part in the standard platform league.

Cooperation with the former, but still existent team RFC St. Ellingen, is
limited to sharing the laboratory. The current team was explicitly founded for

the participation in the humanoid league and thus started from the beginning
with new robots and a newly developed codebase.

We are using the Darwin OP robots produced by Robotics and Mechanisms
Laboratory. All team members are currently studying computer science and are
working on their bachelor’s or master’s degrees. This explains our lack of expe-
riences in the humanoid league but provides us with referees in the SPL.

Our ﬁrst competition will be the RoboCup German Open 2012 in Magdeburg.
In addition we participate in friendly matches with other team, for example
two of our team members will take part in the RoBOW’12.1 in Berlin in February.

4 Code from other Teams

Right now most of our codebase is written from scratch with the exception
of the image-processing module. We are currently using some code written by
the RFC St. Ellingen, which is used in the standard plattform league. This
code furthermore contains little pieces written by the current world champion
BHuman.

We are activly working on our own image-processing software, because we
are keen to try out other ways of processing the raw data to extract the desired
information we need. We hope to ﬁnish the main work in this area to replace
the borrowed code with our own in time for the RoboCup tournament.

5 Statements

5.1 Participate

We assure to participate in the RoboCup 2012 Humanoid League.

5.2 Referee

We assure that we have a person with suﬃcient knowledge of the rules. We assure
that this person will be available as referee during the competition.

6 Conclusion

Our team is still a beginner in this ﬁeld, but our team members are highly
motivated and interested in robotics. We are looking forward to get in contact
with more people in the RoboCup community.

We see the RoboCup World Championships as an opportunity to exchange
our experiences with other students and researchers from all over the world and
to improve and communicate our knowledge.

We sincerely hope to get the chance to be part of this great event.

