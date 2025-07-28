MASTERTHESISReinforcementLearningzumselbstoptimierendenLaufenmitKraftsensorenimRoboCupvorgelegtvonFabianFiedlerMIN-FakultätFachbereichInformatikTAMS-TechnicalAspectsofMultimodalSystemsStudiengang:InformatikMatrikelnummer:6208316Erstgutachter:Prof.Dr.JianweiZhangZweitgutachter:Dr.NormanHendrichAbstract

Humanoid walking has been an active ﬁeld of research for over 50 years.
One of the widespread theories about a stable movement is to control the so
called zero-moment-point (ZMP) inside the support polygon of the stance
leg. However, calculating the exact position of the ZMP is not possible
without deep knowledge about the robot, especially about the actuators,
and the ground. Therefore it is hardly possible to calculate the trajectory,
which achieves a desired position of the ZMP. Current walking algorithms
use an approximation for the controlling, which is not accurate enough. To
compensate for this inaccuracy, manually tuned parameters are added.

Fortunately the current ZMP can be determined by force sensors between
the robot and the ground. This master’s thesis intends to develop and
integrate force sensors for the robots of the Department of Informatics
based RoboCup team and to adapt the information about the ZMP via
reinforcement learning to enhance the walking capabilities of the robots on
non ﬂat grounds such as artiﬁcial turf. This should render the widespread
need for a tedious conﬁguration of the walking algorithm unnecessary.

III

Zusammenfassung

Am Gang von humanoiden Robotern wird seit über 50 Jahren aktiv ge-
forscht. Im Rahmen dieser Forschung ist die Theorie des zero-moment-point
(ZMP) weit verbreitet. Dieser Punkt wird innerhalb des Support Polygons
der Füße gehalten. Allerdings ist die genaue Berechnung ohne tiefergehen-
des Wissen über den Roboter und seine Motoren nicht möglich. Daher ist
im Allgemeinen die Bewegung zum Steuern des ZMP zum gewünschten
Punkt nicht berechenbar. Aktuelle Ansätze des humanoiden Gehens nut-
zen eine ungenaue Annäherung des ZMP für die generierten Bewegungen.
Die Fehler dieser Annäherung werden durch Parameter ausgeglichen, die
aufwendig durch Ausprobieren optimiert werden müssen.

Die Position des ZMP lässt sich allerdings auch durch Kraftsensoren in den
Füßen berechnen. Ziel dieser Masterarbeit ist es, Kraftsensoren für die Füße
zu entwickeln und diese in die Roboter der RoboCup-AG des Fachbereichs
Informatik zu integrieren. Mit diesen Kraftsensoren soll nun der ZMP
bestimmt werden sowie das Laufen der Roboter mittels Reinforcement
Learning und dem gemessenen ZMP verbessert werden. Dadurch soll die
bisher allgegenwärtige aufwendige Konﬁguration des Laufalgorithmus durch
den Nutzer vermieden werden.

IV

Inhaltsverzeichnis

1 Einleitung

1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 RoboCup . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Roboterplattform . . . . . . . . . . . . . . . . . . . . . . .
1.4 Vergleichbare Arbeiten . . . . . . . . . . . . . . . . . . . .

2 Theoretische Grundlagen

2.1 Direkte und inverse Kinematik . . . . . . . . . . . . . . . .
2.2 Menschliches Laufen . . . . . . . . . . . . . . . . . . . . .
2.3 Gang humanoider Roboter . . . . . . . . . . . . . . . . . .
2.4 Stabilität von Robotern . . . . . . . . . . . . . . . . . . .

3 Hardwaregrundlagen

3.1 Motoren . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3D-gedruckte Kraftsensoren . . . . . . . . . . . . . . . . .
3.2

4 Hardwaredesign

3D-Druck-Fuß . . . . . . . . . . . . . . . . . . . . . . . . .
4.1
4.2 Prototyp-Platine
. . . . . . . . . . . . . . . . . . . . . . .
4.3 PCB-Platine . . . . . . . . . . . . . . . . . . . . . . . . . .

5 Software

5.1 Reinforcement Learning . . . . . . . . . . . . . . . . . . .
5.2 Softwarearchitektur . . . . . . . . . . . . . . . . . . . . . .
5.3 Policy Struktur . . . . . . . . . . . . . . . . . . . . . . . .
5.4 Policy Darstellung
. . . . . . . . . . . . . . . . . . . . . .
5.5 Policy Initialisierung . . . . . . . . . . . . . . . . . . . . .

1
1
3
6
8

13
13
14
16
17

25
25
26

31
31
33
34

37
37
42
45
46
48

V

Inhaltsverzeichnis

6 Evaluation

6.1 Sensorgenauigkeit . . . . . . . . . . . . . . . . . . . . . . .
6.2 Hardwareeinschränkungen . . . . . . . . . . . . . . . . . .
6.3 Gelernte Policy . . . . . . . . . . . . . . . . . . . . . . . .
6.4 Portierbarkeit . . . . . . . . . . . . . . . . . . . . . . . . .

7 Zusammenfassung und Ausblick

7.1 Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . .
7.2 Ausblick . . . . . . . . . . . . . . . . . . . . . . . . . . . .

50
50
51
55
66

69
69
70

VI

Abbildungsverzeichnis

1.1
Im Rahmen der Masterarbeit entwickelter Fuß . . . . . . .
. . . . . . . .
1.2 Minibot und Hambot während eines Spieles
1.3 Der Kunstrasen . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Minibot und Hambot . . . . . . . . . . . . . . . . . . . . .
1.5 Das kinematische Modell des Minibot von vorne . . . . . .
1.6 Kinematisches Modell und technische Zeichnungen des Minibot
1.7 Ein passiv-dynamischer Laufroboter . . . . . . . . . . . . .

2.1 Laufmuster eines Menschen . . . . . . . . . . . . . . . . .
2.2 Fuß eines Menschen und Fuß eines Roboters . . . . . . . .
2.3 Visualisierung der Fußbelastung beim Gehen . . . . . . . .
2.4 Zielpositionen des Fußes des Spielbeins . . . . . . . . . . .
2.5 Visualisierung des Support Polygons eines sechsbeinigen
Roboters . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6 Visualisierung des ZMP . . . . . . . . . . . . . . . . . . .
2.7 Visualisierung der auftretenden Kräfte unter einem ﬂachen
Fuß . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.1 Schaltplan des ITR8307 . . . . . . . . . . . . . . . . . . .
3.2 Kalibrierungssetup für den Entfernungsmesser und die ge-
. . . . . . . . . . . . . . . . . . . . . . . .
3.3 OpenSCAD-Rendering eines einfachen Kraftsensors . . . .

messene Kurve

4.1 Erster Prototyp und ein gebrochener Kraftsensor
. . . . .
4.2 Das Fußmodell in OpenSCAD und eine Nahaufnahme des
Kraftsensors . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Zweite Version des Fußes . . . . . . . . . . . . . . . . . . .
4.4 Schaltplan der Prototyp-Platine . . . . . . . . . . . . . . .
4.5 Ausschnitt vom entwickelten Fuß . . . . . . . . . . . . . .
4.6 Neu entwickelte Platine . . . . . . . . . . . . . . . . . . . .

5.1 Einﬂuss des Feedbacksignal ri auf die benachbarten Tiles .
. . . . . . .
5.2 Abstrahiertes Diagramm des Laufalgorithmus

2
4
6
7
8
9
11

14
15
15
16

19
22

23

28

29
30

31

32
32
34
35
36

41
42

VII

Abbildungsverzeichnis

5.3 Laufgenerator mit und ohne Stabilisator
. . . . . . . . . .
5.4 Abstrahiertes Klassendiagramm . . . . . . . . . . . . . . .
Initiale Policy . . . . . . . . . . . . . . . . . . . . . . . . .
5.5
5.6 Minibot beim Austarieren seiner stabilen Position . . . . .

6.1 Minibot beim Balancieren auf einem geneigten Untergrund
6.2 Kraftverteilung und Motorwinkel während des Balancierens
auf einem geneigten Untergrund . . . . . . . . . . . . . . .
6.3 Beispiel des Unterschiedes zwischen Zielwert und dem er-
reichtem Winkel während des Gehens . . . . . . . . . . . .
6.4 Ausschnitt aus einem Versuch, den Oﬀset der Motoren durch
ein übergeordnetes Steuersystem zu beheben . . . . . . . .
6.5 Gelernte Policy mit der Finite Diﬀerence Methode . . . . .
6.6 Gelernte Policy mit TD(λ) . . . . . . . . . . . . . . . . . .
6.7 Gelernte Policy mit TD(λ) und Gauß-Filter
. . . . . . . .
6.8 ZMP des linken Fußes auf der x-Achse . . . . . . . . . . .
6.9 Vergleich der linken und rechten Policy . . . . . . . . . . .
6.10 Ausgeführte Policy über mehrere Schritte . . . . . . . . . .
6.11 Minibot während eines Schrittes . . . . . . . . . . . . . . .
6.12 Ausgeführte Seitwärtstrajektorie . . . . . . . . . . . . . . .
6.13 Entstehende Kräfte während des Gehens . . . . . . . . . .

43
44
47
48

50

51

52

53
55
56
57
60
60
61
62
64
65

VIII

Abkürzungsverzeichnis

CoM Center of Mass
ZMP Zero-Moment-Point
CoP Center of Pressure
IK Inverse Kinematik
TD Temporal Diﬀerence
PID Proportional, Integral und Derivative
ROS Robot Operating System

IX

1 Einleitung

Die Hamburg Bit-Bots ist eine am Fachbereich Informatik der Universität
Hamburg angesiedelte studentische Arbeitsgemeinschaft, die an den Fußball-
Roboter-Weltmeisterschaften des RoboCup teilnimmt. Ein umfangreiches
Forschungsthema innerhalb der Bit-Bots ist das Gehen der Roboter. In der
Einleitung dieser Masterthesis wird erst das Forschungsfeld des Gehens
beschrieben und dann eine Einführung in den RoboCup gegeben. Danach
werden die genutzten Roboter vorgestellt. Abschließend erfolgt eine Analyse
vergleichbarer Arbeiten.

Das zweite Kapitel dieser Thesis erklärt die theoretischen Grundlagen des
Laufalgorithmus, die Bewegungen der Füße werden modelliert und das
Stabilitätskriterium Zero-Moment-Point (ZMP) wird erklärt. Aus dem
ZMP wird der Reward — also das Qualitätsmaß für den Lernalgorithmus —
generiert. In den Kapiteln drei und vier werden sowohl die Grundlagen als
auch die Umsetzung der Hardware dargestellt, um den ZMP präzise messen
zu können. Auf Basis des gemessenen ZMP werden im fünften Kapitel
zuerst die verwendeten Techniken zum Lernen des optimalen Ganges erklärt
und anschließend auf die Modellierung und Umsetzung dieser Techniken
zur eigentlichen Ausführung des Laufens eingegangen. Daran anschließend
wird in Kapitel sechs die entwickelte Software evaluiert und dabei die
Ergebnisse der Versuche mit dem Roboter vorgestellt. Am Ende erfolgt
eine Zusammenfassung der Ergebnisse und ein Ausblick.

1.1 Motivation

Das Laufen von Robotern mit Beinen ist seit langem ein aktives For-
schungsfeld. Trotzdem ist stabiles schnelles Laufen bisher selten erreicht
und immer stark auf die jeweilige Plattform ausgelegt. Obwohl mit dem
Zero-Moment-Point (ZMP) seit 1972 [Juricic and Vukobratovic, 1972] eine
mathematische Modellierung für die Stabilität von Bewegungsabläufen

1

1 Einleitung

Abbildung 1.1: Im Rahmen der Masterarbeit entwickelter Fuß. In den
Ecken sind in weiß die Spitzen der Kraftsensoren sichtbar, welche die
beim Laufen entstehenden Kräfte messen. Oben sind Teile der Pitch-
und Rollmotoren des Sprunggelenkes sichtbar. Rechts zwischen Fuß
und Rollmotor beﬁndet sich die entwickelte Prototyp-Platine, die die
Sensoren ausliest.

besteht, ist die Entwicklung stabiler Laufalgorithmen auf Basis des ZMP bis
heute schwierig. Um den ZMP während eines Bewegungsablaufes berechnen
zu können, wird fundiertes Wissen über alle auftretenden Kräfte benötigt.
Insbesondere der Einﬂuss der Aktoren auf den ZMP ist kaum abzuschätzen,
da ihre Performance stark von ihrer Temperatur und weiteren Faktoren
abhängig ist.

Der klassische Ansatz, diese Unkenntnis über die tatsächlich auftretenden
Kräfte auszugleichen, ist das Einfügen von Parametern. Diese werden solan-
ge per Hand modiﬁziert, bis sich der Roboter stabil fortbewegt. Allerdings
sind diese Parameter in der Regel nicht mathematisch herleitbar und ohne
genaue Kenntnis des Algorithmus nicht anpassbar. Dieser Ansatz wird
häuﬁg in den Weltmeisterschaften des Roboterfußballturniers RoboCup
angewendet. Ein Beispiel hierfür ist der Laufalgorithmus des Team DAR-
wIn [Team-Darwin, 2017, Song, 2010], der von etlichen anderen Teams
übernommen wurde. Ein anderes Beispiel ist der Laufalgorithmus des
Teams NimbRo [Team Nimbro, 2009, Missura, 2005], der im Rahmen einer
Promotion entwickelt wurde. Dieser Algorithmus umfasst 77 Parameter,

2

1 Einleitung

die stark auf eine spezielle Roboterplattform optimiert sind. Selbst der
Autor des Algorithmus hatte es in den Weltmeisterschaften 2014 – 2016
nicht geschaﬀt, dass der Algorithmus ebenso gute Ergebnisse mit der neu
entwickelten Plattform erreicht.

Kraftsensoren bieten die Möglichkeit, die aktuelle Stabilität eines Roboters
aktiv zu messen und dabei auf der realen Hardware zu bleiben. Es entsteht
also keine Abstraktion durch den Einsatz von Simulatoren, die dazu füh-
ren, dass der Algorithmus in der Realität deutlich schlechtere Ergebnisse
erzielt. Allerdings wird Hardware bei falscher Nutzung schnell beschädigt.
Deshalb müssen Algorithmen, die mit Kraftsensoren arbeiten, den Roboter
entsprechend vorsichtig steuern. Ferner sollten die Roboter auch mit dem
Ausfall eines oder mehrerer Sensoren umgehen können.

Ziel dieser Masterarbeit ist es, einen Laufalgorithmus zu entwickeln, der die
Stärken einer inversen Kinematik nutzt und auf dieser aufbauend selbst-
ständig einen stabilen Gang lernt. Dabei soll der Algorithmus möglichst
viel aus den Kraftsensoren im Fuß (siehe Abbildung 1.1) lernen und wenig
auf Konﬁguration oder Vorinitialisierung durch den Nutzer angewiesen
sein. Dies soll insbesondere auch die Portierbarkeit des Ansatzes auf an-
dere Plattformen gewährleisten und es soll nicht mehr notwendig sein,
bei Änderungen an der Hardware weite Teile des Laufalgorithmus neu zu
konﬁgurieren. Der Algorithmus soll trotzdem robust gegenüber beschä-
digten Sensoren bleiben, da diese z.B. während der Meisterschaften im
RoboCup nicht immer direkt ausgetauscht werden können. Gleichzeitig
soll die Möglichkeit gewährleistet bleiben, aufbauende Algorithmen zur
Stabilisation anzuwenden.

1.2 RoboCup

Der RoboCup ist eine internationale Forschungsinitiative, die 1993 in
Japan gegründet wurde und die 1995 das erste Mal einen internationalen
Wettkampf in Montreal (Kanada) veranstaltet hat [RoboCup Federation,
2017]. Seitdem gibt es jährliche Weltmeisterschaften in verschiedenen Ligen
und Ländern. Während es ursprünglich nur wenige Ligen gab, darunter
Simulationsligen und eine Fußballliga auf kleinen, fahrenden Robotern, hat
sich heutzutage ein breites Spektrum an Ligen entwickelt.

3

1 Einleitung

Neben den Ligen mit fahrenden Robotern, die heutzutage in der Middle-
Size-Liga bereits sehr dynamische Spiele spielen, gibt es die Ligen mit
humanoiden Robotern: Zum einen die Standard-Plattform-Liga, in der alle
Teams mit Robotern des Typ Nao von Aldeberan Robotics spielen. In
dieser Liga führt eine starke Fokussierung auf diesen Robotertyp ebenfalls
zu Spielen, in denen die Strategie der Roboter spielentscheidend ist. Die
Humanoid-Liga ist hingegen stark auf die Entwicklung der Hardware fokus-
siert. Hier treten die meisten Teams mit selbst entwickelten Robotern an,
was den Codeaustausch erschwert, da der Code ausschließlich für die eigene
Plattform entwickelt wird. Aber auch hier wird ein größerer Austausch
gefördert: Zum Beispiel wird zurzeit unter der Leitung der Bit-Bots eine
Standardisierung eines Software-Stacks für die Humanoid RoboCup-Ligen
unterstützt [Bestmann, 2016]. Da der Fokus der Liga auf der Hardware
liegt, sind insbesondere in dieser Liga die beiden Grundfähigkeiten Laufen
und Bildverarbeitung spielentscheidend.

Abbildung 1.2: Links: Minibot (Mitte) beim Versuch über den Rasen zu
laufen, was ein trippelndes, instabiles Schlittern ist. Rechts: Hambot
(hinten) unbeweglich im Tor, da bisher kein funktionierender Laufalgo-
rithmus existiert.

Neben den Fußballligen haben sich im RoboCup insgesamt zehn weitere
Ligen herausgebildet. Beispiele für diese Ligen sind die Rescue-Liga, bei der
Roboter entwickelt und programmiert werden, die in schwer zugänglichen
Gebieten im Katastrophenfall die Rettungskräfte unterstützen sollen, sowie
die Robocup@Home-Liga, deren Roboter als Serviceroboter im Haushalt
helfen sollen.

Die Humanoid-Liga besteht aus drei Teilligen, die im Folgenden der Größe
der teilnehmenden Roboter nach sortiert aufgelistet sind. Die Liga mit den
größten Robotern ist die Adult-Size-Liga, deren Roboter mindestens 130 cm

4

1 Einleitung

groß sein müssen. Hier wurde bisher eins gegen eins in einem modiﬁzierten
Elfmeterschießen gespielt, bei dem der Ball hinter dem Roboter lag und
dieser erst einmal hinter den Ball gehen musste, um ihn dann schießen zu
können. Da die Regeln der Subligen aneinander angepasst werden, wird 2017
mit den Robotern erstmals ein reguläres Spiel „eins gegen eins“ gespielt,
wobei die Besonderheit bleibt, dass ein sogenannter Robot-Handler hinter
dem Roboter stehen darf, um ihn im Notfall aufzufangen, da diese Roboter
ansonsten stark beschädigt werden könnten. Die Roboter der Teen-Size-Liga
sind kleiner und dürfen zwischen 80 cm und 140 cm groß sein – hier wird
„zwei gegen zwei“ gespielt. Die Roboter der Kid-Size-Liga sind die kleinsten
mit 40 bis 90 cm und spielen „vier gegen vier“. Die Roboter der Hamburg
Bit-Bots während eines Spieles der Kid-Size-Liga sind in Abbildung 1.2 zu
sehen. Gerade in der Kid-Size-Liga müssen die Roboter Stürze aushalten
und nach einem Sturz selbstständig aufstehen können. Da die Roboter
entwickelt werden, um Stürze auszuhalten, ist die Anforderung an den
Laufalgorithmus, niemals das Gleichgewicht zu verlieren, nicht zwingend
erforderlich.

Neben der Größe gibt es noch andere Anforderungen an die Roboter, wobei
die Regeln dem Grundsatz folgen, dass der Roboter möglichst menschen-
ähnlich sein soll. Er darf also nur menschliche Sensorik, wie zum Beispiel
(Stereo-)Kameras, Kraftsensoren, Gyroskope oder Accelerometer haben.
Sensorik wie Magnetometer, Lasersensoren oder andere Tiefensensoren sind
dagegen nicht erlaubt.

Auch die Länge der Arme ist auf die 1.2-fache Körperhöhe beschränkt.
Für humanoides Gehen relevant ist insbesondere auch die Größe der Füße,
deren Fläche (2,2·Hcom)2/32 nicht überschreiten darf, wobei Hcom die Höhe
des Schwerpunktes des mit durchgestreckten Knien stehenden Roboters
ist. Auch darf der Fuß nicht mehr als 2.5-mal so lang wie breit sein. Ferner
muss der Roboter sich menschlich fortbewegen; Krabbeln oder Räder sind
nicht erlaubt.

Seit 2015 wird in der Humanoid-Liga auf Kunstrasen gespielt, was insbe-
sondere kleinere Roboter vor eine große Herausforderung stellt, da sie nicht
schwer genug sind, den sehr nachgiebigen Rasen genug zu komprimieren,
um eine glatte und gerade Fläche unter sich zu haben. Sie kippen daher
schon beim Stehen leicht nach vorn oder hinten um. Ein großes Hindernis
beim Laufen ist auch die in Abbildung 1.3 sichtbare Ausrichtung der Rasen-
halme, die sehr prägnant ist. Während ein Roboter mit der Halmrichtung
über das Feld rutschen könnte, ist dies gegen die Halmrichtung unmöglich.

5

1 Einleitung

Abbildung 1.3: Der Kunstrasen, der auch bei den German Open ver-
wendet wird. Der sichtbare Farbunterschied zwischen links und rechts
ist kein Unterschied im Teppich, sondern ausschließlich seine unter-
schiedliche Halmrichtung. Der Unterschied als Laufunterlage ist ähnlich
prägnant wie die Farbunterschiede. Problematisch zum Laufen sind
auch die häuﬁg existierenden Falten, sichtbar als dunkle waagerechte
Streifen im hellen Teil.

1.3 Roboterplattform

Im Rahmen der Hamburg Bit-Bots wurden zwei Roboterplattformen ent-
wickelt, auf denen der in dieser Arbeit vorgestellte Laufalgorithmus ange-
wendet werden soll. Beide Roboter nutzen die Aktuatoren der MX-Reihe
von Robotis (siehe Abschnitt 3.1).

1.3.1 Minibot

Minibot (siehe Abbildung 1.4 links) hat 20 Freiheitsgrade und ist an das
Design des DarWIN-OP von Robotis angelehnt [Ha et al., 2013]. Der
Roboter hat sechs Motoren pro Bein, welche die Bewegungsfreiheit des
Roboters ermöglichen. Je drei Motoren pro Hüfte sind eine Annäherung an
ein Kugelgelenk. Diese stellen jeweils eine der drei Euler-Winkel dar, also
Pitch, Yaw und Roll. Hinzu kommen ein Motor pro Knie und je ein Pitch-
und Rollmotor in den Fußgelenken. Diese Struktur ist in Abbildung 1.5
und Abbildung 1.6 zu sehen und ermöglicht, dass der Roboter fast jede
menschliche Position ansteuern kann. Verbunden sind die Motoren über
ein Skelett aus Aluminium, das zusammen mit den Motoren den Hauptteil
des Gewichts von ca. 5 kg ausmachen. Minibot wurde entwickelt, weil die

6

1 Einleitung

Abbildung 1.4: Minibot (links) und Hambot (rechts), die beiden primären

Plattformen für die entwickelten Algorithmen.

vorher genutzten Darwin-OPs auf dem neuen Kunstrasen kaum noch stehen
können, da sie zu leicht sind. Minibot ist schwerer und mit etwa 70 cm
deutlich größer. Außerdem hat er stärkere Motoren, was die Bewegungen
stabiler macht.

1.3.2 Hambot

Hambot [Bestmann et al., 2015] (siehe Abbildung 1.4 rechts) ist die Ent-
wicklungsplattform der Hamburg Bit-Bots. Dieser ist komplett 3D-gedruckt
und mit 87 cm und ca. 5,5 kg größer und etwas schwerer als Minibot. Da
die komplette Elektronik für Hambot neu entwickelt wird, ist er bis heute
in einem experimentellen Zustand, sodass Minibot die Hauptplattform ist.
Beim Design der Algorithmen in dieser Arbeit wurde Hambot aber immer
mitberücksichtigt.

Größter Unterschied zum Minibot sind neben den Zehen die zwei Freiheits-
grade in der Hüfte: Hambot kann seinen Oberkörper nach vorne und zur
Seite neigen. Er hat damit eine Art Lendenwirbelsäule, die mehr Flexibilität
liefert. Allerdings wird der Roboter durch das Spiel der weiteren Motoren
instabiler (siehe Abschnitt 3.1).

7

1 Einleitung

Abbildung 1.5: Das kinematische Modell des Minibot von vorne. Die
Drehrichtungen der Motoren werden durch die blauen Achsen visua-
lisiert. In der Hüfte und im Fuß liegen die Pitch und Roll Motoren
direkt hintereinander. Deshalb überschneiden sich einige der Achsen
der Koordinatensysteme.

1.4 Vergleichbare Arbeiten

Der klassische Ansatz laufender Roboter ist das Modellieren und Abschätzen
der im Roboter auftretenden Kräfte.

Im RoboCup sind insbesondere Arbeiten von Seungmoon Song
[Song et al., 2011, Song, 2010] relevant. In diesen beschreibt er das Design
des Team-DARwIn Laufalgorithmus, der nicht nur ein de-facto-Standard
für die RoboCup Humanoid-Kid-Size-Liga ist, sondern auch einen Aus-
gangspunkt für diese Masterthesis darstellt. Die zentrale Stelle des Laufal-
gorithmus ist die Deﬁnition des „Body swing“. Über diesen versucht Song

8

1 Einleitung

Abbildung 1.6: Das kinematische Modell des Minibot von der Seite
(links). Die Drehrichtungen der Motoren werden durch die blauen
Achsen visualisiert. In der Mitte ist eine technische Zeichnung des
gesamten Roboters von der Seite dargestellt. Rechts ist eine technische
Zeichnung eines Beines abgebildet, die eine Beispielkonﬁguration zum
Anheben des Beines mithilfe der Freiheitsgerade der Pitch-Motoren
zeigt.

die optimale Bewegung des Oberkörpers herzuleiten. Sein Ergebnis ist, dass
die optimale Bewegung entlang der x- bzw. Vorwärtsachse des Roboters
gemäß folgender Formel erfolgt:

x(t) =x0 · cosh

(cid:18)(cid:114) g

zCoM

(cid:19)

· t

+

(cid:26)

xT − x0 · cosh

(cid:18) g

zCoM

(cid:19)(cid:27)

sinh

· T

·

(cid:16)(cid:113) g

zCoM

(cid:17)

· t

(1.1)

sinh

(cid:16)(cid:113) g

zCoM ] · T

(cid:17)

9

1 Einleitung

In dieser Formel ist t der aktuelle Zeitpunkt, T der Endzeitpunkt des
Schrittes, x0 die Startposition, xT die Endposition, g die Gravitation und
zCoM die z-Position des Schwerpunktes. Allerdings kommt Song zu dem
Ergebnis, dass diese Formel auf echten Robotern nicht funktioniert und
fügt deswegen einen nicht hergeleiteten Parameter tZM P ein [Song, 2010].

x(t) =x0 · cosh

(cid:18)(cid:114) g

zCoM

·

t
tZM P

(cid:19)

+

(cid:26)

xT − x0 · cosh

(cid:18) g

zCoM

·

T
tZM P

(cid:19)(cid:27)

sinh

·

sinh

(cid:16)(cid:113) g

zCoM

(cid:16)(cid:113) g

zCoM

(cid:17)

(cid:17)

·

·

t
tZM P

T
tZM P

(1.2)

Dieser Parameter tZM P muss manuell durch Ausprobieren auf der Robo-
terplattform optimiert werden. Da sich der Parameter aber nicht konstant
über alle Geschwindigkeiten und Beschleunigungen verhält, müssen weitere
Oﬀsets hinzugefügt werden, sodass es am Ende 20 Konﬁgurationswerte für
den Oberkörper gibt, von denen die meisten nicht herleitbar sind, sondern
aufwendig manuell optimiert werden müssen.

Ein anderer im RoboCup verbreiteter Algorithmus ist der des Team-
NimbRo, der im Rahmen der Doktorarbeit von Marcell Missoura bei Prof.
Dr. Behnke an der Universität Bonn entstanden ist [Missura, 2005]. Dieser
Laufalgorithmus hat zwei Komponenten: Zum einen die Berechnung der
Grundbewegung und zum anderen einen darauf aufbauenden Stabilisator,
der auf den sogenannten Capture-Points basiert. Die Capture-Points haben
eine einfach nachvollziehbare physikalische Deﬁnition als Stabilisator. Die
Berechnung der Grundbewegung bleibt allerdings zentraler Bestandteil der
Stabilität und ist noch mehr per Hand optimiert als das Team-DARwIn-
Walking. So hat der ganze Laufalgorithmus insgesamt 140 Konﬁgurations-
werte, von denen die meisten auf die Grundbewegung fallen. Es hat sich
gezeigt, dass es nicht reicht, einen groben Laufalgorithmus zu entwickeln
und die eigentliche Stabilität von den Capture-Steps gewährleisten zu
lassen [Schmidt, 2015].

Der humanoide Roboter iCub ist eine von der EU geförderte Roboterplat-
form, die mittlerweile an vielen Universitäten verbreitet ist. iCub ist einem
dreieinhalbjährigen Kind nachempfunden und kann oﬃziell nur krabbeln
[Metta et al., 2008]. Allerdings wurden Laufalgorithmen auch auf dem
iCub ausprobiert. Ein funktionierender, ebenfalls stark manuell optimierter

10

1 Einleitung

Abbildung 1.7: Ein einfacher passiv-dynamischer Laufroboter mit 4 Mo-
toren: 2 in der Hüfte und 2 im Knie [Morimoto et al., 2005]. Da der
Roboter nur Pitch-Motoren hat, kann er nur nach vorne gehen.

Ansatz ist der von Hu et al. [Hu et al., 2016]. Dieser erreicht allerdings
nur eine Geschwindigkeit von 0,037 m/s, was im Kontext des Robocup
vergleichsweise langsam ist.

Eine weitere verbreitete Strategie ist, das Laufen von zweibeinigen Robotern
mithilfe von Reinforcement Learning zu optimieren. Hierbei ist insbesondere
der Ansatz von Morimoto et al. [Morimoto et al., 2005] interessant, die
mithilfe von einer Poincaré-Map eine Abbildung entwickelt haben, in der
man einen zweckmäßigen Suchraum aufspannen kann. Dieser Suchraum
kann nun exploriert werden, ohne dass der Roboter schnell in instabile
Situationen kommt. Nach einem anfänglichen Lernen im Simulator kann
der Roboter erfolgreich sein Laufen auf der echten Hardware verbessern.
Diese Roboter haben allerdings eine eingeschränkte, nicht menschliche
Bewegungsfreiheit, die häuﬁg auf die Vorwärtsachse beschränkt ist. Sie
fallen nicht so leicht um und sind daher einfacher zu optimieren. Auch in
der Doktorarbeit von Tedrake [Tedrake, 2004] ﬁndet sich diese Art von
Robotern. Allerdings ist bei keinem dieser Ansätze sichtbar, wie man sie
auf komplexere Roboter ausweiten kann, ohne einen zu großen Suchraum
zu erreichen.

Im Rahmen des RoboCups wurde vom Team-EROS ein neuartiger Ansatz
[Saputra et al., 2015] vorgeschlagen, der vollständig auf künstlichen neu-
ronalen Netzen basiert. Aber auch dieser wurde noch nicht öﬀentlich auf
Hardware getestet, weshalb seine Performance schwer abschätzbar ist.

11

1 Einleitung

Der Ansatz der aktuellen Robocup-Humanoid-Kidsize-Weltmeister ist ein
sehr einfacher Open-Loop-Spline-basierter Ansatz, der sehr einfach auf die
Zielplattform konﬁgurierbar ist und dessen Ungenauigkeiten sich durch
einen Stabilisator, der Kraftsensoren nutzt, ausgleichen lässt [Rhoban,
2009]. Während Stabilisatoren auf Basis von Kraftsensoren verbreitet
sind, gibt es keine Veröﬀentlichungen über Lernverfahren des eigentlichen
Laufalgorithmus mithilfe von Kraftsensoren auf humanoiden Robotern.

12

2 Theoretische Grundlagen

In diesem Kapitel werden die wichtigsten mathematischen Begriﬀe erläu-
tert. Zuerst wird auf die direkte und inverse Kinematik eingegangen, die
das Verhältnis von Position eines Endeﬀektors im Raum zu den Gelenk-
winkeln berechnen. Wie der Gang humanoider Roboter speziﬁziert werden
kann, wird im Anschluss erläutert. Danach wird dargestellt, unter welchen
Bedingungen ein Roboter in seiner Bewegung stabil ist.

2.1 Direkte und inverse Kinematik

Die direkte Kinematik berechnet aus Gelenkwinkeln eine Position des End-
eﬀektors im Raum. Nach einer anfänglichen Speziﬁkation der Entfernungen
und Rotationen der einzelnen Gelenke zueinander, lässt sich die Position der
Endeﬀektoren durch einfache Matrix-Multiplikation darstellen [Siciliano
et al., 2008].

Die inverse Kinematik (IK) hingegen berechnet aus einer gegebenen Po-
sition des Endeﬀektors im Raum die dazugehörigen Gelenkwinkel. Diese
Berechnung ist mathematisch deutlich komplexer. Im Allgemeinen gibt
es zwei Ansätze zum Lösen der inversen Kinematik. Zum einen kann ein
analytischer Ansatz gewählt werden, dieser muss aber speziell für jeden
Robotertyp einzeln programmiert und optimiert werden. Analytische IK-
Solver haben zusätzlich die Eigenschaft, dass für eine gegebene Position
des Endeﬀektors die Gelenkwinkel immer gleich sind. Zum anderen kann
ein numerischer Näherungsalgorithmus genutzt werden. Dieser kann auf
beliebigen Robotertypen arbeiten, braucht aber deutlich mehr Rechenzeit
und ist im Allgemeinen ungenauer als die analytischen Algorithmen.

Im Rahmen dieser Masterarbeit wurde ein analytischer IK-Solver des
RoboCup-Teams NUbots von der Universität von Newcastle in Australien
genutzt [NuBots, 2017].

13

2 Theoretische Grundlagen

2.2 Menschliches Laufen

Ziel der Robotik im Rahmen des RoboCups ist es Roboter zu entwickeln,
welche dem menschlichen Vorbild möglichst ähnlich sind. Daher ist die ki-
netische Struktur dem Menschen nachempfunden und es ist wünschenswert
auch den menschlichen Gang zu erreichen.

Ein medizinisches Modell der Laufabfolge eines Menschen ist in Abbildung
2.1 zu sehen. Die grundsätzliche Unterteilung von belasteter und unbe-
lasteter Phase ist auch für ein humanoides Gehen auf Robotern sinnvoll.
Allerdings überschneiden sich die beiden doppelt belasteten Phasen im
medizinischen Modell und sind damit Teile beider Belastungsphasen. Um
eine Partitionierung und gleichmäßige Aufteilung zu ermöglichen, ist es
daher für die Modellierung des Laufalgorithmus ratsam, die doppelt belas-
teten Phasen nochmals aufzuteilen. Die doppelt belastete Phase hat dann
ein Standbein, das die Hauptlast trägt und ein Spielbein, das weniger oder
keine Last des Roboters trägt.

Abbildung 2.1: Das Laufmuster eines Jugendlichen [Vaughan and Bri-
an Davis, 1999]. Die Bezeichnungen der belasteten (stance) und der
unbelasteten (swing) Phase beziehen sich auf das rechte Bein. Im me-
dizinischen Modell überschneiden sich die doppelt belasteten (double
support) Phasen der beiden Beine.

Mit der gegebenen Hardware nicht hinreichend abbildbar ist allerdings
die Abrollbewegung des menschlichen Ganges. In Abbildung 2.2 ist links
ein menschlicher Fuß zu sehen und rechts der Fuß von Minibot. Es ist
auﬀällig, dass der menschliche Fuß deutlich komplexer als der des Roboters

14

InitialLoadingMidTerminalPreswingInitialMidswingTerminalcontactresponsestancestanceswingswingStance phaseSwing phaseFirst doublesupportSecond doublesupportSingle limb stance2 Theoretische Grundlagen

ist. Insbesondere die Muskeln und Knochen in Mittelfuß und Zehen sind
beim Roboter nicht vorhanden, genaueres zum Design des Fußes ﬁndet
sich in Abschnitt 4.1. Während die Zehen noch in den Fuß integriert
werden können [Bestmann et al., 2015], ist der Platz für Hardware zum
aktiven Steuern des Mittelfußes nicht ausreichend. Dieser aktive Mittelfuß
ist allerdings für das menschliche Gehen notwendig, wie in Abbildung 2.3
zu sehen ist. Im Teilschritt b ist der Fußaußenrand noch nicht belastet, in
Teilschritt c aber vollständig. Diese Druckveränderung kann nur zustande
kommen, wenn der Mensch beim Gehen die Haltung des Mittelfußes ändert.
Dies führt dazu, dass ein Roboter keine menschenähnliche Abrollbewegung
machen kann.

Abbildung 2.2: Fuß eines Menschen (links) [Swierzewski, 2017] und Fuß
eines Roboters (rechts). Während der Roboterfuß aufgrund der beiden
Motoren nur über zwei Freiheitsgrade verfügt, besteht der menschliche
Fuß neben den Knochen aus vielen Sehnen und Muskeln, die zu vielen
Freiheitsgraden führen.

Abbildung 2.3: Visualisierung der Fußbelastung beim Gehen. Oben ist
die Fußposition und darunter die dazugehörige Druckverteilung zu
sehen [Debrunner, 2002].

15

2 Theoretische Grundlagen

2.3 Gang humanoider Roboter

Das generelle Ziel der Laufalgorithmen ist es, sich möglichst nahe an
das menschliche Gehen anzunähern (vgl. Abschnitt 2.2). Mithilfe einer
inversen Kinematik lassen sich für den Gang relevante Bewegungen der
Beine mithilfe der Zielpositionen von Oberkörper, rechtem Fuß und linkem
Fuß beschreiben. Da Roboter beim Gehen ihre Füße nicht abrollen können,
wird häuﬁg modelliert, dass die Fußsohle immer parallel zum Boden bleibt.
Dadurch wird die Berechnung des Gehens deutlich vereinfacht, da so für
den unbelasteten Fuß die Zielposition durch Höhe und Vorwärtsbewegung
bzw. Seitwärtsbewegung modellierbar ist.

Um den Bewegungsablauf optimal zu gestalten, muss die Eigenschaft
der Motoren beachtet werden, dass sie nicht die Position direkt sondern
den Antriebsstrom steuern. Der Antriebsstrom korreliert stark mit dem
Drehmoment des Motors. Deswegen sollten weder die Position noch die
Geschwindigkeit Sprünge in ihren Werten haben, d.h. die Positionsfunktion
sollte zweimal diﬀerenzierbar sein.

Abbildung 2.4: Zielpositionen des Fußes des Spielbeins. Während das
Spielbein den Boden berührt, die Höhe also null ist, beﬁndet sich der
Roboter in einer der doppelt belasteten Phasen. Der Roboter bewegt in
diesen seinen Oberkörper, um das Standbein und Spielbein zu wechseln.
Wenn das Spielbein angehoben wird, liegt die Last vollständig auf dem
Standbein. Das nun unbelastete Bein kann nach vorne bewegt werden.

16

2 Theoretische Grundlagen

Die Sinusfunktion ist beliebig oft diﬀerenzierbar und leicht konﬁgurierbar,
daher eignet sie sich gut als Positionssignal. Für die Vorwärts- bzw. Seit-
wärtsbewegung eignet sich die Funktion: sin(x) + 1 für x ∈ [0,π). Die Höhe
hingegen lässt sich durch sin(x) + 1 für x ∈ [0,2π) darstellen. Diese beiden
Funktionen ergeben die in Abbildung 2.4 dargestellten Bewegungen.

Bewegt der Roboter nur den unbelasteten Fuß, fällt er um, da diese Bewe-
gung nicht stabil ist. Es muss also auch der Oberkörper bzw. der Schwer-
punkt des Roboters bewegt werden, um eine stabile Bewegung zu erreichen,
die dazu führt, dass der Roboter nicht umkippt. Da aus der Beobachter-
sicht der belastete Fuß sich nicht bewegt, sollte sich auch die modellierte
Position des belasteten Fußes nicht ändern. Die Ausgleichsbewegung sollte
also ausschließlich durch die Position des Oberkörpers gesteuert werden.
Das Laufen der Roboter kann daher als Tripel (Position des Oberkörpers,
Position des linken Fußes, Position des rechten Fußes) aufgefasst werden,
von denen die Positionen der beiden Füße leicht deﬁnierbar sind. Die Steue-
rung des Oberkörpers soll die Stabilität des Systems gewährleisten. Dies
wird in den nächsten Kapiteln beschrieben. Der Mensch hat dabei seinen
Oberkörper und insbesondere auch den Kopf immer aufrecht, was auch im
RoboCup eine wichtige Anforderung ist, damit das Sichtfeld des Roboters
nicht eingeschränkt wird.

Die Schrittfrequenz des Roboters ist nach Song [Song, 2010] optimal, wenn
sie mit der Eigenfrequenz des virtuellen Pendels vom CoM zum Boden
korreliert. Mit zCoM als Höhe des CoM und g der Gravitationskonstante
ist die Frequenz des Ganges fGang mit dem wählbaren Faktor a:

fGang = a ·

(cid:114) g

zCoM

(cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:26)

a ∈

n ∪

1
n

(cid:27)

| n ∈ N

(2.1)

Da die Schrittfrequenz nicht beliebig sein kann, sollte die Geschwindigkeit
des Gehens hauptsächlich mit der Schrittweite gesteuert werden.

2.4 Stabilität von Robotern

Damit der Roboter möglichst stabil laufen kann, ist es notwendig herauszu-
ﬁnden, wie stabil der Roboter gerade ist. Hierfür wird der relevante Begriﬀ
der konvexen Hülle kurz erläutert und anschließend mit dem Center-of-
Mass (CoM) das Stabilitätskriterium für ein System ohne Kräfte erklärt.

17

2 Theoretische Grundlagen

Dieses wird dann mit dem Zero-Moment-Point (ZMP) auf den dynamischen
Fall erweitert, um abschließend mit dem messbaren Center-of-Pressure in
Bezug gesetzt zu werden.

2.4.1 Konvexe Hülle

Für die formale Deﬁnition der Stabilität von Robotern ist der Begriﬀ der
konvexen Hülle relevant. Eine Menge M von Punkten (z.B. Berührungs-
punkte des Roboters mit dem Boden) ist konvex, wenn auch stets alle
Punkte auf der Verbindungsstrecke von je zwei Punkten zu dieser Menge
M gehören [Lau, 2004]. Die konvexe Hülle ist dann die kleinste konvexe
Menge M um alle Punkte der Menge M :

M :=

(cid:26)
X ∈ Rn×1 (cid:12)
(cid:12) ∃t ∈ N ∃λ1, . . . ,λt ∈ R ∃X1, . . . ,Xt ∈ M :
(cid:12)

(∀i : 0 ≤ λi ≤ 1) ∧

t
(cid:88)

i=1

λi=1 ∧ X =

(cid:27)

λi · Xi

t
(cid:88)

t=1

(2.2)

2.4.2 Schwerpunkt

Wenn mit Ausnahme der Gravitation keine Kräfte auf ein Objekt wirken, so
ist der Schwerpunkt (CoM – vom englischen Center of Mass) die kritische
Kenngröße. Das Center of Mass ist für ein Objekt R, das aus n Teilobjekten
besteht, wie folgt deﬁniert:

CoM(R) =

1
i=1 mi

(cid:80)n

n
(cid:88)

i=1

miri

(2.3)

mit ri als Position vom Teilobjekt i und mi als Masse des Teilobjekts i
[Radi, 2013].

Wenn das CoM innerhalb der konvexen Hülle der Standﬂächen ist, steht
das Objekt stabil, wie in Abbildung 2.5 zu sehen. Diese Fläche wird auch
als Support Polygon bezeichnet. Wenn der CoM außerhalb der konvexen
Hülle liegt, fällt bzw. dreht sich das Objekt in die Richtung des CoM.
Hierbei korreliert die Geschwindigkeit der Drehung mit der Entfernung des
CoM von der konvexen Hülle.

18

2 Theoretische Grundlagen

Abbildung 2.5: Visualisierung des Support Polygons eines sechsbeinigen
Roboters [Siciliano and Khatib, 2008]. Das in orange eingezeichnete
Support Polygon ist durch die Standbeine des Roboters deﬁniert.

Wenn kein Feedback über die aktuellen Kräfte vorliegt, ist es im allgemeinen
Fall zweckmäßig, das CoM in die Mitte der konvexen Hülle zu verschieben.
Dadurch können möglichst große Interferenzen, wie zum Beispiel Stöße,
abgefangen werden.

Das CoM ist aber nur dann ausschlaggebend, wenn keine Kräfte auf den
Roboter wirken. Wenn hingegen eine Kraft nach vorne auf den Roboter
wirkt, kann das den Roboter aus dem Gleichgewicht bringen, auch wenn
die Position des CoM nicht verändert wird. Daher muss ein Stabilitätsmaß
entwickelt werden, das die Kräfte beachtet: Der Zero-Moment-Point.

2.4.3 Zero-Moment-Point

Deﬁntion

Der Zero-Moment-Point (ZMP), ist der Punkt auf der Oberﬂäche des
Bodens, an dem die Summe aller anliegenden physikalischen Momente
gleich null ist. Der Punkt kann stark vereinfacht als Verallgemeinerung des
CoM unter Beachtung der auftretenden Kräfte interpretiert werden. Wenn
der ZMP innerhalb der konvexen Hülle des Fußes liegt, steht der Roboter
stabil.

Vukobratovic legte die Grundsteine für den ZMP und deﬁnierte ihn als:

Deﬁnition 1. „The overall indicator of the mechanism behavior is the
point where the inﬂuence of all forces acting on the mechanism can be
replaced by one single force. This point was termed the Zero-Moment-Point.“
[Vukobratović and Borovac, 2004]

19

2 Theoretische Grundlagen

In der Literatur bestehen verschiedene Deﬁnitionen, die jeweils auf be-
stimmte Aspekte des ZMP fokussiert sind.

Deﬁnition 2. „The Zero-Moment-Point is that point on the ground at
which the net moment of the inertial forces and the gravity forces has no
component along the horizontal axes.“ [Dasgupta and Nakamura, 1999]

Deﬁnition 3. „p is the point that Tx = 0 and Ty = 0, Tx, Ty represent the
moments around x- and y-axis generated by reaction force Fr and reaction
torque Tr , respectively. The point p is deﬁned as the Zero Moment Point
(ZMP). When ZMP exists within the domain of the support surface, the
contact between the ground and the support leg is stable:

pZM P = (xZM P ,yZM P ,0) ∈ S,

where pZM P denotes a position of ZMP. S denotes a domain of the support
surface. This condition indicates that no rotation around the edges of the
foot occurs.“ [Arakawa and Fukuda, 1997]

Deﬁnition 4. „ZMP is the point on the ground where the total moment
generated due to gravity and inertia equals to zero.“ [Takanishi et al., 1990]

Deﬁnition 5. „The ZMP (Zero-Moment Point) is deﬁned to be a point on
the ground at which the tangential component of the moment generated
by the ground reaction force/moment becomes zero.“ [Harada et al., 2003]

Deﬁnition 6. „The ZMP is deﬁned as that point on the ground at which the
net moment of the inertial forces, the external disturbance and gravity forces
has no component, along the horizontal axes.“ [van Oort and Stramigioli,
2011]

Die Deﬁnitionen 3 und 5 weisen auf eine wichtige Bedingung hin, die bei
den anderen nur implizit mitschwingt: Die Reibungskraft zwischen Fuß
und Boden muss hoch genug sein, um die entstehenden Kräfte entlang des
Bodens aufzuheben.

Was die Deﬁnitionen nicht deutlich machen, ist eine in der Wissenschaft bis
heute geführte Diskussion, wie der ZMP im Falle eines instabilen Systems
deﬁniert ist. Während die verbreiteten mathematischen Modellierungen
des ZMP sinnvolle Ergebnisse für instabile Systeme liefern, widersprechen
einige Forscher, dass diese Berechnungen dann der ZMP seien. Es gibt
hauptsächlich drei Interpretationen für den instabilen Fall:

20

2 Theoretische Grundlagen

• Der ZMP kann immer dem Druck unter dem Fuß zugeordnet werden.
Der ZMP bleibt dann an der Kante des Fußes [Sardain and Bessonnet,
2004].

• Die mathematische Modellierung berechnet einen Punkt außerhalb
des Fußes, dieser wird als ZMP gesehen [Vukobratović and Borovac,
2004].

• Der ZMP ist nur im Falle eines stabilen Systems deﬁniert, die Ergeb-
nisse der Berechnungen werden dann häuﬁg als Foot-Rotation-Index
(FRI) bezeichnet [Goswami, 1999].

Mathematische Grundlage

Für die Berechnung des Zero-Moment-Point ist das Moment M gi
beliebigen Punkt Q wichtig [Sardain and Bessonnet, 2004]:

Q um den

M gi

Q = QG × mg − QG × maG − ˙HG

(2.4)

Bei dieser Gleichung ist QG der Vektor von Q zu G, m ist die Masse und g
ist die Gravitationskraft. Also ist QG × mg der Einﬂuss der Gravitations-
kraft auf den Punkt Q. Wohingegen aG die Beschleunigung des CoM und
˙HG das Drehmoment des CoM beschreiben. Da der ZMP der Punkt ist,
an dem kein Drehmoment existiert, muss er also die Gleichung 2.5 erfüllen.

Q × n = 0
Wobei n die Normale des Untergrunds ist, also im Regelfall die z-Achse
des Systems [Sardain and Bessonnet, 2004].

(2.5)

M gi

Die Gleichungen 2.4 und 2.5 lassen sich zusammenfassen. Wenn zusätzlich
die Normale des Untergrunds der z-Achse gleichsetzt wird, lässt sich der
ZMP wie folgt berechnen (vgl. [Sardain and Bessonnet, 2004]):

OD =

mgz × OG × z + z × ˙HG
mg + mag · z

(2.6)

Der so berechnete Zero-Moment-Point ist nun ein direktes Stabilitätsmaß
für den Roboter. Der Gangalgorithmus sollte nun den tatsächlichen ZMP
möglichst nahe am optimalen halten. Da der Roboter keine abrollende
Bewegung machen kann, ist im Allgemeinen der optimale ZMP in der

21

2 Theoretische Grundlagen

Abbildung 2.6: Visualisierung des ZMP eines instabilen Systems. G ist
der Schwerpunkt des Roboters und C seine Projektion auf den Boden.
D ist der ZMP, P ist der COP (modiﬁziert nach [Goswami, 1999]).

Mitte des Fußes während der einzeln belasteten Phase, da der Roboter auf
diese Weise einen möglichst großen Sicherheitsrahmen hat. Er kann so die
größtmöglichen Stöße in jede Richtung aushalten ohne umzukippen.

Wenn OD der Vektor von einem beliebigen Ursprung O zum aktuellen ZMP
und OZ der Vektor zum optimalen ZMP ist, sollte der Laufalgorithmus
nach Dasgupta die mittlere quadratische Abweichung minimieren [Dasgupta
and Nakamura, 1999]:

(cid:90)

minimize

||OD − OZ||2dt

(2.7)

Da sich über diese Formel die Qualität eines Schrittes quantiﬁzieren lässt,
kann ein Lernalgorithmus, der den aktuellen ZMP kennt, das Ergebnis des
Integrals für eine festlegbare Zeit als Reward verwenden.

22

2 Theoretische Grundlagen

Abbildung 2.7: Visualisierung der auftretenden Kräfte unter einem ﬂa-
chen Fuß und dem dazugehörigen CoP [Goswami, 1999]. Die Kräfte
lassen sich in zwei Klassen einteilen, zum einen die Kräfte entlang der
Normalen des Fußes und zum anderen die Drehkräfte unter dem Fuß.
Die Summe der Kräfte wirken am CoP.

2.4.4 Center of Pressure

„CoP [Center of Pressure] represents the point on the support
foot polygon at which the resultant of distributed foot ground
reaction forces acts.“ [Vukobratovic et al., 2001]

Mit Hilfe von Kraftsensoren ist es möglich, die Kräfte zwischen Roboter
und Boden zu messen. Diese Kräfte können als eine einzelne Kraft darge-
stellt werden, die an einem bestimmten Punkt (vgl. Abbildung 2.7 rechts)
anliegt: Dem Center of Pressure (CoP). Hierfür reicht es, im Falle eines
ﬂachen Bodens, vier Kraftsensoren in die Ecken des Fußes zu integrieren
[Vukobratović and Borovac, 2004].

23

2 Theoretische Grundlagen

Nun lässt sich der CoP leicht berechnen:

OP =

(cid:80) rifi
(cid:80) fi

(2.8)

wobei ri die Position des i-ten Sensors und fi dem Sensorwert entspricht
[Goswami, 2015].

Es lässt sich zeigen, dass der CoP und der ZMP im Falle eines stabilen
Ganges übereinstimmen [Sardain and Bessonnet, 2004] [Vukobratovic et al.,
2001]. Mithilfe von vier einfachen Kraftsensoren lässt sich also direkt ein
Stabilitätsmaß für einen humanoiden Gang berechnen.

24

3 Hardwaregrundlagen

In diesem Kapitel wird auf die genutzten Servomotoren eingegangen. Dabei
wird insbesondere ein Fokus darauf gelegt, wie sie angesteuert werden und
wie sie intern ihre Position anfahren.

Anschließend wird erklärt, wie mit 3D-Druckern Kraftsensoren hergestellt
und wie diese kalibriert werden, um aussagekräftiges Feedback zur aktuellen
Druckverteilung zu liefern.

3.1 Motoren

In den Robotern sind Servomotoren der MX-Reihe des Unternehmens
Robotis verbaut. Es gibt drei verschiedene Stärken der Motoren: MX-28 mit
2.5 N m, MX-64 mit 6 N m und MX-106 mit 8.4 N m nominellen Stillstands-
Drehmoment (stall torque). Die Erfahrungen im RoboCup zeigen aber,
dass die Motoren eﬀektiv ein deutlich niedrigeres Stillstands-Drehmoment
haben. Betrieben werden die Motoren bei 12 Volt. Unter Last ﬂießen laut
Datenblatt bis zu 5 Ampere durch den Motor.

3.1.1 Ansteuerung

Die Motoren haben eine integrierte Positionskontrolle, sie steuern also
selbstständig ihre gesetzte Zielposition an. Der Zielwinkel kann in Schritten
von 0,088 Grad eingestellt werden, wobei der Motor aber deutlich ungenauer
ist. Während der Bewegungen liegt durch die Motorsteuerung die eﬀektive
Genauigkeit bei bis zu 8 Grad [Rhoban, 2017].

Die Kommunikation mit den Motoren ﬁndet über ein von Robotis deﬁniertes
Dynamixel-Protokoll statt, das auf einem TTL-Bus basiert und damit ein
asynchrones Half-Duplex-Verfahren ist. Bei diesem Protokoll werden die

25

3 Hardwaregrundlagen

Binärdaten über eine einzelne Ader mit 1-Megabaud übertragen. Jeder
Motor muss einzeln nacheinander angesteuert werden, sodass eine eﬀektive
Updaterate der Motoren zwischen 100 und 150 Hertz erzielt werden kann.

3.1.2 PID-Regler

Die Motoren von Robotis steuern ihre Zielposition über einen PID-Regler an.
PID-Regler basieren darauf, ein Stellglied in Abhängigkeit der Abweichung
eines Zielwertes anzupassen. PID steht dabei für proportional, integral und
derivative. Der P-Regler steuert das Signal proportional, er steuert also
im Verhältnis zur Abweichung vom Sollwert. Der I-Regler summiert den
Fehlerwert über die Zeit auf und steuert so über die Zeit einem Fehler
entgegen. Der D-Regler leitet den Fehlerwert über die Zeit ab und regelt
so in Abhängigkeit von der Veränderung des Fehlerwertes.

Der PID-Regler ist nicht nur mathematisch einfach, sondern auch sehr
ﬂexibel einsetzbar [Bennett, 1984]. Er wird daher für einfache Motorsteue-
rungen häuﬁg genutzt. Allerdings hat sich bei Tests gezeigt, dass Robotis
den PID-Regler in mancher Hinsicht ungewöhnlich umgesetzt hat. Zum
einen hat Robotis nicht dokumentiert, mit welcher Maßeinheit sie steuern.
So dokumentieren sie nur, dass der Standardwert des P-Reglers als 4 ins
Motormodell übertragen wird, aber geben keine Informationen über die
Dimension dieser 4 [Robotis, 2017]. Ein Hindernis ist z.B., dass die Motoren
anscheinend den Fehlerwert ständig integrieren und er nicht zurücksetzbar
ist — dadurch kann man ihn nicht beliebig aus- und einschalten, da er dann
fehlerhaft vorinitialisiert ist. Andererseits ist es aber nicht ratsam, den
I-Regler die ganze Zeit mitlaufen zu lassen, da der Fehlerwert je nach Belas-
tungssituation deutlich unterschiedlich ist (vgl. Abschnitt 6.2). Deswegen
ist der I-Regler der Motoren nicht eﬀektiv einsetzbar.

3.2 3D-gedruckte Kraftsensoren

3D-Druck ist ein additives Herstellungsverfahren, das sich seit dem Aufkom-
men der RepRap Drucker sehr stark verbreitet hat [Moilanen and Vadén,
2013]. Bei diesen Druckern handelt es sich um Fused-Deposition-Modeling
Drucker, die das Plastik-Filament schmelzen und dabei eine Kunststoﬀ-
schicht erzeugen. Das Zielobjekt wird so Schicht für Schicht erstellt. Diese
Technologie ermöglicht es, insbesondere Prototypen schnell und einfach zu
erstellen und so Hardware in iterativen Schritten zu entwickeln.

26

3 Hardwaregrundlagen

Da sich gleiche 3D-gedruckte Objekte vom selben Drucker unter Last
sehr ähnlich verformen, lassen sich mithilfe von 3D-Druckern einfache, auf
den Anwendungsfall zugeschnittene Kraftsensoren entwickeln, die darauf
basieren, die Verformung des Objektes unter Last zu messen. Als ﬂexibler
Ansatz wurde das Messen der Verformung über Näherungssensoren gewählt.
Hierbei wird unter Krafteinﬂuss der Abstand zwischen dem 3D-gedruckten
Objekt und einem Näherungssensor verringert. Dadurch verändert sich
dann der gemessene Wert des Näherungssensors. Diese Abbildung von
Kraft zu Sensorwert muss kalibriert werden, um sinnvolle Informationen
zu bekommen.

Für die Kalibrierung sind zwei Faktoren relevant: Zum einen die Verfor-
mung des Objektes durch die Kraft, zum anderen die unterschiedlichen
Sensorwerte durch den Abstand des Objektes vom Sensor. Insbesondere
die Veränderung des Sensorwertes ist nicht linear und daher aufwendig zu
kalibrieren. Um die Kalibrierung möglichst generell zu halten, können die
zwei Faktoren unabhängig voneinander kalibriert werden. Es wird dann
zweistuﬁg der Sensorwert auf eine Entfernung vom Sensor abgebildet und
anschließend die Kraft aus der Entfernung berechnet. Diese doppelte Abbil-
dung hat den Vorteil, dass die aufwendigere Kalibrierung der Entfernung
zum Sensorwert nur einmal durchgeführt werden muss und dann beim
Wechseln des 3D-gedruckten Objektes nur die Verformung kalibriert werden
muss.

3.2.1 Kalibierung von Näherungssensoren

Optische Näherungssensoren können die Verformung und damit Kräfte
bestimmen, indem sie den Abstand zwischen dem Sensor und einem Objekt
messen. Im Rahmen der Masterarbeit wurden die Reﬂexlichtschranken
„ITR8307 “ von Everlight genutzt [Everlight Electronics, 2010]. Diese enthal-
ten eine Infrarotdiode und einen NPN-Fototransistor, dessen Schaltplan in
Abbildung 3.1 gezeigt ist. Der Fototransistor kann für den Anwendungsfall
als variabler Widerstand gesehen werden, dessen eﬀektiver Widerstands-
wert von dem einfallenden Infrarotlicht und damit der Entfernung des
reﬂektierenden Objektes abhängt. Die Infrarotdiode sendet das Licht aus,
dessen Reﬂexion den Widerstand des Fototransistors bestimmt.

Optische Näherungssensoren sind im Allgemeinen nicht linear bezüglich
ihrer Reaktion auf veränderte Entfernungen, daher muss eine Kalibrierung
über die gesamte Sensorkurve durchgeführt werden. Hierfür wird eine

27

3 Hardwaregrundlagen

Abbildung 3.1: Der Schaltplan des ITR8307: Unten die Infrarot-LED

und oben der Fototransistor [Everlight Electronics, 2010].

Menge von Kalibrierungspunkten aufgenommen, zwischen denen dann
interpoliert wird, um die eﬀektive Position zu bestimmen.

Im Verlauf dieser Masterthesis wurde ein Testsetup erstellt, das den Sensor
an einem handelsüblichen 3D-Drucker befestigt. Dieses Setup ist in Abbil-
dung 3.2 links zu sehen, rechts in dem Bild ist die Düse des 3D-Druckers,
an dessen Halterung der Sensor befestigt wurde. Das Testsetup lässt sich
dadurch sehr präzise bewegen. Der Sensor ist in der Mitte des Bildes sicht-
bar und beﬁndet sich knapp oberhalb der Oberﬂäche des Balkens, gegen die
gemessen wird. Teile des Sensors verdeckend ist ein Lichtschutz zu sehen,
der vor einfallendem Infrarotlicht der Sonne oder anderen Quellen schützt.

Da die Reﬂexionseigenschaften jedes Materials unterschiedlich sind, sollte
die Kalibrierung für den späteren Einsatz mit dem Zielobjekt durchge-
führt werden. Der schichtweise Aufbau des 3D-gedruckten Objektes führt
zu unterschiedlichen Reﬂexionseigenschaften in Abhängigkeit davon, ob
die Achse der Oberﬂäche den Schichten entspricht. Dieser Unterschied
macht bis zu 15% der Reﬂexion aus, daher sollte die Kalibrierung auch die
Orientierung des Objektes beachten.

28

3 Hardwaregrundlagen

Abbildung 3.2: Kalibrierungssetup für den Entfernungsmesser (links).
Der Näherungssensor ist über einen Stab am Drucker befestigt und
nahe an den weißen Balken gefahren, der in weiten Teilen von einem
Infrarotschutz umgeben ist. Beim Hochfahren des Sensors werden die
Sensorwerte aufgenommen. Die dabei entstehende Abbildungskurve
von Sensorwert zu Distanz ist rechts visualisiert.

Der Sensor wird beim Setup auf Sicht an die Messoberﬂäche herangefahren
und der Wert des Sensors ausgelesen. Da das Druckbett des 3D-Druckers
bei Druck nachgibt, wird der Sensor nicht direkt beschädigt, falls es zum
Kontakt mit der Oberﬂäche des Balkens kommt. Der Sensor wird nun
präzise in 0,1 mm Schritten von der Oberﬂäche weggefahren und dabei
werden weitere Sensorwerte aufgenommen. Mithilfe der so erstellten Tabelle
(Abbildung 3.2 rechts) lassen sich gegebene Sensorwerte durch Interpolation
zwischen den gemessenen Werten sehr genau auf die tatsächliche Entfernung
abbilden.

3.2.2 Kalibrierung von Verformungen

Wenn die Verformung des Objektes bekannt ist, muss noch die Verfor-
mung auf die Kraft abgebildet werden. Während die generelle Verformung
von Objekten nur über die Finite-Elemente-Methode berechenbar und
damit sehr komplex ist, lässt sich das Problem vereinfachen, indem das
verformende Objekt speziell gestaltet wird. Der einfachste Fall ist ein sich
verbiegender Balken, bei dem das Hooke’sche Gesetz gilt [Wasserfall et al.,
2017].

29

3 Hardwaregrundlagen

Die anliegende Kraft F ist durch die Federkonstante k und die Verformung
δl berechenbar:

F = k · δl

(3.1)

Um die Verformung nun zu kalibrieren, reicht es den Sensor gegen eine
einfache Waage zu drücken und die Kraft und Verformung zu messen. Die
Federkonstante ist dann:

k =

F
δl

(3.2)

Zusammengesetzt lässt sich das Prinzip in Abbildung 3.3 sehen.

Abbildung 3.3: OpenSCAD-Rendering eines einfachen Kraftsensors.
Oben in gelb ist der verformbare Balken. In blau und grün sind der
Entfernungssensor beziehungsweise der Messpunkt angegeben, der be-
nutzt wird, um die entsprechenden Kräfte zu messen [Wasserfall et al.,
2017].

30

lFsProximity sensorDeformable beamPredicteddeflectionOptional baseSensor marker4 Hardwaredesign

Im Rahmen dieses Kapitels wird die Entwicklung der Hardware beschrie-
ben. Zuerst wird der Prototyp erklärt, bei dem die Sensoren nur an einem
bestehenden Fuß befestigt wurden. Danach wird der neu entwickelte 3D-
gedruckte Fuß vorgestellt. Im anschließenden Abschnitt wird über den
Entwurf des kleinen Prototypboards, das die für die Sensoren benötigte
Elektronik platzsparend integriert, berichtet und abschließend die Entwick-
lung des professionellen Boards erläutert, das die Kraftsensoren in Füßen
zukunftsfähig machen soll.

4.1 3D-Druck-Fuß

Abbildung 4.1: Links ein Foto des ersten Prototypen. Rechts ein ge-
brochener Kraftsensor, dessen Bruchstelle am rechten Rand sichtbar
ist.

Beim ersten Prototypen wurden die Kraftsensoren an einem bestehenden
Fuß befestigt, dieser ist in Abbildung 4.1 zu sehen. Hier waren die Sensor-
kabel zur Seite herausgeführt. An diesen Kabeln konnte sich der Roboter
jedoch schnell verhaken, sodass sie leicht abgerissen wurden. Zusätzlich war
der Näherungssensor fest mit dem verformbaren Balken verbunden, sodass
der Balken im Falle von Beschädigungen (siehe Abbildung 4.1 rechts) nicht
einfach austauschbar war. Die feste Verbindung führte auch dazu, dass
keine Modiﬁzierung der Auﬂösung durch unterschiedliche Dicke des Balkens
möglich war.

31

4 Hardwaredesign

Abbildung 4.2: Links: Das Fußmodell in OpenSCAD. Rechts: Eine Nah-
aufnahme des Kraftsensors. Die umgebende Lichtschutzhülle wurde
für das Foto entfernt. In weiß ist der sich verbiegende Balken zu sehen.
Die große schwarze Fläche ist ein Teil des Fußes, in die unterhalb
des Balkens der Näherungssensor geklebt wurde. Dieser Sensor ist zur
Hälfte sichtbar, inklusive Fototransistor neben der Infrarot-LED mit
ihren jeweiligen Anschlüssen.

Abbildung 4.3: Links: Die zweite Version des Fußes mit den integrierten
Sensoren. Rechts das dazugehörige Board mit den Widerständen. Ins-
besondere die Kabelführung ist bei diesem Prototypen problematisch.

Um eine gute Integration der Sensoren in den Fuß zu ermöglichen, wurde
daher der Fuß in OpenSCAD neu entworfen. Das Design ist Abbildung 4.2
von oben zu sehen. In den Ecken sind die Aussparungen für die Anschlüsse
der Sensoren zu sehen. Am Rand der Längsseiten sind die Schraubenlöcher
für die sich verformenden Balken zu erkennen. Ferner gibt es Aussparungen
für Platinen und Kabel sowie die Befestigung für die Ferse in der Mitte
des Fußes. Der ausgedruckte Fuß ist in Abbildung 4.2 rechts zu sehen. Die
Näherungssensoren werden von unten in den Fuß geklebt und die Kabel
nach oben weggeführt.

32

4 Hardwaredesign

4.2 Prototyp-Platine

Die Kabelführung war, wie in Abbildung 4.3 erkennbar, immer noch nicht
ausreichend. Zum einen war es nicht ersichtlich, welches stromführende
Kabel zu welchem Sensorkabel gehörte. Zum anderen hatten die Standard-
Prototypstecker nicht genügend Halt und verloren daher die Verbindung.
Schließlich gab es keinen Ort, um die Platine anzubringen. Daher wurde
eine kleine integrierte Platine entwickelt.

Hierfür wurde als Microcomputer-Board ein Teensy3.2 benutzt, der auf ei-
nem ARM Cortex-M4 basiert und in weiten Teilen kompatibel zur Arduino-
Plattform ist [PJRC, 2010]. Dieser wurde an eine Lochrasterplatine gelötet
und die dazugehörigen Widerstände möglichst platzsparend verlötet.

Der Schaltplan ist in Bild 4.4 zu sehen. Das Ausmessen des Sensorwertes
basiert auf dem Prinzip des Spannungsteilers [Bernstein, 2012]. Von der
3,3 V Spannungsversorgung ist ein 10.000 Ω Widerstand vor dem Fototran-
sistor geschaltet. Zwischen dem Widerstand und dem Fototransistor wird
die Spannung gemessen. Ist dabei der Widerstand des Transistors niedrig,
fällt die ganze Spannung am Widerstand ab: Die gemessene Spannung ist
ebenfalls niedrig. Ist der Widerstand des Transistors hoch, ist hingegen die
gemessene Spannung hoch, da am Transistor die meiste Spannung abfällt.

Die LEDs sind mit einem 360 Ω Vorwiderstand ausgestattet, um das nöti-
ge Infrarotlicht für den Fototransistor zu emittieren. In dem Schaltplan
beﬁndet sich das eigentliche Board auf der linken Seite. Auf der rechten
Seite sind die im Fuß verklebten Sensoren zu sehen. Zwischen den beiden
Teilen beﬁnden sich 4er Stecker.

Der Teensy liest über seine integrierten ADC-Pins die Spannung an den
Sensoren und interpoliert eine Entfernung mithilfe der aufgenommenen
Daten (vgl. Abbildung 3.2). Bei der Kalibrierung wurde eine Federkonstante
von D = 17,95 N/mm gemessen. Der Teensy berechnet dann mit der
Anfangsentfernung des Balkens d0 und der aktuellen Entfernung dt die
gemessene Kraft F (siehe Gleichung 4.1) und überträgt diese dann über
den integrierten USB-Chip als serielles Signal.

F = 17,95 · (d0 − dt)

(4.1)

33

4 Hardwaredesign

4.3 PCB-Platine

Im Rahmen der Hardwareentwicklung wurde in Kooperation mit ande-
ren Mitgliedern der Hamburg Bit-Bots eine komplette Neuentwicklung
des Mikrocontroller-Boards (siehe Bild 4.6 links) durchgeführt. Dieses
Board basiert auf einem STM32F103 und beinhaltet unter anderem einen
TTL-Treiber und einen 24-Bit Analog-Digital-Converter. Der TTL-Treiber
unterstützt eine Kommunikation über den TTL-Bus der Dynamixel Mo-
toren, deswegen benötigt der Chip kein eigenes USB-Kabel zum Rechner.
Die 24-Bit des ADC-Chip ermöglichen eine deutlich höhere Auﬂösung der
gemessenen Spannung. Außerdem kann der Chip auch diﬀerenzielle Signale

Abbildung 4.4: Schaltplan der Prototyp-Platine. Links beﬁndet sich das
Pinout des Teensy, mit den 3,3 und 5 V Pegeln. In der Mitte sind die
Widerstände für die LEDs und für die Spannungsteiler. Rechts sind
die vier Drucksensoren, die jeweils aus einer Infrarot-LED und einem
Phototransistor bestehen.

34

4 Hardwaredesign

Abbildung 4.5: Ausschnitt vom entwickelten Fuß. Links in weiß ist der
verformbare Balken des Kraftsensors gut zu sehen. Im Fuß oberhalb
des Spalts zum Balken ist der Näherungssensor verklebt, dessen Kabel
auf der Oberseite des Fußes sichtbar sind.

von Dehnungsmessstreifen verarbeiten. Das Board ist damit nicht nur in
der Lage, die auf Näherungssensoren basierenden Kraftsensoren, sondern
auch industriell gefertigte Wägezellen auszuwerten.

Industrielle Wägezellen basieren genauso wie die gedruckten Kraftsensoren
darauf, dass die Verformung eines Messbalkens gemessen wird. Diese Wäge-
zellen sind wie in Abbildung 4.6 rechts erkennbar meist aus Metall gefertigt.
Der messbare Hub ist bei der gleichen Kraft deshalb deutlich kleiner als
bei 3D-gedruckten Sensoren. Genauso wie auch die gedruckten Sensoren
müssen die verwendeten Dehnungsmessstreifen ebenfalls kalibriert werden,
wobei auch bei diesen Sensoren die Veränderung des Widerstands linear
zur Verformung ist. Deswegen lässt sich die Verformung e mit folgender
Formel berechnen [Fraden, 2010]:

e =

dR
R · Se

(4.2)

wobei Se ein materialspeziﬁscher Faktor ist, der sich zusammen mit der
Federkonstante einfach gegen eine Waage kalibrieren lässt.

Programmiert ist der STM32F103 in C++ mithilfe der STM32Plus Library
von Andy Brown [Brown, 2017]. Die Software des Chips (vgl. Code auf der
beiliegenden CD) kommuniziert in Dauerschleife mit dem LTC-4422-ADC
und liest auf dem Motorbus durch Hardware-Interrupts die Pakete mit,

35

4 Hardwaredesign

Abbildung 4.6: Die neu entwickelte Platine (links) und eine einsetzbare
Wägezelle (rechts). Die Platine enthält sowohl alle benötigten Kompo-
nenten, um die Kommunikation über den Motorbus zu ermöglichen, als
auch einen genauen Analog-Digital-Konverter, um die Sensoren präzise
auszuwerten.

um dem Master antworten zu können. Allerdings gibt es bisher keinen
vollständig einsatzfähige Prototypen, sodass die Platine nicht evaluiert
werden konnte.

36

5 Software

Im Rahmen des Kapitels zur entwickelten Software wird zunächst die
Technik des Reinforcement Learnings eingeführt, die genutzt wird, um
das Gehen auf dem physischen Roboter während der Bewegungen zu
optimieren und damit zu stabilisieren. Danach wird der Einsatzbereich des
Reinforcement Learning im Kontext der bestehenden Klassen und Abläufe
eingeordnet.

Im Anschluss wird genauer speziﬁziert, was der Algorithmus lernen soll
und wie die dazugehörige Policy strukturiert bzw. visualisiert werden kann.
Abschließend wird dargestellt, wie die Policy sinnvoll vorinitialisiert werden
kann, um das anfängliche Lernen zu beschleunigen.

5.1 Reinforcement Learning

„Reinforcement Learning is learning what to do - how to map
situations to actions - so as to maximize a numerical reward
signal. [...] The learner [...] must discover which actions yield
the most reward by trying them.“ [Sutton and Barto, 1998]

Durch Reinforcement Learning kann Software Probleme lösen, ohne dass die
exakte Lösung im Vorwege programmiert wird. Der Algorithmus probiert
verschiedene Strategien aus und beobachtet anschließend das numerische
Feedback bzw. den Gewinn R, um langfristig das bestmögliche Feedback
zu erhalten.

Die aktuelle Strategie, die von einem Reinforcment Learning Algorithmus
ausgeführt wird, ist die Policy π, die bestimmt, dass in dem Zustand s die
Aktion a ausgeführt wird. Ein Zustand kann die Phase des Laufalgorithmus
sein und die Aktion die Position des Oberkörpers. Das anschließende Re-
wardsignal kann nun die Abweichung des ZMP vom Zielwert sein. Dadurch

37

5 Software

ist es möglich, dass die Bewegung des Oberkörpers nicht explizit modelliert
ist, sondern sich in Abhängigkeit der Performance des Roboters verändert.

Die klassischen Ansätze von Sutton et. al. speichern eine Value-Funktion,
die eine Qualitätsabschätzung des jeweiligen Zustandes darstellt. Im Allge-
meinen berechnet die Value-Funktion also eine Abschätzung des zukünf-
tigen Gewinns. Diese Ansätze werfen aber im Kontext von humanoiden
Robotern, insbesondere wenn die Aktionen a kontinuierlich sind, viele
Probleme auf [Deisenroth et al., 2013], die bei Algorithmen ohne Value
Funktion nicht in dem Maße auftreten [Peters et al., 2003].

Aufgabe des Reinforcement Learnings ist es nun, die optimale Policy her-
auszuﬁnden. Die Policy ist optimal, wenn sie den Gewinn maximiert. Das
Lernverfahren darf dabei den Roboter nicht beschädigen und sollte nicht
zu viel Zeit benötigen. Aus diesem Grund ist eine randomisierte Suche
nicht tolerierbar, auch wenn sie theoretisch ein optimales Ergebnis erzielen
würde. Es müssen aufwendigere Ansätze wie die Policy Gradient Algorith-
men angewendet werden, um schnell und vergleichsweise sicher ein lokales
Optimum zu ﬁnden. Eine Schwäche dieser Algorithmen ist, dass dieses
Optimum weit vom globalen entfernt sein kann.

Die Aktion a ist dabei ein Tupel von zwei Gleitkommazahlen, welche die
Position in Metern vom Startpunkt des Oberkörpers darstellt. Gesteuert
wird die x- (vorwärts) und y- (seitwärts) Position des Oberkörpers.

Im Folgenden werden die Techniken des Reinforcement Learning eingeführt,
die für die Evaluation (vgl. Kapitel 6) der Software verwendet wurden.

5.1.1 Policy Gradient Algorithmen

„Policy search is a subﬁeld in reinforcement learning which
focuses on ﬁnding good parameters for a given policy para-
metrization. It is well suited for robotics as it can cope with
high-dimensional state and action spaces, one of the main chal-
lenges in robot learning.“ [Deisenroth et al., 2013]

Während klassische Reinforcement Learning Algorithmen in ihrer aktiven
Lernphase eine randomisierte Suche durchführen, die den gesamten Such-
raum evaluiert, suchen Policy Gradient Algorithmen nur in der Nähe der
aktuellen Policy. Sie schätzen dabei den Gradienten des zu erwartenden
Gewinnes ab, um damit entlang des Gradienten die Policy zu verbessern.

38

5 Software

Ausschließlich entlang des Gradienten zu suchen, erhöht zwar deutlich das
Risiko, in einem lokalen aber nicht globalen Minimum zu landen, allerdings
reduziert die Abwesenheit von randomisierter Suche die Gefahr, den Roboter
zu beschädigen. Wenn der Roboter bereits einen vergleichsweise stabilen
Gang aufweist, dann führt die Policy Gradient Suche dazu, dass der Roboter
sich nicht aus dem stabilen Gang entfernt. Hat der Roboter noch keinen
stabilen Gang gelernt, ist im Allgemeinen ein menschlicher Beobachter
anwesend, der notfalls eingreifen kann. Der Roboter macht durch eine
Gradientensuche im Normalfall keine unerwarteten Bewegungen, was das
Eingreifen des Beobachters erleichtert. Um die Wahrscheinlichkeit von
gefährlichen Bewegungen noch weiter zu reduzieren, kann die Steigung des
Gradienten begrenzt werden: Sobald der Gradient diese Grenze erreicht
hat, steigt er nicht mehr. So führen einzelne massive Abweichungen im
Rewardsignal zu keinen großen Problemen.

5.1.2 Rewardsignal

Da der Roboter den Fuß nicht abrollen kann und die optimale Position
für den ZMP sich deswegen im Rahmen dieser Thesis in der Mitte des
Fußes beﬁndet, wird in Anlehnung an Gleichung 2.7 das Rewardsignal Rx
für die x-Policy in Gleichung 5.1 und Ry für die y-Policy in Gleichung 5.2
deﬁniert. Der gemessene CoP ist 0, wenn er exakt in der Mitte des Fußes
ist. Das Rewardsignal ist damit eine Minimierungsaufgabe. Der Reward
ist optimal, wenn er null ist. Daraus ergibt sich:

min(Rx(|CoPx|))

min(Ry(|CoPy|))

(5.1)

(5.2)

Dieser Reward kann nach jeder Kommunikation mit den Motoren und
Sensoren gegeben werden. Da es auch keine Extrabelohnung am Ende eines
Schrittes gibt, kann der Algorithmus online und durchgängig beim Gehen
lernen.

39

5 Software

5.1.3 Finite Diﬀerenzen Policy Gradient

Die einfachste Variante eines Policy Gradient Algorithmus basiert auf
Finiten Diﬀerenzen. Dieser Algorithmus nutzt eine Episoden-basierte Eva-
luationsstrategie. Der Algorithmus schätzt dabei den Gradienten anhand
der Erfahrungen ab, die er durch mehrere Durchgänge gewonnen hat. Da-
für fügt er kleine Störungen δΘ zur ausgeführten Bewegung hinzu. Dann
können die Unterschiede im Feedback δR = R(Θ + δΘ) − R(Θ) beobachtet
werden. Anschließend kann der Gradient wie folgt abgeschätzt werden
[Deisenroth et al., 2013]:

∇E(R(π))Θ = (δΘT δΘ)−1δΘT δR

(5.3)

5.1.4 ZMP-Position als Gradientenabschätzung

Während die Finite Diﬀerenzen Policy Gradient Methode eine Blackbox-
Methode ist, um den Gradienten zu bestimmen, lässt sich aus der Position
des ZMP direkt eine Abschätzung des Policy Gradienten ableiten. Wenn
der ZMP zu weit vorn ist, muss der Roboter sich weiter nach hinten lehnen,
um auch den ZMP nach hinten zu verschieben. Beim ZMP als Gradien-
tenabschätzung wird das Rewardsignal um die Richtung der Abweichung
erweitert:

Rx(Richtung,Reward) =

(cid:26) Rx(1,|CoPx|)

Rx(−1,|CoPx|)

falls CoPx < 0
falls CoPx ≥ 0

Ry(Richtung,Reward) =

(cid:26) Rx(1,|CoPy|)

Rx(−1,|CoPy|)

falls CoPy < 0
falls CoPy ≥ 0

(5.4)

(5.5)

Beim Lernen wird die Zielposition der Policy in Abhängigkeit der Richtung
und des Rewards verändert.

40

5 Software

5.1.5 Temporal Diﬀerences „TD(λ)“

Beim Temporal Diﬀerences (TD) Learning wird nicht nur das aktuelle
Reward-Signal betrachtet, sondern auch, wie gut der erreichte Zustand ist.
Hierfür gibt es bei dem TD(λ)-Ansatz sogenannte „eligibility traces“, bei
denen für die nächsten n Zustände der Reward jeweils um dem Faktor
λ ∈ (0,1) reduziert mit einﬂießt [Sutton and Barto, 1998]. Der Reward ist
dann:

Rt(π) = rt + λ · rt+1 + λ2 · rt+2 + . . . + λn · rt+n

(5.6)

5.1.6 Funktionsapproximation mit Tile-Coding

Eine Herausforderung im Reinforcement Learning für Roboter ist die Konti-
nuität des Zustandsraums. Ein Beispiel hierfür ist die Zeit seit dem Anfang
des Schrittes. Aus dieser Kontinuität folgt, dass es nicht möglich ist, alle
erreichbaren Zustände aufzulisten, da es unendlich viele von ihnen gibt. Die
möglichen Zustände müssen daher über Funktionen approximiert werden.
Eine der einfachsten und wichtigsten Ansätze ist das Tile-Coding [Sutton
and Barto, 1998].

Beim Tile-Coding wird der Zustandsraum in Partitionen aufgeteilt, in
denen die Funktion als konstant angenommen wird. Der Zustandsraum
wird also künstlich diskretisiert.

5.1.7 Gauß-Filter

Abbildung 5.1: Einﬂuss des Feedbacksignal ri auf die benachbarten Tiles
(modiﬁzierte Graﬁk aus [Sutton and Barto, 1998] über Radial Basis
Functions).

Das Rewardsignal kann mit einem Gauß-Filter über adjazente Tiles geﬁltert
werden. Dieser glättet die Auswirkungen des Lernsignals auf mehrere Tiles.
Dadurch wird eine gleichmäßigere Bewegung in der erlernten Policy erreicht.

41

5 Software

Die Veränderung an den Tiles ist durch den Gauß-Filter eine ableitbare
Funktion. Der Einﬂuss des Rewardsignal ri hat in den benachbarten Tiles
ci in Abhängigkeit von der Breite σ in folgender Form Einﬂuss:

ci(ri) = exp

(cid:19)

(cid:18) ||s − ci||2
2σ2

(5.7)

5.2 Softwarearchitektur

Abbildung 5.2: Abstrahiertes Diagramm des Laufalgorithmus in dem
die Abfolge von beteiligten Steuerelementen dargestellt ist, die aus
einer Richtung bzw. Geschwindigkeit des Laufalgorithmus die physische
Bewegung auf dem Roboter generiert.

Die generelle Struktur des Laufalgorithmus ist in Abbildung 5.2 darge-
stellt. Zunächst wird die Zielposition für das Ende des Schrittes bestimmt,
anschließend die aktuelle Position des Roboters im kartesischen Koordina-
tensystem. Diese wird mithilfe der inversen Kinematik in die entsprechenden
Gelenkwinkel übersetzt. Diese Zielwinkel werden dann an die Motoren
übertragen, auf denen ein PID-Regler das Drehmoment steuert. Wenn
die Kommunikation mit den Motoren abgeschlossen ist, wird der aktuelle
Schritt weitergeführt oder wenn nötig ein neues Schrittziel berechnet.

42

5 Software

Abbildung 5.3: Laufgenerator mit und ohne Stabilisator. Das Sensor-
feedback soll nicht wie in den Standardansätzen in einen Stabilisator
integriert werden (links), der kaum Möglichkeit hat, aus dem Feedback
für die Zukunft zu lernen. Stattdessen wird das Sensorfeedback direkt
in den Generator der Zielpositionen integriert (rechts). Dadurch kann
die generierte Trajektorie des Roboters dauerhaft verbessert werden.
Die linke Graﬁk wurde aus [Siciliano and Khatib, 2008] übernommen.

Im Rahmen der Software werden die Informationen über den ZMP im
zweiten Teilschritt genutzt: Es wird gelernt, wie die aktuelle Zielposition
sein muss, um ein möglichst stabiles Laufen zu ermöglichen. Im Gegen-
satz zu klassischen Ansätzen mit Sensoren kommt kein Stabilisator (vgl.
Abbildung 5.3) zum Einsatz. Ein solcher Stabilisator erhält die generierte
Abfolge des Laufalgorithmus und modiﬁziert diese in Abhängigkeit vom
aktuellen Feedback. Dadurch, dass diese Stabilisatoren kein Wissen über
den Zustand des Laufalgorithmus haben, sind sie nicht in der Lage, durch
aktuelles Feedback die Bewegungsabfolge langfristig zu verbessern. Das
Sensorfeedback wird wie in Abbildung 5.3 rechts zu sehen, direkt in den
Generator der Bewegungsabfolge integriert, damit das Feedback die eigent-
liche Abfolge verbessert und so eine langfristige Verbesserung zeigt. Dabei
bleibt der Generator der Abfolge aber von den Sensoren weitestgehend
unabhängig: Die Bewegungen des Oberkörpers sind ausschließlich von der
Position und Geschwindigkeit der Füße abhängig. Dies ermöglicht es, auf
diesem Algorithmus aufbauende Stabilisatoren zu entwickeln, solange diese
selten in die ausgeführte Bewegung eingreifen.

Ein Überblick über die relevanten Klassen zum Lernen mit dem ZMP ist in
Abbildung 5.4 zu sehen. Die zentrale Klasse Walking stellt zum einen die
Schnittstelle zum Rest des Systems dar. Zum anderen werden in der Klas-
se die mathematisch einfach modellierbaren Teile des Laufens berechnet,
unter anderem die Phase des Schrittes, die Schrittabfolge, aber auch die
Positionen der Beine. Insbesondere strukturell ist diese Klasse noch an den
ursprünglichen Code vom Team DARwIn angelehnt [Team-Darwin, 2017].

43

5 Software

Abbildung 5.4: Abstrahiertes Klassendiagramm. In der Mitte ist die
Klasse Walking dargestellt, welche die Schnittstelle zum restlichen
System deﬁniert. Die Berechnung der Oberkörperposition ist in den
ZMP-Lerner und dessen Subklassen ausgelagert. Die Kommunikation
mit den Motoren geschieht über die Klassen Motion und Lowlevel.

Die Klassen Motion und Lowlevel stellen die wichtigsten Funktionen für
den Laufalgorithmus bereit. Das Lowlevel organisiert die Kommunikation
mit dem Motorbus, bildet also aus den Zielwinkeln die entsprechen Motor-
befehle. Die Klasse Motion kümmert sich um Aufgaben, wie das Aufstehen
nach einem Sturz des Roboters. Die Klasse steuert auch, ob der Roboter
nach den aktuellen Regeln des Spieles gerade laufen darf. Die inverse Kine-
matik berechnet aus den Zielpositionen die Zielwinkel der Motoren, welche

44

5 Software

das Walking direkt an die Motion weiterleitet. Hierdurch erfolgt sämtliche
Kommunikation mit dem restlichen Softwaresystem ausschließlich durch
die Walking Klasse.

Die klare und übersichtliche Schnittstelle führte dazu, dass der Laufal-
gorithmus nach ROS portiert und erfolgreich ausgeführt werden konnte
[Bestmann, 2016].

Das Ziel des ZMP-Lerner ist das Lernen der Oberkörperbewegung, sodass
der ZMP möglichst nahe am Optimum ist (vgl. Gleichung 2.7). Da der
Roboter mit seinem Fuß nicht abrollen kann, wird im Rahmen dieser Thesis
der allgemeine Fall angenommen, dass der optimale ZMP sich in der einzeln
belasteten Phase immer in der Mitte des Fußes beﬁndet.

5.3 Policy Struktur

Um die Zielposition des Oberkörpers zu bestimmen, bekommt der ZMP-
Lerner die aktuelle Position der Füße übergeben. Da die Trajektorie der
Füße mathematisch fest modelliert ist (vgl. Abschnitt 2.3 „Gang humanoider
Roboter“) und daher konstant über die Durchgänge bleibt, wird diese
Information aufbereitet und in Form eines Prozentwertes des Schrittes
übergeben. Die Bewegungsrichtung des Roboters wird mit übergeben, da
diese die optimale Trajektorie des Oberkörpers beeinﬂusst. Zusätzlich
muss auch die Geschwindigkeit beachtet werden: Wenn der Roboter sich
schneller bewegt, werden auch die entstehenden Bewegungskräfte größer,
der Oberkörper muss also anders bewegt werden.

Wünschenswert wäre es, wenn der aktuelle ZMP vom Lerner beachtet
werden würde. Allerdings ist dies mit dem verwendeten Ansatz des Tile-
Codings schwer vereinbar, da viele Kombinationen von ZMP und Position
selten erreicht werden. Tile-Coding hingegen benötigt genau diese Eigen-
schaft, um jede ihrer Tiles zu lernen. Man müsste daher eine andere Art
der Funktionsapproximation wählen, um den aktuellen ZMP im Lerner zu
beachten.

Aktuell interagiert die Klasse Walking noch direkt mit den Kraftsensoren.
Mit der überarbeiteten Platine (vgl. Abschnitt 4.3) hingegen wird das
Interface der Klasse etwas übersichtlicher, da die Kraftsensoren über die
Klassen des „Lowlevel“ ausgelesen werden sollen, da dann die Kraftsensoren
über den Motorbus angeschlossen sind.

45

5 Software

Die zu lernende Abbildungsfunktion ist also:

fcom(Speedx, Speedy, Speedα, belastetesBein, P hase) → (x,y)

(5.8)

Die Variable x steht hier für die Vorwärts-Position und die Variable y für
die Seitwärts-Position des Oberkörpers relativ zum Startpunkt. Es wird
ausschließlich die Position gelernt. Der Roboter soll beim Gehen nicht
geneigt werden, da hierdurch das Blickfeld der Kamera beeinträchtigt wird.

Der kontinuierliche Input wird mithilfe von Tile-Coding diskretisiert. Die
Zielgeschwindigkeit des Laufalgorithmus wurde während eines Spieles auch
vorher schon diskret in fünf Geschwindigkeitsstufen gesetzt. Es entste-
hen im Rahmen des bestehenden Systems also keine problematischen
Einschränkungen durch die Diskretisierung der Zielgeschwindigkeiten. Da
der Roboter sich nicht exakt symmetrisch verhält, ist das belastete Bein
relevant. Dadurch kann die Phase im Intervall [0,1) modelliert werden.

5.4 Policy Darstellung

Beim Lernen kann die Gleichung 5.8 aufgeteilt werden. Während meh-
rerer aufeinander folgender Schritte ändert sich die Geschwindigkeit im
allgemeinen nicht, d.h. das Lernsignal bezieht sich auf feste Werte von
Speedx, Speedy, Speedα. Wenn die Zielgeschwindigkeit geändert wird, lernt
der Algorithmus diese neue Geschwindigkeit unabhängig von der alten. Des-
halb sind zum Verständnis des Lernverfahrens die Parameter belastetesBein,
P hase wichtig. Dadurch, dass der Roboter zwei Beine besitzt, lässt sich die
Policy durch zwei Abbildungen mit dem Parameter Phase, also f (P hase) =
(x,y), darstellen.

Die Policy, also die Bewegung des Oberkörpers, ist in Abbildung 5.5 für
(Speedx = 1, Speedy = 0, Speedz = 0) visualisiert. Das obere Teilbild
visualisiert die Bewegung, während das linke Bein das Standbein ist, das
untere Teilbild entsprechend mit dem rechten Bein als Standbein.

Die rote bzw. schwarze Linie stehen für die Seitwärts- respektive Vorwärts-
achse des Oberkörpers, wobei ein Wert von 0 bedeutet, dass der Oberkörper
des Roboters sich genau in der Mitte der Anfangsposition der beiden Beine
beﬁndet. Da der Roboter sich vorwärts bewegt, startet die Vorwärtsposition
des Oberkörpers im negativen Bereich in der Mitte zwischen den beiden
Füßen. Danach bewegt sich der Oberkörper nach vorne über das vordere

46

5 Software

Abbildung 5.5: Initiale Policy: Oben ist die Policy mit links als Stand-
bein und unten die Policy mit rechts als Standbein dargestellt. Zur
Unterteilung in doppelt und einfach belastete Phasen ist die Höhe des
jeweiligen Spielbeins in grün eingezeichnet. Die x- und y-Positionen
sind die Vorinitialisierung der Policy. Beim Wechsel des Standbeins
ändert sich die Nullposition des Oberkörpers um eine Schrittweite,
wodurch der Start und der Endpunkt der x-Policy den gleichen Ort im
Raum beschreiben.

Bein, dann wird das hintere Bein angehoben. Dieser Bewegungsablauf ist
durch die grüne Linie angedeutet. Der Oberkörper beﬁndet sich während-
dessen über dem Standbein. Das Spielbein wird dabei nach vorne gesetzt
und der Oberkörper abschließend wieder in die Mitte zwischen den beiden
Beinen bewegt.

Bei der Seitwärtsposition startet der Oberkörper ebenfalls in der Mitte
zwischen seinen Beinen, bewegt sich aber über das Schrittbein, um das
Gleichgewicht zu halten und bewegt sich am Ende wieder zurück.

47

5 Software

5.5 Policy Initialisierung

Abbildung 5.6: Minibot beim Austarieren seiner stabilen Position auf
einem Bein. Er bewegt dabei seinen Oberkörper langsam nach rechts
und hebt dabei das linke Bein, bis er die Position des Oberkörpers
gefunden hat, in der er das linke Bein beliebig anheben kann, ohne
umzufallen.

Um den Roboter beim anfänglichen Lernen nicht zu beschädigen, muss die
Policy initialisiert werden, z.B. wie in Abbildung 5.5. Es ist am einfachsten,
eine Startpolicy für ein sehr langsames Gehen zu deﬁnieren, da hier die
dynamischen Eﬀekte vernachlässigt werden können.

2

, Schrittweite
2

Für die Vorwärtsbewegung sind die obengenannten Positionen im Intervall
(cid:3) hinreichend. Da die Füße parallel zueinander sind,
(cid:2)− Schrittweite
ist die Stabilität eines stehenden Roboters für die Vorwärtsachse in der
Nullpose auch auf einem Bein gegeben. Die Seitwärtsbewegung hingegen
muss auf der Hardware exploriert werden, da im Allgemeinen nicht bekannt
ist, wann der Roboter auf einem Bein stehend zur Seite umkippt.

48

5 Software

Aus diesem Grund wurde eine Anwendung entwickelt, die den Oberkörper
des Roboters zur Seite bewegt, dann versucht ein Bein anzuheben und dabei
detektiert, ob der Roboter umkippt und entsprechend mit dem Oberkörper
gegensteuert. Diese Position wird dann zusammen mit der Schrittweite
genutzt, um die Policy zu initialisieren. Die Anfangsinitialisierung, die auf
dem Roboter Minibot errechnet wurde, ist in Abbildung 5.5 zu sehen.

Wenn der Laufalgorithmus bei hstart Prozent den Fuß anhebt, bei hende den
Fuß wieder auf den Boden setzt und ystabil die detektierte stabile Position
ist, lässt sich die initiale Policy für das linke Standbein durch die folgenden
Formeln darstellen. Das rechte Standbein folgt mit einem negativen ystabil
analog.

πx(phase) =

πy(phase) =









− Schrittweite
2

+ Schrittweite
2

· phase
hstart

für 0 ≤ phase ≤ hstart

0

Schrittweite
2

· phase−hende
(1−hende)

für hstart < phase ≤ hende

für hende < phase ≤ 100

ystabil · phase
hstart

ystabil
ystabil − ystabil · phase−hende
(1−hende)

für 0 ≤ phase ≤ hstart

für hstart < phase ≤ hende

für hende < phase ≤ 100

49

6 Evaluation

Im Folgenden werden die Ergebnisse des Ansatzes evaluiert. Hierbei wird
zuerst die Qualität der Sensoren getestet. Danach wird auf die durch die
Motoren entstehenden Einschränkungen eingegangen sowie die Versuche
erläutert, diese auf Softwareebene zu beheben. Anschließend werden die
verschiedenen Reinforcement Algorithmen miteinander verglichen.

6.1 Sensorgenauigkeit

Abbildung 6.1: Minibot beim Balancieren auf einem geneigten Unter-
grund. Insbesondere die Hüftmotoren sind stark geneigt, damit der
Roboter nicht nach hinten umkippt.

Um die Genauigkeit der Sensoren zu evaluieren, wurde ein einfacher Test
entwickelt. Hierfür wurde Minibot auf einen kippbaren Untergrund gestellt.
Ziel ist es nun, mithilfe der Sensoren und einem einfachen PID-Regler die
Winkel der Pitch-Motoren so zu steuern, dass sich der CoP in der Mitte des
Fußes beﬁndet. Die Zielwerte der Motoren sowie die Winkel der Motoren

50

6 Evaluation

Abbildung 6.2: Kraftverteilung und Motorwinkel während des Balancie-

rens auf einem geneigten Untergrund.

sind in Abbildung 6.2 zu sehen. Die Sprünge in der Kraftverteilung in den
Sekunden 2,9 und 16 sind durch ein schnelles Kippen des Untergrundes
zustande gekommen, während der Untergrund in den Sekunden von 22 bis
27 langsam geneigt wurde. Es ist bemerkenswert, dass obwohl sich die auf
den Sensoren anliegenden Kräfte während der Zeit deutlich unterscheiden,
die Gesamtsumme der Kräfte aber sehr konstant ist. Das Oszillieren des
Kraftunterschiedes zwischen den vorderen und den hinteren Sensoren kam
neben der ungenauen Steuerung mit dem PID-Regler insbesondere dadurch
zustande, dass die Daten mit dem ersten Protoypen des Fußes aufgenommen
wurde, der sehr nachgiebig war.

6.2 Hardwareeinschränkungen

Die eingesetzten Dynamixel Motoren haben deutlich Spiel in der Steuerung
und im Getriebe. Das Team Rhoban, das eine alternative Firmware für
die Motoren geschrieben hat, hat eine Abweichung von bis zu 8 Grad pro
Motor gemessen [Rhoban, 2017]. Während die vollen 8 Grad im Motor
im Rahmen der Versuche nicht gemessen wurden, waren jedoch 2,5 Grad
wie in Abbildung 6.3 die Regel. Allerdings ist die Richtung des Ausschlags
belastungsabhängig: Während das Bein belastet ist, wird der Zielwinkel
nicht erreicht. Unbelastetet hingegen überzieht der Motor. Da diese Abwei-
chungen von der Belastung abhängig sind, summieren sich die Fehler der
einzelnen Motoren auf. Zusätzlich gibt es noch eine Verformung in dem
tragenden Aluminiumskelett des Roboters, welche die Abweichung vom
Sollwert noch verstärkt.

51

6 Evaluation

Abbildung 6.3: Beispiel des Unterschiedes zwischen Zielwert und dem er-
reichtem Winkel des rechten Hüftmotors während des Gehens. Ein sehr
negativer Winkel des Motors bedeutet, dass der Oberkörper sich sehr
weit rechts beﬁndet und damit das Gewicht des Roboters hauptsächlich
auf dem rechten Bein lastet. Durch das hohe Gewicht des Roboters
arbeitet der Motor nicht ausreichend, um den Zielwinkel zu erreichen,
wodurch der Unterschied zwischen dem Ziel- und dem aktuellen Winkel
entsteht.

Dieses Problem mindert insbesondere die Seitwärtsstabilität des Roboters.
Die Beine sind bezogen auf die x-Achse in der Mitte des Roboters. Deswegen
führt eine Anhebung des einen Beines zwar dazu, dass das ganze Gewicht
des Roboters auf dem anderen Bein lastet, aber diese Last ist hauptsächlich
entlang der Achse des Beines. Bezogen auf die y-Achse sind die Beine sehr
weit am Rand des Roboters. Dieser Abstand der Motoren zum Mittelpunkt
führt für die einzeln belasteten Phasen in sehr kurzer Zeit zu einen sehr
hohen Drehmoment am Motor. Diesen Anstieg des Drehmoments kann
die Steuerung des Motors nicht ausgleichen. Deswegen zeigen insbesondere
die Roll-Motoren des Roboters die starken Abweichung und weniger die
Pitch-Motoren.

Dies führt dazu, dass der Roboter beim Laufen umkippt. Er versucht sich
stabil auf einem Bein zu halten und erreicht nach ein paar Lerndurchgängen
eine stabile Position für die einzeln belastete Phase. Hierbei entstehen
zwei Probleme. Erstens: Wenn er nun das andere Bein senkt, dann triﬀt

52

6 Evaluation

der Fuß mit relativ hoher Geschwindigkeit auf den Boden und gibt dem
Roboter dadurch einen Stoß. Dieser Stoß führt dazu, dass der Roboter
sein Gleichgewicht verliert und umkippt. Zweitens: Wenn der Roboter
eine stabile Position erreicht hat, wirkt die Hebelkraft der Gravitation am
Motor schlagartig in die andere Richtung. Die Position des Motors kann
sich dann sprunghaft verändern.

Ein erster Ansatz, diese Probleme zu beheben, war es, den Zielwert der
Motorwinkel zu korrigieren. Dafür wurde über verschiedene Schritte die
Abweichung errechnet, um dann entsprechend das Ziel anzupassen, wie in
Abbildung 6.4 zu sehen. Dadurch entstand allerdings eine hohe Varianz
in den Zielwerten der Motoren, was zu einer vermehrten Oszillation des
ganzen Roboters führte. Durch diese Oszillation und die Varianz wurde
der Roboter sehr instabil. Außerdem hat der Algorithmus bei 70,25 s nicht
ausreichend und bei 71 s hingegen zu viel gegengesteuert. Während der
Ansatz also meist richtig gegensteuert, führten die Fehlstellen und die
erhöhte Oszillation dazu, dass der Ansatz die Stabilität kaum verbesserte.

Abbildung 6.4: Ausschnitt aus einem Versuch, den Oﬀset der Motoren
durch ein übergeordnetes Steuersystem zu beheben. Hierbei wurden
die Abweichungen der vorherigen Durchgänge als Grundlage der kor-
rigierten Zielwerte genutzt. Die Abweichungen des Ist-Winkels vom
Ziel-Winkel war in diesem Fall aber nicht wiederholbar genug, um diese
Abweichung so sinnvoll auszugleichen.

53

6 Evaluation

Ein zweiter Ansatz, das Problem des Zusammenstoßes mit dem Boden zu
beheben, entsprach dem Versuch, die aktuelle Abweichung der Ist-Position
zu berechnen und diese bei der Soll-Position zu beachten. Die Berechnung
der aktuellen Position ist über die direkte Kinematik errechenbar, allerdings
ist es schwierig diese Information zu nutzen. Es ist nicht möglich, die
Zielposition des Standbeins auf die Realposition zu ändern, in diesem Fall
würde eine andere Zielposition den Motoren übergeben werden, wodurch
diese weiter nachgeben und noch weiter entfernt von der ursprünglichen
Zielposition wären. Es ist also nur möglich, die Zielposition des Spielbeins
soweit anzupassen, dass sie sich nicht unterhalb der aktuellen Position des
Standbeins beﬁndet, um den oben genannten Stoß zu vermeiden. Allerdings
führt das Spiel in den Motoren im Spielbein dazu, dass ein leichter Impuls
kaum verhinderbar ist. Dieser Impuls führt zu Nachregelungen in den
Motoren, sodass auch dieser Ansatz nicht ausreicht, zu verhindern, dass
der Roboter umkippt.

Auch ein weiteres Optimieren des PID-Reglers führt nicht zum gewünsch-
ten Erfolg. Der I-Anteil des Reglers ist nicht vollständig dokumentiert.
Insbesondere lässt sich der Integrationspart nicht aktiv zurücksetzen und es
wirkt so, als ob der Motor ihn auch bei ausgeschaltetem I-Regler berechnet.
Durch die ständige Berechnung ist der I-Regler bei Aktivierung in einem
fehlerhaften Zustand, wodurch der Motor unkontrollierbare Bewegungen
ausführt. Auch ein ständig aktivierter I-Regler führt zu keinem positiven
Ergebnis, da die starke Belastungsphase im Vergleich zu den anderen Pha-
sen relativ kurz ist. Ein Verstärken des P-Glieds ist auch problematisch,
da der Roboter dann zu oszillieren beginnt.

Ebenso reduzierte ein Umbau von Minibot mit stärkeren Motoren die
Abweichungen vom Sollwert nur wenig. Dies verdeutlicht, dass das Problem
hauptsächlich in der Ansteuerung innerhalb der Motoren liegt und nicht
durch fehlende Kraft in den Motoren entsteht. Am geeignetsten wäre
deshalb ein Korrigieren dieser Abweichungen innerhalb der eigentlichen
Motorsteuerung und nicht auf einer höheren Software-Ebene. Die Firmware
der Motoren ist allerdings nicht veröﬀentlicht worden und daher nicht
anpassbar.

54

6 Evaluation

6.3 Gelernte Policy

Im Folgenden wird für die angewendeten Strategien die jeweils gelernte
Policy erklärt und die Vor- und Nachteile des Ansatzes diskutiert. Nach
Morimoto et al. können die Sagittalachse (x-Achse) und die Lateralachse
(y-Achse) unabhängig voneinander gelernt werden [Morimoto et al., 2005].
Dies ermöglicht, dass im ersten Ansatz des Finite Diﬀerence Policy Gradient
ausschließlich die x-Achse gelernt wird und erst in den späteren Ansätzen
auch die y-Achse.

6.3.1 Finite Diﬀerence Policy Gradient

Abbildung 6.5: Gelernte Policy mit der Finite Diﬀerence Methode. Zur
Unterteilung in doppelt und einfach belastete Phase ist die Höhe des
jeweiligen Spielbeins in grün eingezeichnet. In schwarz ist die gelernte
Policy visualisiert.

In Abbildung 6.5 ist die Visualisierung der gelernten Policy für die Finite
Diﬀerence Methode abgebildet. Der Gradient wurde evaluiert, sobald für
den Tile fünf mal Feedback vorlag. Die Abweichungen δΘ für das Lernen
entstammten aus der Gleichverteilung [−0.0025,0.0025].

Es ist keine sinnvolle Lerntendenz in Abbildung 6.5 sichtbar, obwohl der
Roboter beim Laufen deutlich nach hinten geneigt war. Auch führen die
gelernten Sprünge zu einem instabilen Laufen, da die Motoren entsprechend
stark ihren Torque verändern.

Während es verbesserte Blackboxabschätzungen des Gradienten wie REIN-
FORCE von Williams [Williams, 1992] gibt, die vermutlich besser abschnei-
den würden, scheint die Variabilität des Roboters bei aufeinanderfolgenden

55

6 Evaluation

Schritten zu stark für Blackboxabschätzungen des Gradienten zu sein. Da
es mit der Abweichung des ZMP vom Zielwert auch eine direkte Abschät-
zung des Gradienten gibt, wurden keine weiteren Blackboxabschätzungen
implementiert.

6.3.2 TD(λ)

Die Finite Diﬀerence Methode zeigt zwei deutliche Probleme. Neben der
oben genannten Schwäche von Blackbox-Gradientenabschätzungen, die
durch den ZMP abgelöst wurde, ist auch die hohe Varianz der Policy
ein Problem: Die einzelne Auswertung jedes Tiles führt zu Sprüngen in
der Policy. Diese Sprünge verursachen sprunghafte Bewegungen in den
Motoren, die deutlich schlechter steuerbar und sehr viel ungenauer sind.
Eine gleichmäßigere Policy ist deutlich vorteilhafter. Der Einﬂuss der
zukünftigen Zustände in dem TD(λ) Ansatz ermöglicht eine gleichmäßigere
Policy. In Abbildung 6.6 ist die gelernte Policy mit TD(λ) und dem ZMP
als Gradientenabschätzung zu sehen, λ hatte beim Lernen den Wert 0.2
und n den Wert 10.

Beim Lernen brach ein Sensor, was während des Versuches nicht bemerkt
wurde. Dieser gebrochene Sensor wurde nur belastet, wenn das andere
Bein angehoben wurde. Der Bruch führte zum Sprung in der Policy bei
75%. Während die grundsätzliche Policy nun nicht mehr die unerwünschten
Schwankungen hat, kann es immer noch zu Sprüngen führen, die für die
Stabilität des Ganges ebenfalls massive Nachteile haben.

Abbildung 6.6: Gelernte Policy mit TD(λ). Zur Unterteilung in doppelt
und einfach belastete Phase ist die Höhe des jeweiligen Spielbeins in
grün eingezeichnet. In schwarz ist die x-Position der Policy und in rot
die y-Position eingezeichnet.

56

6 Evaluation

Abbildung 6.7: Gelernte Policy mit TD(λ) und Gauß-Filter. Obwohl
die Policy vom linken und rechten Standbein im Optimalfall nahezu
gespiegelt sind, bestehen genug kleine Unterschiede, die dazu führen,
dass es sinnvoll ist, sie getrennt voneinander zu lernen.

6.3.3 TD(λ) mit Gauß-Filter

Um die Sprünge in der gelernten Policy zu vermeiden, lässt sich das Feed-
back mithilfe eines Gauß-Filters glätten. Das Strecken des Feedbacks über
viele Tiles ermöglicht das Feedback-Signal besonders auf die einzeln be-
lasteten Phasen zu optimieren. Der Roboter steht deutlich stabiler in der
doppelt belasteten Phase, da die konvexe Hülle der beiden Füße zusammen
deutlich größer als die eines Fußes ist. Da der Oberkörper sich immer in
Bewegungsrichtung bewegt, verschiebt sich auch der ZMP während des
Schrittes in Bewegungsrichtung. Da am Ende des vorherigen Schrittes
sich der ZMP in der Mitte des hinteren Fußes beﬁndet und der ZMP von
diesem Punkt aus sich in Bewegungsrichtung mit bewegt, reicht es nun,
ausschließlich Feedback zu geben, wenn der ZMP über den Mittelpunkt des
vorderen Fußes hinausgeht. Der Rest der Zieltrajektorie wird über TD(λ)
und dem Gauß-Filter deﬁniert.

57

6 Evaluation

Die gelernte Policy mit TD(λ) und Gauß-Filter ist in Abbildung 6.7 zu
sehen. Bei dem Versuch gab es 200 Tiles pro Standbein. Die Breite σ war
mit 70 sehr groß, um eine möglichst gleichmäßige Bewegung zu erreichen,
wobei die Breite des Einﬂusses zusätzlich auf 150 Tiles beschränkt war.
Die y-Policy ist nur begrenzt aussagekräftig, da der Roboter aufgrund
der Hardwareprobleme gleichwohl umfällt, wenn er nicht gestützt wird.
Die x-Policy zeigt eine Verschiebung der Kurve in den negativen Bereich,
der Roboter scheint also beim Laufen eine Neigung nach vorne zu haben.
Das Feedback erreichte nach der anfänglichen Verschiebung ihr Minimum
und die x-Policy veränderte sich anschließend kaum. Das dazugehörige
aufsummierte Reward-Signal ist in Tabelle 6.1 zu sehen. Insbesondere
die x-Policy des linken Fußes ist bereits nach acht Schritten in einem
vergleichsweise stabilen Gang. Die x-Policy mit dem rechten Standbein
bekommt bereits anfänglich einen schlechteren Reward, verbessert sich
aber ebenfalls deutlich über die Zeit. Die Schwankungen in den Motoren
führen dazu, dass der Algorithmus bei der y-Policy nicht in der Lage ist,
den Reward signiﬁkant zu verbessern.

Der ZMP unter dem linken Fuß während eines Schrittes ist in Abbildung 6.8
eingezeichnet. Da das Gewicht des Roboters nur während der einzeln
belasteten Phase vollständig auf dem linken Bein lastet, ist hier der ZMP
besonders relevant. Diese Phase ist auch am kritischsten bezüglich der
Stabilität. Der ZMP war hier im Bereich von ±15% vom Fußmittelpunkt
entfernt — ein solcher Unterschied entsteht bereits durch das ungenaue
Stützen des Roboters.

Da der Roboter nicht exakt symmetrisch ist, gibt es Unterschiede in den
gelernten Policys. Diese Unterschiede sind in Abbildung 6.9 dargestellt.
Die gelernten Policys der y-Achse unterscheiden sich nicht besonders stark,
da es softwareseitig eine Begrenzung der maximalen Veränderung pro
Schritt gibt, die regelmäßig von dem Algorithmus erreicht wird. Bei der
x-Policy hingegen ist ein Unterschied zwischen der linken und der rechten
Policy sichtbar, während das Plateau der Position des Roboters über dem
Standbein beim rechten Fuß bei −0.035 m ist, beﬁndet sich das Plateau
bei −0.015 m. Der Unterschied entsteht unter anderem dadurch, dass die
Nullpositionen der Motoren nicht exakt gleich sind. Deswegen ist der
Oberkörper des Roboters bei gleicher Zielstellung entsprechend leicht anders
gekippt und dadurch das Gewicht anders verteilt.

58

6 Evaluation

Linker Fuß x-Reward

Linker Fuß y-Reward

0.1391

0.1324

0.1184

0.0864

0.1109

0.0896

0.0715

0.0406

0.2254

0.2585

0.2659

0.2186

0.2674

0.2679

0.1747

0.3412

Rechter Fuß x-Reward Rechter Fuß y-Reward

0.2352

0.2354

0.2062

0.1724

0.1562

0.1560

0.1366

0.1367

0.2277

0.2540

0.2742

0.2535

0.2566

0.2710

0.2675

0.2464

Schritt 1

Schritt 2

Schritt 3

Schritt 4

Schritt 5

Schritt 6

Schritt 7

Schritt 8

Schritt 1

Schritt 2

Schritt 3

Schritt 4

Schritt 5

Schritt 6

Schritt 7

Schritt 8

Tabelle 6.1: Der durchschnittliche Reward für das linke und rechte Stand-
bein. Da die Updatefrequenz der Motoren und davon abhängig die
Menge an Feedback pro Schritt nicht konstant ist, ist der Durchschnitt
des Reward aussagekräftiger als die Summe. Der Reward ist dabei ein
Fehlerwert, der perfekte Reward wäre null. Während der Fehlerwert
der x-Policy am konvergieren ist, führen die Probleme der Motoren
zusammen mit dem Stützen des Roboters dazu, dass die y-Policy nicht
konvergiert.

59

6 Evaluation

Abbildung 6.8: ZMP des linken Fußes auf der x-Achse. Die Länge des
Fußes ist 0.14 m, deshalb ist die Höhe des Plots ±0.07 m. Die Position
des ZMP unter dem linken Fuß während der doppelt belasteten Phase
— wenn die Höhe des rechten Fußes gleich 0 ist – deﬁniert nur kaum
die Stabilität des Roboters, da die Last auf dem rechten Fuß ebenfalls
relevant ist. Während der kritischen einzeln belasteten Phase liegt der
ZMP im ±0.01 m.

Abbildung 6.9: Vergleich der linken und rechten Policy jeweils während
des Schrittes 8. Damit der Unterschied besser sichtbar wird, ist die
y-Policy mit rechten Standbein horizontal gespiegelt.

60

6.3.4 Veränderungen der Policy beim Lernen

6 Evaluation

Abbildung 6.10: Ausgeführte Policy mit TD(λ) und Gauß-Filter über
mehrere Schritte. Oben ist die x-Policy unten ist die y-Policy jeweils für
das linke Standbein visualisiert. Die starken Steigungen in der Mitte
der jeweiligen Policy sind Artefakte des Lernens und bedeuten, dass
der Lernalgorithmus noch nicht konvergiert ist.

In Abbildung 6.10 sind die Zielpositionen des Oberkörpers während mehre-
rer Schritte vom TD(λ) mit Gauß-Filter eingezeichnet. Schon während des
ersten Schrittes bekommt der Algorithmus genug Feedback um die Policy
zu verbessern. Die starken Steigungen in der Mitte der jeweiligen Bewe-
gung entstehen dadurch, dass der Lernalgorithmus bereits in der Mitte des
Schrittes genug Feedback bekommen hat, um zu lernen. Dieses Lernsignal
verändert über den Gauß-Filter auch den Wert der Tiles, die während
dieses Schrittes noch nicht angewendet wurden. Diese Online Veränderung
der Policy während ihrer Ausführung führt zu dem sichtbaren Artefakt
und entsteht nur, wenn die Policy durch das Lernsignal stark verändert
wird. Der Roboter ist dann nicht in einem stabilen Gang und es besteht die
Gefahr, dass der Roboter entgegen der Richtung des Artefaktes umkippt.
Um die Artefakte zu vermeiden, wäre es möglich, immer erst am Ende eines
Schrittes und dann für den Schritt als Episode und nicht kontinuierlich

61

6 Evaluation

zu lernen. Die y-Policy wurde nicht mit der Position aus der Austarie-
rung sondern mit einer niedrigeren Zielposition vorinitialisiert, wodurch
die deutliche Steigerung der maximalen y-Position zustande kommt.

6.3.5 Seitwärtstrajektorie

Abbildung 6.11: Minibot während eines Schrittes. Das Testsetup mit den
drei verklebten Apriltags ist deutlich erkennbar, mit dessen Hilfe die
realen Positionen des Oberkörpers und der Beine zueinander gemessen
wurden. Besonders ab dem Bild unten links geben die Motoren des
Roboters beim Anheben des rechten Beins nach, wodurch der Roboter
sich nach rechts neigt. Dies entspricht den starken Abweichungen der
realen von der Zielposition in Abbildung 6.12.

62

6 Evaluation

Die ausgeführte Seitwärtstrajektorie während des Gehens ist in Abbil-
dung 6.12 zu sehen. Die in rot eingezeichnete y-Zielposition ist die ausge-
führte Policy, die von der inversen Kinematik in die Motorwinkel übersetzt
wird. Die Zielwinkel der Motoren unterscheiden sich von den real angefah-
renen. Die Position des Oberkörpers wird aus den Motorpositionen mithilfe
der direkten Kinematik berechnet und ist in grün visualisiert. Während
des Gehens wurden mithilfe von Markern die realen Positionen des Ober-
körpers gemessen. Der Versuchsaufbau von den Aufnahmen von Minibot
beim Laufen ist in Abbildung 6.11 dargestellt. Die verklebten Marker
sind von einer Bildverarbeitung gut erkennbare „Apriltags“, die für das
Detektieren von Positionen im Raum entwickelt worden sind [Olson, 2011].
Die unter den Füßen wirkenden Kräfte in Abhängigkeit der Zielposition
sind in Abbildung 6.13 eingezeichnet.

Während der doppelt belasteten Phasen, bei denen in Abbildung 6.12
keine Fußpositionen eingezeichnet sind, ist die ausgeführte Trajektorie
relativ genau. Innerhalb der einzeln belasteten Phase, zu den Zeitpunkten
sind die gelben Fußpositionen eingezeichnet, knickt der Roboter ein und
die Position des Oberkörpers bewegt sich schnell und stark zur Mitte.
Über weite Zeitspannen sind die gemessene und die über die Odometrie
berechneten Positionen sehr ähnlich, einen Großteil der Abweichungen
erkennen die Motoren also selber. Ob die Abweichungen zwischen der
gemessenen und durch die Odometrie berechneten Trajektorie in den
Sekunden bis 82, 90 bis 92 und ab 99 Ungenauigkeiten in der Positionierung
und Detektion der Apriltags sind oder durch ungenaue Kodierung der
aktuellen Motorpositionen entstehen, ist nicht ersichtlich.

63

6 Evaluation

Abbildung 6.12: Ausgeführte Seitwärtstrajektorie der Schritte 7 und 8
aus der Abbildung 6.10. In gelb ist die Position des jeweiligen Stand-
beines eingezeichnet. Die Positionsangaben sind immer im Bezug zum
Standbein, damit die Odometrie und die gemessenen Positionen ver-
gleichbar sind. Die messbare Rotation des Fußes ist nicht dargestellt.

64

6 Evaluation

Abbildung 6.13: Entstehende Kräfte während des Gehens. Oben sind
die Kräfte an den Kraftsensoren unter dem linken und unten die unter
dem rechten Fußes eingezeichnet. Die wichtigsten Zielpositionen des
Roboters sind in der Mitte visualisiert. Der Roboter wurde während des
Gehens gestützt, wodurch nicht immer das ganze Gewicht des Roboters
auf den Sensoren lastete.

65

-10 0 10 20 30 40 50 60 85 90 95 100 105Kraft [N]Kräfte am linken FußVorne LinksVorne RechtsHinten LinksHinten RechtsSumme linker FußSumme-0.1-0.05 0 0.05 0.1 0.15 85 90 95 100 105Position in mPositionen des RobotersY-ZielpositionX-ZielpositionHöhe linker FußHöhe rechter Fuß-10 0 10 20 30 40 50 60 85 90 95 100 105Kraft [N]Kräfte am rechten FußVorne LinksVorne RechtsHinten LinksHinten RechtsSumme rechter FußSumme gesamt6 Evaluation

6.4 Portierbarkeit

Der Algorithmus ist mit dem Ziel entwickelt worden, möglichst leicht auf
andere Plattformen portiert werden zu können, deswegen sollte möglichst
wenig angepasst und für die neue Plattform ausschließlich eine inverse
Kinematik implementiert werden.

Insbesondere durch die Integration in ROS ist der Algorithmus leicht auf
viele Roboterplattformen portierbar, da es mit beispielsweise KDL oder
IKFast Implementationen für eine inverse Kinematik gibt, die leicht auf
verschiedene Plattformen anwendbar sind. Allerdings muss sich die Abfolge
der Motorwinkel bei gleicher Trajektorie wiederholen, diese Anforderung
wird nicht von allen numerischen Näherungsalgorithmen erfüllt. Neben
der inversen Kinematik müssen zum Portieren nur vergleichsweise wenige
Einstellungen angepasst werden:

Höhe des Ober-
körpers

Durch diese Einstellung wird bestimmt, inwieweit der
Roboter beim Laufen in die Knie geht.

Zcom

Die Position des Schwerpunktes auf der z-Achse. Zcom
ist leicht ausmessbar.

Schrittgeschwin-
digkeit

Sollte nach Gleichung 2.1 mit der natürliche Frequenz
des Pendels der Länge Zcom korrelieren.

Schrittlänge

Dieser Parameter bestimmt die Grundlänge eines
Schrittes. Während des Gehens ist die tatsächliche
Schrittlänge ein in Abhängigkeit der Zielgeschwindig-
keit Vielfaches dieser Grundlänge.

Geschwindig-
keitsstufen

66

die Geschwindigkeitsstufen wird

die
Durch
gesteuert.
Endgeschwindigkeit
Zur Zeit
ist die maximale Geschwindigkeit:
Geschwindigkeitsstuf en · Schrittgeschwindigkeit
· Schrittlänge.

Roboters

des

6 Evaluation

Schritthöhe

Die Höhe des Fußes am höchsten Punkt der Bewe-
gung.

Belastungs-
phasen

Das Verhältnis der Belastungsphasen, also den ein-
fachen und doppelt belasteten Phasen. Die vorein-
gestellten Werte sollten im Allgemeinen ausreichend
sein.

Fuß-Trajektorie Hierüber kann insbesondere eingestellt werden, wie
hoch der Fuß bereits gehoben sein muss, bevor er
nach vorne bewegt werden kann. Die voreingestellten
Werte sollten im Allgemeinen ausreichend sein.

Lern-Faktoren

Die Lern-Faktoren, wie λ des TD(λ), entscheiden über
die Konvergenzgeschwindigkeit. Die voreingestellten
Werte sollten im Allgemeinen ausreichend sein.

Keine der oben genannten Eigenschaften muss aufwendig durch Ausprobie-
ren optimiert werden, was einen signiﬁkanten Unterschied zu allen bekann-
ten Algorithmen darstellt. Die Lern-Faktoren sind direkt mit dem Feedback
des Reinforcement Learnings verbunden. Die aktuelle Position des ZMP
wird in der Vorverarbeitung auf den Bereich −1 bis +1 normiert. Durch
diese Normierung wird auf unterschiedlichen Robotern der Algorithmus
mit den gleichen Faktoren ähnlich gut konvergieren. Die Fuß-Trajektorie
ist insbesondere im RoboCup relevant, da der Rasen unterschiedlich hoch
sein kann. Bei besonders hohen Halmen des Rasens muss sich der Fuß
daher anders bewegen, um sich nicht zu verhaken. Dieser Faktor hat aber
auf normalem Untergrund einen geringen Einﬂuss auf die Stabilität des
Roboters.

Nicht trivial ist einzig das Verhältnis der Belastungsphasen, also die re-
lative Zeit, die sich der Roboter auf einem bzw. beiden Beinen beﬁndet.
Hier sollten aber im Allgemeinen die voreingestellten Werte einen guten
Richtwert liefern.

Die restlichen Konﬁgurationen sind (mit Ausnahme des messbaren Zcom)
Designentscheidungen des Entwicklers, die relativ frei gewählt werden
können.

67

6 Evaluation

Auch die Anforderung einer inversen Kinematik ist wenig problematisch,
da kaum ein Roboter ausschließlich gehen können soll. Für viele der ande-
ren Aufgaben des Roboters, wie im RoboCup das Schießen oder andere
Ganzkörperbewegungen, wird ebenfalls eine inverse Kinematik benötigt.

68

7 Zusammenfassung und

Ausblick

7.1 Zusammenfassung

Im Rahmen der Masterarbeit wurde ein neuer Algorithmus entwickelt, der
mithilfe von Kraftsensoren die Steuerung des Oberkörpers beim Gehen
lernt. Er benötigt dabei, im Gegensatz zu den bekannten Algorithmen,
keine aufwendigen Simulationen, ist gleichzeitig aber leicht portierbar.

Während die genutzte Plattform Schwächen zeigt — insbesondere bezüglich
der Seitwärtsstabilität — wurde die Vorwärtsbewegung durch das Lernen
deutlich stabilisiert. Dabei funktioniert die Repräsentation anschließend
auch ohne Kraftsensoren. Dies lässt die Möglichkeit oﬀen, die Sensoren zu
deaktivieren, wenn sie beschädigt sind oder unrealistische Werte liefern —
z.B. weil der Lichtschutz des Sensors das Infrarotlicht der Umgebung nicht
vollständig blockiert.

Mit dem Algorithmus wurde ein Ansatz erprobt, der die Grundbewegung
des Roboters optimiert und dabei den Einsatz übergeordneter Stabilisatoren
ermöglicht, solange der Roboter stabile Phasen hat. Wenn das System nur
selten aus dem Gleichgewicht gerät, lassen sich alle bekannten Stabilisatoren
anwenden, z.B. Strategien auf Basis von Capture-Points [Pratt et al., 2006]
oder die Algorithmen von Yi et al. [Yi et al., 2011]. Auch ein PID-Regler ist
implementierbar. Dieser modiﬁziert die Zielposition des Oberkörpers, wenn
der ZMP sich außerhalb eines Toleranzbereichs beﬁndet. Allerdings muss,
nachdem der Stabilisator eingegriﬀen hat, im Allgemeinen das Lernen kurz
ausgesetzt werden, damit keine fehlerhaften Werte erlernt werden.

Durch die leichte Portierbarkeit der implementierten Software und ihre
Integration in ROS besteht die Möglichkeit, dass die Software schnell und
eﬀektiv auch auf anderen Robotern eingesetzt werden kann, solange es eine
inverse Kinematik und Kraftsensoren gibt.

69

7 Zusammenfassung und Ausblick

7.2 Ausblick

Um ein stabiles Laufen der Roboter zu ermöglichen, muss evaluiert werden,
wie die genutzte Hardware stabilisiert werden kann. Dies erfordert aber
wahrscheinlich tiefergehende Veränderungen an den Roboterplattformen.
Eine Möglichkeit ist ein zusätzliches Zahnrad, damit die Motoren mehr
Torque produzieren und dabei weniger Spiel haben, wie es beispielsweise
von dem iranischen Team Baset für ihren Adult-Size Roboter umgesetzt
worden ist [Hosseini et al., 2016].

Eine mögliche Softwarelösung ist die alternative Firmware „Dynaban“ vom
französichen Team Rhoban [Rhoban, 2017], bei der die Möglichkeit besteht,
nicht nur aktuelle Positionen anzugeben, sondern eine Trajektorie, die von
den Motoren angefahren werden soll. Dieses Feature ist allerdings bislang
noch nicht ausführlich getestet worden.

Neben der Motorproblematik wäre es sinnvoll die Prototyp-Platinen gegen
die professionell hergestellten PCB-Platinen zu tauschen, bei denen jedoch
die noch bestehenden Fehler behoben werden müssten.

Schließlich sollte ein funktionierender Stabilisator auf Basis der Kraftsenso-
ren implementiert werden. Wenn die angesprochenen Aufgaben umgesetzt
worden sind, kann der implementierte Algorithmus in der nächsten Robo-
Cup Weltmeisterschaft in Nagoya eingesetzt werden. Dies wird zu einem
stabileren Gehen führen.

70

Literaturverzeichnis

[Arakawa and Fukuda, 1997] Arakawa, T. and Fukuda, T. (1997). Natural
motion generation of biped locomotion robot using hierarchical trajec-
tory generation method consisting of ga, ep layers. In Robotics and
Automation, 1997. Proceedings., 1997 IEEE International Conference
on, volume 1.

[Bennett, 1984] Bennett, S. (1984). Nicholas minorsky and the automatic

steering of ships. IEEE Control Systems Magazine.

[Bernstein, 2012] Bernstein, H. (2012). Elektrotechnik/Elektronik für Ma-
schinenbauer : Grundlagen und Anwendungen. Vieweg+Teubner Verlag.

[Bestmann, 2016] Bestmann, M. (2016). Towards Using the Robot Opera-
ting System in RoboCup Humanoid League. Master’s thesis, Universität
Hamburg.

[Bestmann et al., 2015] Bestmann, M., Reichardt, B., and Wasserfall, F.
(2015). Hambot: An open source robot for robocup soccer. In RoboCup
2015: Robot World Cup XIX on RoboCup 2015: Robot World Cup XIX -
Volume 9513, New York, NY, USA. Springer-Verlag New York, Inc.

[Brown, 2017] Brown, A. (Retrieved: 03.01.2017). Stm32plus-framework.

https://github.com/andysworkshop/stm32plus.

[Dasgupta and Nakamura, 1999] Dasgupta, A. and Nakamura, Y. (1999).
Making feasible walking motion of humanoid robots from human motion
capture data. In Robotics and Automation, 1999. Proceedings. 1999
IEEE International Conference on, volume 2.

[Debrunner, 2002] Debrunner, A. (2002). Orthopädie. Orthopädische Chir-
urgie. Patientenorientierte Diagnostik und Therapie des Bewegungsap-
parates. Bern, Göttingen, Toronto.

[Deisenroth et al., 2013] Deisenroth, M. P., Neumann, G., and Peters, J.
(2013). A survey on policy search for robotics. Foundations and Trends R(cid:13)
in Robotics, 2.

71

Literaturverzeichnis

[Everlight Electronics, 2010] Everlight Electronics (2010). Datenblatt des
everlight itr8307. http://www.everlight.com/ﬁle/ProductFile/ITR8307.
pdf. Retrieved 2016-10-23.

[Fraden, 2010] Fraden, J. (2010). Handbook of modern sensors, volume 3.

Springer.

[Goswami, 1999] Goswami, A. (1999). Postural stability of biped robots
and the foot-rotation indicator (fri) point. The International Journal of
Robotics Research, 18.

[Goswami, 2015] Goswami, A. (2015). Walking Robots. Springer London,

London.

[Ha et al., 2013] Ha, I., Tamura, Y., and Asama, H. (2013). Development
of open platform humanoid robot darwin-op. Advanced Robotics, 27.

[Harada et al., 2003] Harada, K., Kajita, S., Kaneko, K., and Hirukawa,

H. (2003). Zmp analysis for arm/leg coordination. In IROS.

[Hosseini et al., 2016] Hosseini, M., Mohammadi, V., Jafari, F., and Bam-
dad, E. (2016). Baset adult - size 2016 team description paper. In Robot
Soccer World Cup. Springer.

[Hu et al., 2016] Hu, Y., Eljaik, J., Stein, K., Nori, F., and Mombaur, K.
(2016). Walking of the icub humanoid robot in diﬀerent scenarios:
Implementation and performance analysis. In 2016 IEEE-RAS 16th
International Conference on Humanoid Robots (Humanoids).

[Juricic and Vukobratovic, 1972] Juricic, D. and Vukobratovic, M. (1972).
Mathematical modeling of biped walking systems. ASME Publication.

[Lau, 2004] Lau, D. (2004). Algebra und Diskrete Mathematik 2. Springer

Spektrum.

[Metta et al., 2008] Metta, G., Sandini, G., Vernon, D., Natale, L., and Nori,
F. (2008). The icub humanoid robot: An open platform for research in
embodied cognition. In Proceedings of the 8th Workshop on Performance
Metrics for Intelligent Systems, PerMIS ’08, New York, NY, USA. ACM.

[Missura, 2005] Missura, M. (2005). Analytic and Learned Footstep Control
for Robust Bipedal Walking. PhD thesis, Rheinischen Friedrich-Wilhelms-
Universität Bonn.

72

Literaturverzeichnis

[Moilanen and Vadén, 2013] Moilanen, J. and Vadén, T. (2013). 3d prin-
ting community and emerging practices of peer production. First Mon-
day.

[Morimoto et al., 2005] Morimoto, J., Nakanishi, J., Endo, G., Cheng, G.,
Atkeson, C. G., and Zeglin, G. (2005). Poincare-map-based reinforcement
learning for biped walking. In Proceedings of the 2005 IEEE International
Conference on Robotics and Automation.

[NuBots, 2017] NuBots (Retrieved: 03.01.2017). Github page. https:

//github.com/NUbots/NUbots.

[Olson, 2011] Olson, E. (2011). Apriltag: A robust and ﬂexible visual
ﬁducial system. In 2011 IEEE International Conference on Robotics
and Automation.

[Peters et al., 2003] Peters, J., Vijayakumar, S., and Schaal, S. (2003). Rein-
forcement learning for humanoid robotics. In Proceedings of the third
IEEE-RAS international conference on humanoid robots.

[PJRC, 2010] PJRC (2010). Die Dokumentation des Teensy 3.2. https:

//www.pjrc.com/store/teensy32.html. Retrieved 2016-10-23.

[Pratt et al., 2006] Pratt, J., Carﬀ, J., Drakunov, S., and Goswami, A.
(2006). Capture point: A step toward humanoid push recovery. In 2006
6th IEEE-RAS International Conference on Humanoid Robots.

[Radi, 2013] Radi, H. A. (2013). Principles of Physics: For Scientists and

Engineers. Springer, Berlin Heidelberg.

[Rhoban, 2009] Rhoban (2009). Rhobans IKWalker. https://github.com/

Rhoban/IKWalk. Retrieved 2017-01-13.

[Rhoban, 2017] Rhoban (Abgerufen am: 31.01.2017). Dynaban README.

https://github.com/RhobanProject/Dynaban.

[RoboCup Federation, 2017] RoboCup Federation (2017). A brief history
of robocup. http://robocup.org/a_brief_history_of_robocup. Retrie-
ved 03.02.2017.

[Robotis, 2017] Robotis (Aberufen am: 07.02.2017). Dokumentation der
Motoren, PID-Regler. http://support.robotis.com/en/product/actuator/
dynamixel/mx_series/mx-106.htm#Actuator_Address_1A.

73

Literaturverzeichnis

[Saputra et al., 2015] Saputra, A. A., Khalilullah, A. S., and Kubota, N.
(2015). Development of Humanoid Robot Locomotion Based on Biologi-
cal Approach in EEPIS Robot Soccer (EROS). Springer International
Publishing, Cham.

[Sardain and Bessonnet, 2004] Sardain, P. and Bessonnet, G.

(2004).
Forces acting on a biped robot. center of pressure-zero moment point.
IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems
and Humans, 34.

[Schmidt, 2015] Schmidt, R. (2015). Development of a stable robot walking
algorithm using center-of-gravity control. Master’s thesis, University of
Hamburg.

[Siciliano and Khatib, 2008] Siciliano, B. and Khatib, O., editors (2008).

Springer Handbook of Robotics. Springer.

[Siciliano et al., 2008] Siciliano, B., Sciavicco, L., Villani, L., and Oriolo, G.
(2008). Robotics: Modelling, Planning and Control. Springer Publishing
Company, Incorporated, 1st edition.

[Song, 2010] Song, S. (2010). Development of an Omni-directional Gait
Generator and a Stabilization Feedback Controller for Humanoid Robots.
Master’s thesis, Virginia Polytechnic Institute and State University.

[Song et al., 2011] Song, S., Ryoo, and DW, H. (2011). Development of
an omnidirectional walking engine for full-sized lightweight humanoid
robots. In 35th Mechanisms and Robotics Conference., volume Volume
6.

[Sutton and Barto, 1998] Sutton, R. S. and Barto, A. G. (1998). Introduc-
tion to Reinforcement Learning. MIT Press, Cambridge, MA, USA, 1st
edition.

[Swierzewski, 2017] Swierzewski

(Retrieved:

03.01.2017).

www.

healthcommunities.com/foot-anatomy/muscles-tendons-ligaments.
shtml.

[Takanishi et al., 1990] Takanishi, A., Takeya, T., Karaki, H., and Kato, I.
(1990). A control method for dynamic biped walking under unknown
external force. In Intelligent Robots and Systems 90. Towards a New
Frontier of Applications, Proceedings. IROS 90. IEEE International
Workshop on, volume 2.

74

Literaturverzeichnis

[Team-Darwin, 2017] Team-Darwin (Retrieved: 27.01.2017).

https://

github.com/UPenn-RoboCup/UPennalizers.

[Team Nimbro, 2009] Team Nimbro (2009). Code release. https://github.

com/NimbRo/nimbro-op-ros. Retrieved 03.02.2017.

[Tedrake, 2004] Tedrake, R. L. (2004). Applied Optimal Control for Dy-
namically Stable Legged Locomotion. Doctor’s thesis, Massachusetts
Institute of Technology.

[van Oort and Stramigioli, 2011] van Oort, G. and Stramigioli, S. (2011).
Geometric interpretation of the zero-moment point. In Robotics and
Automation (ICRA), 2011 IEEE International Conference on.

[Vaughan and Brian Davis, 1999] Vaughan, C. and Brian Davis, J. C. O.

(1999). Dynamics of Human Gait.

[Vukobratović and Borovac, 2004] Vukobratović, M.

and Borovac, B.
(2004). Zero-moment point - thirty ﬁve years of its life. Internatio-
nal Journal of Humanoid Robotics, 1.

[Vukobratovic et al., 2001] Vukobratovic, M., Borovac, B., and Surdilovic,
D. (2001). Zero moment point-proper interpretation. Proc. IEEE-RAS
Int. Conf. Humanoid Robots Tokyo, Japan.

[Wasserfall et al., 2017] Wasserfall, F., Hendrich, N., Fiedler, F., and Zhang,
J. (2017). 3d-printed low-cost modular force sensors. CLAWAR 2017:
Proceedings of the 20th International Conference on Climbing and Wal-
king Robots and Support Technologies for Mobile Machines.

[Williams, 1992] Williams, R. J. (1992). Simple Statistical Gradient-
Following Algorithms for Connectionist Reinforcement Learning. Springer
US, Boston, MA.

[Yi et al., 2011] Yi, S. J., Zhang, B. T., Hong, D., and Lee, D. D. (2011).
Practical bipedal walking control on uneven terrain using surface learning
and push recovery. In 2011 IEEE/RSJ International Conference on
Intelligent Robots and Systems.

75

Eidesstattliche Erklärung

Hiermit versichere ich an Eides statt, dass ich die vorliegende Arbeit im
Masterstudiengang Informatik selbstständig verfasst und keine anderen als
die angegebenen Hilfsmittel – insbesondere keine im Quellenverzeichnis
nicht benannten Internet-Quellen – benutzt habe. Alle Stellen, die wörtlich
oder sinngemäß aus Veröﬀentlichungen entnommen wurden, sind als solche
kenntlich gemacht. Ich versichere weiterhin, dass ich die Arbeit vorher nicht
in einem anderen Prüfungsverfahren eingereicht habe und die eingereichte
schriftliche Fassung der auf dem elektronischen Speichermedium entspricht.

Hamburg, den 6. April 2017

Fabian Fiedler

Veröﬀentlichung

Ich stimme der Einstellung der Arbeit in die Bibliothek des Fachbereichs
Informatik zu.

Hamburg, den 6. April 2017

Fabian Fiedler

