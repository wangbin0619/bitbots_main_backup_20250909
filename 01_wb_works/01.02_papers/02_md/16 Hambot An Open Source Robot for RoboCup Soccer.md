Hambot:
An Open Source Robot for RoboCup Soccer

Marc Bestmann, Bente Reichardt, and Florens Wasserfall

Hamburg Bit-Bots, Fachbereich Informatik, Universit¨at Hamburg,
Vogt-K¨olln-Straße 30, 22527 Hamburg, Germany
{0bestman,9reichar,wasserfall}@informatik.uni-hamburg.de
http://robocup.informatik.uni-hamburg.de

Abstract. In this paper a new robot is presented which was designed
especially for RoboCup soccer. It is an approach to evolve from the stan-
dard Darwin based skeleton towards a robot with more human motion
capabilities. Many new features were added to the robot to adapt it for
the special requirements of RoboCup Soccer. Therefore, the interaction
possibilities with the robot were improved and it has now more degrees of
freedom to easier grip a ball and balance itself while walking. The design
is open source, thus allowing other teams to easily use it and to encour-
age further development. Furthermore, nearly all parts can be produced
with a standard 3D printer.

Keywords: RoboCup; Humanoid; Open Source; Robot; Design; 3D print-
ing; Rapid Prototyping

1

Introduction

Since the release of the Darwin-OP robot [7] in 2010 there was not much devel-
opment of hardware in the humanoid league. Nearly all currently used platforms
use the same structure as the Darwin-OP and are still expensive. Therefore, we
started developing our own robot platform, designed to be cheap, open source
and usable in kid- and teen-size league. The ﬁrst prototype was developed in
2014 and was presented at the RoboCup world championship in Brazil. An im-
proved second prototype was build in early 2015, almost completely from 3D
printed parts. It will be used by us, the Hamburg Bit-Bots, in the 2015 season of
RoboCup tournaments. Throughout this paper we frequently use the Darwin-OP
as reference platform, due to its inﬂuence in the league.

2 Current Problems in the RoboCup Humanoid League

The existing speciﬁcation limits for robots in the Humanoid League are quite
open. However, nearly all teams in the kid- and teen-size league use a Darwin-OP
or a robot with the same skeleton and DOF layout. It contains only the major
joints of a human, e.g shoulder, hip or knee. Some teams made small modiﬁca-
tions to the Darwin, e.g. changing the camera or mainboard. Other teams built

2

Hambot: An Open Source Robot Designed for RoboCup Soccer

a robot on their own, for example CIT Brains [5] and Hanuman KMUTT [13],
but used the Darwin motor layout as well. The only group which did a major
change is the FUmanoids team [12]. They added an additional joint between the
hip and the upper body, similar to the human lumbar spine, and used parallel
kinematics in the robot’s legs. Even the newer platforms Nimbro-OP [11] and
the robot of team Baset [3] use nearly the same layout. Most of the robots in the
competition in 2014 were not especial designed for RoboCup. The battery lay-
out is a good illustration for this problem. Batteries must be changed during the
game due to their limited capacity. Although this is time critical the batteries
are located inside the robot and connected to the electronics by an extra cable.
Further the robot is often diﬃcult to handle during development, because most
interaction is done via a connected laptop and not on the robot itself. Therefore,
the attention of the developer is divided between the laptop and robot.

The existing platforms are quite expensive, approx. 10,000 e [8] for the too
small Darwin-OP and approx. 22,000 e [14] for the newer Nimbro-OP. These
costs make it diﬃcult for a new team to start in the league, because they need
at least 4 robots. Even the existing teams need to buy parts and new robots as
well when the number of players increases, which is planned in the Humanoid
League proposed roadmap [2].

3 Goals of the New Robot

After analyzing the current robots and their limitations, we extracted the fol-
lowing goals for the new robot platform. Achieving these goals should improve
the performance and the usability of the robot during competitions.

Costs Reducing the hardware cost lowers the barrier for new teams and enables
established teams to upgrade their robots. The motors are a major part of
the price, therefore the costs can be reduced by reusing servos which are
currently used. The Dynamixel servos, especially the MX-28 [9], are very
common in the league. For the mechanical parts, simple aluminum sheet
metal and 3D printed plastic parts are low cost alternatives to carbon parts,
used in the Nimbro, which are expensive and harder to obtain.

Interaction The RoboCup competitions usually start with some set-up days
for the teams to prepare their robots. This is required because many algo-
rithms, e.g. walking or vision, need to be adapted for the new environment.
To simplify these tasks, the robot should be equipped with a direct human
robot interface. This includes simple buttons as well as higher level controls
to do recurrent tasks, such as parameter adjustments, without the need of a
laptop. Good debug information is crucial to ﬁnd bugs quickly. In addition
to the wireless network, audio and visual output is desired to simplify this
task. A human understandable voice is very helpful for debugging purposes
and is a step towards robot to robot communication with natural language.

Hambot: An Open Source Robot for RoboCup Soccer

3

Open Source Established platforms like the Darwin or Nimbro are not en-
tirely open source due to the restrictions on third party standard parts (e.g.
CM-730 motor controller board and the Dynamixel servos). This leads to dif-
ﬁculties concerning replacement, repairs and changes in the ﬁrmware. It also
limits development of the hardware. This is one reason why there are so few
modiﬁcations of the Darwin platform. Most of the extensions are limited to
the replacement of cameras, batteries or motor controller boards. Although a
more open platform is clearly desirable, we currently stick with the existing
Dynamixel motors due to the low upgrading cost from the Darwin and the
lack of an adequate alternative. Another diﬃculty is changing the plastic
parts of the Darwin-OP because these are made by injection molding. Thus
the production method has to be simple to enable other teams to produce
their own parts.

Designed for RoboCup Soccer Competition There are no robots available
which are designed exclusively for RoboCup soccer, because the market is
too small for it. Even the NAO robot, which has a league on its own, is
used in RoboCup because it is common in other research ﬁelds. Standard
robots are missing helpful features and have functions which are not needed.
For example a fast battery change as well as a handle to pick up the robot
is required during a RoboCup game but not necessary for many other re-
search activities. Therefore, we wanted to design the robot from scratch for
RoboCup. Features such as fast repair and an anatomy made especially for
soccer playing are major concerns.

Progress in Relation to the Darwin-OP As mentioned in section 2, most
of the currently used robots in humanoid soccer have a very similar body
composition to the Darwin-OP. With more degrees of freedom (DOF) in
the torso of the robot, it is possible to bend the upper body in pitch and
roll direction independently from the legs. This is useful for kicking, walking
stabilization and for standing up. A third DOF in the shoulder would enable
the robot to move the arms more freely. This important for the throw-ins.

4 ”GOAL”

The ﬁrst prototype GOAL was made out of aluminum sheets in 2014. Only three
additional MX-64 [9] and two additional MX-28 motors were used to upgrade
one Darwin to a 87 cm tall robot with 24 DOF. The robot was able to stand
and walk, but was unable to get up, because the motors were not able to lift the
weight of the upper body.
Besides the problem of getting up, we experienced high lead times for the pro-
duction of the sheet metal parts, signiﬁcantly delaying the development. The
production method considerably constrains the design of complex parts, which
are required especially in the torso, where parts have to be connected in all three
dimensions. This particularly aﬀects the cable routing. Changing existing parts

4

Hambot: An Open Source Robot Designed for RoboCup Soccer

Fig. 1: Prototypes of GOAL (left) and Hambot (right). CAD model (center).

later on is complicated due to these constraints and the high production time.
Another problem which is already known from the Darwin-OP is loosening nuts
and screws, resulting in instable part connections.

5 ”Hambot”

The second and current prototype version is designed to be fabricated using 3D
printers. Almost all parts have been designed again from scratch and reﬁned by
several steps of evolution in a rapid prototyping and testing process. Upgrading
from a Darwin only ﬁve MX-106 and four MX-64 are needed. This minimize the
costs of production.

5.1 Body Composition

Feet The capability to control the toes extends the feet by another DOF, po-
tentially improving both walking stability and standing up movements. This
ﬁrst design is simple but it can be replaced by one which is more useful for
high kick. The toes can be bend up to 90◦ (Fig. 2).

Legs The legs are designed in a pipe-like shape. This has advantages compared
to the U-proﬁle composition, which is often used with sheet metals. Cables
are routed directly through these pipes, preventing abrasion of the wires.
Besides, it looks more human and is more comfortable to touch and hold
(Fig. 2).

Hambot: An Open Source Robot for RoboCup Soccer

5

Waist At the waist an additional joint with two DOF has been added at the
waist, which allows the robot to move its upper body independently from the
legs. The joint should be similar to the lumbar spine and the lower thoracic
spine of humans, but only in two directions. This ﬂexibility is necessary for
human walking because the upper body moves and rotates during every step
[6]. By doing so, human walking is very energy eﬃcient [10]. With the roll
axis of the new waist joint this movement is possible. Furthermore it allows
to move the center of mass over the supporting leg during a kick. The pitch
axis improves standing up and picking up the ball. With this joint we can
move the upper body about 45◦ to left and right, 35◦ to the front and 12◦
to the back.

Fig. 2: CAD model of the leg (left) and explosion view of the torso (right).
Note the additional shoulder servos (blue) and the new waist joint (purple).
The two batteries (yellow, only one shown) are inserted from the left and locked
by a bolt (brown) which ﬁts into a bayonet socket. The powerboard (red) and
motor controller board (not shown) are directly plugged into the backbone board
(green) and locked by a side plate (not shown).

Torso The torso consists of a cage-like structure with detachable side plates for
easy access. 3D printing allows the production of complex parts that exactly
ﬁt into each other or are slidable to one side. The electronics consist of the
main computer board (Odroid XU3 lite [4]), the powerboard and a subboard.
The powerboard manages the power sources and the voltage conversions.
The subboard controls the servos and other peripheral electronics, such as
the LEDs and the audio output. These two boards are directly plugged into
a backbone board, which is located at the side of the robot and replaces the

6

Hambot: An Open Source Robot Designed for RoboCup Soccer

Fig. 3: Time for battery change, tested by a group of trained and untrained test
persons. Median time: Darwin 28s, Hambot 13s.

cables, which would normally run through the torso. Therefore, no cables are
necessary inside the torso, which simpliﬁes maintenance. All boards except
the Odroid XU3 lite are open source and developed by ourself. The two
batteries in the robot can be hot swapped. Each has an own printed case
which can be slid into the robot and locked with a bolt, thus enabling a
fast change, approximately 13s for both batteries (Fig. 3). LEDs on the side
are showing the current battery charge levels and which battery is currently
used.

Shoulders The human shoulder is a joint with three DOF, whereas the shoulder
of the Darwin-OP has only two DOF. For many tasks this is suﬃcient,
but not for a good throw-in. An additional motor was added to the robots
shoulder to enable a movement in yaw direction. This third DOF allows the
robot to hold the ball behind his head like a human, while his elbows point
to the sides.

5.2 Interaction

The Hambot has eight free programmable buttons on the back, which are
equipped with LEDs to indicate their state. There is a LCD touch display in
the back for laptop free interaction (sec. 3). A ring of RGB LEDs is embedded
into the front. Every LED can be individually controlled. This is handy to ex-
press the robots current beliefs, e.g. the position of the ball. The audio output
is used for debugging. Therefore, a dedicated text-to-speech chip and a speaker
with a human resonance frequency is installed to ensure good speech quality.

5.3 3D Printing

All parts were designed to be smaller than 20x20x10 cm and therefore printable
with a low cost fused deposition modeling (FDM) consumer printer. The two
most used plastic print materials are acrylonitrile butadiene styrene (ABS) and
polylactic acid (PLA) which can be printed by almost all consumer printers.
While it is possible to build the robot with both materials, ABS is preferred due
to its better strength and heat resistance [1]. The printing direction is important
for the stability of prints. Therefore, all parts are printed in a direction that
maximizes the plane between two layers and improves adhesion. Standard socket
cap screws (ISO 4762 12.9) and nuts (ISO 4032) were used to connect the parts.

Hambot: An Open Source Robot for RoboCup Soccer

7

Screwing directly into the plastic would be possible, but threads in plastic tend to
wear oﬀ very fast. Multiple disassembles due to repairs would destroy the parts.
Therefore, steel nuts were used for tightening. They are inserted into prepared
holes, which clamp them into their position. Thus all screws can be tightened
without a wrench and the parts can be assembled multiple times. The estimated
print time for a complete Hambot is two weeks with a standard FDM printer.
Parallel printing reduces this time.

5.4 Costs

100 e 100 e
Filament
120 e 120 e
Odroid XU3 lite
60 e
60 e
Logitech C910
550 e 550 e
Other electronics
Dynamixel servos 6800 e 3520 e
7630 e 4350 e
Total

The estimated hardware costs for the parts
to build a whole Hambot are listed in
table 1. It is possible to reduce them sig-
niﬁcantly by reusing the parts of the Dar-
win, because only four additional MX-64
and ﬁve MX-106 servo motors are needed.
Therefore, the cost for upgrading a Darwin
reduces to approximately 4350 e. Expenses
for maintaining the 3D printers are not in-
cluded in this calculation. It is possible to
use the electronics from the Darwin to save
more money, but the additional interaction possibilities would not be usable. It
is also possible to reuse some metal connectors of the Darwin, but these can be
replaced by 3D printed parts.

Table 1: Estimated hardware
costs for one Hambot (left) and for
an upgrade from a Darwin (right).

6 Conclusion and Further Work

This work introduces an open source humanoid robot. The costs are signiﬁcantly
lower than buying new robots that are currently available on the market. The
costs for switching from Darwin-like robots with approximately 45 cm height
over to a 87 cm robot are even lower. This becomes even more important, with
increasing robot size and number of players in the next years [2]. Due to its
size, Hambot is currently allowed to play in the Kid- and Teen-size league. The
increased interaction possibilities enable a faster development as well as a better
handling during the game. First tests in real environment were done at the
IranOpen and GermanOpen 2015 and showed that the 3D printed structure is
suﬃciently stable. The size of the motors was increased to enable more stable
getting up and walking. The new version will be used by us, the Hamburg Bit-
Bots, at the world championship in China during July 2015. Next steps include
the development of more human feet and a better camera system.
We encourage other teams to use the projects source code which is available at:
https://github.com/bit-bots

8

Hambot: An Open Source Robot Designed for RoboCup Soccer

Bibliography

[1] Plastic Properties of Acrylonitrile Butadiene Styrene (ABS), 2015. URL

http://www.dynalabcorp.com/technical\_info\_abs.asp.

[2] J. Baltes, M. Missoura, D. Seifert, and S. Sadeghnejad. Robocup soccer

humanoid league. Technical report, 2013.

[3] H. Farazi, M. Hosseini, V. Mohammadi, F. Jafari, D. Rahmati, and D. E.
Bamdad. Baset humanoid team description paper. Technical report, Hu-
manoid Robotic Laboratory, Robotic Center, Baset Pazhuh Tehran coop-
eration. No 383, 2014.
co., Ltd.

speciﬁcation,
2015. URL http://www.hardkernel.com/main/products/prdt_info.
php?g_code=G141351880955.

ODROID-XU3 Lite product

[4] Hardkernel

[5] Y. Hayashibara, H. Minakata, K. Irie, T. Fukuda, V. T. S. Loong,
D. Maekawa, Y. Ito, T. Akiyama, T. Mashiko, K. Izumi, Y. Yamano,
M. Ando, Y. Kato, R. Yamamoto, T. Kida, S. Takemura, Y. Suzuki, N. D.
Yun, S. Miki, Y. Nishizaki, K. Kanemasu, and H. Sakamoto. Cit brains (kid
size leaguge). Technical report, UnChiba Institute of Technology, 2015.
[6] S. Mochon and T. A. McMahon. Ballistic walking. Journal of biomechanics,

13(1):49–57, 1980.

[7] Robotis. Darwin OP Project Information, 2015. URL http://darwinop.

sourceforge.net.

[8] Robotis.

Robotis

international

shop, 2015.

URL http://www.

robotis-shop-en.com/?act=shop_en.goods_list&GC=GD070001.

[9] Robotis. Robotis international shop, 2015. URL http://www.robotis.

com/xe/dynamixel_en.

[10] F. Romeo. A simple model of energy expenditure in human locomotion.

Revista Brasileira de Ensino de F´ısica, 31(4):4306–4310, 2009.

[11] M. Schwarz, M. Schreiber, S. Schueller, M. Missura, and S. Behnke. Nimbro-
op humanoid teensize open platform. In Proceedings of 7th Workshop on Hu-
manoid Soccer Robots. IEEE-RAS International Conference on Humanoid
Robots, 2012.

[12] D. Seifert, L. Freitag, J. Draegert, S. G. Gottlieb, R. Schulte-Sasse,
G. Barth, M. Detlefsen, N. Rugh¨oft, M. Pluhatsch, M. Wichner, and R. Ro-
jas. Berlin united - fumanoids team description paper. Technical report,
Freie Universit¨at Berlin, Institut f¨ur Informatik, 2015.

[13] N.

Suppakun,

S. Wanitchaikit, W.

Sanprueksin,
A. Phummapooti, N. Tirasuntarakul, and T. Maneewarn. Hanuman-
kmutt: Team description paper.
Technical report, King Mongkut’s
University of Technology Thonburi, 2014.

Jutharee, C.

[14] Universit¨at Bonn, Institute for Computer Science. Nimbro Homepage, 2015.

URL http://www.nimbro.net/OP/.

Acknowledgments. Thanks to the RoboCup team Hamburg Bit-Bots. Thanks
for help building this robot to Marcel Hellwig, Dennis Reher and special thanks
to Nils Rokita.

