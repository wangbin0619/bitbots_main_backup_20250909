Ballveri(cid:28)kation

Robocup Projektbericht

Lasse Einig

Kay Peikert

Anja Richter

Informatik B.Sc.

WS 2010/11 & SoSe 2011

Universit(cid:228)t Hamburg

Betreuer: Janis Sch(cid:246)nefeld

10. Februar 2012

1

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Inhaltsverzeichnis

1. Einleitung

1.1. RoboCup Soccer (Humanoid, Middle-Size, Simulation, Small-Size, Stan-

dard Platform Liga(SPL), Mixed-Reality) . . . . . . . . . . . . . . . . . . .

1.2. Rescue League (Robot, Simulation) . . . . . . . . . . . . . . . . . . . . . .

1.3. RoboCup@Home . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1.4. RoboCup Junior (Soccer, Dance, Rescue) . . . . . . . . . . . . . . . . . . .

2. Standard Platform League im Projekt

2.1. Objekterkennung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.2. Kollisionserkennung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.3. Bewegungsabl(cid:228)ufe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.4. Verhalten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4

5

6

7

7

8

8

9

9

9

2.5. Hardware des Roboters ansteuern . . . . . . . . . . . . . . . . . . . . . . . 10

3. Aufgabenstellung

4. Vor(cid:252)berlegungen

11

12

4.1. Schwierigkeiten der Objekterkennung . . . . . . . . . . . . . . . . . . . . . 12

4.2. Annahme

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

5. Ausgangssystem

6. Realisierung

15

15

6.1. Ansatz . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

6.2. Histogramm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

6.3. Farbr(cid:228)ume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

6.3.1. RGB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

6.3.2. HSV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

7. Funktionsweise und Implementierung der Ballveri(cid:28)kation

8. Bewertung unseres Verfahrens

21

26

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 2 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

9. Fazit

10.Anhang

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

27

28

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 3 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

1. Einleitung

Die Teilnahme am RoboCup ist Teil des gleichnamigen Projektes an der Universit(cid:228)t Ham-
burg. RoboCup ist eine internationale Initiative zur F(cid:246)rderung der Forschung und inter-
disziplin(cid:228)ren Ausbildung in den Bereichen K(cid:252)nstliche Intelligenz und autonome mobile

Systeme.[1]

Im RoboCup werden Wettbewerbe in verschiedenen Disziplinen bzw. Ligen ausgetragen.

Da der RoboCup der Forschung und somit dem Fortschritt dient, werden nach dem Wett-

kampf die L(cid:246)sungsans(cid:228)tze der Teams ver(cid:246)(cid:27)entlicht. Dies soll verhindern, dass ein Team

(cid:18)gute(cid:16) Software so lange unver(cid:228)ndert benutzt, wie die anderen Teams damit zu schlagen

sind. Die einzelnen Ligen unterscheiden sich vor allem in der Art der Roboter und in der

Art der zu bew(cid:228)ltigenden Aufgaben. Diese Unterscheidung ist aufgrund der derzeitigen

Problematik in einzelnen Bereichen der Robotik notwendig.

Da die humanoide Fortbewegung der Ro-

boter noch ein eigenes Forschungsgebiet

ist und die entsprechenden Roboter sich

derzeit noch sehr langsam (cid:252)ber das Spiel-

feld bewegen, eignen sich diese beispiels-

weise noch nicht f(cid:252)r die praktische Er-

forschung von kollektivem Verhalten bzw.

Schwarmintelligenz. Um jedoch auch die-

sen Bereich voran zu bringen, verzichtet

man in anderen Ligen auf eine anspruchs-

volle Fortbewegung und spielt mit radge-

triebenen Robotern.

Abbildung 1: SPL-Spielfeld mit Naos

Die Anforderungen bzw. Spielregeln der einzelnen Ligen werden zus(cid:228)tzlich jedes Jahr dem

Fortschritt angepasst, um den Anspruch und die Anforderungen an die Leistungsf(cid:228)higkeit

der Roboter zu erh(cid:246)hen.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 4 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Folgende Ligen werden derzeit angeboten

• RoboCup Soccer

• Rescue League

• RoboCup@Home

• RoboCup Junior

1.1. RoboCup Soccer (Humanoid, Middle-Size, Simulation,

Small-Size, Standard Platform Liga(SPL), Mixed-Reality)

Die humanoiden Ligen benutzen alle (wie im Namen

schon angedeutet) menschen(cid:228)hnliche Roboter. Da-

bei kommt es auf die jeweilige Liga an, wie streng

die Vorschriften bez(cid:252)glich der Hardware sind. In der

SPL gibt es ein Reglement, dass jegliche Modi(cid:28)kati-

on der Hardware verbietet. Die Hardware ist vorge-

fertigt, also sind die Roboter nicht von den Teams

selbst gebaut. Die Schwierigkeit der Humanoiden

ist haupts(cid:228)chlich die Fortbewegung. Das Laufen auf

zwei Beinen ist nach wie vor schwierig. Aber auch

das Aufstehen nach einem Sturz ist nicht trivial. Ge-

Abbildung 2: Middle-Size Roboter

auf ihrem Spielfeld

nerell ist das Ausf(cid:252)hren der Aktionen hier vordergr(cid:252)ndig, nicht so sehr das Fu(cid:255)ballspielen

an sich. Taktiken spielen lediglich eine Nebenrolle.

Die Middle-Sized Liga, die sich auch mit Fu(cid:255)ball spielenden Robotern besch(cid:228)ftigt, hat

andere Schwerpunkte. Da hier keine menschen(cid:228)hnlichen Roboter verwendet werden, gibt

es das Problem der Fortbewegung auf zwei Beinen nicht. Die Roboter sehen ein wenig aus

wie eine Boje, die aus dem Wasser schaut. Die Roboter haben einen niedrigen Schwerpunkt

und bewegen sich auf R(cid:228)dern. Somit sind sie deutlich agiler als z. B. unsere Naos [5].

Deshalb geht es in dieser Liga in erster Linie um Teamplay und nicht darum, z. B. die

Agilit(cid:228)t zu erh(cid:246)hen.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 5 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Die omnidirektionale Kamera, die es dem Roboter

jederzeit erm(cid:246)glicht, Objekte zu erkennen, ohne ih-

nen mit der Vorderseite zugewandt sein zu m(cid:252)ssen

ist eine weitere Erleichterung. Die Roboter sollen,

wie im richtigen Fu(cid:255)ball auch, im Team zusammen-

spielen.

Typische Situationen sind z. B. das Freistellen bei

einem Einwurf, um anspielbar zu sein, das Blocken

Abbildung 3: Mixed-Reality

eines ankommenden Gegners durch R(cid:252)ckw(cid:228)rtsfah-

Roboter auf

einem Bildschirm

ren oder das Ausspielen des Gegnes durch Passspiel.

Eine andere Herangehensweise an das Thema Robo-

terfu(cid:255)ball verfolgt die Mixed-Reality Liga. Hier sind

lediglich die Roboter real, Spielfeld und Ball werden auf einem Monitor dargestellt, auf

dem sich die Roboter bewegen. (cid:220)ber Deckenkameras wird das Spielgeschehen beobachtet

und mit den gewonnenen Daten gesteuert.

1.2. Rescue League (Robot, Simulation)

Diese Liga besch(cid:228)ftigt sich mit dem Aufsp(cid:252)ren von

eventuell verletzten Personen, dem Zurecht(cid:28)nden

in fremden Umgebungen und deren Kartographie-

rung etc. Daf(cid:252)r gab es beim RoboCup einen Hinder-

nisparcours, der durch farbige B(cid:228)nder an der Ban-

denoberseite deutlich macht, welcher Klasse die Ro-
boter angeh(cid:246)ren. Es gibt dabei Kriterien wie auto-
nom und halb autonom sowie verschiedene Schwie-

rigkeitsgrade bei der Fortbewegung z. B. holprige

Abschnitte, Treppen, steile Schr(cid:228)gen und weitere.

Abbildung 4: Rescue-Roboter

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 6 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

1.3. RoboCup@Home

Aufgabe von Teilnehmern dieser Liga ist die Entwicklung von Haushaltshilferobotern.

Dabei m(cid:252)ssen die Roboter sich selbstst(cid:228)ndig in der h(cid:228)uslichen Umgebung zurecht(cid:28)nden.

Au(cid:255)erdem sollen sie Personen kennenlernen k(cid:246)nnen, sich also deren Gesichter einpr(cid:228)gen

und sie somit wiedererkennen, wenn sie sie in der Wohnung tre(cid:27)en. Per Stimmeneinga-

be empfangen die Roboter Befehle, die sie ausf(cid:252)hren sollen. Dabei geht es um typische

Alltagsaufgaben wie Ketchup oder ein Getr(cid:228)nk aus dem K(cid:252)hlschrank holen und zu einer

bestimmten Person bringen.

1.4. RoboCup Junior (Soccer, Dance, Rescue)

Die Junior Liga ist f(cid:252)r Sch(cid:252)ler. Es geht hier mehr um

das spielerische Ausprobieren und Arbeiten mit den

Robotern, als um die Weiterentwicklung des Fach-

gebietes. Entsprechend locker ist das Regelwerk. Die

Roboter sind meist eine Kombination aus Lego mit

verbauten Motoren. Dabei reicht die Bandbreite der

Roboter von Fu(cid:255)ballrobotern ((cid:228)hnlich der Middle-

Sized Liga) bis zu Themenrobotern, wie z. B. Spon-

ge Bob, Tom und Jerry und andere, die auf vorge-

fertigten Parcours umherfahren. Der Robotik-Anteil

reduziert sich hier auf ein einfaches fest implemen-

Abbildung 5: Junior-League-

Roboter

tiertes Verhalten, wie z. B. dem Folgen einer schwarzen Linie. In erster Linie soll der

Nachwuchs Interesse an der Robotik entwickeln und sich spielerisch der Thematik wid-

men.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 7 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

2. Standard Platform League im Projekt

Das RoboCup Projekt zielt auf die Teilname an der

Standard Platform League ab. Wie bereits oben er-

w(cid:228)hnt, treten in diesem Wettkampf humanoide Ro-

boter zum Fu(cid:255)ballspielen an. Die Roboter dieser Li-

ga werden von der franz(cid:246)sischen Firma Aldebaran

Robotics hergestellt. Die Schwierigkeit liegt in der

Programmierung der Roboter, da die Hardware un-

ver(cid:228)ndert bleiben muss. Ziel ist es, autonom Fu(cid:255)ball

zu spielen. Sobald ein Spiel gestartet ist, d(cid:252)rfen von

au(cid:255)en keinerlei Eingri(cid:27)e mehr erfolgen. Die Roboter

m(cid:252)ssen also von sich aus z. B. Ball und Tor erken-

Abbildung 6: Nao-Roboter auf dem

Testfeld

nen k(cid:246)nnen, um dann auf das Tor schie(cid:255)en zu k(cid:246)nnen. Dazu sind Eigenschaften, wie eine

gute Selbstlokalisierung und ein Weltmodell unabdingbar. Die Arbeiten im Projekt ori-

entieren sich an den Richtlinien der Standard Platform League des RoboCups. Daraus

ergeben sich unter anderem die folgenden Teilgebiete

• Objekterkennung

• Kollisionserkennung

• Bewegungsabl(cid:228)ufe

• Verhalten

• Hardware des Roboters ansteuern

2.1. Objekterkennung

Die Objekterkennung im Kontext des RoboCups beeinhaltet das Erkennen von Ball, Tor

und Spielfeld. Dabei gibt es verschiedene Anhaltspunkte, um dies zuverl(cid:228)ssig zu erreichen.

Die Tore haben unterschiedliche Farben, aber gleiche Formen. Zur Unterscheidung der

Tore ist also haupts(cid:228)chlich die Farbe von Bedeutung. Das Spielfeld hat charakteristische

Linien, anhand derer man sich orientieren kann. Der Ball ist, auch wenn das mittlerweile

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 8 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

nicht mehr erstrebenswert ist, rot und kann so relativ gut auf dem Spielfeld gesehen

werden. Es gab dieses Jahr aber unterschiedliche Rott(cid:246)ne, sodass die Farbe allein nicht

mehr ausreichend war, um den Ball zuverl(cid:228)ssig zu (cid:28)nden.

2.2. Kollisionserkennung

Durch die vier Ultraschallsensoren in der Brust ist der Nao in der Lage, dicht vor ihm

be(cid:28)ndliche Gegenst(cid:228)nde, z. B. andere Roboter oder einen Torpfosten, zu erkennen und
ihnen gegebenfalls auszuweichen. Dies ist besonders hilfreich, um Strafen wegen pushing[7,

Seite 20] zu vermeiden.

2.3. Bewegungsabl(cid:228)ufe

Jeder Vorgang hat einen eigenen Bewegungsablauf. Damit alles (cid:18)wie aus einem Guss(cid:16) wirkt

und auch von der Geschwindigkeit her ausreichend ist, m(cid:252)ssen die die Bewegungsabl(cid:228)ufe

intensiv analysiert werden. So gab es dieses Jahr gro(cid:255)e Unterschiede beim Schie(cid:255)en des

Balles. Viele Teams lie(cid:255)en den Roboter daf(cid:252)r das Gewicht auf einen der beiden F(cid:252)(cid:255)e

verlagern, er kippte also leicht zur Seite. Dann holte er mit dem anderen Fu(cid:255) aus, um zu

schie(cid:255)en. Insgesamt dauerte der Vorgang zu lange, sodass im Spiel mehrfach ein Schien-

bein des Gegners getro(cid:27)en wurde, weil der Ball sich nicht mehr vor dem Fu(cid:255) des Roboters

befand, als der eigentliche Schuss ausgef(cid:252)hrt wurde. Andere Teams hingegen lie(cid:255)en den

Roboter lediglich den Fu(cid:255) schnell nach vorne bewegen, was sich in der Umsetzung we-

sentlich komplizierter gestaltet, als zu vermuten w(cid:228)re. Denn auch hier muss nat(cid:252)rlich die

Balance gehalten werden, etc. Es war im Vergleich zum klassischen Schuss allerdings sehr

e(cid:27)ektiv, weil es deutlich schneller ging.

2.4. Verhalten

Dieser Teilbereich ist noch nicht sehr ausgepr(cid:228)gt, wenn man das Teamplay mit einbezieht.

Ein Spiel besteht aus mehreren Phasen, und in jeder Phase muss sich der Roboter anders

verhalten. Ein grunds(cid:228)tzliches Verhalten der Roboter besteht also aus mindestens einem

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 9 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Teilverhalten f(cid:252)r jede Phase. Wie dieses Verhalten aussieht, ist allerdings von Team zu

Team verschieden. Vom simplen Finden und ins Tor schie(cid:255)en des Balles bis zum Ausspielen

des Gegners per Seitenschuss oder gar Passspiel ist alles vorhanden. Das Zusammenspiel

der Roboter im Team ist noch in der Findungsphase. Gr(cid:246)(cid:255)ere Ziele zu verfolgen, ist jedoch

schwierig, wenn die Roboter noch immer mit der Bewegung k(cid:228)mpfen.

2.5. Hardware des Roboters ansteuern

Sinnvoll ist z. B., die vorhandenen LEDs zu nutzen, um dem Team w(cid:228)hrend eines Spiels

R(cid:252)ckmeldung zu geben (cid:252)ber das, was der Roboter gerade tut. In dieser Phase ist das die

einzige M(cid:246)glichkeit, etwas von den Robotern zu erfahren, da sie im Spiel autonom agieren

m(cid:252)ssen und daher keinerlei Verbindung zu ihnen hergestellt werden darf. So k(cid:246)nnte man

beispielsweise eine Farbkodierung der Augen-LED benutzen, um das Ball-Tracking (das
Verfolgen des Balles allein mit Blicken) anzuzeigen. Eine m(cid:246)gliche Kombination w(cid:228)re Auge
rot f(cid:252)r Ball nicht gefunden, Auge gelb f(cid:252)r Ball suchen sowie Auge gr(cid:252)n f(cid:252)r Ball gefunden.

Unser Team hat sich im Projekt RoboCup der Objekterkennung (cid:21) und hier speziell der

Ballerkennung (cid:21) gewidmet.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 10 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

3. Aufgabenstellung

Die konkrete Aufgabenstellung lag in der Entwicklung einer e(cid:30)zienten Ballerkennung

unter Ber(cid:252)cksichtigung des Einsatzkontextes und der zugrunde liegenden Hardware. Der

Roboter nimmt mit der Kamera fortlaufend Bilder auf, diese werden vorsegmentiert und

auf Vorhandensein eines Balls gepr(cid:252)ft. Schlu(cid:255)endlich soll die Ballerkennung anhand einer

Abweichungsfunktion berechnen, ob es sich um einen Ball handelt.

Folgende Eigenschaften galt es zu ber(cid:252)cksichtigen

• Eigenschaften der Roboter

(cid:21) x86 AMD GEODE 500 MHz CPU

(cid:21) 256 MB SDRAM

(cid:21) 2 GB Flash Memory

(cid:21) OS (Embedded Linux)

(cid:21) Kameraau(cid:29)(cid:246)sung 640 x 480 px

(cid:21) Kameraframerate 30 fps

(cid:21) Neigungswinkel des Kopfes -39◦ - +30◦

• Eigenschaften der Spielregeln

(cid:21) Daten(cid:252)bertragung im Wireless-Lan

(cid:21) Keine Deckenkamera

(cid:21) Keine Markierungselemente am Feldrand

(cid:21) Anzahl der Roboter im Spiel

Als Basis f(cid:252)r unsere Ballerkennung dienen so genannte Regions of Interest (ROI). Hierbei

handelt es sich um nicht vorsegmentierte Bilder der Gr(cid:246)(cid:255)e 12 x 12 Pixel, welche von der

bereits existierenden Bildverarbeitungssoftware in einem Datenformat des Frameworks

VIGRA [6] bereitgestellt werden. Diese sogenannten ROIs sollen im weiteren Verlauf dar-

auf untersucht werden, ob sie einen Ball enthalten. Die Einbettung der Ballerkennung

in den Kontext Fu(cid:255)ball spielender Roboter stellt Anforderungen an Echtzeitf(cid:228)higkeit der

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 11 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Ballerkennung mit weichen Echtzeitanforderungen. Dies bedeutet in unserem Fall, dass

ein Fehler in der Ballerkennung zwar zu einem Gegentor f(cid:252)hren kann, aber keinen Schaden

an der Hardware zur Folge hat.. Das bedeutet, dass die Bilder innerhalb von fest vorge-

gebenen Zeitgrenzen segmentiert und durch die Ballerkennung gepr(cid:252)ft werden, um eine

Wahrscheinlichkeit f(cid:252)r das Enthaltensein des Balls zur(cid:252)ckzugeben. Die Zeitbedingungen

werden zum einen durch die maximale Bildrate der Kamera beschr(cid:228)nkt. Allerdings l(cid:228)sst

die derzeitige Fortbewegungsgeschwindigkeit der Roboter und die daraus resultierende

geringe Spielgeschwindigkeit zu, dass eine Verarbeitung von 30 Bildern pro Sekunde f(cid:252)r

eine e(cid:30)ziente Objekterkennung und Ballverfolgung ausreichend sind. Da bei zeitweiligem

(cid:220)berschreiten der Zeitanforderungen kein Schaden entsteht und die Ergebnisse f(cid:252)r den

weiteren Spielverlauf verwendet werden k(cid:246)nnen, sind keine harten Echtzeitanforderungen

gegeben.

4. Vor(cid:252)berlegungen

4.1. Schwierigkeiten der Objekterkennung

Die gro(cid:255)en Herausforderungen der Objekterkennung sind der Umgang mit wechselnden

Lichtverh(cid:228)ltnissen, die Verdeckung des gesuchten Gegenstands sowie hardwareseitig die

Leistungsf(cid:228)higkeit des Rechners aufgrund der gro(cid:255)en Datenmengen von Bildern und die

Gew(cid:228)hrleistung von Echtzeitf(cid:228)higkeit.

Wechselnde Lichtverh(cid:228)ltnisse sorgen beispielsweise daf(cid:252)r, dass Objekte je nach Lichtein-

strahlung heller oder dunkler erscheinen. Bei der Untersuchung eines Bildes weist ein und

dasselbe Objekt somit unterschiedliche RGB-Farbwerte auf, je nachdem wo es aufgenom-

men wurde.

Das wohl gr(cid:246)(cid:255)te Problem, f(cid:252)r das bisher keine L(cid:246)sungsans(cid:228)tze gefunden werden konnten,

ist jedoch das Bildverstehen.

Unsere Roboter besitzt kein semantisches Modell von einem Ball. Er hat keine Erfah-

rungswerte bez(cid:252)glich der Eigenschaften eines Balles und wei(cid:255) somit nicht, wie dieser

in bestimmten Situationen aussehen kann. Somit k(cid:246)nnen wir nicht erwarten, dass der

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 12 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Roboter das Erkennen eines Balls veri(cid:28)ziert, sondern lediglich, dass er erkennt, ob das

Ball-Pr(cid:228)dikat (die f(cid:252)r seine Entscheidung relevanten Eigenschaften des Balls) erf(cid:252)llt ist.

Die Physiologie des menschlichen Sehens erm(cid:246)glicht es dem Menschen, das Gesehene auf

verschiedene Weise zu interpretieren. So vervollst(cid:228)ndigt unser Gehirn beispielsweise Kan-

ten von zwei sich (cid:252)berlagernden Objekten, selbst wenn diese auf einem Bild wegen einer

Farb(cid:228)hnlichkeit tats(cid:228)chlich gar nicht vorhanden sind. Ein Roboter hingegen sieht nur das,

was wirklich da ist. Kantenvervollst(cid:228)ndigung ist bei Robotern zwar m(cid:246)glich, jedoch in der

Standardausf(cid:252)hrung unserer Roboter nicht vorhanden.

4.2. Annahme

Zun(cid:228)chst erfassten wir die Eigenschaften des zu erkennenden Objektes, in unserem Falle

die Eigenschaften des Balles. F(cid:252)r die Ballerkennung im Rahmen des RoboCups k(cid:246)nnen

folgende Eigenschaften vorausgesetzt werden

Die Ballfarbe wird vom Veranstalter vorgegeben, in diesem Jahr ein kr(cid:228)ftiges Rot.

Der Farbverlauf wird von der Beleuchtung beein(cid:29)usst. Das Spielfeld wird durch eine

Deckenbeleuchtung erhellt. Diese ist meist zentral (cid:252)ber der Mitte des Spielfelds

angebracht. Bei der Gr(cid:246)(cid:255)e des Spielfeldes und der relativen Entfernung der Decken-

beleuchtung sowie aller m(cid:246)glichen Positionen des Balls auf dem Spielfeld kann ein

konstanter Farbverlauf in der Mitte des Balls ermittelt werden. Ein konstanter Farb-

verlauf bedeutet, dass die ˜nderung des Farbwertes f(cid:252)r alle ROIs denselben Verlauf

nimmt. Eine Farbwertberechnung, die das ambiente Licht der Halle und die sehr

intensive Punktlichtquelle beinhaltet ergibt folgendes Muster:

Werde der Ball vollst(cid:228)ndig auf einem 12 x 12 Pixel gro(cid:255)em 2 dimensionalem Bild ab-

gebildet. Der Mittelpunkt des Balls be(cid:28)ndet sich hierbei exemplarisch im Nullpunkt

eines kartesischen Koordinatensystems. Dann erkennt man stets eine abnehmende

Helligkeit und einen st(cid:228)rker werdenden Rot-Ton entlang der abnehmenden y-Achse,
also von y = 1 bis y = 10, in der Mitte des Balls, also von x = 5 bis x = 6.

Dieser Farbverlauf entsteht u.a. durch die Form des Balles und dadurch, dass die

Deckenbeleuchtung (cid:252)ber dem Spielfeld sehr viel intensiver ist als sonstige umge-

bende Lichtquellen der Halle. So ist eine deutliche Unterscheidung zwischen dem

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 13 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Ball und anderen gleichfarbigen Objekten wie z. B. dem T-Shirt eines Kindes am

Spielfeldrand.

Der Ballschatten resultiert aus der Beleuchtung. Aus der zuvor beschriebenen Beleuch-

tung und der Form des Balls ergibt sich eine weitere Eigenschaft, die man sich f(cid:252)r

eine Ballerkennung zu Nutze machen kann: der Ballschatten. Dieser hat w(cid:228)hrend

des Spiels einen immer gleichen Verlauf. Er be(cid:28)ndet sich zentral unter dem Ball

und hat stets den gleichen Helligkeitswert, sofern die Lichtquellen nicht von ande-

ren Robotern oder den Schiedsrichtern verdeckt werden. Tats(cid:228)chlich treten geringe

Abweichungen des Helligkeitswertes auf, wenn sich die Position des Balles von der

Spielfeldmitte zum Spielfeldrand verlagert. Allerdings werden diese bedingt durch

die Eigenschaften der Roboterkamera auf dem 2D-RGB-Bild nicht dargestellt.

Die Ballgr(cid:246)(cid:255)e ist vorgegeben, deren Abbildung auf der Kamera des Roboters (cid:228)ndert sich

jedoch in Abh(cid:228)ngigkeit der relativen Entfernung zum Roboter. Die runde Form des

Balls kann im Rahmen des Wettkampfes f(cid:252)r eine e(cid:30)ziente Objekterkennung genutzt

werden, muss allerdings aufwendig implementiert werden und ist zum Zeitpunkt

dieser Arbeit noch nicht geplant.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 14 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

5. Ausgangssystem

Die Ballerkennung wird in das bereits vorhandene NodeFramework [2] von Steven K(cid:246)h-

ler integriert und benutzt die Bildverarbeitungbibliothek VIGRA [6] sowie das Multi-

Sensordaten-Fusion-Framework [3] von Janis Sch(cid:246)nefeld. Die Vorverarbeitung rechnet das

Kamerabild von 640 x 480 Pixeln auf 160 x 120 Pixel herunter, um eine Echtzeitbearbei-

tung zu gew(cid:228)hrleisten. Das neue Bild wird segmentiert und in Regions of Interest (ROI)

zerteilt. ROIs enthalten Feldlinien-, Torelement- oder Ballkandidaten. Die Ballkandida-

ten werden als unsegmentiertes 12 x 12 Pixel Bild (cid:252)bergeben. Der Ball kann komplett,

teilweise, teilweise verdeckt oder gar nicht auf dem Bild zu sehen sein.

6. Realisierung

6.1. Ansatz

Die Ballveri(cid:28)kation wird in dieser Arbeit auf der Basis eines Histogrammvergleichs durch-

gef(cid:252)hrt. Ziel dieses Vergleiches ist es, unabh(cid:228)ngig von Umgebungslicht und anderen (cid:228)u-

(cid:255)eren Ein(cid:29)(cid:252)ssen, den Ball m(cid:246)glichst eindeutig zu identi(cid:28)zieren. Zun(cid:228)chst ben(cid:246)tigen wir

eine Basis von ROIs. Diese Basis enth(cid:228)lt sowohl (cid:18)gute(cid:16) als auch (cid:18)schlechte(cid:16) Bilder. Ein

(cid:18)gutes(cid:16) Bild enth(cid:228)lt dabei eine von der Vorverarbeitung ausgew(cid:228)hlte ROI, in der ein Ball

enthalten und auch als solcher leicht zu erkennen ist. Die Bewertung der ROIs erfolgt da-

bei durch den Menschen mit Hilfe einer gra(cid:28)schen Ober(cid:29)(cid:228)che in zwei Kategorien. Durch

mehrfache positive oder negative Auswahl k(cid:246)nnen Bilder mit starken positiven oder ne-

gativen Eigenschaften h(cid:246)her bewertet werden als Bilder mit schwachen Eigenschaften.

Aus der Basis der (cid:18)guten(cid:16) und (cid:18)schlechten(cid:16) ROIs wird ein durchschnittliches Histogramm

in den von uns ausgew(cid:228)hlten Farbr(cid:228)umen erstellt, an dem sp(cid:228)ter die Ball-Kandidaten

gemessen werden.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 15 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

(a) (cid:18)Gute(cid:16) ROI

(b) (cid:18)Schlechte(cid:16) ROI

Abbildung 7: Beispiel-ROIs die von der Vorverarbeitung ausgew(cid:228)hlt wurden

6.2. Histogramm

Die Histogramme werden auf Basis der 12x12 Pixel ROIs erstellt. Jedes Bild hat somit 144

Pixel, von denen wir lediglich 20 Pixel bewerten, die jeweils drei Werte (Rot, Gr(cid:252)n und

Blau) enthalten. Jeder Punkt im Histogramm gibt an, wie oft der Farbwert (z. B. Gr(cid:252)n)

in einer Intensit(cid:228)t vorkommt. Die H(cid:228)u(cid:28)gkeit wird dabei auf der y-Achse aufgetragen, die

Intensit(cid:228)t auf der x-Achse.

Die durchschnittlichen Histogramme werden durch Aufsummieren der Intensit(cid:228)tsh(cid:228)u(cid:28)g-

keiten der Einzelbildhistogramme erstellt und durch die Anzahl der Testbilder dividiert.

Ein Wert von 0.1 bei 255 bedeutet also, dass in jeder zehnten Ballkandidaten ROI ein

Pixel mit der roten Intensit(cid:228)t von 255 vorkommt bzw. in 99 keiner und in einem 10.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 16 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

6.3. Farbr(cid:228)ume

6.3.1. RGB

0.1

8 · 10−2

6 · 10−2

4 · 10−2

2 · 10−2

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Red
Green
Blue

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 8: Durchschnittshistogramm der positiven Ball-ROIs im RGB-Farbraum

0.1

8 · 10−2

6 · 10−2

4 · 10−2

2 · 10−2

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Red
Green
Blue

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 9: Durchschnittshistogramm der negativen Ball-ROIs im RGB-Farbraum

In dieser Arbeit verwenden wir sowohl den RGB Farbraum als auch den HSV-Farbraum.

Der RGB-Farbraum bietet sich nicht nur aufgrund der bereits im RGB-Format vorlie-

genden ROIs an. Der von dem SPL-Reglement vorgeschriebene Ball ist vorwiegend rot,

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 17 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

w(cid:228)hrend das Spielfeld gr(cid:252)n und Roboter und Feldlinien wei(cid:255) sind. Aufgrund dieser Farben

erhalten wir im RGB Vergleichshistogramm eine sehr spezi(cid:28)sche Kennlinie f(cid:252)r den Ro-

tanteil, welcher im Wertebereich von 230 bis 256 ein starke H(cid:228)u(cid:28)gkeit aufweist, w(cid:228)hrend

die Werte f(cid:252)r Blau und Gr(cid:252)n eine deutlich (cid:29)achere Kurve aufweisen und im mittleren

Wertesegment (Blau: 55 - 150,Gr(cid:252)n: 90 - 180) geh(cid:228)uft auftreten (siehe Abbildung 8). Das

durchschnittliche Histogramm der positiv bewerteten ROIs unterscheidet sich vor allem in

der Auspr(cid:228)gung der roten Kennlinie. Auf den ersten Blick (cid:228)hnelt der Verlauf der Kennlinie

der negativen ROIs aus Abbildung 9 der Kennlinie der positiven ROIs aus Abbildung 8.

Auf der y-Achse ist jedoch zu erkennen, dass die rote Kennlinie der positiven ROIs mehr

als vier mal so stark ausgepr(cid:228)gt ist. Die blauen und gr(cid:252)nen Kennlinien unterscheiden sich

in beiden Histogrammen kaum, verlaufen aber bei den negativ bewerteten ROIs etwas

di(cid:27)user.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 18 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Lasse Einig
Kay Peikert

6.3.2. HSV

·10−2

3

2

1

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Hue
Saturation
Value

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 10: Durchschnittshistogramm der positiven Ball-ROIs im HSV-Farbraum

·10−2

3

2

1

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Hue
Saturation
Value

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 11: Durchschnittshistogramm der negativen Ball-ROIs im HSV-Farbraum

Der HSV-Farbraum wird, anders als der RGB-Farbraum, nicht durch die einzelnen Farb-
komponenten beschrieben, sondern repr(cid:228)sentiert vor allem Helligkeit (Value) und Farb-
s(cid:228)ttigung (Saturation). Zus(cid:228)tzlich gibt der Farbwinkel (Hue) den Farbton an, welcher aus

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 19 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

einem Farbkreis abgelesen wird. Die Ballfarbe liegt im roten Bereich, zwischen 320◦ und
40◦. (cid:220)berbelichtete bzw. unterbelichtete Bereiche sollten nicht ber(cid:252)cksichtigt werden.

Im Vergleich der beiden durchschnittlichen Histogramme im HSV-Farbraum f(cid:252)r positive

und negative Ballkandidaten sehen wir eine deutliche Di(cid:27)erenzierung zwischen den Kenn-

linien beider Histogramme f(cid:252)r Farbton (Hue) und S(cid:228)ttigung (Saturation), w(cid:228)hrend die
Werte f(cid:252)r Helligkeit (Value) einen (cid:228)hnlichen Verlauf zeigen. Der Schnitt an der 360◦/0◦-
Marke wird durch die Gl(cid:228)ttung der Kurve verursacht und entsteht aufgrund der Skalierung

auf den RGB Farbraum auf 255 Werte an der x-Achse bei 255. Das Histogramm der positi-

ven Beispiele weist eine starke H(cid:228)ufung im roten (im Histogramm 250 bis 15) und orangen

(im Histogramm 15 bis 25) Farbton auf. Im negativen Histogramm ist der Spitzenwert

erst bei 40 (gelb-gr(cid:252)ner Farbton) erreicht und die Kurve verl(cid:228)uft deutlich (cid:29)acher. Des

Weiteren sind im negativen Histogramm deutlich mehr unges(cid:228)ttigte Farben vorhanden (0

bis 40) als im Histogramm mit den positiven Beispielen (40 bis 80).

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 20 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

7. Funktionsweise und Implementierung der

Ballveri(cid:28)kation
200

Negative
Positive

100

0
30

35

40

45

50
Bewertung in %

55

60

65

70

Abbildung 12: Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im RGB-Farbraum

Negative
Positive

200

100

0
30

35

40

45

50
Bewertung in %

55

60

65

70

Abbildung 13: Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im HSV-Farbraum

mit Helligkeit

Negative
Positive

200

100

0
30

35

40

45

50
Bewertung in %

55

60

65

70

Abbildung 14: Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im HSV-Farbraum

ohne Helligkeit

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 21 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Wie zuvor erw(cid:228)hnt, basiert unsere Ballveri(cid:28)kation auf einer berechneten Abweichung von

dem Histogramm des zu bewertenden Bildes und den Durchschnittshistogrammen (cid:18)gut(cid:16)

bzw. (cid:18)schlecht(cid:16). Zun(cid:228)chst m(cid:252)ssen daf(cid:252)r Histogramme vorliegen, die wir nat(cid:252)rlich erst

erstellen m(cid:252)ssen.

Hierf(cid:252)r sind grunds(cid:228)tzlich drei Schritte n(cid:246)tig

1. Normalisierung auf 250

2. Gau(cid:255)-Gl(cid:228)ttung

3. Normalisierung auf die Fl(cid:228)che

Das folgende Vorgehen ist f(cid:252)r jede neue Testumgebung durchzuf(cid:252)hren.

Wir beschreiben das Vorgehen f(cid:252)r die Durchschnittshistogramme, die mit hoher Wahr-

scheinlichkeit einen Ball darstellen. Dazu ben(cid:246)tigen wir Bilder, auf denen der Ball ent-

sprechend gut zu erkennen ist. Die Bilder liegen bereits in einer Gr(cid:246)(cid:255)e von 12 x 12 Pixeln

(ausgeschnitten aus dem Kamerabild) vor. Dies verringert den sp(cid:228)teren Rechenaufwand

erheblich. Die nun beschriebenen Verfahren m(cid:252)ssen je f(cid:252)r alle Farbkan(cid:228)le gemacht werden.

Au(cid:255)erdem einmal im RGB-Farbraum, sowie im HSV-Farbraum. Also im RGB-Farbraum

f(cid:252)r Rot, Gr(cid:252)n und Blau, im HSV-Farbraum f(cid:252)r Hue, Saturation und Value. Wir beschr(cid:228)n-

ken uns hier auf die Beschreibung im RGB Farbraum (konkret auf den roten Farbkanal),

da das Vorgehen f(cid:252)r die restlichen Kan(cid:228)le, sowie f(cid:252)r den HSV-Farbraum identisch ist.

Ein Histogramm sei im Folgenden ein Bild mit den Ma(cid:255)en 256 x 1 Pixel.

Von diesen 144 Pixeln betrachten wir im Folgenden nur 5 <= x <= 6 und 1 <= y <= 10,

also 20 Pixel pro Bild. Diese 20 Pixel bilden die Basis f(cid:252)r die Erstellung der Histogramme.

Auf der x-Achse werden die einzelnen Farbwerte repr(cid:228)sentiert, die y-Achse die tats(cid:228)chliche

H(cid:228)u(cid:28)gkeit des Farbwertes in allen Bildern. F(cid:252)r jedes dieser 20 Pixel wird der Farbwert

ermittelt und der entsprechende Wert im Histogramm inkrementiert um Eins. Als Beispiel:

Hat jedes unserer 224 Testbilder in den 20 betrachteten Pixeln denselben Farbwert (hier
zur Veranschaulichung 144), h(cid:228)tte das Histogramm bei x = 144 den Wert y = 4480.

Dieses Beispiel verdeutlicht die Notwendigkeit von Schritt 1 (dem Normalisieren auf 250).

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 22 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Zu 1. Wir brauchen einen Normalisierungsfaktor, der sich ergibt aus 250 dividiert durch

den maximalen Farbwert im Histogramm (im vorherigen Beispiel 4480). 250 ist ge-

w(cid:228)hlt, da die Werte in einem RGB-Bild gespeichert werden, welches maximal Werte

bis 256 halten kann. Jetzt f(cid:252)llen wir ein neues 256 x 1 Pixel gro(cid:255)es Bild pixel-

weise mit Farbwert * Normalisierungsfaktor. Nun liegt ein auf 250 normalisiertes

Histogramm vor.

Zu 2. Auf das in Schritt 1 erstellte Histogramm wird nun eine Gau(cid:255)-Gl(cid:228)ttung angewandt.[4,

Seite 79]

Zu 3. Weil nach Ausf(cid:252)hrung aller Berechnungen eine Aussage getro(cid:27)en werden soll, mit

welcher Wahrscheinlichkeit es sich bei den untersuchten Bildmotiven um einen Ball

handelt, m(cid:252)ssen wir unser Histogramm noch auf die Fl(cid:228)che normalisieren. Gemeint
ist, dass die Fl(cid:228)che von x = 0 bis x = 256 und y = 0 bis y = 250 den Wert 1 (also

100%) ergeben soll. Dazu m(cid:252)ssen wir nun (cid:228)hnlich wie in Schritt 1 vorgehen. Da wir

nun Werte zwischen 0 und 1 erhalten wollen, berechnen wir zun(cid:228)chst den Norma-

lisierungsfaktor. Dieser ergibt sich aus 1 dividiert durch den maximalen Farbwert

in dem aus 2. gewonnen Histogramm. Entsprechend 1. wird nun der Farbwert jedes

Pixels mit dem so ermittelten Normalisierungsfaktor multipliziert.

Diese Drei Schritte f(cid:252)hren wir f(cid:252)r jedes zu bewertende Bild und die Testbilder durch,

sodass wir letztendlich folgende Histogramme erhalten:

• Histogramm vom zu bewertenden Bild

• Histogramm von den Testbildern (RGB gut)

• Histogramm von den Testbildern (RGB schlecht)

• Histogramm von den Testbildern (HSV gut)

• Histogramm von den Testbildern (HSV schlecht)

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 23 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Diese Histogramme sind nun Grundlage f(cid:252)r die eigentliche Bewertung. Auch dieser Vor-

gang erfolgt in Drei Schritten.

1. Berechnung der Abweichung (Histogramm bewertendes Bild zu Histogramm der

Testbilder)

2. Umwandlung der Abweichung in Prozentangaben

3. Bewertung der in 2. errechneten Angaben / (cid:18)Ballentscheidung(cid:16)

Zu 1. Wir berechnen pixelweise die Di(cid:27)erenz (Testbildhistogramm (gut / schlecht) - Hi-

stogramm zu bewertendes Bild). Dies Rechnung f(cid:252)r jeden einzelnen Farbkanal in

beiden Farbr(cid:228)umen.

Zu 2. Aus den in 1. berechneten Abweichungen m(cid:252)ssen nun Prozentwerte generiert wer-

den. Die Absolutwerte der Di(cid:27)erenzen in 1. (gilt wieder f(cid:252)r beide Farbr(cid:228)ume) wer-

den getrennt nach gut und schlecht aufsummiert und dann durch 6 (3 Kan(cid:228)le f(cid:252)r

gut und 3 Kan(cid:228)le f(cid:252)r schlecht) dividiert. Anschlie(cid:255)end berechnen wir die Di(cid:27)erenz
schlecht−gut+1
2

und wandeln diese durch Multiplikation mit 100 in einen Prozentwert

um.

Zu 3. Wir teilen die Prozentskala (0 - 100) in drei Bereiche. Dazu w(cid:228)hlen wir eine un-
tere Schranke u und eine obere Schranke o. Alle Werte < u werden nicht als Ball
anerkannt, Werte zwischen u und o gelten als unsicher, Werte > o sind als Ball
anerkannt. In praktischen Tests erwiesen sich die Werte u = 40% und o = 60% als

sinnvoll, in anderen Testumgebungen k(cid:246)nnten andere Werte sinnvoller sein.

Anzahl schlechter ROI im Wertebereich

Anzahl guter ROI im Wertebereich

83

1

19

15

6

459

x < 47

47 <= x <= 49

49 < x

Tabelle 1: Konfusionsmatrix im HSV-Farbraum ohne Helligkeitsbewertung f(cid:252)r eine drei-

stu(cid:28)ge Bewertung

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 24 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

40

20

0

45

46

47

48

49

50
52
51
Bewertung in %

53

54

55

56

57

Abbildung 15: Ausschnitt Abbildung 12

40

20

0

45

46

47

48

49

50
52
51
Bewertung in %

53

54

55

56

57

Abbildung 16: Ausschnitt Abbildung 13

40

20

0

45

46

47

48

49

50
52
51
Bewertung in %

53

54

55

56

57

Abbildung 17: Ausschnitt Abbildung 14

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 25 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

8. Bewertung unseres Verfahrens

Die Vorteile des HSV-Farbraum Verfahrens ohne Helligkeitsber(cid:252)cksichtigung w(cid:252)rde sich

mit entsprechenden Testbildern noch klarer hervorheben lassen.

Anhand der Bewertungsdaten ist zu erkennen, dass sich von den drei ausgew(cid:228)hlten Bewer-

tungsverfahren der HSV-Farbraum ohne Helligkeitsbewertung am besten f(cid:252)r die eindeuti-

ge Identi(cid:28)zierung von Ballkandidaten eignet. Der Anteil an falsch identifzierten ROIs ist

minimal, gleichzeitig ist der Schnittpunkt der Kennlinien klar erkennbar. Die Verbesse-

rung zwischen den beiden HSV-Farbraum-Verfahren ist relativ gering, weil alle Testbilder

unter denselben Bedingungen entstanden sind. Der Sonnenlicht-Anteil im Testraum war

relativ gering und die k(cid:252)nstliche Beleuchtung stark und gleichm(cid:228)(cid:255)ig.

Das Bewertungsergebnis des Verfahrens l(cid:228)sst sich am besten mit einem dreistu(cid:28)gen Ma(cid:255)-

stab benutzen. Der Grenzbereich zwischen 47 % und 52 % wird als nicht eindeutig ein-

gestuft. Der Bereich 0 % - 46 % wird als eindeutig kein Ball und 53 % - 100 % eindeutig

als Ball aufgefasst. Dies bietet sich vor allem an, wenn die Ballbeweisprozedur nicht auf

einem Einzelbild sondern auf einer Folge von mindestens zwei Bildern basiert. Bei ersten

Live-Tests auf der German Open 2011 in Magdeburg und im Labor konnte das Ergebnis

best(cid:228)tigt werden.

Unsere praktischen Tests waren sehr erfolgreich. Der Roboter (cid:28)ndet zuverl(cid:228)ssig den Ball.

In Bezug auf die Verwendung f(cid:252)r autonome Roboter w(cid:228)hrend des Spiels ist unsere Imple-

mentation aus e(cid:30)ziensgr(cid:252)nden nicht brauchbar. Die erwarteten 30 fps werden momentan

nicht erreicht. Die Kamera liefert zwar 30 Bilder/Sekunde jedoch k(cid:246)nnen diese nicht ver-

arbeitet werden. Eine E(cid:30)zienzsteigerung ist m(cid:246)glich, wenn man nicht f(cid:252)r jedes neue Bild

ein Histogramm der Testbilder erstellt sondern dies nur im Fall neuer Testumgebungen

und neuer Testbilder erstellt und dann nur f(cid:252)r die Berechnung der Abweichung benutzt.

Bei den praktischen durchgef(cid:252)hrten Tests war der Roboter mit einem Rechner verbunden,

auf dem die Ballveri(cid:28)kation berechnet wurde. Die Rechenleistung des Computers erreichte

die Geschwindigkeit, sodass wir unsere Implementation erfolgreich einsetzen konnten.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 26 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

9. Fazit

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

Das oben beschriebene Verfahren funktioniert sehr gut, kann aber in Zukunft durch eine

kantenbasierte Ballerkennung erg(cid:228)nzt werden um die Robustheit gegen(cid:252)ber wechselnden

Lichtverh(cid:228)ltnissen zu erreichen.

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 27 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

10. Anhang

0.1

5 · 10−2

t
i
e
k
g
(cid:28)
u
(cid:228)
H

0

Negative
Positive

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 18: Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den roten

Kanal

0.1

Negative
Positive

5 · 10−2

t
i
e
k
g
(cid:28)
u
(cid:228)
H

0

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 19: Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den gr(cid:252)-

0.1

5 · 10−2

t
i
e
k
g
(cid:28)
u
(cid:228)
H

0

nen Kanal

Negative
Positive

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 20: Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den blauen

Kanal

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 28 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

·10−2

Negative
Positive

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

3

2

1

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Abbildung 21: Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den Hue-

Kanal

·10−2

3

2

1

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Negative
Positive

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

Abbildung 22: Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den

Saturation-Kanal

·10−2

Negative
Positive

0

20
Intensit(cid:228)t

40

60

80

100 120 140 160 180 200 220 240

3

2

1

0

t
i
e
k
g
(cid:28)
u
(cid:228)
H

Abbildung 23: Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den Value-

Kanal

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 29 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

4

5

6

6

7

8

Abbildungsverzeichnis

1

SPL-Spielfeld mit Naos . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2 Middle-Size Roboter auf ihrem Spielfeld . . . . . . . . . . . . . . . . . . .

3 Mixed-Reality

Roboter auf

einem Bildschirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Rescue-Roboter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Junior-League-Roboter . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Nao-Roboter auf dem Testfeld . . . . . . . . . . . . . . . . . . . . . . . . .

Beispiel-ROIs die von der Vorverarbeitung ausgew(cid:228)hlt wurden . . . . . . . 16

Durchschnittshistogramm der positiven Ball-ROIs im RGB-Farbraum . . . 17

Durchschnittshistogramm der negativen Ball-ROIs im RGB-Farbraum . . . 17

4

5

6

7

8

9

10 Durchschnittshistogramm der positiven Ball-ROIs im HSV-Farbraum . . . 19

11 Durchschnittshistogramm der negativen Ball-ROIs im HSV-Farbraum . . . 19

12 Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im RGB-Farbraum 21

13 Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im HSV-Farbraum

mit Helligkeit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

14 Visualisierung der Bewertung von zuf(cid:228)lligen Ball-ROIs im HSV-Farbraum

ohne Helligkeit

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

15 Ausschnitt Abbildung 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

16 Ausschnitt Abbildung 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

17 Ausschnitt Abbildung 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

18 Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den roten

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

19 Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den gr(cid:252)nen

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

20 Durchschnittshistogramm der Ball-ROIs im RGB-Farbraum f(cid:252)r den blauen

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

21 Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den Hue-

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 30 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

22 Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den Saturation-

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

23 Durchschnittshistogramm der Ball-ROIs im HSV-Farbraum f(cid:252)r den Value-

Kanal

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 31 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

Lasse Einig
Kay Peikert

Literatur

Ballveri(cid:28)kation
Robocup Projektbericht

Anja Richter

[1] Dr. Ansgar Bredenfeld. Robocup GermanOpen. http://www.robocupgermanopen.

de. [letzter Zugri(cid:27) am 06.04.2011].

[2] Steven K(cid:246)hler. Das NodeFramework - Entwurf und Realisierung eines Software-

Frameworks f(cid:252)r robuste, h(cid:246)chstzuverl(cid:228)ssige Anwendungen. Diplomarbeit, Universit(cid:228)t

der Freien und Hansestadt Hamburg, Fachbereich Informatik, Arbeitsbereich Techni-

sche Informatiksysteme, Juni 2011.

[3] Janis Sch(cid:246)nefeld. Real Time Object Recognition in the RoboCup Four Legged League.

Baccarlaureatsarbeit, Universit(cid:228)t der Freien und Hansestadt Hamburg, Fachbereich

Informatik, Arbeitsbereich Technische Informatiksysteme, M(cid:228)rz 2007.

[4] Kristian Bredies und Dirk Lorenz. Mathematische Bildverarbeitung: Einf(cid:252)hrung in

Grundlagen und moderne Theorie. Vieweg+Teubner Verlag, 2010.

[5] Aldebaran Robotics. http://www.aldebaran-robotics.com/en/node/1172. [letzter

Zugri(cid:27) am 08.06.2011].

[6] Generic Programming for Computer Vision. http://hci.iwr.uni-heidelberg.de/

vigra/. [letzter Zugri(cid:27) am 08.06.2011].

[7] RoboCup Rules 2011 SPL.

http://www.tzi.de/spl/pub/Website/Downloads/

Rules2011.pdf. [letzter Zugri(cid:27) am 08.06.2011].

Universit(cid:228)t Hamburg
Betreuer: Janis Sch(cid:246)nefeld

- 32 -

Informatik B.Sc.
WS 2010/11 & SoSe 2011

