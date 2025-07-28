Hamburg Bit-Bots Humanoid League 2020

Marc Bestmann, Niklas Fiedler, Jasper G¨uldenstein,
Jan Gutsche, and Jonas Hagge

Hamburg Bit-Bots, Fachbereich Informatik,
Universit¨at Hamburg, Hamburg, Germany

info@bit-bots.de

www.bit-bots.de

Abstract. This extended abstract describes the current research of the
Hamburg Bit-Bots Humanoid KidSize RoboCup team, lessons learned
from last years competition and improvements planned for 2020.

Keywords: RoboCup · Humanoid · Soccer.

1 Lessons Learned from RoboCup 2019

In the RoboCup 2019 competition, we had recently installed new cameras on
the robots with a new 3D printed head. These heads sometimes broke when the
robot fell. We have learned from this to not make major hardware changes close
to a competition, since there is not enough time to test the changes suﬃciently.
Another lesson we have learned from this problem is to test the robustness of
our hardware more rigorously.

A major problem we faced was the integration of the diﬀerent components of
our software stack. Our software was able to solve most problems when tested
in isolation.

For example, our walking algorithm published inaccurate odometry, overesti-
mating the distance the robot walked. This caused our pathﬁnding to change its
plans more often and radically than necessary. Due to the change in plans, the
walking had to change its speed and direction. This again led to a more unstable
walking and oscillation around the planned path.

2 Major Problems to Solve for RoboCup 2020

One major problem we need to solve is instability in motions which comes from
the servos not reaching their goal position using their internal PID controller.
Thereby the motion is not executed as planned and the robot becomes unstable.
We are currently investigating if better tuning of the PID controller solves this
problem or if other measures need to be taken.

We are experiencing a lot of wear on the servo bus cables, which leads to
frequent communication problems on the servo bus resulting in more repair
time. We started working on this problem last year, but it is still not completely
solved, thus requiring more hardware modiﬁcations. Our developments in [1]

2

Hamburg Bit-Bots

which will be implemented for RoboCup 2020 will furthermore allow us to isolate
bus problems to their respective bus (e.g. a fault in the cables in the arm does
not cause problems in the legs of the robot).

3 Planned Development for RoboCup 2020

We plan to use an updated version of our robot platform from last year. We al-
ready ﬁxed the mechanical issues with the head design. We are currently work-
ing on weight loss in the torso and the feet, as well as better cable handling.
Furthermore, we are currently integrating our new servo/sensor control board
QUADDXL [1] to achieve faster control cycles.

We already used ﬂexible 3D printed parts in the shoulder roll motor at the
last RoboCup. We plan to integrate these in the elbow to reduce damage from
falling. Furthermore, we want to include them in the knee joint with an additional
rotary encoder. While we believe that this will not be ready in the RoboCup
2020, we believe it is necessary for the future so that shocks from walking or
even running can be better absorbed.

We do not plan major improvements to the vision system (described in [2])

for RoboCup 2020 since it performs very well.

Last year we used an implementation of AMCL1 for localization with line
information as input. There were multiple problems since it is optimized for
working with LiDAR sensors. Therefore, we implemented a new particle ﬁlter
based localization, which uses all ﬁeld information from the vision (lines, line
features, posts, ﬁeld boundary, visual compass) and also handles information
from the game controller.

Our decision making uses the Dynamic Stack Decider2. We plan on integrat-

ing rule changes and improving robustness.

The problems with the integration of walking and path planning have al-
ready been solved and we plan to implement better handling of obstacles in for
RoboCup 2020.

Our closed-loop implementations for walking and kicking already work well
and we are only planning on small improvements. The getting up motion is
currently reworked as a closed-loop approach, but we also have the working
open-loop solution from last year.

Our software stack is currently based on ROS Melodic. We will not migrate

to ROS 2 before the world championship but plan to do it right afterward.

References

1. Bestmann, M., G¨uldenstein, J., Zhang, J.: High-frequency multi bus servo and sensor

communication using the dynamixel protocol (2019)

2. Fiedler, N., Brandt, H., Gutsche, J., Vahl, F., Hagge, J., Bestmann, M.: An open

source vision pipeline approach for robocup humanoid soccer (2019)

1 http://wiki.ros.org/amcl
2 https://github.com/bit-bots/dynamic stack decider

