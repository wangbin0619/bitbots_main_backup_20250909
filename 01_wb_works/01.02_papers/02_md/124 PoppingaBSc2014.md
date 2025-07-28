Intelligente Wegﬁndung humanoider
Roboter am Beispiel des RoboCup

Bachelorarbeit
im Arbeitsbereich Knowledge Technology, WTM
Dr. Sven Magg

Department Informatik
MIN-Fakultät
Universität Hamburg

vorgelegt von
Martin Poppinga
am
23.12.2014

Gutachter: Dr. Sven Magg
Stefan Heinrich

Martin Poppinga
Matrikelnummer: 6318650
Siebentunnelweg 5a
25469 Halstenbek

Abstract

Abstract

In this thesis I will investigate the path ﬁnding of humanoid robots. It takes place
in the RoboCup humanoid Kid-Size league environment. It will be tested if a com-
bination of classical potential ﬁelds and evolutionary trained CTRNN can generate
a good solution. Demanded are a correct orientation at the goal and obstacle avoi-
dance. The tests showed that this goals are reachable. CTRNNs are capable to
navigate the robot in a 2D-simulation. The potential ﬁelds are able to perform an
obstacle avoidance and simple navigation tasks. The combination of both provides
good results. With low needs in computation power is the system suitable for ro-
bots and other autonomous systems which work with an incomplete model of their
enviroment.

Zusammenfassung

In dieser Arbeit wird die Pfadﬁndung humanoider Roboter untersucht. Als Kontext
dient die Humanoide Kid-Size Liga des RoboCup. Dabei wird untersucht, inwie-
fern eine Kombination von Potential Fields und evolutionär trainierter CTRNN
zur Wegﬁndung geeignet ist. Es wird in einer Simulationsumgebung untersucht,
ob die notwendigen Aufgaben der Wegﬁndung, wie die korrekte Ausrichtung des
Roboters oder dem Ausweichen von Gegnern, mit diesem kombinierten Ansatz ge-
löst werden können. Die Tests zeigten, dass diese Ziele erreichbar sind. CTRNNs
lieferten eine gute Wegﬁndung in der 2D-Simulation. Die Potential Fields können
Hindernissen ausweichen und eine einfache Navigation durchführen. Die Kombina-
tion beider Verfahren lieferte gute Ergebnisse. Mit seinem geringen Rechenaufwand
ist dieses Verfahren geeignet für Roboter und andere autonome Systeme, die mit
einem unvollständigen Modell ihrer Umgebung arbeiten.

III

Abstract

IV

Inhaltsverzeichnis

1 Einleitung

1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Umfeld . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2 Verwandte Arbeiten und Hintergrundinformationen

2.1 Klassische Wegﬁndung . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Bisherige Verfahren und Konzepte im RoboCup . . . . . . . . . . .
2.3 Potential Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 Künstliche Neuronale Netze . . . . . . . . . . . . . . . . . . . . . .
2.5 Evolutionäre Algorithmen . . . . . . . . . . . . . . . . . . . . . . .

3 Konzept der Software

3.1 Konzept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Anbindung an Softwareumgebung . . . . . . . . . . . . . . . . . . .
3.3 Vereinfachungen und Vorgaben dieser Arbeit . . . . . . . . . . . . .

4 Umsetzung und Ergebnisse

4.1 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Anbindung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Ergebnisse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4 Diskussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5 Fazit und weitere Arbeit

A Parameter

Literaturverzeichnis

1
3
3

7
7
7
9
11
14

17
17
17
18

19
19
24
24
31

35

37

39

V

Contents

VI

Abbildungsverzeichnis

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1 RoboCup[10]
1.2 Schematische Ansicht des RoboCup Frameworks . . . . . . . . . . .

4
5

2.1 Verschiedene Potential Fields[2]

. . . . . . . . . . . . . . . . . . . .

11

4.1 Aufbau der Software . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Aufbau des Netzes
. . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Fitnessverlauf mit 5, 7 und 9 Neuronen . . . . . . . . . . . . . . . .
4.4 Lernfortschritt der Evolution . . . . . . . . . . . . . . . . . . . . . .
4.5 Ausrichten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6 Ausweichen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7 Druck zum Hindernis, mit verschiedenen Fitnessfunktionen trainiert
4.8 Starkes Rauschen auf den Daten
. . . . . . . . . . . . . . . . . . .
4.9 Aufgetretene Probleme
. . . . . . . . . . . . . . . . . . . . . . . .
4.10 Lokale Extrema . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11 Ausweichen mit Potential Fields . . . . . . . . . . . . . . . . . . . .
4.12 Potential Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.13 CTRNN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.14 Vergleich zum bisherigen Verhalten . . . . . . . . . . . . . . . . . .

19
22
25
25
26
27
27
28
29
29
30
30
30
32

VII

List of Figures

VIII

Tabellenverzeichnis

4.1 Legende für Graﬁken . . . . . . . . . . . . . . . . . . . . . . . . . .

26

A.1 Parameter für CTRNN:
. . . . . . . . . . . . . . . . . . . . . . . .
A.2 Parameter für Evolution: . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . .
A.3 Parameter für Simulation:

37
37
37

IX

List of Tables

X

Kapitel 1

Einleitung

Der Themenbereich der Robotik ist eins der großen Forschungsgebiete der heuti-
gen Zeit. Im Bereich von selbständig agierenden und lernenden Systemen hat sich
in den letzten Jahren viel getan. So sind intelligente Begleiter wie Smartphones
allgegenwärtig und aus dem alltäglichen Leben kaum wegzudenken. Auch selbst-
fahrende Autos sind inzwischen so weit entwickelt, dass sie nicht mehr als utopische
Zukunftsgedanken abgestempelt werden, sondern schon auf deutschen Straßen fah-
ren [4]. Bei den Robotern, die klassisch mit dem Begriﬀ des "Roboters"verknüpft
werden, den humanoiden Robotern, zeigte sich auch großer Fortschritt in den ver-
gangenen Jahren, sie sind aber dennoch mitten in der Entwicklung[6]. Die Idee
ist es, Roboter zu entwickeln, die sich problemlos in der Welt der Menschen zu-
rechtﬁnden können, während heutige praxisrelevante Systeme speziell eingerichtete
Umgebungen wie Warenlager oder Fabrikhallen benötigen. Humanoide, dem Men-
schen nachempfundene Roboter, sollen dieses neue, komplexe Feld abdecken, indem
sie zum Beispiel auf zwei Beinen laufen und so alle Bereiche erreichen können, die
auch Menschen zugänglich sind. So sollen sie auch mit Objekten verschiedenster
Art interagieren können. Dies ist essenziell für einen Einsatz im Haushalt als Pﬂe-
gehilfe oder für andere Aufgaben bei denen der Umgang mit Menschen im Zentrum
steht.

Die vorliegende Arbeit handelt im Kontext des RoboCup. Der RoboCup ("Ro-
bot Soccer World Cup")[18] ist eine internationale Initiative und Wettbewerb im
Bereich der Robotik mit einem Fokus auf autonome Systeme. Es forschen Wis-
senschaftler und Studenten von Universitäten aus einer Vielzahl von Ländern im
Bereich der Robotik, um eben diese Problemfelder zu ergründen. Der RoboCup
entstand 1997 und wurde mit dem Ziel gegründet, die Forschung international
vergleichbar und erlebbar zu machen und so den internationalen Forschungsaus-
tausch voran zu bringen. So lässt sich das Spielen von Fußballrobotern als Stan-
dartproblem der Informatik ansehen, wie einst die Herausforderung ein System zu
entwickeln um gegen den amtierenden Schachweltmeister zu gewinnen, was 1997
erfüllt wurde [18][13]. So ist es das selbst gesteckte Ziel des RoboCup bis 2050
gegen die amtierenden FIFA-Fußballweltmeister in einem fairen Fußballspiel nach
den FIFA-Regeln zu gewinnen [18]. Es gibt jährliche Wettkämpfe in verschieden
Teilen der Welt. Eine besondere Bedeutung hat dabei die jährlich in wechseln-

1

Kapitel 1. Einleitung

den Ländern stattﬁndende Weltmeisterschaft. Während 1997 in Japan 40 Teams
zusammentrafen, waren es 2013 in Eindhoven über 3000 Teilnehmer in über 400
Teams und mehr als 40.000 Besucher[21] die die Weltmeisterschaft besuchten. Des
weiteren gibt es in vielen Ländern kleinere Meisterschaften des RoboCup, die eben-
falls jährlich stattﬁnden und sich internationaler Beteiligung erfreuen. Diese sind
zum Beispiel die GermanOpen in Magdeburg oder die IranOpen in Teheran.

Auch wenn der RoboCup als Wettkampf für den Roboterfußball gegründet
wurde, bietet er inzwischen verschiedenen Liegen in unterschiedlichsten Anwen-
dungsbereichen [18]. Die Rescue Liga entwickelt Roboter für Katastrophenhilfe
und Rettungseinsätze, so wurde Beispielsweise auch schon im RoboCup vorgestell-
te Hardware während der Katastrophe in Fukushima eingesetzt [27] um Bilder
aus unbegehbarem Gebiet zu machen. Auch die Menschenrettung steht im Fokus,
wofür die Roboter mit entsprechender Technik wie Wärmebildkameras ausgerüs-
tet sind. Geländegängigkeit der Hardware und Analyse von Signalen auf Hinweise
von Verschütteten sind die Kernpunkte der Liga. In der @Home Liga wird an
Haushaltsrobotern geforscht um beispielsweise körperlich eingeschränkten Men-
schen Aufgaben im Haushalt abzunehmen. Hier stehen Bereiche wie Objekt- und
Spracherkennung im Zentrum, aber auch am Greifen und Transportieren von Ge-
genständen wird geforscht. In der Logistik und der @Work Liga geht es um an-
wendungsbezogene Aufgaben aus dem Bereich der Lagerlogistik sowie Transport
und Erkennung von Arbeitsgegenständen.

Den größten Teil des Wettbewerbes bilden die klassischen Ligen des RoboCup,
die Soccer bzw. Fußballligen mit ihren unterschiedlichen Unterligen. Hier wird zwi-
schen fahrenden und den humanoiden Robotern unterschieden die sich wiederum
jeweils in verschiedene Unterligen nach ihren Größen unterteilen. Jede Liga hat
aufgrund ihres Reglements, die auch die Beschaﬀenheit der Roboter beschreiben,
ihre eigene Herausforderungen.

In allen Ligen ist die Wegﬁndung eine der anzugehenden Problemstellungen,
da sich hier beispielsweise in unbekanntem Gelände bewegt werden muss, oder sich
Bedingungen in der Umgebung dynamisch verändern. Die Wegﬁndung beschreibt
die Fähigkeit des autonomen Systems, in diesem Kontext des Roboters, einen Weg
zu einem vorgegeben Ziel zu ﬁnden. Dieser Weg kann auf Eigenschaften wie die
benötigte Zeit, Energiekosten, Strecke oder einfache Durchführbarkeit optimiert
werden.

Die humanoiden Ligen des RoboCup Soccer bieten mit ihren Regeln ein breites
Feld an Herausforderungen, da diese sich nur auf menschenähnliche Sensorik und
Aktorik verlassen können. So ist es zum Beispiel nicht möglich präzise Positions-
informationen mittels Infrarot oder Lasertechnik zu gewinnen. Alle Berechnungen
müssen auf dem Roboter selbst ausgeführt werden. Die vorliegenden Daten sind
mitunter stark verrauscht und es fehlen teils klare und eindeutige Wegmarken die
im Blickfeld des Roboters verfügbar sind. Die in diesem Sportszenario erforschten
Konzepte können in vielen Bereichen der humanoiden Robotik verwendet werden.

2

1.1. Motivation

1.1 Motivation

1.1.1 Problemstellung

Einen optimalen Weg für einen Roboter in den humanoiden RoboCup Soccer Ligen
zu ﬁnden, ist nicht trivial. So sollte möglichst schnell der Ball erreicht werden ohne
auf dem Weg dahin mit ihm oder mit einem Hindernis zu kollidieren. Am Ball
benötigt der Roboter die richtige Ausrichtung. Erschwerend kommt hinzu, dass
oftmals nicht die komplette Umgebung bekannt ist und sich Hindernisse sowie
Ball bewegen.

1.1.2 Neuer Ansatz und Ziel dieser Arbeit

Ziel dieser Arbeit wird es sein, eine Möglichkeit zu entwickeln, mit welcher der
Roboter in einer simulierten Umgebung einen möglichst eﬃzienten Weg zum Ball
ﬁndet und sich so am Ball ausrichten kann, dass ein Schuss auf das Tor möglich
ist. Dabei wird eine Kombination eines evolutionär trainierten Neuronalen Netzes
(genauer, ein CTRNN, siehe: 2.4.3) mit einer klassischen Potential Map (siehe: 2.3)
zum Ausweichen von Hindernissen getestet. Das Netz und die Potential Fields kön-
nen zu jedem Zeitpunkt dynamisch aus einer Eingabe von relativen Positionen von
Wegmarken auf dem Spielfeld, wie zum Beispiel Ball und Tor, einen Bewegungs-
vektor generieren, der vom Roboter umgesetzt werden kann.

Das Trainieren der Netze wird nicht auf dem Roboter selber ausgeführt, da
hierfür eine Vielzahl von Durchgängen notwendig sind. Stattdessen kommt eine
vereinfachte Simulation zum Tragen, die oﬄine auf einem leistungsstärkeren Sys-
tem geschieht.

Als Anwendungsszenario wird die RoboCup Soccer Humanoid Kid-Size Liga
genommen. Die Arbeit wird so aufgebaut, dass eine Anwendung des Verfahrens in
diesem Szenario später möglich ist.

1.2 Umfeld

1.2.1 Humanoid Kid-Size Rahmenbedingungen

Die genauen Bedingungen jeder Liga werden in dem jeweiligen Reglement festge-
legt. Dieses wird jährlich verändert um dem technologischen Fortschritt zu ent-
sprechen und diesen zu fördern. Für diese Arbeit wird das Reglement von 2014[19]
betrachtet.

In der Humanoid Kid-Size Liga wird mit bis zu 4 Robotern pro Team gegen-
einander gespielt. In der Regel kommen hier je ein Torwart und 3 Feldspieler zum
Einsatz. Die Roboter müssen menschliche Proportionen haben und zwischen 40 cm
und 90 cm groß sein. Das Spielprinzip ist dem des klassischen Fußballs nachemp-
funden. So ist es Ziel des Spiels innerhalb zweier Halbzeiten von je 10 Minuten
möglichst viele Tore zu erzielen. Dabei sind zumindest zur Saison 2014 die To-
re gelb und der Ball orange um die Erkennung zu vereinfachen. Der Untergrund

3

Kapitel 1. Einleitung

(a) Humanoid Kid-Size Spielfeld auf der Weltmeisterschaft
2014 (Brasilien)

(b) Modiﬁzierter DARwIn-
OP (vorne) und Original
(hinten)

Abbildung 1.1: RoboCup[10]

ist grün mit weißen Spielfeldmarkierungen und beinhaltet ähnliche Elemente wie
ein FIFA-Fußballfeld (siehe Abbildung 1.1a). Das Spielfeld ist 6 m mal 9 m groß.
Außer den genannten Objekten gibt es keine deﬁnierten Landmarken, die zur Po-
sitionierung benutzt werden könnten. Neben den 8 Robotern beﬁnden sich ein
Schiedsrichter und zwei Robothandler, eine Person pro Team, welche für die Ro-
boter verantwortlich ist, auf dem Feld. Die Roboter spielen vollkommen autonom
und müssen alle Berechnungen auf der eigenen Hardware durchführen.

1.2.2 Rahmenbedingungen der Hardwareplattform

Die Hardwareplattform auf der die hier entwickelte Software laufen soll entspricht
grundlegend der des DARwIn-OP (Dynamic Anthropomorphic Robot with Intel-
ligence–Open Platform)[22]. Diese Plattform wird in der Humanoid Kid Size Liga
von mehreren Teams benutzt [20]. Obwohl es in dieser Liga möglich ist, die Robo-
ter komplett selbst zu entwickeln, wird dies nicht von allen Teams wahrgenommen.
Da dies einen erheblichen Aufwand darstellt, greifen viele Teams auf diese schon
entwickelte Plattform zurück und nehmen teils Modiﬁkationen vor. Auf der hier
vorliegenden Plattform wurde eine andere Kamera verbaut (siehe Abbildung: 1.1b).
Durch die geringe Bauhöhe ist es problematisch das ganze Feld inklusive der
Feldlinien zu erfassen. Aus der Fläche aufragende Objekte wie der Ball, die Tore
oder Hindernisse sind deutlicher zu erkennen. Außerdem setzen die humanoiden
Roboter viele kleine Schritte, wodurch es zu vergleichsweise starkem Wackeln und
Vibrationen kommt, welche wiederum zu verrauschten Daten führen.

Die Rechenleistung dieser Plattform ist begrenzt [22]. Somit sollte eine Lösung

gefunden werden die keinen unverhältnismäßig hohen Rechenaufwand benötigt.

4

1.2. Umfeld

Abbildung 1.2: Schematische Ansicht des RoboCup Frameworks

1.2.3 Die Softwareumgebung

Die Hamburg Bit-Bots sind ein Team der Humanoid Kid-Size Liga, die seit 2011
an dem RoboCup teilnehmen. Die hier geschriebene Software ist zur Einbindung
in dieses Framework gedacht.

Die Software, die auf den Robotern der Hamburg Bit-Bots läuft, ist mehr-
schichtig aufgebaut. So wird auf verschiedenen Ebenen der Software ein anderes
Abstraktionslevel erzeugt (siehe Abbildung 1.2). Während sich die unteren Ebe-
nen um Sensorik und Aktorik kümmern, dienen die mittleren Schichten zur Ver-
arbeitung der Daten, wie zum Beispiel der Analyse der Bildinformationen oder
der Umsetzung der gewollten Bewegungsrichtung. Diese unteren Ebenen sind zu
großen Teilen in den Programmiersprachen C++ und C geschrieben, die mittlere
Schicht in Cython (typisiertes Python) um die notwendige Performance der zum
Teil mathematisch aufwendigen Verfahren zu erreichen.

Die höherlevelige Architektur, das Verhalten, welches für die abstrakte Planung
des Softwaresystems verantwortlich ist, ist in Python 2.7[17] geschrieben, um eine
einfache Lesbarkeit und Anpassbarkeit zu gewährleisten. Python gilt als übersicht-
liche Sprache, die viele Methoden schon bereitstellt und Bereiche wie die Speicher-
verwaltung intern behandelt. Diese hohe Abstraktion des Frameworks ermöglicht
es mit einem vereinfachtem Modell zu arbeiten. So stehen Postionen von Ball und
Toren in Vektordarstellung relativ zum Roboter bereit. Außerdem kann so die
gewollte Bewegung in drei Werten übergeben werden: der Vor- und Rückwärtsbe-
wegung, der Seitwärtsbewegung und dem Drehen, während sich das Framework um
die Umsetzung kümmert. Wie genau diese Bewegungen umgesetzt werden ist sehr
unterschiedlich. Es gibt viele Einﬂussfaktoren wie den Boden, Hindernisse gegen
die gelaufen wird oder die Hardwarequalität der einzelnen Roboter. So können zu
heiß gewordene Motoren dafür sorgen, dass der Roboter eine Kurve läuft, obwohl
dies nicht erwünscht war.

Eine global agierende Lokalisation ist nicht verfügbar, der Roboter weiß nicht

5

Aktorik / LowlevelBestehendes RoboCup FrameworkSensorikMiddleware (Datenverarbeitung)HighlevelVerhaltenKapitel 1. Einleitung

auf welcher absoluten Position des Spielfeldes er sich gerade beﬁndet. Das Lokali-
sierungsproblem ist eine der größten Herausforderungen in der Humanoiden Liga.
Gerade die Symmetrie des Feldes ist hierbei eine der Herausforderungen, da nicht
visuell erfasst werden kann auf welcher Seite des Feldes sich der Roboter gera-
de beﬁndet. Hier müssen andere Konzepte benutzt werden, wie das Merken der
Bewegung oder bioinspirierter Verfahren[5].

6

Kapitel 2

Verwandte Arbeiten und
Hintergrundinformationen

2.1 Klassische Wegﬁndung

Der Bereich der Wegﬁndung oder auch Motion Planning ist gründlich erforscht
und eins der Standardprobleme der Robotik. Es gibt eine Vielzahl von Algorith-
men und Ansätzen, die auf unterschiedliche Weise optimale Pfade ﬁnden können.
Ein Beispiel ist der A*-Algorithmus[11] welcher den kürzesten, beziehungsweise
besten Weg zu einem Ziel ﬁnden kann. Er bedient sich einer Heuristik welche für
eine gute Laufzeit sorgt. Bei Algorithmen wie A* handelt es sich um Suchen in
einem Graphen zwischen zwei Knoten. Auch wenn sich in vielen Fällen ein Graph
bzw. ein Gitter erstellen lässt, weist dies hier Schwächen auf. Die meisten die-
ser Algorithmen lassen sich nicht problemlos in dem gegeben Kontext anwenden,
da keine Lokalisation beziehungsweise globales Weltmodell mit allen Informatio-
nen der Umgebung existiert und so kein korrekter Graph erstellt werden kann.
Des Weiteren ändert sich die Umgebung dynamisch, da sich viele der Objekte in
der Umgebung vergleichsweise schnell bewegen oder Objekte erst richtig erkannt
werden, wenn der Roboter sich ausreichend nah beﬁndet. So müsste die Suche re-
gelmäßig wiederholt werden. Auch lassen sich Eigenschaften wie die Ausrichtung
des Roboters hier schlecht abbilden. Aus diesen Gründen sind die klassischen Pfad-
ﬁndungsalgorithmen in einem Graphen ungeeignet für dieses Anwendungsszenario.

2.2 Bisherige Verfahren und Konzepte im Robo-

Cup

2.2.1 Allgemein

Die Frage der Pfandﬁndung ist eine der zentralen Punkte im RoboCup. Gerade
in den Simulationsligen war dies einige Zeit einer der großen Forschungsschwer-
punkte. Inzwischen ist die Software der Simulationsligen soweit ausgereift, dass

7

Kapitel 2. Verwandte Arbeiten und Hintergrundinformationen

das Planen der Bewegungen und Aktionen mehrerer Agenten untereinander im
Zentrum stehen [28].

Es gibt hier verschiedene Ansätze. Die meisten dieser Konzepte gehen von ei-
nem globalen Weltmodell aus, einem System in dem die Position des Agenten selber
und aller Mitspieler und ggf. Gegner bekannt ist. Mit diesen Informationen können
komplexe Verhaltensweisen modelliert werden, in denen auch eine klassische Weg-
ﬁndung erstellt werden kann. Auf dem Spielfeld wird ein Gitter gespannt. Über die
nicht durch Hindernisse belegten Felder kann beispielsweise der A*-Algorithmus
angewandt werden um zu einem bestimmten Punkt der Karte zu gelangen. Dies
ist auch in der Small Size Liga und der Middle Size Liga möglich. Diese besitzen
inzwischen eine ausgereifte Lokalisation, da hier im Fall der Small Size Liga eine
Draufsicht mittels Deckenkameras erfolgt. Bei der Middle Size Liga ist eine 360
Grad Ansicht verfügbar und dazu können ohne weiteres leistungsstarke Kameras
und Computer verbaut werden.

2.2.2 Humanoid Soccer

Im Bereich der humanoiden Roboter ist diese Problemstellung, genau wie die Li-
gen selber, eher neu. So galten in den ersten Jahren gerade noch das Fortbe-
wegen und die Interaktion mit dem Ball als Herausforderung, so ist inzwischen
ein Punkt erreicht, an dem Planung und komplexere Verhaltensweisen relevant
werden. Dennoch stellen eine regelmäßige Verschärfung der Regeln, eine oft gerin-
ge Rechenleistung und ein begrenztes, dem Menschen nachempfundenes Sichtfeld,
verbunden mit einer geringen Bauhöhe die Teams vor neue Herausforderungen.
Gerade Kameraqualität und Rechenleistung sind im Bereich der Objekterkennung
und Positionsbestimmung in vielen Fällen begrenzende Faktoren. So sind weiterhin
nur wenige Teams der humanoiden Ligen in der Lage sich fehlerfrei zu Lokalisie-
ren und entsprechende komplexe Verhaltensweisen zu benutzten. Durch erschwerte
Bedingungen durch neue Regeln in vielen Bereichen, wie der Spielfeldgröße, der
Landmarken oder dem Untergrund, sind Bereiche wie eine globale Positionierung
in vielen Fällen noch nicht Spielentscheidend. Deshalb wird sich oftmals nur auf
die aktuelle visuelle Eingabe verlassen um die Bewegung zum Ziel durchzuführen.

2.2.3 Bisherige Lösung bei Hamburg Bit-Bots

Die Hamburg Bit-Bots benutzen ein vereinfachtes Modell der Umgebung das relativ
zum Agenten aufgestellt wird. Es sind die Positionen des Balles und der Tore relativ
zum Roboter vorhanden und, sofern sich ein Hindernis im Sichtfeld beﬁndet, auch
die Position dessen. Hindernisse sind in diesem Fall andere Roboter und Menschen
auf dem Feld. Bisher werden in der Software des RoboCup Teams der Universität
Hamburg, in deren Kontext diese Arbeit entsteht, arithmetisch Berechnungen für
die Bewegung des Roboters in der Vertikalen, der Horizontalen sowie der Rotation
berechnet. Die geschieht abhängig von dem Abstand und Winkel zu den einzelnen
Landmarken wie Tor und Ball.

8

2.3. Potential Fields

Die aktuelle Wegﬁndung unterteilt sich in vier Phasen, die abhängig von der
Position des Roboters zum Ball sind. Die erste Phase kommt bei einer großen
Distanz zum Ball zum Tragen, in der sich der Roboter mit hoher Geschwindigkeit
vorwärts bewegend in Richtung des Balles dreht. Wenn der Roboter in die Nähe
des Balles kommt, wird die Geschwindigkeit verringert und nicht mehr rotiert, um
eine genauere Positionierung zu ermöglichen. Liegt der Ball hinter dem Roboter,
geht dieser gerade zurück und anschließend seitwärts bis den Ball vor sich hat.
Abschließend dreht der Roboter sich um den Ball bis er zu einem Tor ausgerichtet
ist.

Dabei traten verschiedene Probleme auf. So waren zum Beispiel die verwende-
ten harten Grenzen für die Einteilung der Entfernung zu den einzelnen Landmar-
ken in einzelne Zonen problembehaftet, da die Daten zum Teil nicht präzise genug
sind. Es erwies sich oft als schwierig, auf den Eingabewerten gute Funktionen zu
ﬁnden die einen schnellen Pfad erzeugen. Für ein gutes Ergebnis musste häuﬁger
die Pfadplanung mit angepasst werden, wenn sich andere Bereiche des Systems
veränderten, wie kleine Änderungen an der Hardware oder dem Walking. Auch in-
dividuell mussten sich die Berechnungen sich zum Teil unterscheiden, da sich jeder
Roboter etwas unterschiedlich bei der Bewegungsgenauigkeit verhält. Außerdem
erwies es sich als schwierig den Pfad so zu wählen, dass der Roboter sofort richtig
am Ball stand. Darum war in der Regel noch eine Ausrichtungsphase vonnöten.
Das Ausweichen von Hindernissen war nicht eingebaut, wodurch oftmals Roboter
ineinander gelaufen sind und sich somit gegenseitig behindert oder zum Sturz ge-
bracht haben. Auch die Mess- und Vergleichbarkeit verschiedener Varianten war
hier nur schwer gegeben. Ein Vergleich mit der bisherigen Wegﬁndung ist unter
4.4.1 zu ﬁnden.

2.3 Potential Fields

Schon in den Neunziger Jahren hat Ronald C. Arkin das Modell der Potential
Fields[2] im Bereich der Roboternavigation vorgestellt. Dieses Modell ist deutlich
besser für die Wegplanung von Robotern geeignet und wurde schon in vielen Sze-
narien mit autonomen Agenten getestet. Es handelt sich bei Potential Fields um
Karten auf denen Bewegungsvektoren erzeugt werden, die die Agenten in die so
bestimmten Richtungen steuern lassen. Einzelne Positionen auf dieser Karte ha-
ben ein bestimmtes Potential, sodass es einem Agenten einfacher ist, sich in eine
bestimmte Richtung zu bewegen. Es bildet sich eine Art Landschaft mit Bergen
und Tälern. Die Höhenunterschiede werden als Vektoren dargestellt, die Richtung
und Stärke darlegen. Um die Vektoren zu erzeugen gibt es Attraktoren, die die
Vektoren auf sich zeigen lassen und Repulsoren die abstoßend wirken (siehe Ab-
bildung: 2.1a). Dabei ist die Stärke, mit der ein einzelner Repulsor oder Attraktor
auf eine bestimmte Position der Karte wirkt, abhängig von der Entfernung. Je
näher der Agent sich an einem Repulsor beﬁndet, umso stärker ist dessen Kraft.
Diese Kraft kann beschränkt sein, indem sie auf unendlich steigt um eine Barriere
zu erstellen, oder bei größerer Entfernung auf null gesetzt wird. Die Funktionen

9

Kapitel 2. Verwandte Arbeiten und Hintergrundinformationen

zur Stärke können entsprechend der Aufgabe unterschiedlich aussehen. In diesem
Beispiel ist die Stärke (f orce) des Vektors von der Distanz zum Objekt (dist) ab-
hängig. Die Stärke wächst quadratisch an. (cid:126)xv, (cid:126)yv sind die Vektoren des Feldes. Es
werden die Komponenten des Einheitsvektors, welche aus dem Abstand des Objek-
tes pro Ache (xo, yo) und der euklidischen Distanz gebildet werden mit der Kraft
multipliziert (siehe Formel: 2.2 und 2.3).

f orce =

1
dist2

(cid:126)xv =

(cid:126)yv =

−xo
dist

−yo
dist

∗ f orce

∗ f orce

(2.1)

(2.2)

(2.3)

Dabei gibt es verschiedene Arten wie diese Felder aussehen können um ein be-
stimmtes Verhalten zu erzeugen. So können die erzeugten Vektoren unabhängig von
ihrer Position einen uniformen Wert haben um einen Grunddruck zu erzeugen. Die
Felder können von den Rändern entlang einer Achse in die Mitte der Karte zeigen
um einen Korridor (siehe Abbildung: 2.1b) zu erzeugen indem sich der Roboter
bewegen soll. Durch ein sich um einen Punkt drehendes Feld können Präferen-
zen angegeben werden auf welcher Seite zum Beispiel der Roboter ein Hindernis
passieren soll. Diese Felder werden auch Schema oder Verhalten genannt.

Die Felder können beliebig kombiniert werden(siehe Abbildung: 2.1c), indem
man die Vektoren aufsummiert. So verstärken sich Vektoren oder heben sich ge-
genseitig auf. Mit diesen verschieden Feldern können schon umfangreiche Verhalten
bzw. Schemata erzeugt werden.

(cid:126)v =

N
(cid:88)

i=1

(cid:126)vi

(2.4)

Die einzelnen Komponenten des Vektors (cid:126)v bilden sich aus der Summe der
Komponenten der Vektoren der einzelnen Felder (cid:126)vi (siehe Formel: 2.4). Einfa-
che Repulsor- und Attraktorfelder können mit geringem Rechenaufwand erstellt
werden, weswegen sie sich gut für eine simple Steuerung eines Roboters eignen.

Problematisch wird es zum Beispiel, wenn eine bestimmte Ausrichtung er-
wünscht wird, die nicht mit der Bewegungsrichtung übereinstimmt, da sich dieses
nicht direkt abbilden lässt. Auch kann es schnell dazu kommen, dass der Roboter
in ein lokales Maxima gerät und so das Ziel nicht erreicht. Durch ein zusätzliches
randomisiertes Feld kann dies bei kleinen Maxima, wie dem direkten zusteuern auf
ein Hindernis kompensiert werden. Bei sackgassenartigen Situationen ist dies aller-
dings nicht mehr ausreichend. In diesem Fall könnten Felder aufgespannt werden,
die abstoßend sind von Orten an denen man schon einmal war. Das Aufstellen sol-
cher Felder ist komplex, erfordert entsprechend einen hohen Rechenaufwand und
ist ohne ein globales Wissen der Umgebung oft nicht durchzuführen.

10

2.4. Künstliche Neuronale Netze

(a) Repulsor

(b) Korridor

(c) Kombination von mehreren Potenti-
al Fields

Abbildung 2.1: Verschiedene Potential Fields[2]

2.4 Künstliche Neuronale Netze

Der Bereich der Künstlichen Intelligenz ist schon seit vielen Jahren eng mit der
Robotik verknüpft. Sie soll so auf die Umgebung reagieren, dass der größte mög-
liche Nutzen bzw. Erfolg daraus gezogen wird [25]. Dabei wird darauf geachtet,
dass der intelligente Agent auch in unbekannten Umgebungen beziehungsweise in
unbekannten Szenarien gute Leistungen erzielt. So kommt ein Mensch auch in Um-
gebungen zurecht die er noch nie gesehen hat. Genauso soll ein Agent die Umwelt
wahrnehmen und aus dieser lernen. Viele dieser Konzepte sind bioinspiriert, also
der Natur nachempfunden.

Künstliche Neuronale Netze sind ein bioinspiriertes Verfahren der künstlichen
Intelligenz. Sie orientieren sich an den biologischen Neuronalen Netzen wie sie im
Nervensystem von Lebewesen zu ﬁnden sind, wie zum Beispiel im menschlichen Ge-
hirn. Sie zeichnen sich durch eine sehr umfangreiche Vernetzung und eine sehr hohe
Parallelität aus[12][1]. Die künstlichen neuronale Netze sind diesen nachempfunden
und können deutlich schneller arbeiten, besitzen aber auf klassischer Computer-
hardware mit bis zu 8 Prozessoren nur in einem geringen Rahmen die notwendige
Parallelität um die biologischen Vorbilder in vollem Umfang nachzubilden.

11

Kapitel 2. Verwandte Arbeiten und Hintergrundinformationen

Künstliche neuronale Netze bestehen aus künstlichen Neuronen und den Über-
gängen zwischen ihnen. Die einzelnen Neuronen bekommen Eingaben von anderen
Neuronen, die durch den Übergang gewichtet wurden und berechnen auf Grund-
lage dessen ihre Ausgabe den sie an die nächste Schicht oder die Umwelt weiter-
geben. Durch das Anpassen der Kantengewichte kann das Netz lernen, bzw. sich
verändern. [23] Neuronale Netze werden in verschiedenen Bereichen eingesetzt. Sie
können komplexe Funktionen nachbilden und benötigen dabei oft deutlich weni-
ger Rechenzeit als andere Modelle. Neuronale Netze sind in der Anwendung sehr
Laufzeiteﬃzienz, müssen allerdings vorher trainiert werden. Auch können sie dazu
benutzt werden, Funktionen abzubilden, zu denen keine einfachen arithmetischen
Funktionen bekannt sind. So zum Beispiel in der Geräuschverarbeitung oder der
Objekterkennung. Es gibt verschiedene Arten von Netzen, die allen diesem Grund-
prinzip folgen, aber unterschiedlich aufgebaut sind und diﬀerenzierte Eigenschaften
besitzen.

2.4.1 Topologie und Arten von Netzen

Die einfachste Art von Netzen sind Perzeptrone[24], bzw. One-Layer-Feed-Forward
Netze. Netze dieser Art bestehen neben der Eingabeschicht nur aus der Schicht der
Ausgabeneuronen. In den meisten Fällen sind Ein- und Ausgabeschicht von Ein-
nach Ausgabe voll vernetzt. Da die Verbindungen in dieser Art von Netzen nur in
einer Richtung erfolgen, also die Informationen nur vom In- zum Output ﬂießen,
nennen sich diese Netze Feed-Forward Netze. Man kann hier beliebig viele interne
Schichten einfügen, die jeweils zur nächsten Schicht vernetzt sind, diese Schichten
werden auch versteckte Schichten (Hidden Layer) genannt, da sie keine direkte
Interaktion mit der Umwelt haben, sondern Ein- und Ausgabe nur über andere
Neuronen erfolgt. Hiermit können auch komplexere Funktionen abgebildet werden.
Werden die Neuronen mit sich oder mit vorherigen Schichten verknüpft, handelt
es sich um rekurrente Netze. Hierbei ist zum Beispiel auch eine Vollverknüpfung
möglich (alle Neuronen mit allen verknüpft). Da der Input der Rekurrenz im All-
gemeinen erst in der nächsten Iteration von den einzelnen Neuronen betrachtet
werden kann, ist mit diesen Netzen ein Speichern von Informationen über mehrere
Iterationen möglich.

Diese Netze haben eine feste Anzahl von Neuronen und Kanten. Andere Kon-
zepte wie Growing Neural Gas[8] haben die Möglichkeit, zur Laufzeit Neuronen
und Kanten hinzuzufügen und zu entfernen. Auch kann bei Netzen dieser Art
die Position in einem Koordinatensystem der Neuronen wichtig sein, was bei den
klassischen Netzen nicht betrachtet wird.

Es gibt eine Vielzahl verschiedener Netze, die sich in verschiedensten Konzepten
unterscheiden. In der Umsetzung der Arbeit wurde hauptsächlich mit CTRNN
(siehe: 2.4.3) gearbeitet.

12

2.4. Künstliche Neuronale Netze

2.4.2 Funktionsweise und Eigenschaften

Ein Netz besteht aus einer Menge von Neuronen. Je nach Topologie haben diese
unterschiedliche Eigenschaften, sind dennoch ähnlich aufgebaut.

ai =

N
(cid:88)

j=1

wijxj

(2.5)

Die Aktivierung des Neurons ai ist die Summe der mit wij gewichteten Eingaben
xj für alle N vorhergehende Neuronen j.

Aus dieser Aktivierung wird nun ein Ausgabewert berechnet. Dieser wird durch
die Aktivierungsfunktion Φ bestimmt. Die kann im einfachsten Fall linear sein
(Φ(ai) = kai mit einer Konstante k), bei der die Aktivierung ausgegeben wird,
oder bei einer Stufenfunktion bei der nur ein konstanter Wert weitergegeben wird,
wenn ein bestimmter Threshhold Θ überschritten wurde (siehe Formel: 2.6).

Φ(ai) =

(cid:40)

1 ai > Θ
0 ansonsten

(2.6)

Des Weiteren kann der Wertebereich der Ausgabe mithilfe einer Sigmoidfunk-
tion (Beispielsweise Formel 2.7) eingeschränkt werden. Hier werden beliebig große
Werte stetig in den Wertebereich zwischen 0 und 1 abgebildet. Es kann hier noch
ein sogenannter Bias θ zum Tragen kommen. Hierbei handelt es sich um einen
Wert der zusätzlich noch auf die summierte Eingabe gerechnet wird. So kann die
Aktivierungsfunktion in eine bestimmte Richtung verschoben werden.

Φ(ai) =

1
1 + e−kai

(2.7)

Die Ausgabe yi = Φ(ai) wird an alle nachfolgenden Neuronen weitergegeben.

2.4.3 Continous-Time Recurrent Neuronal Network

Das Continous-Time Recurrent Neuronal Network (CTRNN)[7] ist ein Netz das
auch in der Robotik eingesetzt wird.[14] Hier handelt es sich um eine spezielle Art
von rekurrenten neuronalen Netzen die noch einen Zeitfaktor mit betrachten. Eine
mögliche Darstellung eines CTRNNs wie sie auch in dieser Arbeit verwendet wurde
ist in Formel 2.8.

ai = an−1 +

(cid:34)

1
τ

−an−1 +

(cid:35)

wjiyj + θi

N
(cid:88)

j=1

(2.8)

Die Variable τ ist die Zeitkonstante. Durch sie kann das Netz lernen wie schnell
die Neuronen reagieren sollen. Ein hohes τ sorgt für ein träges Neuron. Anschlie-
ßend wird wie bei anderen Netzen auch eine Sigmoidfunktion angewendet.

13

Kapitel 2. Verwandte Arbeiten und Hintergrundinformationen

2.4.4 Modiﬁkation von Netzen

Damit neuronale Netze die gewünschten Resultate liefern und gute Lösungen er-
zeugen, müssen sie angepasst werden. Hierbei werden Teile des Netzes verändert.
Das betriﬀt meist die Gewichte der Kanten und den Bias der Neuronen (der Bias
kann auch als Kante von einem Neuron mit einer konstanten Ausgabe betrach-
tet werden). Es gibt verschiedene Konzepte zum Optimieren der künstlichen neu-
ronalen Netze. Man Unterscheidet zwischen unüberwachtem Lernen(unsupervised
learning)[26], überwachtem Lernen(supervised learning)[23]und bestärkendem Ler-
nen(reinforcement learning)[3]. Des Weiteren gibt es die Möglichkeit Netze mittels
evolutionärer Verfahren zu trainieren[9].

Die einfachste Art zu lernen ist die des unüberwachten Lernens. Hier bekommt
das Netz keine Rückmeldung aus der Umwelt. Dem Netz ist somit nicht bekannt,
was die erwarteten Werte sind. Stattdessen versucht das Netz selber Strukturen
in der Eingabe zu erkennen. Dies wird zum Beispiel beim Clustern oder anderen
Einordnungsaufgaben verwendet.

Beim überwachten Lernen wird ein Satz von Trainingsdaten ausgewählt wofür
die korrekte bzw. erwartete Lösung bekannt ist. Dies kann zum Beispiel eine ma-
thematische Funktion sein. Nach dem Lernen kann die Qualität mit einem Satz
von Testdaten geprüft werden. Diese Daten sind dem Netz noch unbekannt, soll-
ten dennoch zur richtigen Ausgabe führen. Dadurch, dass immer die gewünschte
Lösung bekannt ist kann der Fehler der aktuellen Berechnung für die Ausgabe be-
rechnet werden. Durch Backpropagation kann der Fehler auch für ggf. versteckte
Schichten ermittelt werden. Mithilfe des Fehler können nun die Gewichte der Kan-
ten angepasst werden. Beim überwachten Lernen werden für alle Trainingsdaten
die exakte Lösung benötigt. Wenn Agenten in unbekannten Umgebungen arbeiten,
ist dies in vielen Fällen nicht direkt möglich. Für diese Fälle bietet sich oftmals be-
stärkendes Lernen an. Hier wird nicht jeder Schritt der Fehler berechnet, sondern
über mehrere Schritte hinweg die Qualität beurteilt. Angelehnt an Bestärkung im
Rahmen der Biologie. So hat das Netz das Ziel eine möglichst große Belohnung zu
bekommen. Es gibt hierbei verschiedene Konzepte wie dieses Wissen nun in das
Lernen besserer Netze umgesetzt wird.

2.5 Evolutionäre Algorithmen

Ein Verbesserung in der bioinspirierten künstlichen Intelligenz kann auf verschie-
den Arten erfolgen. Eine davon ist die Verwendung genetischer bzw. evolutionärer
Algorithmen. Ein solcher Algorithmus ist an die Evolution der Natur angelehnt
und dient der Optimierung der Individuen [9]. Es gibt eine Population bestehend
aus einer Menge von Individuen. Diese Individuen müssen veränderbar sein; bei-
spielsweise eine Kette von Aktionen als Lösungsweg oder ein Graph bestehend aus
verschiedenen Knoten und Kanten. Es werden zunächst eine große Anzahl zufälli-
ger Individuen erstellt und auf ihre Fitness geprüft. Die Fitness gibt die Qualität
der Individuen wieder. Hierbei muss ein guter Weg gefunden werden die Qualität

14

2.5. Evolutionäre Algorithmen

zu messen.

Eine gute Fitnessfunktion steht im Zentrum eines evolutionären Ansatzes, da
diese deﬁniert, ob eine Lösung besser ist als eine andere. Dabei sollte darauf ge-
achtet werden, dass die Funktion möglichst stetig ist, sodass die Evolution nicht
in lokale Mini- bzw. Maxima gelangt. Wie so eine Fitnessfunktion aussieht ist sehr
von der gestellten Aufgabe abhängig.

Unter Anderem anhand der Qualität der einzelnen Lösungen wird entschieden
welche Individuen weiter Bestandteil der Population bleiben können. Ein ande-
res Kriterium zur Auswahl wäre zum Beispiel das Alter des Individuums. Durch
Rekombination, dem verknüpfen zweier Individuen und Mutation, zufälliger Ver-
änderung einzelner Merkmale, entstehen neue Individuen, die in die nachfolgende
Generation übergehen. Die Art der Evolution kann meistens sehr frei angepasst
werden. So wird in der Auswahl der Individuen, der Art der Mutation und Rekom-
bination umfangreich variiert. Hierbei wird der Genotyp, die interne Repräsenta-
tion, verändert, dies führt in der Regel zu einem veränderten Verhalten.

Auch neuronale Netze kann man mit evolutionären Verfahren trainieren. Eine
Rekombination der Netze ist in vielen Fällen nicht möglich, da die Netze in der
Regel so verknüpft sind, dass eine Kombination zweier Netze zu keinem sinnvollen
neuen Netz führt. Allerdings ist eine Mutation der Netze recht simpel möglich,
indem die Eigenschaften der Netze zufällig mutiert werden.

Bei jedem Netz aus der Population wird diese Mutation angewendet, dazu wird
über jede Kante des Netzes iteriert und mit einer bestimmten Wahrscheinlichkeit
p diese Kante mutiert. Bei der Mutation wird ein zufälliger Wert r addiert. r ist
ein zufälliger Wert, der beispielsweise durch die Gaußfunktion generiert wird. Er
kann positiv oder negativ sein. So kommt es meist zu kleinen Mutationen, welche
mit einer Selektion die Fitness nach oben treiben. Es kann aber auch zu größe-
ren Sprüngen kommen, die helfen sollen kleineren lokalen Maxima zu entkommen.
Diese Werte haben meist obere und untere Grenzen. Werden diese mit der Zufalls-
zahl überschritten, wird der Zufallswert von der überschrittenen Grenze abgezogen
(Siehe Formel 2.9). Dies soll verhindern, dass genau die Grenzwerte angenommen
werden.

wi =






max − r wi−1 + r > max
min − r wi−1 + r < min
wi−1 + r

ansonsten

(2.9)

Das Gewicht wi ist der neue Wert, wi−1 beschreibt das vorherige Gewicht. Bei
r handelt es sich um den Zufallswert der addiert wird und bei min und max um
die Grenzen.

Um auszuwählen, welche Individuen in die nächste Generation übernommen
werden, gibt es verschiedene Verfahren, so können einfach die Individuen mit der
besten Fitness übernommen werde. Eine andere Möglichkeit ist eine Selektion auf
Basis der Fitness oder dem Rang des Individuums[29].

15

Kapitel 2. Verwandte Arbeiten und Hintergrundinformationen

Die Wahrscheinlichkeit ob ein Individuen ausgewählt wird ist hier abhängig
von der Fitness. Entweder indem die Wahrscheinlichkeit des Auswählens direkt
mit der Fitness im Zusammenhang steht oder durch eine entsprechende Sortie-
rung. Dadurch haben Individuen mit einer hohen Fitness eine gute Chance in die
Folgegeneration zu kommen und dies auch mehrmals. Bei Individuen mit schwacher
Fitness ist dies unwahrscheinlicher allerdings nicht ausgeschlossen. Diese Individu-
en können helfen lokale Maxima zu vermeiden, da so auch alternative Lösungen in
der Population verbleiben.

16

Kapitel 3

Konzept der Software

3.1 Konzept

Potential Fields bieten eine gute Möglichkeit den Roboter zu steuern, zeigen al-
lerdings einige Schwächen. So sind vorhandene Daten der Ball- und Torposition
oftmals stark verrauscht und nicht präzise genug. Außerdem ist es schwer, mit
Potential Fields die genauen Parameter für die Bewegung zu erfahren. So ist die
Frage der Geschwindigkeit und ob ein Drehen des Roboters oder Seitwärtsschritte
besser geeignet sind, nicht direkt zu Beantworten. Auch zeigte es sich als schwie-
rig zu modellieren, dass die verschiedenen Bewegungsarten unterschiedlich eﬃzient
sind (zum Beispiel vorwärts schneller als rückwärts). Ein lernendes Verfahren soll-
te dieses leisten. So ﬁel die Wahl auf ein evolutionär trainiertes CTRNN für die
Wegsteuerung in Verbindung mit den Potential Fields um Hindernissen auszuwei-
chen. Das neuronale Netz ersetzt in diesem Sinne das Attraktorfeld der Potential
Fields und übernimmt die fehlende Dimension (Drehung) der Ansteuerung. Da die
Software später auf einem hohen Abstraktionslevel laufen soll und viele Evolutions-
schritte notwendig sind, fand das evolutionäre Training in einer 2-Dimensionalen
Simulationsumgebung statt.

3.2 Anbindung an Softwareumgebung

Die Simulation und die anderen Teile der hier entwickelten Software sind eigenstän-
dig von der bisherigen Software der Hamburg BitBots und wurden so konzipiert,
dass eine Einbindung des neuronalen Netzes und der Potential Fields in das Frame-
work einfach machbar ist. So wurden die selben Schnittstellen für Ein- und Ausgabe
gewählt wie sie schon vorhanden sind. Auch die Programmiersprache ist identisch,
sodass die Kernkomponenten, das neuronale Netz und die Potential Fields, einfach
in die Modulstruktur eingepﬂegt werden können und nur noch kleine Anpassungen
notwendig sind.

17

Kapitel 3. Konzept der Software

3.3 Vereinfachungen und Vorgaben dieser Arbeit

In Rahmen dieser Arbeit werden einige Annahmen getroﬀen und Gegebenheiten
abstrahiert.

Es wird davon ausgegangen, dass die Software keine Objekte fälschlicherweise
als Bälle, Tore oder Hindernisse erkennt. So kommt es in der Realität häuﬁger zu
false Positives bei der Objekterkennung. Dessen Behebung ist mittels verschiedenen
Verfahren lösbar, aber nicht Teil dieser Bachelorarbeit. Der Fehler auf den Daten
wird mittels einer normalverteilten Zufallsverteilung auf die Daten gerechnet um
das Rauschen der Daten durch Bewegungen o.Ä. zu simulieren. Die Erkennung der
Objekte erfolgt in einer 360◦ Ansicht, das heißt der Roboter kann diese erkennen
auch wenn sie hinter ihm liegen, da zum Beispiel die Kopfbewegung nicht mit
simuliert wird. Auch wird das Symmetrieproblem der Umgebung hier abstrahiert,
der Roboter weiß zu jedem Zeitpunkt welches Tor das des Gegners ist. Des Weiteren
wird innerhalb der Simulation davon ausgegangen, dass Ball und Hindernisse ihre
absolute Position nicht verändern. Da die Berechnungen allerdings Dynamisch für
jeden Zeitschritt ausgeführt werden, sollte dies keinen Unterschied im Resultat
des Verfahrens erzeugen und die Netze sowie die Potential Fields damit umgehen
können.

18

Kapitel 4

Umsetzung und Ergebnisse

4.1 Software

Die entwickelte Software lässt sich in verschiedene Bereiche unterteilen, die im
Folgenden vorgestellt werden. Der grobe Aufbau ist in Abbildung 4.1 zu sehen.
Eine Vielzahl von Parametern sind in einer Konﬁgurationsdatei anpassbar.

4.1.1 Simulation

Neben den eigentlichen Verfahren entstand weitere Software, die für ein funktionie-
rendes System notwendig ist. Die Simulation ist für die Bewertung des Verfahrens
maßgeblich und rechnet die Szenarien mit den entsprechenden Potential Fields und
neuronalen Netzen durch. Sie dient als Schnittstelle zwischen den Verfahren und
der Umgebung und beinhaltet maßgeblich den Teil, der die Realität simuliert. Die
Simulation ist in mehrere Teile gegliedert.

Die graﬁsche Ausgabe ist für das Plotten der einzelnen Simulationen zu-
ständig, dabei wird nach jeder Generation der Evolution, das Individuum mit der
besten Fitness dargestellt. Das Plotten der Pfade geschieht mit der Pythonbiblio-
thek "matplotlib" [15].

Abbildung 4.1: Aufbau der Software

19

WegﬁndungEvolutionNeuronales NetzNeuronSimulationRoboterBallTorHindernisseSimulationsfällelässt bewertenPotential FieldsmutiertbenutztbenutztGraﬁscheAusgabelässt plottenKapitel 4. Umsetzung und Ergebnisse

Die Simulationsfälle beschreiben den Aufbau der Simulationsumgebung. Sie
können entweder vorgegeben werden um spezielle Randfälle abzuprüfen oder zufäl-
lig generiert werden um zu verhindern, dass die Evolution keine allgemeingültige
Lösung ﬁndet, sondern auf die speziellen Fälle trainiert. Es können die Torposition,
die Ballposition, die Gegnerpositionen und deren Anzahl sowie die Position und
die Orientierung des Roboters angeben werden.

Das Weltmodell wird so erstellt, wie der Simulationsfall es vorgibt. Es bein-
haltet die globalen Informationen der Welt und hält die Objekte, die zu der Welt
gehören. Dazu gehören der Ball, das Tor und eine Liste von Hindernissen beliebiger
Anzahl.

Während diese Objekte nur ihre Position halten, hält das Objekt des Robo-
ters weitere Informationen wie die aktuelle Orientierung. Des Weiteren besitzt
es Informationen zum Zustand, wie der aktuellen Bewegung und speichert den
Bewegungsverlauf ab, der später für die Berechnung der Fitness relevant ist.

In jedem Zeitschritt werden die relativen Positionen zu den anderen Objekten
des Weltmodells berechnet. Die interne Repräsentation erfolgt in u (entspricht der
y Achse) und v (entspricht der negativen x Achse). Dieses sind die Werte, mit
denen der Roboter die weiteren Berechnungen anstellt. Diese sind an die Werte
angelehnt, die auf der echten Plattform verfügbar sind. Bei deren Generierung
werden außerhalb der Simulation keine globalen Positionsinformationen benötigt.
Innerhalb der Simulation werden die Werte wie in Formel 4.1 und 4.2 gezeigt
berechnet.

u = −(xr − xo) ∗ cos(ϕ) + (yr − yo) ∗ sin(−ϕ)

v = (xr − xo) ∗ sin(ϕ) − (yr − yo) ∗ cos(ϕ)

(4.1)

(4.2)

Wobei xr, yr die globale Position des Roboters, ϕ die Orientierung des Roboters

und xo, yo die globale Position des Objektes ist.

Des Weiteren berechnet das Objekt die Bewegungsgeschwindigkeit und aktua-

lisiert die Position auf dem Spielfeld.

sn =






max
min
(sn−1 ∗ d + sg)/(d + 1)

sg >= max
sg <= min
ansonsten

(4.3)

sg, der gewünschte Geschwindigkeitswert
sn, die Geschwindigkeit zum Zeitpunkt n
d, eine Konstante zur Verzögerung

Bei der Berechnung der Geschwindigkeit wird eine gewisse Verzögerung erzeugt,
die der echten Umgebung nachgebildet ist. Es wurde für die Tests d = 4 gesetzt.
Diese Berechnung der Geschwindigkeiten gilt für die Vor- und Rückwärtsbewegung
des Roboters sowie der Rotation. Die Minimal- und Maximalwerte (min und max)

20

4.1. Software

werden einzeln festgelegt. Anhand der Bewegung können die neuen Positionen auf
dem Feld berechnet werden.

xn = xn−1 + sn ∗ cos(ϕ) ∗ c

yn = yn−1 + sn ∗ sin(ϕ) ∗ c

(4.4)

(4.5)

Wobei c eine Konstante ist um die Relationen einzuhalten. Und xn, yn die glo-

balen Koordinaten des Roboters zum Zeitpunkt n.

Es gibt noch Funktionen die als Abbruchkriterien dienen. Sie überprüfen, ob
der Roboter nah genug am Ball, richtig ausgerichtet und langsam genug ist. Erst
wenn alle Bedingungen stimmen gilt das Ziel als erreicht und die aktuelle Runde
terminiert. Dabei wurde ein quadratischer Bereich von ca 20cm vor dem Ball und
ein Winkel zum Tor von weniger als 60◦ als Ziel angegeben. Dieser Winkel reicht,
um beispielsweise einen Seitwärtsschuss in Richtung des Tores auszuführen.

4.1.2 Neuronales Netz

Das nächste Modul ist das neuronale Netz. Es ist für das Finden des Pfades zum
Ball und der korrekten Ausrichtung zuständig.

Ein Neuron hält den aktuellen Bias der mit 0 initialisiert wird und den Zeitwert
τ , der mit 3 initialisiert wird. Außerdem hat jedes Neuron seine Aktivierungsfunk-
tion. Diese Funktionen beschreibt die Ausgabe des Neurons.

Es wird ein CTRNN benutzt, wie unter 2.4.3 gezeigt. Ist das τ hoch gewählt,
werden mehr Zeitschritte benötigt bis sich die Ausgabe verändert. Bei einem nied-
rigen τ reagiert das Neuron schnell auf neue Eingaben. Hierdurch ist eine Art
selektiver von Filterung der Daten möglich. In diesem Fall bedeutet es, dass der
Roboter nicht sofort die Richtung ändern will, wenn die Daten der Ballposition
einen Ausreißer enthalten.

Als Sigmoidfunktion kommt Formel 4.6 zum Einsatz. a ist die Aktivierung des

Neurons, Φ bildet diese auf den Wertebereich zwischen -1 und 1 ab.

Φ(a) =

a
1 + |a|

(4.6)

Das Netz besitzt eine mehrschichtige Topologie. Es gibt eine Eingabeschicht
mit 7 Neuronen und eine versteckte Schicht mit 7 Neuronen. Die Ausgabeschicht
besteht aus 3 Neuronen, welche die Bewegung des Roboters angeben (siehe Ab-
bildung 4.2). Die Eingabeneuronen geben die Eingaben direkt weiter nachdem die
Sigmoidfunktion angewandt wurde, die anderen beiden Schichten berechnen ihre
Ausgaben mit der Aktivierungsfunktion des CTRNN.

Als Eingabe dienen die Entfernungen zum Ball und zum Tor in Metern mit je
beiden Achsen sowie die Vektoren des Potential Fields der letzten Iteration. Diese
spiegeln die Diﬀerenz zwischen der gewollten Bewegung des Netzwerkes und der
tatsächlichen Bewegung wieder.

21

Kapitel 4. Umsetzung und Ergebnisse

Abbildung 4.2: Aufbau des Netzes

4.1.3 Potential Field

Das neuronale Netz bildet die wichtigste Schicht für das Potential Field (siehe: 2.3).
Die anderen Schichten bestehend aus den Repulsoren durch die Hindernisse, werden
hier generiert. Das Potential Field wird für jeden Schritt dynamisch generiert, da
keine globalen Positionsinformationen verfügbar sind. Da hier keine komplexen
Funktionen benötigt werden ist das Feld trotzdem performant. Die Berechnung
erfolgt wie in 2.3 beschrieben. Als Funktion der Stärke zeigte sich f orce = ( 800
dist )2
als gute Wahl.

Die Vektoren der einzelnen Netze werden alle aufsummiert und normiert wo-
durch sich der Vektor für den Roboter bildet(siehe Formel: 2.4 ). Dieser wird nun
je nach Einstellung direkt auf die Vorwärts-, Rückwärts- und Seitwärtsbewegung
addiert.

Je näher der Roboter gerade an einem Hindernis ist umso stärker wirkt die

Kraft des Felds auf den Roboter. Dadurch kann der Roboter ausweichen.

Der Wert der Rotation wird nicht angepasst, da so beispielsweise der Roboter
in der Nähe des Balls vom Ball weggedrückt werden würde und eine Ausrichtung
so deutlich erschwert wird (siehe auch Abschnitt 4.3.3).

Felder werden zum Einen von Hindernissen erzeugt, denen so ausgewichen wer-
den kann. Zum Anderen erzeugt der Ball ein Repulsorfeld. So soll verhindert wer-
den, dass der Roboter gegen den Ball läuft, während er sich ausrichtet. Des Weite-
ren sorgt dieses Feld dafür, dass der Roboter abbremst bevor er das Ziel erreicht.
Die Kraft ist hier geringer als bei Gegnern. Außerdem erzeugt der Ball wahlweise
noch einen konstanten Vektor in seine Richtung, dies war bei den Durchläufen mit
dem CTRNN nicht mehr notwendig.

22

Hidden Layer (7 Neuronen Vollvernetzt)Vor- und Rück-wärtsSeitwärtsRotationu - Ballv - Ballu - Tormittev - TormitteAbweichungVor- und RückwärtsAbweichungSeitwärtsAbweichungRotation4.1. Software

4.1.4 Evolution

Die Evolution bearbeitet eine zuvor eingestellte Höchstzahl von Generationen oder
bricht bei einer ausreichenden Genauigkeit ab. Vor dem ersten Durchlauf werden
gemäß der Größe der Population zufällige Individuen bzw. neuronale Netze erstellt.
Die Gewichte der Kanten werden dabei zufällig gesetzt während der Bias und der
Tau-Wert (τ ) mit null bzw. drei initialisiert werden.

Bei allen Zufallsoperationen wird ein Seed aus einem logischen Zeitstempel
und einem gesetzten Ausgangsseed generiert. Damit können trotz Zufallszahlen
Durchläufe exakt wiederholt werden.

Zentral für die Evolution ist die Bewertung der jeweiligen Netze mit einer Fit-
nessfunktion. Die entsprechende Werte bekommt das Modul aus der Simulation,
die die Szenarien schrittweise abarbeitet.

Es reicht nicht, die Zeit zu messen, die der Agent zum erreichen des Zieles
benötigt. Gerade die Ausrichtung zum Tor könnte nur durch Zufall gelingen, wenn
es keinen evolutionären Druck gäbe, die richtige Orientierung einzunehmen. So
wird das Netz belohnt, wenn es in der Nähe das Balles die richtige Orientierung
annimmt. Außerdem wird das Netz bestraft, wenn es zu nah an Hindernisse kommt
(siehe Formel: 4.7).

b =

(cid:34)

N
(cid:88)

i=0

k1 + k2 ∗

di
d0

+ k3 ∗ |wi| ∗

(cid:19)1.75

(cid:18) 500
di

+ k4 ∗

H
(cid:88)

h=1

(cid:18) 1
dh
i

(cid:19)2.75(cid:35)

(4.7)

b : Bestrafung für das Netz
k1 : Konstante Strafe pro Bewegungsschritt
k2 : Konstanter Wert für Gewicht der Distanz
k3 : Konstanter Wert für Gewicht der Ausrichtung
k4 : Konstanter Wert für Gewicht der Hindernissentfernung
wi : Winkel zum Tor zum Zeitpunkt i
di : Distanz zum Ball zum Zeitpunkt i
dh
i : Distanz zum Hinderniss h zum Zeitpunkt i
N : Anzahl der Bewegungschritte
H : Anzahl der Hindernisse

F itness =

1
b

(4.8)

Dabei zählen mehrere Faktoren in die Berechnung der Fitness ein. Die Summe
der Entfernungen des Roboters zum Ball, die Ausrichtung zum Tor in Zusammen-
hang mit der aktuellen Distanz zum Ball sowie die Distanz zu den Hindernissen.
Die hier gewonnene Fitness wird über alle Szenarien bestimmt und aufsum-
miert. So erlangen Netze eine gute Fitness die gute Ergebnisse in allen oder mög-
lichst vielen Szenarien erreichen.

Als Auswahlkriterium wird die Fitness betrachtet und eine Rang basierte Se-
lektion angewendet. Dabei wurde mit einer Wahrscheinlichkeit von p = 0.2 das

23

Kapitel 4. Umsetzung und Ergebnisse

gerade betrachtete Element in der nach Fitness sortierten Menge ausgewählt und
von Beginn der Menge neu begonnen ein Element auszuwählen. Die Fitness wurde
außerhalb der Reihenfolge nicht betrachtet.

Außerdem werden die drei bestbewerteten Individuen übernommen um ein zu-
fälliges Verlieren einer guten Lösung zu verhindern. Somit wurden relativ stark
die besten Individuen selektiert. Dies sorgt für ein schnelles Ansteigen der Fitness.
Trotz dieses hohen Elitismusses gab es keine Probleme mit lokalen Maxima.

Die Mutation passt Bias, τ und die Kantengewichte an, es kommt die Gauß-

funktion mit σ = 1 zur Anwendung.

4.2 Anbindung

Der Quelltext der Potential Fields und des Neuronalen Netzes kann direkt in das
Framework des Roboters eingefügt werden, da es hier keine Abhängigkeiten gibt.
Die Klassen können im Verhalten einfach aufgerufen werden. Als Input dienen wei-
terhin die Entfernungen zu Ball und Tor, sowie die Abweichung beim letzten Zeit-
schritt. Die ausgegebenen Geschwindigkeitswerte werden mit den Potential Fields
verrechnet und sofort an das Framework weitergegeben, welches diese in Bewegung
umsetzt. Die Simulation entfällt auf dem Roboter, da hier die Bewegung tatsäch-
lich umgesetzt wird. Auch das Training soll zumindest nicht hauptsächlich auf dem
Roboter stattﬁnden. Vielmehr wird ein Netz mittels des Pythonmoduls cPickle aus
der Simulation auf einem PC gespeichert und auf den Roboter übertragen, sodass
das trainierte Netz dort verfügbar ist.

4.3 Ergebnisse

Es zeigte sich, dass die Wahl verschiedener Parameter bezüglich Evolution und
Neuronaler Netze auf das Endergebnis oftmals wenig Einﬂuss hatte, auch wenn
Ergebnisse teils schneller erzielt wurden. So erwies sich eine Netztopologie mit
7 Eingabeneuronen, 7 Versteckten und 3 Neuronen zur Ausgabe als eﬃzienteste
Wahl. Sofern nicht anders angegeben erfolge das Training der Netze mit bestimm-
ten Parametern, die im Anhang unter A.1 zu ﬁnden sind.

4.3.1 Lernfortschritt

In Abbildung 4.3 ist der Vergleich der jeweiligen besten Netze zum in der Evolution
in Abhängigkeit zur Anzahl von Neuronen im internen Layer zu sehen. Bei sieben
Neuronen zeigte sich das beste Bild. Dabei ist zu erkennen, dass die Fitness über
die in etwa ersten 100 Generationen das größte Wachstum zeigt und sich danach
nur noch langsam verbessert. Die Durchläufe mit neun Neuronen erreichten eine
Qualität auf dem selben Niveau, benötigten allerdings deutlich mehr Generationen
und mehr Rechenzeit pro Iteration. Fünf Neuronen zeigten ein minimal schlechteres
Wachstum der Fitness.

24

4.3. Ergebnisse

Abbildung 4.3: Verlauf der höchsten Fitness pro Generation bei 5,7 und 9 Neuronen
in der verstecken Schicht (Mittelwerte aus 3 Durchläufen)

(a) Nach 1 Generation

(b) Nach 51 Generationen

(c) Nach 101 Generationen

Abbildung 4.4: Lernfortschritt der Evolution

Bei Abbildung 4.4 sind die Pfade nach 1(a), 51(b), 101(c) Generationen der
Evolution zu sehen. In Tabelle 4.1 ﬁndet sich die Legende zu den nachfolgenden
Abbildungen.

4.3.2 Funktionen der Software

Das erzeugte Netz in Kombination mit den Potential Fields generierte in den meis-
ten Fällen gute Ergebnisse. Es wurde das gewünschte Verhalten erreicht und in
Teilen sogar übertroﬀen.

So wird zuverlässig zum Ball gefunden und sich in Richtung des Tores ausge-
richtet. Dabei erfolgt die Ausrichtung zum Tor meistens schon vor Ankunft am
Ball (siehe Abbildung: 4.5a). War dies nicht möglich, erfolgte die Ausrichtung di-
rekt am Ball (Abb. 4.5b). Auch wenn ein Hindernis den Weg versperrte, konnte

25

Kapitel 4. Umsetzung und Ergebnisse

Tabelle 4.1: Legende für Graﬁken

Großer roter Punkt
Blaue Punkte
Gelbe Punkte
Kleiner roter Punkt
Blaue Pfeile

Ball
Hindernisse
Torpfosten
Startposition
Position und Ausrichtung des
Roboters über die Zeit (jeder 3. Zeitschritt)

(a) Ausrichtung auf dem Weg

(b) Ausrichtung am Ball

(c) Rückwärts Ausrich-
ten

Abbildung 4.5: Ausrichten

in den meisten Fällen ein guter Weg als Alternative gefunden werden (Abb. 4.6c).
Auch wenn kein Hindernis am Ball war zeigte sich in einigen Fällen ein ähnlicher
Pfad um den Ball herum. Auch wenn dies auf den ersten Blick nach einem Umweg
aussieht, ist diese Option zeitsparend, da so der Roboter sich so weniger drehen
muss, besonders in den Fällen, in denen der Roboter zunächst am Ball vorbei lief
(siehe Abbildung: 4.5c).

Es zeigte sich, dass das Netz schnell lernt, dass Vorwärtslaufen eﬃzienter ist
als Rückwärtslaufen, ein anfängliches Wenden aber vergleichsweise lange dauert.
Falls der Ball zum Start hinter dem Roboter lag zeigte sich, dass sich der Roboter
bei günstigen Gelegenheiten eﬃzient umdrehen kann, sofern dies nötig war. (siehe
Abbildung: 4.5a).

Durch die Potential Fields ist der Roboter in der Lage Hindernissen auf dem
Pfad auszuweichen (Abb.: 4.6) oder die Positionierung am Ball so zu ändern, dass
ein anderer Weg gefunden wird. Dabei kann es auch mit einer hohen Anzahl von
Hindernissen umgehen. Auch bestimmte Aktionen wie das Wenden konnten meis-
tens ohne großen Eﬃzienzverlust durchgeführt werden.

Der Roboter war nicht nur in der Lage Hindernissen auszuweichen, auch gelang
es durch einen schwächeren Repulsor sehr gut den Ball so zu umlaufen, dass dieser
nicht aus Versehen berührt werden würde(Abbildung: 4.6c). Dieses Feld sorgte des
Weiteren schon alleine für ein Abbremsen des Roboters vor dem Ball .

Einstellbar ist unter anderem die Stärke der Repulsoren. Hier musste eine gute
Mitte gefunden werden. Waren die Felder zu schwach kamen die Roboter den Hin-

26

4.3. Ergebnisse

(a)

(b)

(c)

Abbildung 4.6: Ausweichen

(a) Fitnessfunktion ohne Hindernisse

(b) Fitnessfunktion mit Hindernisse

Abbildung 4.7: Druck zum Hindernis, mit verschiedenen Fitnessfunktionen trai-
niert

dernissen zu nah. War der Druck zu stark kam es teils zu großen Umwegen, da der
Roboter nicht mehr zwischen zwei Hindernissen entlanglief (siehe Abbildung: 4.9c).
Es zeige sich bei ersten Tests auch nicht vorausgesehenes Verhalten. So lernte
das Netz schnell, dem Druck des Potential Fields zum Ausweichen des Gegners
entgegen zu wirken, da so geringere Umwege beim Training gelaufen werden muss-
ten. Dies war zunächst auch erwünscht, da so das Netz ﬂexibel auf den Input
der Potential Fields reagieren kann. Dadurch kam es jedoch gelegentlich auch zu
Bewegungen auf Hindernisse zu, wenn dieses gerade passiert wurden (siehe Abbil-
dung: 4.7a). Dies konnte durch ein Anpassen der Fitnessfunktion behoben werden
(siehe Abbildung: 4.7b). Es wurde die Entfernung zu den Hindernissen mit einbe-
zogen, was zu besseren Ergebnissen führte. Andere Teile des Pfades waren davon
nicht betroﬀen

Überraschend gut konnte das Netz mit stark verrauschten Daten umgehen
wenn es hier rauf trainiert wurde(siehe Abbildung: 4.8b). Es wurde ein zufälli-
ger, normalverteilter Wert auf die Eingabedaten des CTRNNs addiert. Dabei war
als Standardabweichung σ = 0.3 gesetzt. Dies entspricht 30 cm. Im Vergleich zeigt
sich, dass das Netz sehr gut damit umgehen kann. Wenn das Netz wie in Ab-
bildung 4.8c ohne Rauschen trainiert wurde, kam es bei der Ausrichtung etwas
häuﬁger zu Problemen.

Gelegentlich, gerade bei vielen Hindernissen, kam der Roboter aufgrund der
Bewegungsverzögerung zu nah an ein Hindernis und musste ein kleines Stück zu-
rücklaufen, bevor er seinen Pfad fortsetzten konnte. Dies kostete Zeit, verhinderte

27

Kapitel 4. Umsetzung und Ergebnisse

(a) Sehr geringes Rauschen

(b) Starkes Rauschen

(c) Probleme auf dem Letz-
ten Stück

Abbildung 4.8: Starkes Rauschen auf den Daten

aber erfolgreich eine Kollision (Abbildung: 4.9a). Durch weitere Anpassungen, bei
der die Abweichung der Bewegungen in Zusammenhang mit der aktuellen Be-
wegungsrichtung gestellt werden, könnte dies auch vermieden werden, indem so
vorausschauender seitlich zur Bewegungsrichtung ausgewichen wird.

An einigen Stellen legte die evolutionäre Optimierung Schwächen der Simu-
lation oﬀen, indem sie zum Beispiel ausnutzte, dass die Maximalgeschwindigkeit
für vorwärts und seitwärts einzeln berechnet werden. So lernte das System leicht
schräg zu laufen um so eine erhöhte Gesamtgeschwindigkeit zu haben. Dies spiegelt
zwar die existierenden Grenzwerte im echten Framework wider, dort würde der Ro-
boter allerdings instabiler laufen, was in der Simulation zu diesem Zeitpunkt nicht
betrachtet wird.

Wenn sich mehrere Hindernisse in der Nähe des Balles befanden, wurde zum Teil
ein zu umständlicher Weg eingeschlagen(siehe Abbildung: 4.9b), da die einzelnen
Hindernisse in der Simulation nicht getrennt betrachtet werden. Dies Zeigt eine
der Schwächen des Verfahrens auf. Solche Situationen kommen allerdings selten
vor und sind auch mittels anderer Verfahren schwer lösbar.

4.3.3 Potential Fields

Bei den Potential Fields gab es zwei unterschiedliche Möglichkeiten die Bewegung
des Roboters zu beeinﬂussen, da der Roboter sowohl seitwärts laufen, als sich auch
drehen kann. In Abbildung 4.12 sind die Methonden im Vergleich zu sehen. In Ab-
bildung 4.12a kam ausschließlich das Potential Field ohne Rotation zum Tragen. Es
wurde sich entsprechend nicht am Ball ausgerichtet und die Orientierung während
des gesamten Pfades nicht verändert. In Abbildung 4.12b wurde stattdessen die
Rotation benutzt. In vielen Szenarien wurde so auch ein Pfad gefunden. In 4.12c
ist die bewährte Kombination von Potential Fields (ohne Rotation) und CTRNN
im Vergleich zu sehen. Diese Kombination hat Vorteile im Gegensatz zur Rotati-
on. Wie in Abbildung 4.11 zu sehen ist war das Ausweichen in einigen Situationen
nicht sonderlich eﬀektiv. Außerdem kam es zu Problemen beim Ausrichten zum
Ball wie unter Abbildung 4.9d

Es ist, wie gezeigt, auch möglich, mittels der Repulsoren und einem Attraktor

28

4.3. Ergebnisse

(a) Muss bei Hindernis zu-
rück

(b) Hindernis im Weg

(c) Zu starkes Feld

Schaﬀt Ausrichtung

(d)
nicht

Abbildung 4.9: Aufgetretene Probleme

(a) Potential Field

(b) Neuronales Netz

(c) Kombinierte Lösung

Abbildung 4.10: Lokale Extrema

zum Ball zu ﬁnden. Allerdings ist es wahrscheinlicher in lokale Maxima zu geraten
(Abbildung: 4.10a) als bei einer hybriden Lösung. (Abbildung: 4.10c). Durch die
Kombination mit den CTRNN konnte der Sackgasse entkommen werden und es
wurde den Hindernissen ausgewichen. Dabei ist zu erwähnen, das hier nur Repul-
soren und Attraktoren zum Tragen kamen. Mittels komplexerer Felder oder einem
zufälligen Feld kann dies auch in einem begrenzten Rahmen verhindert werden.

4.3.4 Neuronales Netz

Auch eine Lösung mit ausschließlich neuronalen Netzen ist möglich. So wurden ge-
eignete Wege gefunden. Hier ist allerdings das Ausweichen von Hindernissen nicht
direkt umsetzbar (siehe Abbildung: 4.13). Außerdem kommt es ggf. zu Kollisionen

29

Kapitel 4. Umsetzung und Ergebnisse

(a) Seitwärts

(b) Drehen

Abbildung 4.11: Ausweichen mit Potential Fields

(a) Seitwärts

(b) Drehen

(c) Seitwärts mit Neuronal

Abbildung 4.12: Potential Fields

(a) Nur CTRNN

(b) CTRNN und Potential Fields

Abbildung 4.13: CTRNN

30

mit dem Ball beim Ausrichten. Ließ man diese Bereiche außer Acht, zeigten sich
schon schöne Ergebnisse mit einer Intelligenten Pfadﬁndung mit einem eﬃzienten
Ausrichten am Ziel.

4.4. Diskussion

4.4 Diskussion

4.4.1 Einordnung

Zu anderen Verfahren

Wie in 4.3 gezeigt bietet eine Kombination der beiden Verfahren Vorteile gegenüber
den einzelnen Konzepten im Einzelnen. So hatte die Vorgehensweise mit Potential
Fields Probleme mit Sackgassen (lokalen Maxima) und der richtigen Ausrichtung.
Dafür entﬁel das aufwendige Erstellen der komplexen Felder und es konnte auf sim-
ple Repulsoren zurückgegriﬀen werden. CTRNN leisten dies, brauchen aber eine
Möglichkeit, auf eine variable Anzahl von Hindernissen einzugehen. Das kombi-
nierte Verfahren zeigte Pfade auf, die eﬃzient erscheinen und mit herkömmlichen
Methoden wohl nicht entstanden wären.

Zu bisherigem Verfahren

Zumindest in der simulierten Umgebung zeigte sich dieses Verfahren als deutlich
eﬃzienter als das Bisherige. Der Ball wurde deutlich schneller erreicht. Auch wenn
der Ball hinter dem Roboter lag konnte sich schnell ausgerichtet werden, außerdem
geschah die Ausrichtung zum Tor in den meisten Fällen schon auf dem Weg zum
Ball und nicht erst bei Ankunft. Abbildung 4.14 zeigt einen Vergleich vom alten
Verfahren, dem alten Verfahren mit den hier benutzten Potential Fields sowie dem
neuen Verfahren mit CTRNNs und den Potential Fields.

Der Teil zur Ausrichtung in Richtung des Tores des alten Verhaltens wird nicht
dargestellt, da dieser Teil nicht direkt in der Simulation anwendbar ist. Bei der
zweiten Variante wird der Pfad durch das Hindernis gestört. Dadurch gerät der
Roboter in eine andere Phase der Wegﬁndung, für den Fall, dass der Ball vor dem
Roboter liegt.

Zum theoretischen Optimum

Ein theoretisches Optimum ist schwer zu deﬁnieren, da es einen großen möglichen
Lösungsraum gibt. In den meisten Fällen wurde ein guter Weg gefunden. Bei dem
Ausweichen der Hindernisse zeigte sich ebenfalls meist eine gute Lösung auch wenn
es Fälle gab wie das direkte auf ein Hindernis zu laufen bei denen der Agent zu
stark abbremste oder lieber einen anderen Weg hätte wählen sollen. Teils wurden
sogar Lösungen gefunden die besser waren als der Pfad den man intuitiv gewählt
hätte wenn man den Roboter manuell steuern würde (siehe Abbildung: 4.5c).

31

Kapitel 4. Umsetzung und Ergebnisse

(a) Das alte Verfahren

(b) Altes Verfahren mit Potentieal
Fields

(c) Das neue Verfahren

Abbildung 4.14: Vergleich zum bisherigen Verhalten

4.4.2 Softwarelaufzeit

Das Trainieren des Netzes war im Vergleich zur Laufzeit des Netzes selber sehr
aufwendig. Potential Fields und das neuronale Netz können ohne Probleme auf
dem Roboter ausgeführt werden, ohne dass es zu massiven Performanzproble-
men kommt. Das Berechnen des CTRNN mit 7 Neuronen dauerte mit Python2.7
ca. 0.18 ms (5 Neuronen: 0.12ms). Die Potential Fields brauchten pro Zyklus ca.
0.03 ms bei 8 Hindernissen (0.06 ms bei 18).

Das Training hingegen muss oﬄine auf einer anderen Hardware, wie beispiels-
weise einem PC geschehen, da hier viel Rechenzeit benötigt wird. Das Verwenden
eines anderen Interpreters wie dem pypy-Interpreter[16] beschleunigte das Verfah-
ren stark (ca. Faktor 5). Das Lernen war in diesem Fall je nach Parametern nach
einigen Minuten für kleine Testsätze und einigen Stunden bei großen Testsätzen
abgeschlossen (übliche PC-Hardware, amd64 Architektur, 2.9 GHz). Diese Zeiten,
sowohl Training als auch auf dem Roboter können durch gezielte Programmop-
timierungen, Parallelisierung oder die Wahl einer anderen Programmiersprache

32

4.4. Diskussion

weiter reduziert werden.

4.4.3 Anwendbarkeit im aktuellen Framework

Auch wenn die Kombination beider Verfahren gute Ergebnisse in der Simulati-
on zeigten ist dies zum jetzigen Zeitpunkt außerhalb der Simulation noch nicht
direkt im RoboCup Framework der Hamburg Bit-Bots anwendbar, da nicht durch-
gehend Positionsinformationen aller relevanten Objekte auf dem Feld vorhanden
sind. Wenn ein gutes lokales Weltmodell existiert, dass Daten zu Toren und Ande-
rem dauerhaft verlässlich darstellt auch wenn diese außerhalb des Sichtbereiches
liegen, sollte es möglich sein, nach Anpassung einiger Parameter, das trainierte
Netz auf dem Roboter für eine eﬃziente Wegﬁndung zu benutzen.

33

Kapitel 4. Umsetzung und Ergebnisse

34

Kapitel 5

Fazit und weitere Arbeit

Ziel dieser Arbeit war es mittels einer Kombination von Potential Fields und einem
bioinspirierten Verfahren eine gute Wegﬁndung in einer Simulationsumgebung zu
erreichen. Dies ist gelungen. Es konnten im Rahmen einer Simulation gute Ergeb-
nisse erzielt werden (siehe: 4.3.2). So wurde der Ball mit nur wenigen Ausnahmen,
fast immer erreicht. Auch eine korrekte Ausrichtung am Ziel war möglich sofern
kein Hindernis die Position blockierte. Das Ausrichten erfolgte schon auf dem Weg
und war in der Regel sehr eﬃzient.

Mittels CTRNNs lassen sich gut komplexe Wege und Verhaltensweisen trainie-
ren (siehe: 4.3.4). Dabei bieten diese Netze auch gleich Möglichkeiten zur Filterung
der Daten. Gerade in dem gegebenen Kontext ist eine Filterung sehr hilfreich, da
teils mit vielen Ausreißern zu rechnen ist. Während das Training der Netze re-
chenaufwendig ist, verhalten sich die Netze in ihrer Funktion sehr performant und
benötigen nur wenig Rechenzeit (siehe: 4.4.2). Das evolutionäre Training hatte
keine merklichen Probleme mit lokalen Extrema und schaﬀte es immer gute Lö-
sungen zu ﬁnden. Das CTRNN alleine erzeugte geeignete Wege, jedoch ohne die
Hindernisse zu betrachten.

Potential Fields wurden ergänzend eingesetzt Sie können auch mit einer ho-
hen und variablen Anzahl von Repulsoren umgehen und so eine eﬀektive Obstacle
Avoidance umsetzten (siehe: 4.3.3). Auch das Berühren des Balles lies sich so ver-
hindern. Dabei kamen nur simple Felder wie Repulsoren zum Tragen. Auch hier
war wenig Rechenleistung notwendig. Durch den geringen Rechenaufwand ist die-
ses Verfahren gut für Roboter bzw. autonome Systeme geeignet.

Davon ausgehend, dass alle Objektpositionen relativ zum Roboter bekannt sind,
ließen sich mit diesem Verfahren auch ohne eine globale Lokalisation gute Ergeb-
nisse erzielen.

Auch wenn das Verfahren bereits gute Lösungen zeigt kann beispielsweise wei-
ter an der Fitnessfunktion gearbeitet werden, um noch bessere Pfade oder eine
kürzere Trainingszeit zu erzeugen. Ebenso wichtig ist eine möglichst realitätsnahe
Simulation. So könnte eine 3D-Simulation zum Tragen kommen um Themen wie
Stabilität mit zu betrachten.

In weiteren Arbeiten könnte das hier trainierte Netz weiter verbessert werden,

35

Kapitel 5. Fazit und weitere Arbeit

indem das Training individuell auf die Roboter abgestimmt wird. So könnte ein
ständiges links Driften eines Roboters aufgrund ermüdeter Hardware kompensiert
oder, je nach Untergrund, mehr oder weniger gedreht werden. Das Netzwerk müsste
dies auch schon leisten können, wenn zum Beispiel Feedback mittels einer Decken-
kamera gesammelt wird. So könnte das Netz trainiert werden mit einem Abdriften
umzugehen. Dies ist allerdings noch zu testen.

Denkbar wäre auch eine Lösung, die dies während des Produktivbetriebes ﬂe-
xibel erlernen kann. Beispielsweise indem mittels bestimmter Verfahren der Fehler
von gewollter und tatsächlicher Bewegung zum Lernen benutzt wird um noch bes-
sere Ergebnisse zu bekommen.

Es wäre auch denkbar, das System auf mehrere Agenten zu erweitern und so
zu versuchen, komplexe Verhaltensweisen zu erlernen. So wäre es möglich, mittels
weiterer Eingaben in das Netzwerk, Entfernungen anderer Roboter zum Ball zu
betrachten um so ein abstimmendes Verhalten zu erzeugen.

Ebenso kann das Konzept der Potential Fields in diesem Kontext erweitert
werden, hier gibt es viele Möglichkeiten. So könnten die Seitenlinien als Repulsoren
dienen um zu verhindern, dass der Roboter ungewollt das Spielfeld verlässt. Dazu
ist allerdings eine weiterführende Lokalisation notwendig.

36

Anhang A

Parameter

Tabelle A.1: Parameter für CTRNN:

Kantengewicht
τ
Bias
versteckte Neurone

[−5, 5]
[0.5, 4.5]
[−6, 6]
7

Tabelle A.2: Parameter für Evolution:

Populationsgröße
Mutationswahrscheinlichkeit
Selektionswahrscheinlichkeit
Garantiert übernommene Individuen
Anzahl Testszenarien pro Generation
Anzahl Generationen

70
0.02
0.2
3
400
300

Tabelle A.3: Parameter für Simulation:

Abbruchkriterien

Winkel zm Tor, Position am Ball
Rauschen auf den Daten Gauß-Verteilung σ = 0.001 (in m)

37

Anhang

38

Literaturverzeichnis

[1] Daniel J Amit. Modeling brain function: The world of attractor neural net-

works. Cambridge University Press, 1992.

[2] Ronald C Arkin. Behavior-based robotics. MIT press, 1998.

[3] Andrew G Barto. Reinforcement learning: An introduction. MIT press, 1998.

[4] Team Berlin. Spirit of berlin: An autonomous car for the darpa urban chal-

lenge hardware and software architecture. retrieved Jan, 5:2010, 2007.

[5] Marc Bestmann. Bachelorarbeit: Biologically inspired localization on huma-

noid soccer playing robots. (eingereicht).

[6] J Falconer. Honda developing disaster response robot based on asimo. IEEE

Spectrum, 11, 2013.

[7] Dario Floreano and Claudio Mattiussi. Bio-inspired artiﬁcial intelligence:

theories, methods, and technologies. MIT press, 2008.

[8] Bernd Fritzke et al. A growing neural gas network learns topologies. Advances

in neural information processing systems, 7:625–632, 1995.

[9] David E. Goldberg. Genetic algorithms in search, optimization, and machine

learning. Number 2. Addison-Wesley, Reading, MA, 1989.

[10] Hamburg Bit-Bots. Fotos von Wettbewerben, 2014. http://www.bit-bots.

de/ [Online; Zugegriﬀen 17.12.2014].

[11] Peter E Hart, Nils J Nilsson, and Bertram Raphael. A formal basis for the
heuristic determination of minimum cost paths. Systems Science and Cyber-
netics, IEEE Transactions on, 4(2):100–107, 1968.

[12] Suzana Herculano-Houzel. The human brain in numbers: a linearly scaled-up

primate brain. Frontiers in human neuroscience, 3, 2009.

[13] Feng-hsiung Hsu.
19(2):70–81, 1999.

Ibm’s deep blue chess grandmaster chips.

IEEE Micro,

39

Literaturverzeichnis

[14] Sven Magg and Andrew Philippides. Gasnets and ctrnns–a comparison in
terms of evolvability. In From Animals to Animats 9, pages 461–472. Springer,
2006.

[15] matplotlib. Python plotting, 2014. http://matplotlib.org/ [Online; Zuge-

griﬀen 21.12.2014].

[16] pypy. alternative implementation of the Python language, 2014. http://

pypy.org/ [Online; Zugegriﬀen 21.12.2014].

[17] Python Software Foundation. Python 2.7. https://www.python.org/ [Onli-

ne; Zugegriﬀen 19.12.2014].

[18] RoboCup Federation. A Brief History of RoboCup. http://www.robocup.
org/about-robocup/a-brief-history-of-robocup/ [Online; Zugegriﬀen
20.12.2014].

[19] RoboCup Federation.

HumanoidLeagueRules2014.

http://www.

informatik.uni-bremen.de/humanoid/pub/Website/Downloads/
HumanoidLeagueRules2014-07-05.pdf [Online; Zugegriﬀen 21.12.2014].

[20] RoboCup Federation.

HumanoidLeagueTeams2014.

http://www.

informatik.uni-bremen.de/humanoid/bin/view/Website/Teams2014
[Online; Zugegriﬀen 21.12.2014].

[21] RoboCup Federation.

http://www.
robocup2013.org/final-report-robocup2013-available/ [Online; Zuge-
griﬀen 21.12.2014].

RoboCup2013 - Final Report.

[22] Robotis. DARWIN-OP. http://www.robotis.com/xe/darwin_en [Online;

Zugegriﬀen 17.12.2014].

[23] Raúl Rojas. Neural networks: a systematic introduction. Springer, 1996.

[24] Frank Rosenblatt. The perceptron: a probabilistic model for information sto-
rage and organization in the brain. Psychological review, 65(6):386, 1958.

[25] Stuart Russell, Peter Norvig, and Artiﬁcial Intelligence. A modern approach.

Artiﬁcial Intelligence. Prentice-Hall, Egnlewood Cliﬀs, 25, 1995.

[26] Terence D Sanger. Optimal unsupervised learning in a single-layer linear

feedforward neural network. Neural networks, 2(6):459–473, 1989.

[27] Tomoichi Takahashi and Masaru Shimizu. How can the robocup rescue simu-
lation contribute to emergency preparedness in real-world disaster situations?

[28] Amir Tavaﬁ, Narges Majidi, Michael Shaghelani, and Amir Seyed Danesh.
Optimization for agent path ﬁnding in soccer 2d simulation. In Mobile Com-
munication and Power Engineering, pages 109–114. Springer, 2013.

40

[29] Xin Yao. Evolving artiﬁcial neural networks. Proceedings of the IEEE,

87(9):1423–1447, 1999.

Literaturverzeichnis

41

Literaturverzeichnis

42

Erklärung der Urheberschaft

Ich versichere, dass ich die Bachelorarbeit im Studiengang Informatik selbststän-
dig verfasst und keine anderen als die angegebenen Hilfsmittel – insbesondere keine
im Quellenverzeichnis nicht benannten Internet-Quellen – benutzt habe. Alle Stel-
len, die wörtlich oder sinngemäß aus Veröﬀentlichungen entnommen wurden, sind
als solche kenntlich gemacht. Ich versichere weiterhin, dass ich die Arbeit vorher
nicht in einem anderen Prüfungsverfahren eingereicht habe und die eingereichte
schriftliche Fassung der auf dem elektronischen Speichermedium entspricht.

Ort, Datum

Unterschrift

43

Erklärung zur Veröﬀentlichung

Ich erkläre mein Einverständnis mit der Einstellung dieser Bachelorarbeit in den
Bestand der Bibliothek.

Ort, Datum

Unterschrift

45

