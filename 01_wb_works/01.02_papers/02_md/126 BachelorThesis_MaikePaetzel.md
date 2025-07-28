Spielerkoordination in
RoboCup-Fußballspielen mittels
gesprochener Sprache

Bachelorarbeit
im Arbeitsbereich Nat¨urlichsprachliche Systeme, NATS
Prof. Dr.-Ing. Wolfgang Menzel

Department Informatik
MIN-Fakult¨at
Universit¨at Hamburg

vorgelegt von
Maike Paetzel
am
10. Juni 2013

Gutachter: Prof. Dr.-Ing. Wolfgang Menzel

Dr. Werner Hansmann

Maike Paetzel
Matrikelnummer: 6087233
Wurmsweg 1
20535 Hamburg

Zusammenfassung

Zusammenfassung

In der RoboCup Humanoid Kid Size League wird das gesamte Datenvolumen zwi-
schen den Robotern ¨uber ein drahtloses Netzwerk ausgetauscht, obwohl diese Tech-
nik insbesondere w¨ahrend Turnieren sehr st¨oranf¨allig ist und keine menschen¨ahn-
liche Kommunikationsform darstellt.

Die vorliegende Arbeit zeigt einen Ansatz auf, die teaminterne Roboter-Roboter-
Kommunikation auf ein nat¨urlichsprachliches System umzustellen. Es wird dabei
zun¨achst die Hardware des DARwInOP-Roboters vorgestellt und die Eignung f¨ur
Kommunikation durch Sprache analysiert. Dazu werden auch M¨oglichkeiten der
Hardwareerweiterung aufgezeigt, welche die Ergebnisse in diesem Bereich deutlich
verbessern k¨onnen. Weiterhin werden eine Strategie f¨ur die Dialogmodellierung
und den Nachrichtenaustausch entwickelt und verschiedene Ans¨atze der Sprach-
synthese sowie Sprachanalyse aufgezeigt. Es wird dabei auch ber¨ucksichtigt, in wie
weit sich eine solche Architektur in bestehende Softwaresysteme eingliedern l¨asst,
ohne dass eine große Umstrukturierung des Gesamtsystems n¨otig wird.

Das zentrale Element der Arbeit ist die Implementation eines Systems zur
Roboter-Roboter-Kommunikation basierend auf den vorgestellten Modellen zur
Synthese und Analyse von Sprache. Die im Verlauf der Bearbeitung entstandene
Software bietet ein System, das eigenst¨andig Sounddateien einliest, mittels einer
Methode zur Detektion von Sprachbeginn und Sprachende W¨orter ﬁndet und die-
se auf ihren Inhalt hin analysiert. An Hand von Unterschieden in den Frequenzen
kann eine eingelesene Sounddatei automatisch einem Roboter zugeordnet werden.
Die Qualit¨at der Implementation wird im Rahmen dieser Arbeit durch Vergleich
mit einem zuvor vorgestellten Anforderungskatalog untersucht.

Den Schluss bildet ein Ausblick auf weitere m¨ogliche Forschungsans¨atze, die

sich aus dieser Arbeit ergeben k¨onnen.

III

Zusammenfassung

IV

Inhaltsverzeichnis

1 Motivation

2 Die Dom¨ane RoboCup

2.1 Speziﬁkation der Roboterhardware

. . . . . . . . . . . . . . . . . .
2.1.1 Anforderungen an das Lautsprechersystem . . . . . . . . . .
2.1.2 Anforderungen an die Mikrophone . . . . . . . . . . . . . . .
2.1.3 Einschr¨ankungen durch den Prozessor . . . . . . . . . . . . .
2.2 Analyse der Spielabl¨aufe im Hinblick auf den Nachrichtenaustausch
2.3 Einbindung der Kommunikation in das bestehende Softwaresystem .

3 Der Nachrichtenaustausch

3.1 Die Dialogmanagementstrategie . . . . . . . . . . . . . . . . . . . .
3.2 Die Konversationsmodellierung . . . . . . . . . . . . . . . . . . . .
3.3 Die Vermittlungstechnik . . . . . . . . . . . . . . . . . . . . . . . .

4 Konzepte der Spracherzeugung und Sprachverarbeitung

4.1 Sprachsynthese . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.1 Artikulationssynthese . . . . . . . . . . . . . . . . . . . . . .
4.1.2 Formantsynthese . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . .
4.1.3 Verkettungssynthese
4.2 Spracherkennung . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.1 Vorverarbeitung . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2 Analyse von Beginn und Ende einer Sprachaufzeichnung . .
Spracherkennung mit Hilfe eines Mustervergleichs . . . . . .
4.2.3
Stochastische Sprachverarbeitung . . . . . . . . . . . . . . .
4.2.4
. . . . . . . . . . . . . . . . . . . . . . . . . . .

4.3 Verfahrensauswahl

5 Implementation

5.1 Sprachsynthese . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Sprachsynthese . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.1 Auswahl der Programmiersprache . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
5.2.2 Die Softwarearchitektur
5.2.3 Die Energiewertbestimmung . . . . . . . . . . . . . . . . . .
5.2.4 Der Streambuﬀer . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . .
5.2.5 Die Wortanalyse

1

3
4
4
7
8
8
9

11
11
14
14

17
17
17
18
18
18
18
21
22
23
24

25
25
26
26
26
27
28
28

V

Inhaltsverzeichnis

5.2.6
Speicherung der Referenzdaten . . . . . . . . . . . . . . . .
5.2.7 Test- und Analysestruktur . . . . . . . . . . . . . . . . . . .

6 Evaluation und Ergebnisse

6.1 Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1 Einteilung der Sprachdateien in Sektionen . . . . . . . . . .
6.1.2 Bewertung der Detektion von Sprachbeginn und Sprachende
6.1.3 Evaluation der Signalwertverschiebung f¨ur die Sprachaus-
wertung . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.4 Einﬂuss verschiedener Parameter auf die Worterkennung . .
6.1.5

Implementation einer Robotererkennung durch
Frequenzanpassungen . . . . . . . . . . . . . . . . . . . . . .
6.2 Ergebnisse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.1 Auswertung des gew¨ahlten Verfahrens f¨ur Idealdaten . . . .
¨Ubertragung des gew¨ahlten Verfahrens auf Originaldaten . .
6.2.2
6.2.3 Erforderlichkeit des DTW-Algorithmus . . . . . . . . . . . .
6.2.4 Laufzeitanalyse . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . .

7 Ausblick

Literaturverzeichnis

Abbildungsverzeichnis

Anhang

29
30

31
31
31
32

33
35

36
36
36
37
38
38
39

41

45

47

49

VI

Kapitel 1

Motivation

Die Spielerkoordination in RoboCup-Fußballspielen ist eine sehr komplexe Auf-
gabe: Jeder Roboter erstellt sein eigenes lokales Weltbild, in dem er seine eigene
Position, die Position des Balls und der Tore auf dem Spielfeld kennt. Daraus
kann ein Verhalten abgeleitet werden, das den Roboter bis zum Ball laufen und
ein Tor schießen l¨asst. Der Roboter ist jedoch nicht allein auf dem Feld, da zu
einem Team bis zu drei Roboter geh¨oren k¨onnen. Sobald ein zweiter Roboter des
eigenen Teams mit seinem eigenen lokalen Weltbild hinzukommt, ist eine Kom-
munikation zwischen den beiden w¨unschenswert. So kann verhindert werden, dass
sich die Roboter gegenseitig behindern, w¨ahrend sie zum Ball laufen, es k¨onnen
aber auch Unsicherheiten in der Balllokalisation ausgeglichen werden. Sogar kom-
plizierte Spielz¨uge wie ein Pass um einen gegnerischen Roboter herum sind denk-
bar und auch bereits in vielen Ligen realisiert worden. Voraussetzung hierf¨ur ist
ein st¨orungsfreies Kommunikationssystem. Im RoboCup wird den Regeln gem¨aß
W-LAN eingesetzt. In der Praxis zeigt sich aber, dass w¨ahrend des Turniers kei-
nesfalls davon auszugehen ist, dass aktuelle Daten ohne Verz¨ogerung versendet
werden k¨onnen. In Ermangelung einer anderen Kommunikationsm¨oglichkeit set-
zen die Teams daher auf Einzelentscheidungen der Roboter, obwohl dies meist zu
keinem optimalen Ergebnis f¨uhrt.

Da das Fußballspielen im RoboCup nicht Selbstzweck ist, sondern als Grund-
lage f¨ur die Forschung in anderen Bereichen dienen soll, ist auch ein Blick ¨uber
die Dom¨ane RoboCup Soccer hinaus lohnenswert [3]. Schon heute erhalten Ro-
boter einen ersten Einzug in den Alltag der Menschen, beispielsweise in Form
von intelligenten Staubsaugern. Damit die Roboter weitere Aufgaben im Haushalt
¨ubernehmen und auch einer informatikfernen Gruppe von Menschen zur Verf¨ugung
gestellt werden k¨onnen, ist eine Kommunikation ¨uber nat¨urliche Sprache unerl¨ass-
lich. Roboter sollen den Menschen unterst¨utzen und das k¨onnen sie nur, wenn der
Nachrichtenaustausch f¨ur den Menschen so nat¨urlich wie m¨oglich abl¨auft. Auch in
einer h¨auslichen Umgebung ist der Einsatz einer Roboter-Roboter-Kommunikation
denkbar, denn der Mensch f¨urchtet sich grunds¨atzlich vor einer Aktion von Maschi-
nen, die f¨ur ihn nicht nachvollziehbar ist [18][25]. Kommunizieren nun verschiedene
intelligente Systeme im unmittelbaren Umfeld der Menschen ¨uber einen Kommu-
nikationsweg, der sich nur schwer ¨uberwachen l¨asst, st¨arkt dies das Vertrauen der

1

Kapitel 1. Motivation

Menschen in die Maschinen nicht. K¨onnen sie die Interaktion jedoch nachvollzie-
hen, da diese sich ¨uber nat¨urliche Sprache abspielt, ist das Verhalten der Roboter
leichter verst¨andlich und wird weniger abgelehnt.

Das Ziel dieser Arbeit ist daher, eine alternative Spielerkoordination in RoboCup-
Fußballspielen basierend auf nat¨urlicher Sprache zu entwickeln, um eine Unabh¨angig-
keit vom W-LAN-Netzwerk zu erreichen und einen weiteren Schritt in Richtung
menschen¨ahnlichem Fußballspiel zu gehen. Dar¨uber hinaus soll ein erster Ansatz
f¨ur eine Maschine-Maschine-Kommunikation und -Kooperation geliefert werden,
die f¨ur den Menschen nachvollziehbar ist und so eine gr¨oßere Akzeptanz von Ser-
vicerobotern erm¨oglicht.

2

Kapitel 2

Die Dom¨ane RoboCup

Der RoboCup ist ein internationaler Wettbewerb mit dem Ziel, den Austausch
und die Vergleichbarkeit in der Forschung an humanoiden Robotern zu f¨ordern. In
unterschiedlichen Ligen mit klar deﬁniertem Regelwerk treten die Roboter gegen-
einander an.

Die Dom¨ane dieser Bachelorarbeit ist die Humanoid Soccer League, in der bis
zu drei Roboter, ein Torwart und zwei Feldspieler pro Team, gegeneinander Fußball
spielen. Sowohl die Hardware als auch die Software werden von den Forschungs-
gruppen selbst entwickelt, wobei nur menschliche oder menschen¨ahnliche Sensoren
und Aktoren eingesetzt werden d¨urfen. Eine Ausnahme bildet hier nur die Kommu-
nikation, die noch ¨uber ein drahtloses Netzwerk abl¨auft. Per Wireless Local Area
Network (W-LAN) unterhalten sich nicht nur die Roboter untereinander, sondern
der Schiedsrichter kann so auch ein Tor oder ein Foul den Spielern mitteilen.

Jedes Jahr wird das Regelwerk in den einzelnen Ligen angepasst und so immer
mehr Elemente des menschlichen Fußballs eingef¨uhrt. Das Ziel, im Jahr 2050 in
einem fairen Spiel gegen den amtierenden Fußballweltmeister der Menschen anzu-
treten und zu gewinnen gibt den Weg vor. Voraussetzung f¨ur ein Spiel unter fairen
Bedingungen ist es, dass sowohl die Regeln als auch die Ausstattung der Hard-
ware im Roboterfußball an die Menschen und ihre Fußballregeln angepasst sind.
Die Kommunikation wird daher im Laufe der Zeit ohne eine Netzwerkverbindung
auskommen m¨ussen, da diese Kommunikation auf einem Spielfeld in einer lauten
Umgebung einen großen Wettbewerbsvorteil bringen w¨urde, der f¨ur die Menschen
so nicht zu nutzen ist.

Eine Motivation, den Austausch der Roboter schon heute auf die Synthese
und Verarbeitung nat¨urlicher Sprache umzustellen, ergibt sich aus den best¨andi-
gen Problemen mit der Netzwerkinfrastruktur auf den Turnieren. In jeder Liga
haben sowohl das Spielfeld als auch die Arena ihr eigenes Netzwerk. Um dies zu
realisieren, werden in jeder Halle mehrere Dutzend W-LAN-Router parallel betrie-
ben. Doch auch viele Teams nutzen zu Testzwecken ein eigenes W-LAN, Roboter
werden nach einem Spiel nicht wieder aus dem oﬃziellen Netzwerk genommen und
Besucher in der Halle haben immer ¨ofter Smartphones dabei, die sich mit den of-
ﬁziellen Netzwerken verbinden wollen. Die Folge sind Interferenzen und Ausf¨alle
der Router, die wie bei einer Distributed Denial of Service Attacke (DDoS) den

3

Kapitel 2. Die Dom¨ane RoboCup

st¨andigen Anfragen nicht mehr Stand halten k¨onnen. H¨auﬁg m¨ussen Spiele daher
komplett ohne Netzwerk stattﬁnden oder die Signale kommen nur mit einer großen
Verz¨ogerung an.

Auf eine Kommunikation zwischen den Robotern kann dennoch nur schwerlich
verzichtet werden: Nicht jeder Roboter hat ein Modell des gesamten Spielfeldes,
oft ist nur die direkte Umgebung bekannt. Daher kann ein Roboter allein nicht
absch¨atzen, ob er selbst derjenige Spieler ist, der am n¨achsten zum Ball steht und
daher zum Ball laufen sollte, oder ob ein anderer bereits auf dem Weg ist. Findet
keine Kommunikation statt, bewegen sich mehrere Roboter zum Ball und bringen
sich dabei h¨auﬁg gegenseitig zu Fall. Auch kann es passieren, dass ein Roboter
die Orientierung auf dem Spielfeld verliert oder den Ball nicht mehr ﬁnden kann.
Eine erneute Lokalisation ist aufwendig und kann zu Fehlern f¨uhren. Dabei sehen
Mitspieler vielleicht noch den Ball oder wissen, wo sie sich auf dem Feld beﬁnden.
Ein Austausch solcher Informationen kann wertvolle Zeit und Rechenressourcen
sparen.

Da bisher noch kein Team seine Kommunikation auf nat¨urliche Sprache umge-
stellt hat, ist der Ansatz der nat¨urlichsprachlichen Kommunikation nicht nur ein
großer Schritt hin zu menschen¨ahnlicherem Fußball, sondern k¨onnte auch einen
deutlichen Vorteil bei Turnieren bieten, weil die Roboter nicht mehr auf die feh-
leranf¨alligen W-LAN-Netzwerke angewiesen sind.

2.1 Speziﬁkation der Roboterhardware

An der Universit¨at Hamburg werden DARwIn-OP Roboter (Dynamic Anthropo-
morphic Robot with Intelligence – Open Platform) im Team Hamburg Bit-Bots
genutzt. Diese wurden von der koreanischen Firma ROBOTIS in Zusammenar-
beit mit der Virginia Tech, Purdue University, und der University of Pennsylvania
entwickelt und werden inzwischen von vielen Teams in der Humanoid Kid Size
League verwendet [14]. Große Teile der Hardware sind f¨ur die Anforderungen des
Fußballspiels optimiert. Da eine Kommunikation ¨uber nat¨urliche Sprache nicht zu
diesem Anforderungskatalog z¨ahlt, wird im folgenden Kapitel die Hardware dieser
Roboter im Hinblick auf die neuen Anspr¨uche untersucht.

2.1.1 Anforderungen an das Lautsprechersystem

Nach oﬃzieller Herstellerspeziﬁkation ist im DARwIn-OP ein Lautsprecher mit
einem Schalldruckpegel von 93 ± 3 dB [0,1 m/0,1 W] mit einer Impedanz von 8 Ω
± 15 % bei 1,0 V verbaut.

Ein erster Test unter Realbedingungen bei einem Testspiel mit Publikum hat
gezeigt, dass das Mikrophon klar und deutlich Umgebungsger¨ausche auch ¨uber
gr¨oßere Distanzen aufnimmt. Aufgrund der Gr¨oße des Lautsprechers ist seine Aus-
gangsleistung jedoch begrenzt, so dass die Sprache der Roboter auch mit gr¨oßter
Aussteuerung nur bis zu einer Distanz von drei Metern aufgezeichnet werden konn-
te.

4

2.1. Speziﬁkation der Roboterhardware

Abbildung 2.1: Versuchsaufbau Leistungstest der Lautsprecher des DARwIn-OP

Um genauere Anforderungen f¨ur eine Hardwaremodiﬁkation zu evaluieren, wur-
de eine Testreihe mit dem Lautsprecher aus dem DARwIn-OP und einem vergleich-
baren 3-Watt-Breitbandlautsprecher mit 8 Ω Impedanz und einer Membrangr¨oße
von 9 cm x 5 cm durchgef¨uhrt, im Folgenden mit Referenzl. abgek¨urzt. Dazu wur-
den ein Schallpegel-Messger¨at der Firma Rhode&Schwartz sowie ein Frequenzge-
nerator von Grundig verwendet. Der exakte Versuchsaufbau ist in Abbildung 2.1
dargestellt.

Dabei sind Messungen bei 0,5 V und 1,0 V eﬀektiver Spannung jeweils bei
frontaler Ausrichtung der Lautsprecher sowie bei einer Drehung um 90◦ erfolgt.
Gemessen wurde bei Frequenzen im Bereich von 600 Hz bis 1500 Hz.

Folgende Messwerte wurden bei einer Durchf¨uhrung mit 0,5 V Spannung er-

mittelt:

Typ
DARwIn-OP (frontal)
DARwIn-OP (gedreht)
Referenzl. (frontal)
Referenzl. (gedreht)

600 Hz 800 Hz 1000 Hz 1200 Hz 1500 Hz
23 dB
24dB
44 dB
35 dB

27 dB
20dB
50 dB
48 dB

40 dB
39dB
41 dB
39 dB

38 dB
27dB
50 dB
42 dB

32 dB
27dB
53 dB
46 dB

Folgende Messwerte wurden bei einer Durchf¨uhrung mit 1,0 V Spannung ermittelt:

Typ
DARwIn-OP (frontal)
DARwIn-OP (gedreht)
Referenzl. (frontal)
Referenzl. (gedreht)

600 Hz 800 Hz 1000 Hz 1200 Hz 1500 Hz
30 dB
27 dB
52 dB
42 dB

42 dB
31 dB
58 dB
53 dB

39 dB
35 dB
61 dB
51 dB

34 dB
26 dB
62 dB
57 dB

50 dB
43 dB
52 dB
45 dB

Die Auswertung zeigt, dass der bereits im Roboter verbaute Lautsprecher in
einem Bereich von 800 Hz eine sehr gute Leistung auch im Vergleich zu Lautspre-
chern mit einer h¨oheren Wattzahl und einer gr¨oßeren Membran erbringen kann.
Jedoch nimmt diese Leistung bereits im Bereich von 600 Hz und 1000 Hz stark

5

50cm50cmFrequenzgeneratorSchallpegel-MessgerätKapitel 2. Die Dom¨ane RoboCup

Abbildung 2.2: Messreihe der Lautsprecherleistung f¨ur den DARwIn-OP und einen
Referenzlautsprecher, links bei 0,5 V Spannung, rechts bei 1,0 V Spannung

ab (vergleiche Abbildung 2.2). Da die vom Roboter synthetisch erzeugte Sprache
jedoch zum großen Teil Frequenzen von unter 500 Hz produziert (vergleiche Abbil-
dung 2.3), ist eine Ver¨anderung des Lautsprechers sinnvoll, so dass auch im unteren
Frequenzbereich lautere T¨one erzeugt werden k¨onnen. Der Frequenzbereich ¨uber
10000 Hz kann dagegen vollst¨andig ignoriert werden, da die vom Roboter synthe-
tisch erzeugte Sprache keine so hohen Frequenzen erzeugt. Werden Frequenzen in
einem h¨oheren Bereich aufgezeichnet, k¨onnen diese als Umgebungsger¨ausche oder
Rauschen identiﬁziert und herausgeﬁltert werden. Zus¨atzlich ist eine weitere Si-
gnalverst¨arkung ratsam – diese k¨onnte durch einen der USB-Anschl¨usse auf dem
Mainboard oder ein externes, kleines Akkusystem mit Energie versorgt werden. Ei-
ne Vergr¨oßerung der Lautsprechermembran ist dagegen nur in einem sehr geringen
Umfang m¨oglich, da weder in der Brust noch im Kopf des Roboters zwischen dem
Metallger¨ust und der ¨außeren Plastikverkleidung gen¨ugend Platz zur Verf¨ugung

Abbildung 2.3: Frequenzanalyse des synthetisch erzeugten Wortes

Distance“

”

6

6008001000120015000102030405060Spannung 0.5 VoltDARwIn-OP (frontal)DARwIn-OP (gedreht)Referenzlautsprecher (frontal)Referenzlautsprecher (gedreht)HertzDezibel6008001000120015000102030405060Spannung 0.5 VoltDARwIn-OP (frontal)DARwIn-OP (gedreht)Referenzlautsprecher (frontal)Referenzlautsprecher (gedreht)HertzDezibel600800100012001500010203040506070Spannung 1.0 VoltHertzDezibel2.1. Speziﬁkation der Roboterhardware

steht. An einer anderen Stelle darf der Lautsprecher dem Regelwerk entsprechend
nicht angebracht werden.

Beim Einbau des Lautsprechersystems ist darauf zu achten, dass ein Roboter
einem anderen Roboter nur selten frontal gegen¨ubersteht. Wie in den Vergleichs-
kurven (Abb. 2.2) zu sehen ist, nimmt die Lautst¨arke bei einer Drehung um 90◦ in
den meisten Frequenzbereichen bereits enorm ab. Dies ist dem Aufbau des Laut-
sprechers geschuldet, der nur auf eine Abstrahlung nach vorn und nicht zur Seite
ausgelegt ist. Hinzu kommt die Abschirmung durch das Plastikgeh¨ause, das um den
Lautsprecher herum angebracht ist. Beides f¨uhrt zu einem erh¨ohten Leistungsan-
spruch an den Lautsprecher, damit diese Einschr¨ankungen kompensiert werden
k¨onnen.

2.1.2 Anforderungen an die Mikrophone

Es sind serienm¨aßig zwei Mikrophone im Kopf des DARwIn-OP verbaut, die je-
weils eine Sensitivit¨at von -62 ± 2 dB, eine Impedanz von 2,2 kΩ und ein Fre-
quenzspektrum von 50 bis 16000 Hz haben. Diese Mikrophone sind jedoch, wie in
Abbildung 2.4 gezeigt, nur ¨uber Analogports an das CM-730-Board im Roboter
angeschlossen. Daher k¨onnen die Mikrophone mit der aktueller Firmware nur mit
einer maximalen Abtastrate von 100 Hz ausgelesen werden. Nach dem Abtast-
theorem von Shannon muss jedoch ein Signal mit einer Bandbreite von fmin bis
fmax mit 2 · fmax abgetastet werden, damit eine vollst¨andige Rekonstruktion des
Signals m¨oglich ist [16]. Menschliche Sprache hat eine Minimalfrequenz von 50 Hz
und eine Maximalfrequenz von ca. 6000 Hz [4], der DARwIN-OP Roboter dagegen
erzeugt seine Sprachausgabe zwar haupts¨achlich im Bereich bis 1000 Hz, trotzdem
erstreckt sich das Frequenzspektrum, wie in Abbildung 2.3 zu sehen ist, bis 10000
Hz. Nach dem Abtasttheorem muss also eine Abtastung mit mindestens 2000 Hz,
besser jedoch sogar 20000 Hz m¨oglich sein. Die beschriebenen Mikrophone sind
daher ungeeignet.

Im Kopf des DARwIN-OP ist noch ein weiteres Mikrophon in der Logitech-
C905-Webcam verbaut. Da es sich bei der Webcam nicht um ein Bauteil von
ROBOTIS handelt, ist auch keine Open-Source-Speziﬁkation dazu ver¨oﬀentlicht.
Auch bei einer Recherche beim Hersteller konnte keine n¨ahere Speziﬁkation der

Abbildung 2.4: Schaltplan des Microphone Ampliﬁer auf dem CM-730-Board [19,
S. 22].

7

Kapitel 2. Die Dom¨ane RoboCup

Mikrophone gefunden werden. Da es jedoch ¨uber die Webcam mit USB 2.0 an
den im DARwInOP verbauten FitPC2 angeschlossen ist, lassen sich problemlos
Abtastraten von ¨uber 20000 Hz realisieren.

Um ein Sprachanalysesystem langfristig auf dem DARwInOP zu etablieren, ist
es jedoch notwendig, mehr als ein Mikrophon zu benutzen, um st¨arkere Signalwerte
in einem gr¨oßeren Bereich um den Roboter herum zu erhalten. L¨asst sich durch
ein Firmware-Update des CM-730-Boards noch keine signiﬁkante Verbesserung in
der Abtastrate erzielen, ist auch die Installation von zwei eigenen Mikrophonen im
Kopf denkbar. Diese k¨onnten am Kopfplastik befestigt werden und ¨uber USB oder
den ebenfalls auf dem FitPC2 verbauten Klinkenanschluss angeschlossen werden.
Eine Nutzung von mehr als zwei Mikrophonen gleichzeitig ist nach Regelwerk nicht
gestattet.

2.1.3 Einschr¨ankungen durch den Prozessor

Im DARwInOP ist ein FitPC2 bzw. FitPC2i verbaut. Dieser besitzt eine Intel Atom
Z530-CPU mit 1,6 GHz Taktung und einem Gigabyte RAM. Die Sprachverarbei-
tung muss unter diesen gegebenen Bedingungen trotzdem noch in einer solchen
Geschwindigkeit berechnet werden, dass ein dynamisches Spiel m¨oglich ist. Dabei
ist zu beachten, dass sich daraus keine Rechenzeitnachteile f¨ur die Bilderkennung
oder die Berechnung der Roboterbewegungen ergeben d¨urfen, die ebenfalls dieselbe
Hardware nutzen.

2.2 Analyse der Spielabl¨aufe im Hinblick auf den

Nachrichtenaustausch

In der bisherigen Architektur werden bereits in den folgenden Bereichen Daten
¨uber das W-LAN-Netzwerk unter den Robotern ausgetauscht bzw. ein Austausch
der Daten ist geplant:

• Spielstatus: Bisher erfahren die Roboter ¨uber das Netzwerk, wenn ein an-
derer Roboter ein Foul begangen und daher das Spielfeld verlassen hat. Diese
Information kann unmittelbar in der Spielstrategie verwendet werden, da so
beispielsweise ein anderer Roboter die Aufgaben des Torwarts ¨ubernehmen
kann, wenn dieser das Spielfeld verlassen muss. Ist die Strafe vor¨uber und
hat der Roboter seine Orientierung auf dem Spielfeld wiedergefunden, sollte
er dieses ebenfalls mitteilen.

• Balldistanz: Damit nicht alle Roboter zum Ball laufen, sobald sie diesen se-
hen, wird die gesch¨atzte Distanz zum Ball kommuniziert. Derjenige Roboter,
der die k¨urzeste Distanz gemeldet hat, versucht dann den Ball zu erreichen,
w¨ahrend die anderen Roboter abwarten bzw. sich in eine g¨unstige Position
zu bringen versuchen. Sinnvoll ist es, die Balldistanz und die bestm¨ogliche
Strecke direkt in eine gesch¨atzte Dauer bis zur Erreichung des Balles um-
zurechnen, denn potentielle Hindernisse auf dem Weg k¨onnen dazu f¨uhren,

8

2.3. Einbindung der Kommunikation in das bestehende Softwaresystem

dass ein Roboter zwar nach euklidischer Distanz n¨aher zum Ball steht, den
direkten Weg jedoch nicht nehmen kann und daher l¨anger als die anderen
Roboter braucht.

• Position auf dem Spielfeld: Um sich ein globales Bild vom Spielfeld zu
machen, braucht der Roboter nicht nur die globale eigene Position und die
Ballposition, sondern auch die Position der Mitspieler. Zwar kann er deren
Position aus seinen Kamerabildern heraus berechnen, um jedoch ein globales
gemeinsames Weltbild zu schaﬀen, m¨ussen die Ergebnisse der Berechnung
regelm¨aßig mit den anderen Spielern abgeglichen werden.

• Einsatzgebiet des Roboters: Die Roboter k¨onnen kommunizieren, ob sie
gerade als Feldspieler oder Torwart spielen. Diese Information kann sowohl
f¨ur die Teamstrategie, als auch f¨ur eine Vereinfachung der Lokalisation ge-
nutzt werden. Weiß der einzelne Roboter zum Beispiel, dass ein Ball weniger
als zwei Meter vom Torwart entfernt und dieser im eigenen Tor ist, kann an-
genommen werden, dass sich der Ball in der eigenen Spielfeldh¨alfte beﬁndet.

2.3 Einbindung der Kommunikation in das be-

stehende Softwaresystem

Bei einem funktionsf¨ahigen W-LAN, ¨uber das die Roboter Daten austauschen
k¨onnen, bietet diese Art der Kommunikation heute noch entscheidende Vortei-
le, die durch die Kommunikation ¨uber nat¨urliche Sprache noch nicht zu leisten
sind. So kann jeder Roboter mehrmals pro Sekunde aktuelle Daten aller anderen
Roboter in seine Berechnungen einbeziehen. Es ist unter diesen Voraussetzungen
nicht notwendig zu pr¨ufen, welche Daten dringend notwendig sind, da ohnehin
alle Daten zur Verf¨ugung stehen. F¨ur die Kommunikation ¨uber nat¨urliche Spra-
che muss sowohl die Anzahl der zu kommunizierenden Nachrichten als auch die
Kommunikationsh¨auﬁgkeit deutlich reduziert werden. Eine Umstellung auf eine
Softwarearchitektur, die entscheidet, welche Informationen in einer bestimmten
Situation ben¨otigt werden, und diese dann ¨uber Sprache erfragt, ist notwendig,
wenn nat¨urlichsprachliche Kommunikation genutzt werden soll.

Um die Vorteile beider Systeme zu nutzen, ist es empfehlenswert, die Soft-
warearchitektur auf ein hybrides System umzustellen: Unter Normalbedingungen
nutzen die Roboter weiterhin das W-LAN zur Kommunikation. Dabei merkt sich
jedoch jeder Roboter, wie viel Zeit seit dem letzten Update durch das Netzwerk
vergangen ist. Wird diese Zeit zu groß, wird die Kommunikation auf nat¨urliche
Sprache umgestellt. Sobald das W-LAN wieder aktuelle Daten liefert, kann der
Nachrichtenaustausch wieder darauf umgestellt werden.

9

Kapitel 2. Die Dom¨ane RoboCup

10

Kapitel 3

Der Nachrichtenaustausch

Die Roboter auf dem Spielfeld ben¨otigen f¨ur ihr Spielverhalten regelm¨aßig Infor-
mationen von anderen Robotern. Dazu m¨ussen sie Nachrichten austauschen bzw.
kommunizieren, um an diese Informationen zu gelangen. Die bisherige Kommuni-
kation wurde mittels Versendung von Paketen ¨uber das Netzwerk realisiert. Eine
Umstellung auf direkte lautsprachliche Kommunikation erfordert die Entwicklung
neuer Nachrichtenaustauschstrategien, die im Folgenden beschrieben werden [16].

3.1 Die Dialogmanagementstrategie

Wenn an ... [einer] Kommunikation mindestens zwei Personen beteiligt sind, die
”
sich sowohl selbst ¨außern, als auch die ¨Außerung der anderen unmittelbar wahr-
nehmen, spricht man von einem Dialog, einer Wechselrede zwischen mindestens
zwei Sprechern.“ [4, S. 395]

Ein Dialog erfordert, dass jeder Kommunikationspartner bereits erhaltene Infor-
mationen speichern und dahingehend verarbeiten kann, dass er daraus Handlungen
oder weitere ¨Außerungen bzw. Nachfragen generieren kann.

Innerhalb eines Dialogmanagementsystems ist die Dialogkontrolle daf¨ur zust¨andig,

auf Basis eines gegebenen Inputs eine solche Entscheidung zu treﬀen. Dazu ben¨otigt
es ggf. Kontextinformationen, die durch das Kontextmodellierungssystem des Dia-
logmanagers aufbereitet werden [9].

Die Dialogkontrolle l¨asst sich nach Jokinen und McTear basierend auf Graphen
oder Frames realisieren. Ein graphenbasiertes Modell besteht aus einer endlichen
Menge an Zust¨anden und l¨asst sich durch eine Menge von Knoten, welche die ei-
genen Fragen oder Aussagen repr¨asentieren, und eine Menge von ¨Uberg¨angen zwi-
schen den Knoten beschreiben, welche die m¨oglichen Antworten des Dialogpartners
enthalten. Der Vorteil eines solchen Systems liegt in der einfachen Modellierung, da
nur eine endliche Menge an vorher bekannten Zustands¨uberg¨angen implementiert
werden muss. Dies wird dann zu einem Nachteil, wenn das System an Komplexit¨at
zunimmt.

Eine andere M¨oglichkeit f¨ur die Dialogkontrolle liegt in der Benutzung von
Frames. Ein Frame besteht dabei aus einer Reihe von Variablen, die als freie Platz-

11

Kapitel 3. Der Nachrichtenaustausch

Abbildung 3.1: Gegen¨uberstellung von graphenbasiertem und framebasiertem Dia-
logkontrollsystem

halter f¨ur bestimmte Daten dienen, die w¨ahrend des Dialogs gesammelt werden
sollen. Immer wenn eine neue Information aufgenommen wurde, wird der entspre-
chende Platz im Frame dadurch besetzt. Zun¨achst kann nach irgendeiner Informa-
tion gefragt werden, denn alle Variablen sind noch unbelegt. Ist eine Information
verarbeitet, kann abh¨angig von der Dialogstrategie ein anderer Wert abgefragt
werden. Frames bieten eine wesentlich ﬂexiblere M¨oglichkeit der Dialogsteuerung,
denn insbesondere bei unspeziﬁschen Fragen k¨onnen in der Antwort unterschied-
lich viele Informationen enthalten sein. Bei einem graphenbasierten Dialogmodell
m¨usste f¨ur jede Anzahl an Informationen ein eigener ¨Ubergang geschaﬀen werden,
w¨ahrend bei einem framebasierten Kontrollsystem einfach die entsprechenden Fel-
der belegt werden. Die beiden unterschiedlichen Verfahren sind in Abbildung 3.1
dargestellt.

F¨ur den Nachrichtenaustausch zwischen den Robotern ist ein framebasiertes
Kontrollsystem in diesem Anwendungskontext besser geeignet als ein graphenba-
siertes Verfahren. Die Frames lassen sich einfach als Dictionary oder Map imple-
mentieren, wobei die Schl¨ussel oder Keys der Map den Feldern entsprechen und die
Werte mit den aktuellen Informationen belegt werden. Ein weiterer Vorteil ist, dass
die Frames leicht zu erweitern sind, wenn Dialoge ausgebaut werden. Außerdem
kann ein Feld angelegt werden, das daf¨ur genutzt wird, den Zeitpunkt der letzten
¨Anderung im Frame zu speichern. Dadurch l¨asst sich leicht entscheiden, ob eine
Information noch aktuell genug ist. Ein weiteres Entscheidungskriterium f¨ur ein
framebasiertes Kontrollsystem ist, dass das jetzige Kommunikationsmodell bereits
auf Frames beruht, die in jedem Updatezyklus mit Daten gef¨ullt werden. Es ist
daher keine Umstellung der Architektur notwendig, sondern lediglich eine Erwei-
terung, da mit der Kommunikation ¨uber nat¨urliche Sprache nicht mehr in jedem
Updatezyklus alle Informationen bereitgestellt werden. Stattdessen muss berech-
net werden, welche Informationen im aktuellen Spielstatus relevant sind, um diese
gegebenenfalls abzufragen.

Die relevanten Kontextinformationen lassen sich ebenfalls in Frames abspei-
chern bzw. aus diesen gewinnen. Jokinen und McTear beschreiben f¨unf relevante
Punkte, die eine Kontextmodellierung liefern sollte:

• Dialogverlauf: In beschriebenen Kontext wird kein kompletter Dialogverlauf
ben¨otigt, da bestimmte Daten wie z.B. eine Balldistanz vor mehreren Mi-
nuten f¨ur das aktuelle Verhalten nicht mehr relevant sind. Alle zuk¨unftig

12

3.2. Die Konversationsmodellierung

weiterhin relevanten Daten aus dem Verlauf bleiben in den Frames gespei-
chert.

• Aufgabenbeschreibung: Durch die unbesetzten Felder, die in den Frames vor-
gehalten werden, weiß der Roboter stets, welche relevanten Daten er noch
sammeln muss.

• Modell der Dom¨ane: Wie bereits in Abschnitt 2.3 beschrieben, sollte die Soft-
warearchitektur so gestaltet werden, dass die Kommunikation und Dialog-
modellierung ohne Kenntnis der Dom¨ane auskommt. An anderer Stelle sollte
berechnet werden, welche Informationen zum aktuellen Zeitpunkt n¨utzlich
sind. Das Kommunikationsmodul benutzt dieses Wissen, um daraus einen
Dialog zu generieren.

• Modell der Konversationskompetenz: Der Roboter ben¨otigt ein Modell da-
von, wann er in einem Dialog selbst die Dialogkontrolle ¨ubernehmen darf und
an welcher Stelle er lediglich auf Fragen antworten sollte (siehe Kapitel 3.2).

• Pr¨aferenzmodell der Dialogpartner: Der Roboter ben¨otigt keine erweiterten
Informationen ¨uber die anderen Roboter, da sich ihre Pr¨aferenzen unterein-
ander nicht unterscheiden.

Abbildung 3.2: Links das globale Dialogmodell als Peer-to-Peer-Struktur, rechts
der einzelne Dialog als Client-Server-Modell.
DARwIn-OP Graﬁk von http://darwinop.sourceforge.net/

13

AnfrageAntwortClientServerKapitel 3. Der Nachrichtenaustausch

3.2 Die Konversationsmodellierung

Grunds¨atzlich gibt es bei jeder Modellierung des Nachrichtenaustauschs zwei m¨ogli-
che Beziehungen, in denen die Dialogpartner zueinander stehen k¨onnen: Eine sym-
metrische Beziehung und eine asymmetrische Beziehung.

In einer asymmetrischen Beziehung, oft auch als Client-Server-Modell bezeich-
net, stellt einer der Kommunikationspartner, der Client, eine Anfrage an den Ser-
ver. Der Server selbst kann keine Anfragen stellen, sondern nur Anfragen von den
Clients beantworten und so Informationen bereitstellen. Im Kontrast dazu steht
das symmetrische Modell, auch Peer-to-Peer-Verbindung genannt, in dem jeder
Kommunikationspartner sowohl Anfragen stellen als auch beantworten kann [10].
Bezogen auf die Dom¨ane RoboCup bieten sich so zwei M¨oglichkeiten: Eine
zentrale Instanz, zum Beispiel der Torwart, stellt Anfragen an die anderen Roboter.
Alle anderen Roboter fungieren als Server, die lediglich Informationen bereitstellen.
Der Torwart errechnet aus den Informationen ein Spielverhalten f¨ur die anderen
Roboter und gibt diese in Form von Anweisungen an die Mitspieler weiter. Dieses
Modell bietet allerdings keinerlei Ausfallsicherheit – wenn der Torwart wegen eines
Defekts vom Platz genommen werden muss oder durch eine ¨Uberlastung keine
Anfragen mehr beantworten kann, ﬁndet keine Kommunikation mehr statt. Das
Problem der Ausfallsicherheit durch ein zentrales Kommunikationssystem kann
durch die Implementation eines Client-Server-Systems nur verschoben werden.

Aus diesen ¨Uberlegungen ergibt sich, dass jeder Roboter in der Lage sein muss,
selbst einen Dialog durch Anfragen an andere Roboter zu beginnen, aber auch auf
Anfragen zu reagieren. Um die Konversation f¨ur die Roboter zu vereinfachen, bietet
es sich jedoch an, jeden einzelnen Dialog als Client-Server-Modell zu modellieren.
Es kann also global betrachtet jeder Roboter eine Anfrage an andere Roboter
stellen und eine solche auch beantworten. Innerhalb eines Dialogs fungiert aber
immer ein Roboter als Client und einer als Server. Derjenige Roboter, der den
Dialog beginnt, nimmt die Rolle des Clients ein, und der antwortende Roboter ist
der Server. Die antwortenden Roboter k¨onnen jedoch ihrerseits im Anschluss einen
eigenen Dialog beginnen, um selbst eine Frage stellen zu k¨onnen. Abbildung 3.2
zeigt das Zusammenspiel der beiden Modelle.

3.3 Die Vermittlungstechnik

Ein Dialog kann durch die direkte Ansprache eines Dialogpartners initiiert wer-
den (Punkt-zu-Punkt-Verbindung) oder durch eine generelle Frage, auf die jeder
antworten kann, der die Frage geh¨ort hat (Broadcast).

Die erste beschriebene M¨oglichkeit einer Punkt-zu-Punkt-Dialogvermittlung
zeichnet sich durch eine eindeutige Kennzeichnung aus, welcher m¨ogliche Kom-
munikationspartner angesprochen werden soll. Dazu wird entweder eine direkte
Ansprache per Namen ben¨otigt oder ein Verbindungsaufbau mittels Augenkon-
takt oder Gesten. Da die Roboter bisher nicht pr¨azise andere Roboter erkennen
k¨onnen, bleibt nur ein Kommunikationsaufbauversuch mittels direkter Ansprache.

14

3.3. Die Vermittlungstechnik

Geeignet ist diese Vermittlungstechnik immer dann, wenn einen Roboter die In-
formation von genau einem anderen Roboter interessiert. Es wird im Quelltext
festgelegt, dass in einem solchen Fall der Satz immer mit dem Namen des ange-
sprochenen Roboters beginnen soll.

Oft wird es in der Kommunikation unter den Robotern notwendig sein, eine
Information von allen Robotern zu erhalten. In diesem Fall verl¨angert sich die
Nachrichtenaustauschzeit stark, wenn ein Roboter zun¨achst jeden einzelnen Robo-
ter ansprechen muss. Es bietet sich daher an, eine allgemeine Frage ohne konkreten
Adressaten zu stellen. Das erste Wort einer allgemeinen Frage ist dann nicht der
Name eines Roboters. Haben alle Roboter die Frage vernommen, ist nun noch
zu regeln, in welcher Reihenfolge sie antworten d¨urfen, damit nicht alle Roboter
gleichzeitig mit dem Sprechen beginnen. Hier bietet es sich an, die Nummer der
Roboter im Team zu nutzen, so dass zun¨achst der Roboter mit der kleinsten Num-
mer spricht. Hat dieser seinen Satz beendet oder in einem deﬁnierten Zeitraum
nicht mit dem Sprechen begonnen, kann der n¨achste Roboter beginnen. Da die
Reihenfolge klar deﬁniert ist, kann auch jeder Roboter erkennen, welcher Roboter
gerade spricht und sich diese Information im entsprechenden Frame abspeichern.
Jeder Roboter, der Frage und Antworten der anderen Roboter vernommen hat,
kann so seine eigenen Frames aktualisieren.

Auf den Aufbau einer Verbindung durch eine Synchronisation und eine Best¨ati-
gung des Nachrichteneingangs durch den Synchronisationspartner wird verzichtet,
da der Nachrichtenaustausch so wenig Zeit wie m¨oglich in Anspruch nehmen darf.
So k¨onnen die Roboter auf Basis der erhaltenen Nachrichten schnell ihre Spielz¨uge
planen.

15

Kapitel 3. Der Nachrichtenaustausch

16

Kapitel 4

Konzepte der Spracherzeugung
und Sprachverarbeitung

4.1 Sprachsynthese

Unter einer Sprachsynthese verstehen wir
die Umsetzung von geschriebener Spra-
”
che ... in Lautsprache, also in Sprachsignale“ [16, S. 194], im Folgenden auch als
Text-to-Speech-System (TTS) bezeichnet. Als Bewertungskriterium f¨ur die Qua-
lit¨at von Sprachsynthese wird heute vor allem die Nat¨urlichkeit der Aussprache
gesehen [8]. Einige Autoren unterscheiden zwischen High-Level- und Low-Level-
Synthese, wobei sich erstere mit der Phonetik (also der Produktion und physi-
kalischen Beschaﬀenheit von Sprache) und letztere mit der Funktion von Sprach-
lauten im Sprachsystem (Phonologie) besch¨aftigt [11]. Im Folgenden werden drei
unterschiedliche Ans¨atze im Bereich der Low-Level-Sprachsynthese vorgestellt. Die
Phonologie wird hierbei nicht betrachtet, da sie f¨ur unseren Anwendungskontext
nicht unmittelbar relevant ist.

4.1.1 Artikulationssynthese

Der Ansatz der Artikulationssynthese ist es, die neurophysiologischen und biome-
chanischen Abl¨aufe bei der Lautbildung des Menschen m¨oglichst exakt zu kopieren.
Dabei werden mit Hilfe von Parametern die Kieferstellung und die Zungenbewe-
gung angepasst und nachgebildet. Dieses Verfahren erfordert nicht nur eine lang-
wierige Anpassung der Parameter, sondern vor allem einen mechanischen Nachbau
des menschlichen Sprechapparats bzw. eine entsprechende Softwaresimulation. Bei-
des ist sehr aufwendig, die Ergebnisse aber dennoch nicht so humanoid wie erhoﬀt.
Daher wird in neueren Forschungen daran gearbeitet, die dynamischen Parameter
direkt aus dem Sprachsignal zu gewinnen und damit einen direkten Zusammenhang
zwischen Modell und Sprachsignal herzustellen [16][23].

17

Kapitel 4. Konzepte der Spracherzeugung und Sprachverarbeitung

4.1.2 Formantsynthese

Als Formanten bezeichnet man einen Frequenzbereich,
in dem die Obert¨one st¨arker
”
erscheinen als in anderen Frequenzbereichen“[4, S. 201]. Grundlage der Formant-
synthese ist es, dass f¨ur die Lautwahrnehmung in erster Linie Lage, H¨ohe und G¨ute
des Formanten ausschlaggebend sind. In der Regel werden pro Formant mehrere
Filter eingesetzt, die das Sprachsignal erzeugen sollen. Daraus ergibt sich vor allem
die M¨oglichkeit, Laut¨uberg¨ange zu formen, so dass kein st¨orendes Stocken zwischen
den Lauten wahrgenommen wird [16].

4.1.3 Verkettungssynthese

Die Modellierung von Sprache wird hier als eine Konkatenation von einzelnen
Spracheinheiten betrachtet, die passend aneinandergereiht werden. Spracheinhei-
ten k¨onnen zum Beispiel Phone,
die kleinste diskrete Lauteinheit im Lautkonti-
”
nuum“[7, S. 299] oder Diphone sein. Diphone werden entweder diejenigen Lautein-
heiten genannt, die von der Mitte eines Phons bis zur Mitte des n¨achsten Phons
reichen, oder solche, die vom Punkt der geringsten ¨Anderung im ersten Phon bis
zum gleichen Punkt im n¨achsten Phon reichen. Im Gegensatz zur Phon-Synthese
werden bei der Diphon-Synthese die Laut¨uberg¨ange mitbetrachtet, so dass die er-
zeugte Sprache ﬂ¨ussiger klingt.

Der Diphon-Ansatz wird immer dann gew¨ahlt, wenn nur wenige Grundelemente
zur Verf¨ugung stehen sollen. Erweitert man die Datenbank der Grundelemente, so
dass variantenreichere Worte zur Verf¨ugung stehen, dann spricht man von Korpus-
synthese. Hier versucht das System die Worte entweder direkt aus der Datenbank
zu entnehmen oder m¨oglichst große und ¨ahnlich klingende Wortteile miteinander zu
verketten. Nur wenn das nicht gelingt, wird auf die Diphon-Synthese zur¨uckgegrif-
fen. Um den Preis h¨oheren Speicherbedarfs bietet einem die Verkettungssynthese
eine nat¨urlichere Lautausgabe.

4.2 Spracherkennung

Als Spracherkennung wird
das Umsetzen eines Sprachsignals in eine textliche
”
Form“ bezeichnet [16, S. 28]. In den nachfolgenden Abschnitten werden zun¨achst ei-
nige Vorverarbeitungsschritte beschrieben, die eine Analyse ¨uberhaupt erst erm¨ogli-
chen oder erleichtern. Anschließend werden zwei verschiedene Ans¨atze zur Spra-
cherkennung vorgestellt und basierend darauf eine Verfahrensauswahl f¨ur den An-
wendungskontext getroﬀen.

4.2.1 Vorverarbeitung

Um das aufgezeichnete Signal einer Sprachanalyse zuzuf¨uhren, muss es zun¨achst in
eine daf¨ur geeignete Form gebracht werden. Dies beinhaltet sowohl St¨orger¨ausche
fr¨uhzeitig zu eliminieren als diese auch von Intensit¨at und Grundfrequenz zu ab-

18

4.2. Spracherkennung

strahieren. Die folgenden Abschnitte beschreiben Ans¨atze und Algorithmen einer
solchen Vorverarbeitung.

Diskrete Fouriertransformation: Mit Hilfe einer Fouriertransformation (DTF)
l¨asst sich eine Signalfunktion x(n), also der Verlauf eines Signalparameters ¨uber
die Zeit, in eine Spektralfunktion X(k), also die Energie im Frequenzspektrum,
¨uberf¨uhren:

X(k) =

N −1
(cid:88)

n=0

x(n)e−j(2π/N )kn,

0 ≤ k ≤ N − 1

(4.1)

x(n) =

1
N

N −1
(cid:88)

k=0

X(k)ej(2π/N )kn,

0 ≤ k ≤ N − 1

(4.2)

N entspricht hierbei der Anzahl der Abtastwerte.

Nimmt man am Anfang einer Aufnahme stets mehrere Sekunden ohne ein
Sprachsignal von Robotern auf, kann mit Hilfe des dort erhaltenen Frequenzspek-
trums eine Filterung der sp¨ateren Aufnahmen durchgef¨uhrt werden. Unerw¨unschte
St¨orsignale wie Rauschen und Umgebungsger¨ausche in den Aufnahmen werden da-
durch erheblich reduziert.

Mel-Cepstrum:
In der Sprachverarbeitung wird eine Fouriertransformation h¨au-
ﬁg nur als Teil eines komplexeren Vorverarbeitungsverfahrens benutzt, bei der

Abbildung 4.1: Algorithmus der Transformation eines Sprachsignals in das Mel-
Cepstrum von [12]

19

EingangssignalUmwandlung in FramesDFTLogarithmus des AmplitudenspektrumMel-Skala und FilterDiskrete KosinustransformationMFCCKapitel 4. Konzepte der Spracherzeugung und Sprachverarbeitung

unter anderem das Spektrum gegl¨attet, eine Grundperiode erkannt oder ein ¨Uber-
tragungskanal kompensiert werden kann. Einen Algorithmus f¨ur eine solche Fal-
tung, die eine Eingangsfolge x(n) im Zeitbereich in eine Ausgangssequenz c(m)
¨uberf¨uhrt, nennt man Cepstrum. Statt einer reinen Abbildung auf das Frequenz-
spektrum, wie im Abschnitt ¨uber die Diskrete Fouriertransformation beschrieben,
wird in der Sprachverarbeitung eine Abbildung auf die so genannte Mel-Skala be-
vorzugt, denn diese abstrahiert von Intensit¨at und Grundfrequenz des Signals.
Dazu wird folgende Skalentransformation durchgef¨uhrt:

h(f ) = 2595 · log10 (1 +

f
700Hz

)

(4.3)

f beschreibt hier die Frequenz in Hz [16].

Nach Beth Logan l¨asst sich eine ¨Uberf¨uhrung in ein Mel-Cepstrum durch die
in Abbildung 4.1 abgebildeten Schritte durchf¨uhren [12]. Zun¨achst wird das ge-
samte Signal in kleinere Frames, auch als Fenster bezeichnet, aufgeteilt. Diese
sind typischerweise 20 ms lang und dienen dazu, Kanteneﬀekte zu vermeiden. Ab
jetzt wird jede der folgenden Operationen auf die Frames getrennt angewendet.
Zun¨achst wird nach dem beschriebenen Verfahren eine Fouriertransformation an-
gewendet. Da die wahrgenommene Lautst¨arke n¨aherungsweise logarithmisch be-
schrieben werden kann, wird von dem Ergebnis der DFT der Logarithmus gebildet.
Die Frequenzb¨ander werden nun erneut in so genannte Beh¨alter unterteilt, wobei
diese nicht in jedem Frequenzbereich gleich groß sind. Je h¨oher die Frequenz, desto
gr¨oßer ist der Frequenzbereich pro Beh¨alter, d.h. es ﬁnden sich mehr Frequenzbe-
reiche in einem Beh¨alter wieder. Da tiefere Frequenzen in der Sprachverarbeitung
eine gr¨oßere Bedeutung haben als hohe, entsteht so eine gr¨oßere Skalierbarkeit
in den Beh¨altern mit den niedrigen Frequenzbereichen. Die Abbildung des Fre-
quenzspektrums auf das Mel-Cepstrum, die pro Beh¨alter vorgenommen wird, ist
in Abbildung 4.1 rechts dargestellt. Zuletzt wird durch eine diskrete Kosinustrans-
formation eine Dekorrelation der Komponenten bewirkt:

Xk =

N −1
(cid:88)

n=0

xn cos

(cid:20) π
N

(cid:18)

n +

(cid:19)

(cid:21)

k

,

1
2

k = 0, . . . , N − 1

(4.4)

Formel 4.4 ist jedoch nur eine Anlehnung an die eigentliche Formel, die sich aus
der DFT ergibt:

(cid:20)

(log Sn) cos

m · (n −

(cid:21)

,

1
2

)

π
J

0 ≤ m ≤ D

(4.5)

J
(cid:88)

n=1

1
J
(cid:88)

c(m) =

Sn =

X(k) · Hn(k),

1 ≤ j ≤ J

(4.6)

k

Hn(k) entspricht der Anwendung des n-ten Filters der Mel-Filterbank, X(k) ist
das Ergebnis der Fouriertransformation und D die Anzahl cepstraler Koeﬃzienten
[16].

20

4.2. Spracherkennung

Hoch- und Tiefpassﬁlter, Rauschﬁlterung: Um Realdaten aus einem Mi-
krophon zu nutzen, sind weitere Vorverarbeitungsschritte wie eine Rauschﬁlterung
oder auch eine Hoch- bzw. Tiefpassﬁlterung w¨unschenswert, um die zu analysie-
renden Daten mit so wenig irrelevanten Signalwerten wie m¨oglich zu belasten. Ins-
besondere zur Rauschﬁlterung gibt es bereits zahlreiche verschiedene Ans¨atze und
Algorithmen, die nicht Gegenstand dieser Arbeit sind. Daher wird – sofern n¨otig
– auf eine h¨andische Vorverarbeitung durch die freie Software Audacity zur¨uckge-
griﬀen [13].

4.2.2 Analyse von Beginn und Ende einer Sprachaufzeich-

nung

W¨ahrend eines Spielszenarios nimmt der Roboter mit seinen Mikrophonen st¨andig
Umgebungsger¨ausche wahr. Damit Rechenzeit gespart werden kann, ist es n¨utzlich
zu deﬁnieren, ab wann ein relevantes Sprachsignal vorliegt und wann lediglich
Grundrauschen aufgenommen wird.

Pﬁster und Kaufmann schlagen hier ein einfaches automatisiertes Verfahren
vor, dass einen Intensit¨atsschwellwert S, eine Minimaldauer einer ¨Außerung ta und
die Maximaldauer einer Pause tb ben¨otigt [16]. Der Roboter soll sich danach stets
in einem von f¨unf Zust¨anden beﬁnden, wobei bei mehreren Aufnahmen hinterein-
ander auch der f¨unfte Zustand durch einen ¨Ubergang vom vierten Zustand zur¨uck
in den ersten ersetzt werden kann. Der f¨unfte Zustand, der den Endzustand be-
schreibt, f¨allt dadurch weg. Abbildung 4.2 zeigt, unter welchen Umst¨anden ein
Zustands¨ubergang erfolgt. Initial beﬁndet sich das System dabei in Zustand S1,
in welchem noch kein Sprachsignal wahrgenommen wurde. Wird die Intensit¨at des
aktuellen Signalparameters gr¨oßer als der Schwellwert S, so ﬁndet ein Wechsel
in Zustand S2 statt. Sinkt die Intensit¨at des Signalparameters wieder, bevor eine
deﬁnierte Zeitdauer ta ¨uberschritten wurde, wird der Anstieg der Intensit¨at als Da-

Abbildung 4.2: Zustands¨uberg¨ange bei der Detektion von relevanten Sprachsigna-
len in Anlehnung an [16]

21

S1InitialS2Intensität > SchwellwertIntensität < SchwellwertS3Dauer > taS4Intensität < SchwellwertIntensität > SchwellwertDauer Pause > tbKapitel 4. Konzepte der Spracherzeugung und Sprachverarbeitung

tenausreißer gewertet und daher wieder verworfen. Das System kehrt in Zustand
S1 zur¨uck. Bleibt die Intensit¨at dagegen konstant ¨uber dem Schwellwert f¨ur l¨anger
als ta, folgt ein Zustands¨ubergang zu Zustand S3. In diesem Zustand wurde der
Anfang eines gesprochenen Textes detektiert. Solange sich das System in diesem
Zustand beﬁndet, werden alle eingehenden Signalparameter als zur Spracheingabe
geh¨orig eingestuft. Sinkt in diesem Zustand die Intensit¨at des aktuellen Signal-
werts wieder unter den Schwellwert, geht das System in Zustand S4, dem Ende
der Sprachaufzeichnung ¨uber. Nur wenn f¨ur l¨anger als tb die Intensit¨at niedriger
als der Schwellwert verbleibt, wird das Ende der Sprachaufzeichnung best¨atigt und
das System geht in Zustand S1 ¨uber, so dass eine neue Spracheingabe detektiert
werden kann. Steigt die Intensit¨at in S4 wieder ¨uber den Schwellwert, so geht
das System in Zustand S3 zur¨uck und die Signalwerte werden der Spracheinga-
be zugerechnet. Alle nicht explizit beschriebenen Ereignisse f¨uhren stets zu einem
reﬂexiven Zustands¨ubergang.

Da dieses Verfahren haupts¨achlich f¨ur ruhige Umgebungen gedacht ist, gilt es
zu pr¨ufen, in wie weit das Verfahren trotzdem im RoboCup Anwendung ﬁnden
kann.

4.2.3 Spracherkennung mit Hilfe eines Mustervergleichs

Beim Sprachmustervergleich wird ein aufgezeichnetes Sprachsignal mit allen Sprach-
signalen verglichen, die vorher vorgegeben wurden. Die Signalfunktion mit der ge-
ringsten Distanz zum Mikrophon-Input wird f¨ur die weiteren Analysen verwendet
(vgl. [16]).

Vorbedingungen: Der Mustervergleich erfordert neben der aufgezeichneten Si-
gnalfunktion von jeder m¨oglichen Eingabe ein Vergleichsmuster. Da alle Roboter
die gleiche Sprachsynthese benutzen, reicht als Vergleichsmuster ein aufgezeichne-
tes Signal aus. Zu jedem Vergleichsmuster muss der gesprochene Text in Schrift-
sprache gespeichert sein, da w¨ahrend des eigentlichen Analyseschrittes das am
besten passendste Referenzmuster berechnet und von diesem der schriftlich zuge-
ordnete Text zu Weiterverarbeitung genutzt wird.

Durchf¨uhrung: Ein Vergleich zwischen zwei Signalen l¨asst sich durch eine Di-
stanzfunktion realisieren. Dabei sollen Funktionen, die sich sehr ¨ahnlich sind, eine
geringe Distanz aufweisen. Da das Signal in Form einer Funktion des Signalpara-
meters ¨uber die Zeit vorliegt, kann f¨ur jeden Zeitpunkt ein Vektor angeben werden,
der den Signalparameter und den Zeitpunkt enth¨alt. Zum selben Zeitpunkt ist der
Unterschied der beiden Signalfunktionen also nur die Diﬀerenz im Signalparameter.
Das Problem des Sprachmustervergleichs liegt in den Unterschieden vom auf-
gezeichneten Signal und den Datenbanksignalen auf Ebene der Prosodie, also
den lautlichen Strukturen der Sprache [2]. Es liegen Diﬀerenzen im Bereich der
Lautst¨arke, der L¨ange, des Sprechrhythmus und der Sprachmelodie vor. Die Un-
terschiede in Lautst¨arke und Grundfrequenz werden bereits in der Vorverarbei-

22

4.2. Spracherkennung

tung durch ¨Uberf¨uhrung der Sprachsignale und der Vergleichsfunktionen in das
Mel-Cepstrum aufgel¨ost. Das Signal liegt nun als Vektor von Frames vor. F¨ur den
eigentlichen Mustervergleich muss nun die Distanz zu jedem Zeitpunkt zwischen
dem Referenzsignal und dem zu analysierenden Signal berechnet werden.

Durch eine Variation in der L¨ange der ausgesprochenen Silben und einer ¨Ande-
rung des Sprechrhythmus kann jedoch nicht davon ausgegangen werden, dass zum
gleichen Zeitpunkt im Referenzsignal und dem aufgezeichneten Signal die gleiche
Silbe gesprochen wird. Es muss also f¨ur jeden Zeitpunkt des zu analysierenden
Signals derjenige Punkt gefunden werden, dessen Abstand zum Referenzsignal am
geringsten ist. Dabei m¨ussen bestimmte Bedingungen erf¨ullt werden, beispielswei-
se die Einhaltung der zeitlichen Reihenfolge der Silben. Dies wird mit Hilfe des
Dynamic-Time-Warping-Algorithmus (DTW) realisiert, welcher eine minimale Di-
stanz zwischen zwei Sprachsignalen unter bestimmten Vorbedingungen berechnen
kann.

4.2.4 Stochastische Sprachverarbeitung

Vorbedingungen:
In der stochastischen Sprachverarbeitung werden keine Re-
ferenzsignalkurven ben¨otigt, daf¨ur jedoch eine Zuordnung von Signalmerkmalen
zu Lauten, Silben oder W¨ortern sowie ein Lexikon, das s¨amtliche zu erkennende
Einheitensequenzen enth¨alt.

Durchf¨uhrung: Nach Rabiner [17] und Ebert und Ebert [4] l¨auft eine stochas-
tische Spracherkennung in f¨unf Schritten ab, wobei die letzten beiden Schritte
lediglich einer Suchraumeingrenzung dienen und nicht von elementarer Bedeutung
sind.

Die Verarbeitung beginnt, wie auch bei der Spachanalyse durch Musterver-
gleich, mit einer Digitalisierung des Sprachsignals, sowie mit einer Vorverarbei-
tung durch Filterung und Frequenzanalyse. Zur Vorverarbeitung z¨ahlt jedoch hier
als elementarer Schritt die Merkmalsextraktion aus dem Sprachsignal. In diesem
Schritt ﬁndet eine erhebliche Datenreduktion statt. Im Anschluss werden diese
Merkmale in Laute, Silben oder W¨orter ¨uberf¨uhrt, je nachdem f¨ur welche Granu-
larit¨at von Untereinheiten man sich entschieden hat. Die Erkennung einer Einheit
beruht nun auf einer Wahrscheinlichkeitsberechnung nach dem Hidden-Markov-
Modell. Im Hidden-Markov Modell wird davon ausgegangen, dass die Wahrschein-

Abbildung 4.3: Spracherkenner nach Rabiner [4]

23

Kapitel 4. Konzepte der Spracherzeugung und Sprachverarbeitung

lichkeit f¨ur einen Zustands¨ubergang, in unserem Fall also die Erkennung einer
Einheit, nur vom aktuellen Zustand abh¨angt und die Wahrscheinlichkeiten f¨ur den
Zustands¨ubergang konstant sind. Die Wahrscheinlichkeit f¨ur die Erkennung einer
Untereinheit h¨angt also deterministisch von den vorher erkannten Einheiten ab.
Die Zust¨ande selbst sind dabei verborgen und k¨onnen nur durch die Ausgabe der
wahrscheinlichsten Einheit beobachtet werden. Aus diesen Untereinheiten werden
in der Weiterverarbeitung W¨orter und S¨atze nach einem vorliegenden Lexikon
gebildet. Weitere Einschr¨ankungen bei der Eliminierung von m¨oglichen Einheiten-
sequenzen bieten syntaktische und semantische Analysen, wobei diese ebenfalls mit
umfangreichen W¨orterb¨uchern bzw. Verarbeitungsverfahren implementiert werden
m¨ussen. Am Ende der Verarbeitung ist die Wortfolge ermittelt, die mit gr¨oßter
Wahrscheinlichkeit in dem Sprachsignal enthalten war.

4.3 Verfahrensauswahl

Da sich diese Arbeit ausschließlich auf eine Roboter-Roboter-Kommunikation be-
schr¨ankt, k¨onnen durch die Auswahl von geeigneten Verfahren in der Sprachsyn-
these Vereinfachungen in der Sprachanalyse erwirkt werden: F¨allt die Entschei-
dung auf eine Syntheseart, bei der keine ¨Anderungen im Sprachrhythmus und der
Sprachgeschwindigkeit von Worten auftreten k¨onnen, sondern das gleiche Wort an
jeder Stelle im Satz und in jeder Satzumgebung immer gleich klingt, so ist beim
Mustervergleich bereits eine sehr gute Erkennungsrate zu erwarten. Es kann sogar
gepr¨uft werden, in wie weit von dem DTW-Algorithmus abstrahiert werden kann
und ob dieser durch eine rein lineare Signalverschiebung entlang der Zeitachse er-
setzt werden kann. Dies wird m¨oglich, da zwar der exakte Anfangszeitpunkt des
Sprachsignals nicht bekannt ist, aber immer die gleiche Silben- und Pausenl¨ange
garantiert werden kann. Dies l¨asst eine Reduktion der Zeit und Rechenkomplexit¨at
erwarten, die unter den gegebenen Hardwareeinschr¨ankungen und im Hinblick auf
einen dynamischen Spielﬂuss sehr relevant sind.

Eine stochastische Sprachverarbeitung ist unter diesen Voraussetzungen nicht
nur sehr komplex in der Berechnung, sondern kann kaum eine Verbesserung in der
Erkennungsrate bringen, da diese schon im Mustervergleich nahezu optimal sein
sollte.

Die Wahl f¨ur das zu implementierende System f¨allt daher auf eine Verkettungs-
synthese, die zur Erzeugung eines Satzes immer gleich klingende Worte aus einer
Datenbank verbindet, in Zusammenhang mit einem (ggf. vereinfachten) Muster-
vergleich zur Sprachanalyse.

Sprachanalysen mittels Mustervergleich sind nur bedingt auf die Erkennung
von menschlicher Sprache, die nicht auf einen bestimmten Sprecher trainiert ist,
zu ¨ubertragen. Es w¨are nicht nur eine große Anzahl von Referenzmustern n¨otig,
sondern auch eine gr¨oßere Variabilit¨at im Signal, das vom DTW-Algorithmus nicht
gew¨ahrleistet werden kann. Daher bedeutet diese Wahl der Sprachanalyse eine
starke Einschr¨ankung f¨ur die m¨ogliche Erweiterung auf die Interaktion der Roboter
mit Menschen und die damit verbundene Analyse menschlicher Sprache.

24

Kapitel 5

Implementation

Nachfolgend wird ein beispielhafter Ansatz zur Implementation einer Roboter-
Roboter-Kommunikation vorgestellt. Dabei wird von der konkreten Anwendung
auf dem DARwIn-OP-Roboter abstrahiert und sowohl f¨ur die Sprachsynthese als
auch f¨ur die Sprachanlyse ein allgemeiner Ansatz vorgestellt, der sich in beliebige
Programmiersprachen und auf beliebige Systeme ¨ubertragen l¨asst.

5.1 Sprachsynthese

In Kapitel 4.3 ist die Verkettungssynthese als optimaler Ansatz ermittelt worden,
wobei ganze Worte als Einheiten verwendet werden sollen. Im Laufe der Recherche
gelang es jedoch nicht, ein bereits existierendes Programm ausﬁndig zu machen,
das eine solche Synthese realisiert und sich einfach in das bestehende Softwarear-
chitektursystem auf dem Roboter integrieren l¨asst.

Die Wahl ist daher auf das Programm eSpeak gefallen, welches die Formant-
synthese anwendet und in vielen Sprachen erh¨altlich ist [1]. Es l¨auft unter Linux
als Konsolen-Tool und kann daher einfach in Programmiersprachen integriert wer-
den, auch wenn es keine Bibliothek f¨ur diese Sprache gibt. Eine Nachinstallation
auf den Robotern ist nicht n¨otig, da es in der Linuxversion, die auf den Robo-
tern l¨auft, bereits vorhanden ist. Ein großer Vorteil des Konsolenprogramms ist,
dass sich Sprechgeschwindigkeit und Pitch des Sprachsignals einfach ¨uber Para-
meter anpassen lassen. So kann leicht jedem Roboter eine unterscheidbare Stimme
gegeben werden, ohne große ¨Anderungen im Programmtext vornehmen zu m¨ussen.
Das Programm eSpeak ist nicht darauf ausgelegt, eine menschen¨ahnliche Stim-
me zu erzeugen, so dass das Ergebnis der Synthese eindeutig als mechanisch er-
zeugtes Signal zu erkennen ist. Es stellte sich jedoch als problematisch heraus,
dass, bedingt durch die Formantsynthese, das gleiche Wort am Satzanfang anders
ausgesprochen wird als am Satzende oder in der Satzmitte. Damit dies nicht zu
einem Problem f¨ur die Sprachverarbeitung f¨uhrt, wird die Formantsynthese so ver-
wendet, dass die Ausgabe wie eine Verkettungssynthese erscheint: Innerhalb eines
Satzes steht nach jedem Wort ein Punkt, so dass das System jedes Wort als ei-
genen Satz behandelt und somit immer gleich ausspricht. Diese Art der Synthese

25

Kapitel 5. Implementation

bietet als weiteren Vorteil l¨angere Pausen zwischen den einzelnen W¨ortern, die eine
Trennung einzelner W¨orter im Satz m¨oglich machen.

Eine Trennung zwischen zwei S¨atzen kann auf zwei Arten realisiert werden:
Eine M¨oglichkeit besteht darin, dass ein Satzende durch ein deﬁniertes letztes
Wort bestimmt wird. Problematisch ist hier jedoch, dass die Satzseparierung nicht
korrekt m¨oglich ist, wenn das letzte Wort fehlerhaft erkannt wurde. Daher bietet
es sich auch hier an, die Satztrennung an Hand einer Pause zu detektieren, wobei
diese Pause mindestens doppelt so lang wie die Wortpause sein muss, damit eine
klare Trennung der beiden Pausen m¨oglich wird.

5.2 Sprachsynthese

5.2.1 Auswahl der Programmiersprache

Die Softwarearchitektur der Roboter des Hamburger RoboCup-Teams setzt sich
aus einem komplexen Klassenkonstrukt zusammen, das zum einen Teil in der In-
terpretersprache Python und zum anderen in der Compilersprache C++ verfasst
ist. Dieses hybride System erm¨oglicht durch kurze Compile-Zeiten schnelle Soft-
ware¨anderungen auch w¨ahrend eines Spiels, da nur wenige Sekunden gebraucht
werden, um die aktuelle Software zu kompilieren.

Damit sich die Sprachanalyse optimal in die bestehende Softwarearchitektur
einpﬂegen l¨asst, ist es notwendig, Teile der Software in C++ und Teile in Python
zu implementieren, um einerseits die Compile-Zeit gering zu halten und anderer-
seits aufwendige Rechenoperationen wie die Distanzberechnung von Vektoren so
zeitsparend wie m¨oglich ausf¨uhren zu k¨onnen. Um jedoch zun¨achst das Verfahren
an sich unabh¨angig von den Robotern zu testen, ist die Wahl auf eine Sprache ge-
fallen, die Audioanalyse durch eigene Bibliotheken gut unterst¨utzt. Daher ist das
Testsystem, das im Folgenden vorgestellt wird, in Java verfasst.

5.2.2 Die Softwarearchitektur

Herzst¨uck der Software ist ein Zustandsautomat entsprechend der Abbildung 4.2.2.
Im Initialzustand werden daf¨ur die Referenzdaten eingelesen, außerdem wird der zu
pr¨ufende Audiostream initialisiert. Jeder danach eingelesene Signalwert wird dar-
auf ¨uberpr¨uft, ob er bloßes Grundrauschen darstellt oder Sprache zugeordnet wer-
den kann. Sobald ein Wert als von sprachlicher Herkunft klassiﬁziert wurde, wird
dieser als Wortanfang gespeichert. Folgt allerdings innerhalb der n¨achsten zehn
Samples wieder ein Datenwert, der nicht zur Sprache z¨ahlt, wird dieser Anfangs-
wert wieder verworfen. Folgen erst im weiteren Verlauf Signalwerte, die dem Grund-
rauschen zugeordnet werden, wird ein potentielles Wortende markiert. Dieses wird
jedoch erst best¨atigt, wenn die folgenden Samples ebenfalls dem Grundrauschen
zugeordnet werden. Wie groß die Anzahl dieser Pausensamples ist, h¨angt davon
ab, ob es sich bei den Analysedaten um Idealdaten oder Originaldaten aus Mikro-
phonaufnahmen handelt. Im ersten Fall muss die Pause mindestens eine L¨ange von

26

5.2. Sprachsynthese

5000 Samples aufweisen, im zweiten Fall ist der Minimalwert der Pause doppelt so
lang. Dieser hohe Wert wurde gew¨ahlt, damit die einzelnen Worte bei der Spra-
cherzeugung als eigenst¨andiger Satz generiert werden k¨onnen (vgl. 5.1). So folgt
auf jedes Wort eine lange Pause, die gut f¨ur eine eine Segmentierung geeignet ist.
Sind Wortanfang und Wortende gefunden, wird die L¨ange des Wortes gepr¨uft. Ist
dieses kleiner als 500 Samples, kann es sich nicht um ein Wort handeln, sondern
ein St¨orger¨ausch wurde irrt¨umlich detektiert. Die Aufnahme wird im Ergebnis ver-
worfen und es wird nach einem neuen Wortanfang gesucht. Anderenfalls wird das
gefundene Wort der eigentlichen Analyse ¨ubergeben. Der Zyklus der Worterken-
nung beginnt gleichzeitig von vorn.

5.2.3 Die Energiewertbestimmung

Die Energiewertbestimmung soll f¨ur einen gegebenen Signalwert entscheiden, ob
dieser zu einer Spracheingabe geh¨ort oder nicht. Zu diesem Zweck wird ¨uber die
letzten im Buﬀer gespeicherten Werte des Signalparameters ein gleitender Durch-
schnittswert berechnet. Ist das eingehende Signal mindestens doppelt so laut wie
dieser Durchschnittswert und wird dabei zus¨atzlich ein bestimmter Schwellwert
¨uberschritten, so wird ein Signalwert einer Spracheingabe zugeordnet. Der gleiten-
de Durchschnitt D berechnet sich dabei wie folgt:

D =

n
(cid:88)

i=0

value(i)
n

(5.1)

value(i) entspricht dabei dem Signalwert mit dem Index i und n der Anzahl der
betrachteten Samples. Die Zahl n bestimmt sich nach der aktuellen Anzahl der
Werte, die im Buﬀer gehalten werden. Durchschnittlich sind dies 6000 Samples,
Abweichungen davon gibt es sowohl bei der Speicherung der ersten Signalwerte als
auch bei l¨angeren Worten. Ein einmal als Sprachanfang markierter Wert bleibt so
lang im Buﬀer, bis er revidiert wurde oder ein komplettes Wort erkannt wurde.

Der Vorteil der gleitenden Durchschnittsberechnung ¨uber den Werten im Stream-
buﬀer liegt auf der einen Seite darin, dass der Durchschnittswert durch einen
Ausreißer-Signalwert nicht zu stark beeinﬂusst wird. Andererseits ﬂießen auch nicht
zu viele Werte in die Berechnung ein, denn dies w¨urde dazu f¨uhren, dass auch kor-
rekte Spracheingaben nicht mehr detektiert werden, da sich der Durchschnittswert
zu langsam anpasst.

F¨ur die Wortanalyse wird die Zuordnung eines Signalparameters zu einer Sprach-
eingabe vor der Weiterverarbeitung geﬁltert. Der Filter h¨alt dazu eine Liste der
letzten zehn Signalparameter bereit. Sind unter diesen mindestens zwei, die nach
der Energiewertbestimmung einem Sprachsignal zugeordnet werden k¨onnen, wird
jeder eingehende Wert ebenfalls Sprache zugeordnet. Im Filter werden die ur-
spr¨unglichen Zuordnungen nach dem gleitenden Durchschnitt gespeichert, die ge-
ﬁlterten Werte werden lediglich f¨ur die Weiterverarbeitung genutzt. So werden die
Signalwerte um ein tats¨achliches Sprachsignal herum gegl¨attet.

27

Kapitel 5. Implementation

5.2.4 Der Streambuﬀer

Im Streambuﬀer ist die tempor¨are Speicherung der eingelesenen Signalwerte rea-
lisiert. Dabei werden neue Werte aus dem Audiostream abgefragt und in einem
Array gespeichert. Bei jedem Einlesen eines neuen Wertes wird außerdem ¨uber-
pr¨uft, ob Daten aus dem Buﬀer wieder entfernt werden k¨onnen. Dies ist dann der
Fall, wenn kein Wortanfang markiert und die L¨ange des Buﬀers von 6000 Samples
¨uberschritten ist.

Der Streambuﬀer bietet Methoden an, einen neuen Wortanfang und ein neues
Wortende zu setzen und gesetzte Werte wieder zur¨uck zu setzen. Mit Hilfe dieser
Methoden kann ein Array zur¨uckgegeben werden, das die Signalwerte f¨ur ein de-
tektiertes Wort plus den Puﬀerbereich f¨ur die Verschiebung enth¨alt (vgl. Quellcode
5.1).

// B e r e c h n e t d i e Laenge f u e r d a s zu e r z e u g e n d e Array
i n t

l e n g t h = e n d i n t e r e s t i n g −s t a r t i n t e r e s t i n g +2∗ c o n f i g .OVERHEAD;

{

1 p u b l i c d o u b l e [ ] g e t I n t e r e s t i n g D a t a ( )
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

}
r e t u r n temp ;

temp [ i ] = b u f f e r . g e t ( i ) ;

}

}

temp = new d o u b l e [ l e n g t h ] ;

d o u b l e [ ]
// Fuegt d i e Werte i n d a s Array z u r Ausgabe e i n
f o r ( i n t
{

i <temp . l e n g t h ;

i = 0 ;

i ++)

// H i e r w i r d d e r F a l l a b g e f a n g e n , d a s s v o r dem Wortanfang
// n i c h t g e n u e g e n d B u f f e r w e r t e z u r V e r f u e g u n g s t e h e n
i f ( c o n f i g .OVERHEAD < s t a r t i n t e r e s t i n g )
{
temp [ i ] = b u f f e r . g e t ( i+s t a r t i n t e r e s t i n g −c o n f i g .OVERHEAD) ;
}
e l s e
{

Quellcode 5.1: Erzeugung des Arrays mit dem relevanten Sprachbereich f¨ur die
weitere Analyse

5.2.5 Die Wortanalyse

Wenn eine Gruppe von Samples als interessante Region gekennzeichnet wurde,
gilt es als n¨achstes, die gr¨oßte ¨Ubereinstimmung mit einer der Sounddateien, die
als Referenzdaten angegeben sind, zu suchen. Wegen der St¨orger¨ausche kann da-
bei nicht gew¨ahrleistet werden, dass der Anfang und das Ende des Wortes exakt
erkannt worden sind. Daher werden f¨ur jedes zu analysierende Wort 256 lineare
Verschiebungen getestet und das globale Minimum ¨uber alle daraus resultierenden
Distanzberechnungen gebildet. Dazu werden im Buﬀer immer 2048 Samples vor-
gehalten, die vor dem markierten Wortanfang und nach dem markierten Wortende
liegen. Es wird nun in jedem Analysedurchgang ein neuer Anfangswert a f¨ur die
Analyse bestimmt und von diesem bis zum Signalwert a + Wortl¨ange L gepr¨uft.
Hat also die Wortanalyse den Wortanfang an der Stelle x markiert, so wird im
ersten Analysedurchlauf von x-1024 bis x-1024+L gepr¨uft. Im n¨achsten Durchlauf
wird sowohl auf den Wortanfang als auch auf das Ende vom vorherigen Durch-
gang ein Indexwert von acht Samples addiert und daraus ergibt sich der n¨achste
zu pr¨ufende Bereich. Es ergibt sich also, dass jede achte Verschiebung im Bereich

28

5.2. Sprachsynthese

1024 + detektiertes Wort + 1024 getestet wird.

Jeder so erhaltene Wert wird gegen alle m¨oglichen Referenzdaten gepr¨uft.
Dazu wird zun¨achst der in jedem Schritt zu ¨uberpr¨ufende Bereich in das Mel-
Cepstrum umgewandelt. Zur Umwandlung der Sounddateien wird eine Bibliothek
von Klaus Seyerlehner verwendet [21][22]. Die Bibliothek liefert ein Array von Vek-
toren zur¨uck, in denen pro Cepstrum-Beh¨alter die Werte gespeichert sind. Jeder
Vektor in dem Array der zu pr¨ufenden Sounddateien wird nun gegen den Vektor
mit dem gleichen Index in den Referenzdaten gepr¨uft. Der Quelltextausschnitt 5.2
beschreibt dieses Verfahren. Von allen berechneten Distanzwerten wird nur das
globale Minimum gespeichert, alle anderen Vergleichswerte werden verworfen.

F¨ur die Referenzdatei, deren berechnete Distanz am geringsten war, wird der
Inhalt durch Nachschlagen in einer Datei ermittelt, in welcher die Zuordnung von
Dateiname und gesprochenem Inhalt vermerkt ist.

r e f e r e n z e n . k e y S e t ( ) )

j e d e r m o e g l i c h e n R e f e r e n z d a t e i

temp ,

i n t

i )

// F u e h r t d i e Umwandlung i n d a s Mel−Cepstrum d u r c h
V e c t o r<d o u b l e [ ] > toCheck = g e n e r a t e V e c t o r ( temp ) ;

:

// P r u e f t U e b e r e i n s t i m m u n g mit
f o r ( S t r i n g s
{

1 p r i v a t e v o i d computeMin ( d o u b l e [ ]
2 {
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18 }

m i n D i s t a n c e = d i s t a n c e ;
v a l u e O f M i n D i s t = s ;

}

}

// V e k t o r d i s t a n z b e r e c h n e n
d o u b l e d i s t a n c e = g e t V e c t o r D i s t a n c e ( toCheck ,
// G l o b a l e s Minimum s p e i c h e r n
i f ( d i s t a n c e < m i n D i s t a n c e )
{

r e f e r e n z e n . g e t ( s ) ) ;

Quellcode 5.2: Berechnung der besten ¨Ubereinstimmung durch Umwandlung der
Sounddatei in das Mel-Cepstrum und anschließende Vektordistanzberechnung

5.2.6 Speicherung der Referenzdaten

Da jeder Roboter, der eine Sprachanalyse im Spiel durchf¨uhren soll, Referenzdaten
ben¨otigt und diese auf allen Robotern identisch sind, bietet es sich nicht an, eine
Menge von Sounddateien als Referenz zu verwenden. Der Speicherplatzbedarf f¨ur
die erforderliche Datenmenge w¨are unn¨otig groß, außerdem m¨usste jeder Roboter
zu Beginn der Sprachanalyse die Referenzdaten in ein Mel-Cepstrum umwandeln,
wodurch eine hohe Redundanz entsteht und Rechenzeit verschwendet wird. Es
bietet sich daher an, den Referenzdatensatz vor dem ¨Uberspielen auf die Roboter
in das Mel-Cepstrum umzuwandeln und lediglich die so entstandene Array- und
Vektorstruktur zu speichern. Als Speicherform wurde das XML-Format gew¨ahlt,
wobei die Speziﬁkation der Sounddatei das h¨ochste Element bildet. Diesem Element
sind die einzelnen Arrays untergeordnet, welche wiederum die Vektoren enthalten.
Auf unterster Ebene werden in jedem Vektor die einzelnen Mel-Cepstrum-Werte
als Element eingef¨ugt (vgl. Abb. 5.1). Beim Starten der Sprachanalyse m¨ussen nur
noch die XML-Files wieder eingelesen und in die erwartete Array-Vektor-Struktur
gebracht werden.

29

Kapitel 5. Implementation

Abbildung 5.1: Struktur der erzeugten XML-Dateien.

5.2.7 Test- und Analysestruktur

Um das System auch ohne Roboter testbar zu machen, wurde eine Architektur
entwickelt, die einen Mikrophoninput mit einer Audiodatei simulieren kann. Diese
Klasse liest die Datei zwar komplett ein, stellt die Signalwerte aber nur nach und
nach zur Verf¨ugung. Mit dieser Hilfsklasse ist es sowohl m¨oglich auf dem Rechner
selbst erzeugte Idealdaten zu testen, als auch auf dem Roboter aufgenommene
Audiodateien zu verwenden.

F¨ur die Analyse der Erkennungsraten wird ein Ordner mit zu pr¨ufenden Da-
ten eingelesen. In diesem ist eine Datei hinterlegt, die zu jeder Sounddatei die
tats¨achlich synthetisch erzeugten Worte speichert. F¨ur jede Analyse werden die
vom Programm errechneten W¨orter mit den tats¨achlich erzeugten verglichen. Rich-
tig erkannte Worte werden sowohl nach Position als auch nach Inhalt gespeichert,
so dass eine prozentuale Auswertung der Erkennungsraten nach beiden Mustern
m¨oglich ist.

30

Kapitel 6

Evaluation und Ergebnisse

In diesem Kapitel werden verschiedene Aspekte der im vorherigen Kapitel be-
schriebenen Implementation kritisch beleuchtet, außerdem werden die Ergebnisse
vorgestellt, die damit erzielt werden konnten.

6.1 Evaluation

6.1.1 Einteilung der Sprachdateien in Sektionen

In der ersten Version des Programms wurde die Spracheingabe durch den endli-
chen Zustandsautomaten (State-Machine) lediglich in S¨atze unterteilt. Dies f¨uhr-
te dazu, dass nur f¨ur die Daten zur Distanzberechnung von 0,00 bis 6,00 Meter
600 Referenzdatens¨atze pro eingegebenem Satz gepr¨uft werden mussten. Um eine
zukunftsf¨ahige Software zu schaﬀen, die auch f¨ur gr¨oßere Distanzen und weitere
Datens¨atze wie die Angabe einer Position auf dem Spielfeld nutzbar ist, muss die
Menge an Referenzdaten m¨oglichst klein gehalten werden.

Die Idee war daher, den Algorithmus so umzustellen, dass die Spracheingabe
nach einzelnen Worten getrennt wird und diese einzeln analysiert werden. Grund-
voraussetzung daf¨ur ist, dass die einzelnen Worte untereinander in ihrer Abbildung
im Mel-Cepstrum einen gen¨ugend großen Abstand voneinander haben, so dass sie
weiterhin klar voneinander abgegrenzt werden k¨onnen. In einem Test wurden daher
zun¨achst die Referenzdaten gegen sich selbst gepr¨uft, um die Distanz der Worte
zueinander zu errechnen. Tabelle 6.1 zeigt das Ergebnis, wobei als Referenzdaten
auf dem Computer erzeugte eSpeak-Sounddateien verwendet wurden.

Die Matrix zeigt, dass es zwar einzelne Distanzen wie die von Nine zu Five gibt,
die mit 7,5 recht gering sind, im Durchschnitt jedoch ein Abstand von 16,02 der
einzelnen Soundﬁles zueinander gegeben ist. Da diese Werte hoch genug sind, um
einen Mustervergleich darauf aufzubauen, wurde die Sprachanalyse ab der zweiten
Version auf die Detektion von W¨ortern umgestellt.

31

Kapitel 6. Evaluation und Ergebnisse

D
D 0.0
M 17.7
17.1
P
17.4
0
20.5
1
20.4
2
22.7
3
20.3
4
16.9
5
20.0
6
17.5
7
22.1
8
17.8
9

M
17.7
0.0
18.6
15.5
19.7
18.3
20.0
18.2
19.1
17.8
16.8
19.4
19.1

P
17.1
18.6
0.0
15.1
13.4
14.3
15.9
14.2
11.5
16.3
13.3
20.6
13.2

0
17.4
15.5
15.1
0.0
21.2
18.1
21.2
18.1
16.4
17.7
11.2
23.7
17.7

1
20.5
19.7
13.4
21.2
0.0
17.2
16.6
12.3
13.3
19.7
19.3
19.1
13.3

2
20.4
18.3
14.3
18.1
17.2
0.0
10.5
16.4
16.5
14.2
17.0
18.6
17.9

3
22.7
20.0
15.9
21.2
16.6
10.5
0.0
17.0
17.2
15.4
19.6
19.5
19.0

4
20.3
18.2
14.2
18.1
12.3
16.4
17.0
0.0
12.9
17.8
16.2
21.3
14.5

5
16.9
19.1
11.5
16.4
13.3
16.5
17.2
12.9
0.0
18.3
13.4
22.6
7.5

6
20.0
17.8
16.3
17.7
19.7
14.2
15.4
17.8
18.3
0.0
16.7
16.1
19.9

7
17.5
16.8
13.3
11.2
19.3
17.0
19.6
16.2
13.4
16.7
0.0
23.3
15.4

8
22.1
19.4
20.6
23.7
19.1
18.6
19.5
21.3
22.6
16.1
23.3
0.0
22.3

9
17.8
19.1
13.2
17.7
13.3
17.9
19.0
14.5
7.5
19.9
15.4
22.3
0.0

Abbildung 6.1: Distanzen der Referenzdatens¨atze zueinander, wobei D f¨ur das Wort
Distance“, M f¨ur
”

Meter“ und P f¨ur
”

Point“ steht
”

6.1.2 Bewertung der Detektion von Sprachbeginn und Spra-

chende

Die Detektion von Wortbeginn und Wortende beruht insbesondere auf der Sprach-
pause, die zwischen den W¨ortern gemacht wird. Dank der Spracherzeugung durch
eSpeak, die darauf beruht, dass jedes Wort als einzelner Satz erzeugt wird, lassen
sich die W¨orter sehr gut an Hand der Ruhephase zwischen den W¨ortern segmen-
tieren. Des Weiteren wird jeder Frame als relevante Sprachinformation betrachtet,

Abbildung 6.2: Kennzeichnung der Einzelworte in einem Idealdatensatz

32

6.1. Evaluation

Abbildung 6.3: Kennzeichnung der Einzelworte in einer Originalaufnahme

dessen Signalwert mehr als doppelt so hoch wie der durchschnittliche Signalwert
ist. Ebenfalls spielt die Durchschnittsberechnung eine Rolle, welche nur die letzten
6000 Signalwerte betrachtet, und die Aussortierung von einzelnen Peaks, auf die
direkt eine l¨angere Pause folgt.

Das Zusammenspiel der benannten Parameter ist sehr komplex und die daraus
resultierenden kombinatorischen M¨oglichkeiten ließen im Rahmen dieser Arbeit
nur eine experimentelle Bestimmung ihrer Belegung zu.

Die Graﬁken 6.2 und 6.3 zeigen das Ergebnis der Wortdetektion. In rot ist
jeweils die Signalfunktion eingezeichnet, gr¨un sind die Bereiche, die von der Si-
gnalst¨arke her einem Wort zugeordnet werden k¨onnen, und in schwarz sind die
durch die State Machine tats¨achlich detektierten Worte markiert. Abbildung 6.2
ist dabei mit Idealdaten erstellt, die auf dem eigenen Computer erzeugt und da-
nach analysiert wurden. Abbildung 6.3 zeigt Realdaten, die mit dem Mikrophon
im Roboter aufgenommen wurden. Beiden Abbildungen liegt ein Sprachinput von

Distance. 3. Point. 7. 3. Meter.“ zu Grunde.

”

6.1.3 Evaluation der Signalwertverschiebung f¨ur die Sprach-

auswertung

Statt des DTW-Algorithmus wird in der vorgestellten Software eine lineare Ver-
schiebung der Signalwerte verwendet. Die Abbildungen 6.4 und 6.5 zeigen die sich
daraus ergebenden Abst¨ande f¨ur alle verwendeten Verschiebungen und alle Refe-
renzdaten. Abbildung 6.4 zeigt dabei die Analyse des Wortes Distance, Abbildung
6.5 die Analyse des Wortes Seven. Beide Analysen beruhen auf Idealdaten. In rot

33

Kapitel 6. Evaluation und Ergebnisse

Abbildung 6.4: Distanzberechnungen f¨ur das Wort

Distance“

”

Abbildung 6.5: Distanzberechnung f¨ur das Wort

Seven“

”

ist der Distanzverlauf des jeweils korrekten Wortes eingezeichnet, in den anderen
Farben die Distanzen aller anderen Referenzdaten.

Es zeigt sich, dass es jeweils in den abgebildeten Sektionen Bereiche gibt, in
denen das korrekte Wort in der Distanz deutlich unter allen anderen liegt. Es gibt

34

6.1. Evaluation

aber auch solche Bereiche, in denen andere, nicht korrekte Worte eine geringere
Distanz haben. Es wird deutlich, dass eine Verschiebung der Referenzdaten sinn-
voll ist, weil abh¨angig von der G¨ute der Worterkennung nicht immer im selben
Verschiebungsbereich das korrekte Referenzdatum die geringste Distanz aufweist.
Somit stellt die Verschiebung sicher, dass trotz einer ungenauen Erkennung des
Wortanfangs stets das Referenzdatum zum tats¨achlich gesagten Wort die gerings-
te Distanz aufweist, wenn das globale Minimum betrachtet wird.

6.1.4 Einﬂuss verschiedener Parameter auf die Worterken-

nung

Da das Verfahren zur Worterkennung auf einer Distanzberechnung der aufgenom-
menen Daten zu Referenzdaten beruht, ist die Erkennung um so besser, je gr¨oßer
die Distanz der Referenzdaten zueinander ist. Dieser Abstand wird vor allem durch
die Gr¨oße der Fenster beeinﬂusst, in die das Signal aufgeteilt wird, sowie durch die
Samplingrate, mit der die Sounddatei abgetastet wird. Die in 6.1.1 beschriebene
Matrix ist mit einer Fenstergr¨oße von 1024 Samples und einer Samplingrate von
44100 Hz entstanden.

L¨asst man die Samplingrate ﬁx bei 44.1 kHz und ¨andert lediglich die Fenster-
gr¨oße, so hat dies die in Tabelle 6.6 gezeigten Auswirkungen auf den mittleren Ab-
stand der Worte zueinander. Es zeigt sich deutlich, dass der mittlere Wortabstand
mit steigender Fenstergr¨oße ebenfalls vergr¨oßert wird. Allerdings hat sich in der
Praxis eine Fenstergr¨oße ab einschließlich 2048 Samples nicht mehr als praktikabel
erwiesen, da es Worte gibt, die k¨urzer sind, und damit die Worterkennungsrate
wieder massiv sinkt.

Im zweiten Versuch wird die Fenstergr¨oße unver¨andert bei 1024 Samples belas-
sen und die Samplingrate ver¨andert. In Tabelle 6.7 ist das Ergebnis des Versuchs
dargestellt. Es zeigt sich, dass der mittlere Wortabstand bis zu einer bestimmten
Samplingrate zusammen mit dieser deutlich ansteigt. Dies ist der Punkt der eige-
nen Samplingrate der Soundaufnahmen, der hier bei 22050 Hz liegt. Danach ist
nur noch ein sehr schwacher Anstieg und zuletzt sogar ein Abfall der Abst¨ande zu

Fenstergr¨oße Mittlerer Wortabstand
128 Samples
256 Samples
512 Samples
1024 Samples
2048 Samples
4096 Samples

4,95
8,02
11,50
16,02
21,88
29,74

Abbildung 6.6: Mittlerer Wortabstand bei einer Samplingrate von 44 kHz und
variabler Fenstergr¨oße

35

Kapitel 6. Evaluation und Ergebnisse

Samplingrate Mittlerer Wortabstand

8000 Hz
11025 Hz
16000 Hz
22050 Hz
32000 Hz
44100 Hz
48000 Hz
96000 Hz

12,72
13,57
14,48
15,16
15,79
16,02
16,04
15,99

Abbildung 6.7: Mittlerer Wortabstand bei einer Fenstergr¨oße von 1024 Samples
und variabler Samplingrate

verzeichnen. Daraus l¨asst sich schließen, dass die optimale Samplingrate diejenige
ist, die in der Sounddatei verwendet wurde. Wird eine wesentlich niedrigere Ra-
te benutzt, wirkt sich dies negativ auf die Erkennungsrate der W¨orter aus. Eine
h¨ohere Rate f¨uhrt dagegen nicht zu einer nachhaltigen Verbesserung der Untersu-
chungsergebnisse.

6.1.5

Implementation einer Robotererkennung durch
Frequenzanpassungen

Elementar bei den in dieser Arbeit pr¨asentierten Dialogablaufstrategien ist, dass
die Roboter bei der Analyse der Daten erkennen, welcher Roboter diese Daten
gesprochen hat. Als Versuchsreihe wurden dazu als Referenzdaten pro Wort drei
verschiedene Sounddateien erzeugt, jeweils mit einer unterschiedlichen Sprachfre-
quenz. Es zeigte sich, dass die Frequenzwerte so gew¨ahlt werden k¨onnen, dass
bei der Analyse von 600 Idealdatens¨atzen (200 pro Frequenzwert) zu 100 % der
richtige Roboter als Sprecher erkannt werden konnte. In der Testreihe wurden die
eSpeak-Pitches 30, 50 und 70 verwendet. Wie groß die Erkennungsrate der einzel-
nen Wortinhalte ist, ist nicht Gegenstand der Testreihe gewesen.

Im Ergebnis ist es m¨oglich, den verschiedenen Roboter eine unterschiedliche

Stimme zu geben und sich diese bei der Sprachanalyse zu Nutze zu machen.

6.2 Ergebnisse

6.2.1 Auswertung des gew¨ahlten Verfahrens f¨ur Idealdaten

Zu Testzwecken wurden mit Hilfe eines Python-Skripts 600 voneinander verschie-
dene Sounddateien der Art
Distance. X. Point. Y. Z. Meter.“ erzeugt, wobei es
sich bei X, Y und Z um ganzzahlige Werte zwischen 0 und 6 f¨ur X und zwischen 0

”

36

6.2. Ergebnisse

und 9 f¨ur Y und Z handelt. Das Testprogramm analysiert die eingegebenen Sound-
dateien, errechnet das Ergebnis und vergleicht dieses mit dem tats¨achlichen Wort,
das aus einer Textdatei ausgelesen wird.

Die Erkennungsrate f¨ur diese Sounddateien lag bei 100 %, es wurde kein einziges

Wort falsch erkannt.

6.2.2

¨Ubertragung des gew¨ahlten Verfahrens auf Original-
daten

F¨ur die ¨Ubertragung des Verfahrens auf Originaldaten wurden zun¨achst neue Re-
ferenzdaten ben¨otigt. Die Originaldaten sollen durch die Mikrophone des Roboters
aufgenommen werden. Dazu wurden zwei Roboter in einer Entfernung von einem
Meter zueinander aufgestellt, so dass der Lautsprecher des einen und das Mikro-
phon des anderen Roboters zueinander zeigten (siehe Abb. 6.8). Die auf die be-
schriebene Weise aufgenommenen Referenzdaten wurden mit Hilfe der Detektion
von Wortanfang und Wortende und dem Programm Audacity so geschnitten, dass
keine Samples außer denen zum Wort zugeh¨origen gespeichert wurden.

Es wurden weitere Aufnahmen mit dem gleichen Versuchsaufbau gemacht, wo-
bei der eine Roboter nun ¨uber mehrere Minuten komplette Tests¨atze erzeugte und
ausgab. Der andere Roboter speicherte diese ab, so dass sie sp¨ater zur Analy-
se herangezogen werden konnten. Auch die Testdatens¨atze wurden mit Hilfe des
Programms Audacity manuell voneinander separiert, wobei hier jedoch absichtlich
zu Beginn und Ende unterschiedlich viel Pause belassen wurde. Sowohl die Refe-
renzdaten als auch die Testdatens¨atze wurden per Rauschreduktion in Audacity
vorverarbeitet.

Von den 100 Originaldatens¨atzen lag die Erkennungsrate bei 100 %. Dabei wur-
de nicht mit Robotern gearbeitet, die sich beim Sprechen und Zuh¨oren bewegen,
um die Umgebungsger¨ausche gering zu halten. Allerdings wurden die Aufzeichnun-
gen mit stehenden Robotern gemacht, so dass die Motoren- und L¨ufterger¨ausche
deutlich auf den Aufnahmen zu h¨oren sind. Unter den momentan auf den Robo-

Abbildung 6.8: Versuchsaufbau bei der Aufnahme der Originaldatens¨atze und Re-
ferenzdaten.
DARwIn-OP Graﬁk von http://www.robotis.com/img/img ko/ sub/DARwIn img 05.jpg

37

1 MeterKapitel 6. Evaluation und Ergebnisse

tern gegebenen Hardwarebedingungen sind andere Testszenarien nicht erfolgver-
sprechend (vgl. Kapitel 2.1).

6.2.3 Erforderlichkeit des DTW-Algorithmus

In Kapitel 4.3 wurde die These aufgestellt, dass eine Implementation des DTW-
Algorithmus f¨ur die Roboter-Roboter-Kommunikation durch eine einfache lineare
Verschiebung der Vergleichsmuster ersetzt werden kann.

Wie in den vorhergehenden Kapiteln 6.2.1 und 6.2.2 beschrieben, liefert der
gew¨ahlte Algorithmus Erkennungsraten von 100 %. Eine lineare Verschiebung der
Sprachsignale ist somit tats¨achlich ausreichend.

Die Verwendung einer linearen Verschiebung hat ihren Vorteil gegen¨uber dem
DTW-Algorithmus in der Laufzeit begr¨undet: Der Dynamic-Time-Warping-Algo-
rithmus hat eine Rechenkomplexit¨at im Bereich O(N 2), also eine quadratische
Laufzeit. Zwar gibt es Ans¨atze, einen Algorithmus basierend auf dem DTW in
linearer Laufzeit zu schaﬀen (Fast-DTW), allerdings ist in diesen Ans¨atzen bisher
nur eine im Optimalfall n¨aherungsweise lineare Rechenkomplexit¨at erzielt worden.
Im Gegensatz zum DTW-Algorithmus ﬁndet der Fast-DTW auch nicht in jedem
Fall das optimale Ergebnis [20]. Die lineare Verschiebung demgegen¨uber kommt mit
einer Laufzeit von O(N ) aus, da in einer einfachen Schleife nur jeder achte Wert
einmalig verglichen wird. Gerade unter den gegebenen Hardwareeinschr¨ankungen
der Roboter l¨asst sich hier eine wertvolle Einsparung an Rechenzeit erreichen.

6.2.4 Laufzeitanalyse

Auf dem Laptop, auf dem die Analysen gemacht wurden (DELL INSPIRON N5110,
Intel Core i7-2670QM CPU, 2.20GHz x 8), wurde pro Satzanalyse eine Zeit zwi-
schen einer und drei Sekunden ben¨otigt. Dies liegt noch unter der Laufzeit der
Sounddateien, die etwa vier Sekunden lang sind.

Eine so geringe Laufzeit kann auf dem Roboter durch die Hardwareeinschr¨ankun-
gen aktuell nicht erreicht werden. Das Programm bietet jedoch reichlich Optimie-
rungspotential, nicht zuletzt durch die Verwendung einer hardwaren¨aheren Pro-
grammiersprache f¨ur die Vektorberechnungen wie C++. Ein großer Zeitfaktor in
der Analyse ist die h¨auﬁge Verschiebung der Signalwerte, nach der jeweils wieder
das Mel-Cepstrum gebildet wird und eine Distanzberechnung zu allen Referenz-
daten erfolgen muss. Hier ist mit deutlich weniger Verschiebungen auszukommen,
wenn man die Struktur der sich ergebenen Distanzwerte, wie in Abschnitt 6.1.3
beschrieben, mitbetrachtet. Es w¨are m¨oglich, mit wenigen Datenpunkten das je-
weilige Minimum pro Referenzdatum zu bestimmen und nur die jeweiligen Minima
miteinander zu vergleichen. Welche weiteren Laufzeitverbesserungen erzielt werden
k¨onnen und welche minimale Laufzeit erzielt werden kann, ist in weitergehenden
Arbeiten zu untersuchen.

38

6.3. Zusammenfassung

6.3 Zusammenfassung

Diese Arbeit stellt sowohl theoretische Ans¨atze f¨ur die Hardwareanpassung der
DarwinOP-Roboter f¨ur die Nutzung von Kommunikation durch nat¨urliche Spra-
che, Dialogstrategien und eine Eingliederungsstrategie in das bestehende Softwa-
resystem des RoboCup-Teams Hamburg Bit-Bots dar, als auch eine praktische
Implementation vor, die die folgenden Anforderungen erf¨ullt:

• Abstraktion vom DTW-Algorithmus durch lineare Verschiebung der Signal-

werte.

• Leichte Erweiterbarkeit auf neue Anwendungsszenarien durch Erg¨anzung der

Referenzdatens¨atze.

• Analyse der Mel-Cepstrum-Parameter.

• Verwendbarkeit des Systems mit Realdaten des Roboters.

• Leichte Test- und Analysierbarkeit durch Simulation des Audiostreams.

• Ressourcensparende Speicherung der Referenzdaten in XML-Dateien.

• Unterst¨utzung einer Sprechererkennung durch Erzeugung von Sprache in ver-

schiedenen Frequenzbereichen.

39

Kapitel 6. Evaluation und Ergebnisse

40

Kapitel 7

Ausblick

Aufbauend auf der vorliegenden Arbeit ergeben sich einige Forschungsans¨atze, die
in weiterf¨uhrenden Arbeiten zu betrachten sind: Die hier vorgestellte Erkennung
von Sprachanfang und Sprachende setzt eine relativ ruhige Umgebung voraus, die
in einer realen Spielsituation bei RoboCup-Turnieren nicht gegeben ist. Denkbar
w¨are hier beispielsweise die Erweiterung des vorgestellten Ansatzes, wie in [6] be-
schrieben. Andere Ans¨atze, wie die Verwendung einer Spektralmaske, einer Geome-
tric Source Separation (GSS) oder einer Computational Auditory Scene Analysis
(CASA) sind bereits in Zusammenhang mit mobilen Robotern getestet worden, so
dass eine Umsetzung f¨ur das Fußballspiel denkbar w¨are [5][15][24].

Dar¨uber hinaus ist eine Laufzeitoptimierung notwendig, um das Verfahren
im Spiel unter den Hardwareeinschr¨ankungen der Roboter einsetzen zu k¨onnen.
Ans¨atze daf¨ur sind bereits in Kapitel 6.2.4 beschrieben. In den Tests mit Original-
daten wurde stets eine manuelle Rauschreduktion verwendet. Um eine autonome
Erkennung auf dem Roboter zu erm¨oglichen, muss eine solche Rauschﬁlterung un-
ter den gegebenen Anforderungen an Hardware und Laufzeit automatisiert werden.
Diese Arbeit bietet weiterhin globalere Ansatzpunkte, das Spielverhalten im
RoboCup zu verbessern. Zun¨achst liegt nat¨urlich eine Erweiterung auf die Ana-
lyse von menschlicher Sprache nahe. Die W-LAN-Netzwerkarchitektur w¨urde so
nicht nur bei der Roboter-Roboter-Kommunikation ¨uberﬂ¨ussig, auch der elektro-
nische Schiedsrichter k¨onnte so ersetzt werden. Die Schiedsrichteranweisungen sind
deutlich durch ihre Verbindung mit der Benutzung der Pfeife zu erkennen. Durch
das klar deﬁnierte Regelwerk mit eindeutigen Bezeichnungen f¨ur Fouls und andere
Spielsituationen ist eine gemeinsame Sprachbasis bereits gegeben und muss nur
noch in die Roboter implementiert werden.

Eine Mensch-Roboter-Kommunikation im RoboCup bringt weitere Vorteile mit
sich: Wie im menschlichen Fußball auch k¨onnte es einen Trainer am Spielfeldrand
geben, der taktische Anweisungen gibt. Um hier jedoch einen Missbrauch durch
gegnerische Teams oder das Publikum zu unterbinden, sind weitere Vorkehrungen
wie die Sprecheridentiﬁkation n¨otig. Eine andere M¨oglichkeit bietet die Analyse
der Stimmen im Publikum. Schon heute bringen sich insbesondere die Kinder am
Spielfeldrand in das Spiel ein, in dem sie Hinweise wie:
Da liegt der
”
Ball!“ geben. K¨onnte der Roboter diese Hinweise analysieren, k¨onnte er beispiels-

Schieß!“ oder
”

41

Kapitel 7. Ausblick

weise den Bereich, in dem nach dem Ball zu suchen ist, viel genauer eingrenzen.
Problematisch ist auch hier wieder, dass Potential f¨ur Missbrauch er¨oﬀnet wird.

Doch auch ohne die Implementation einer Mensch-Roboter-Kommunikation
k¨onnen neue Wege in einigen Verfahren beschritten werden. Beispielhaft sei hier
die Lokalisation auf dem Spielfeld angef¨uhrt. Zwar ist dem Roboter eine exakte
Lokalisation an Hand der Feldlinien und den Vorinformationen m¨oglich, jedoch
kann es im Spielverlauf dazu kommen, dass ein Roboter neu oder nach einer Pause
wieder in das Spiel eingesetzt wird und keinerlei Orientierung hat. Durch die Sym-
metrie des Spielfelds ist es ihm nun nicht m¨oglich zu bestimmen, auf welcher der
beiden Spielfeldh¨alften sein eigenes Tor steht. Bisherige Ans¨atze besch¨aftigen sich
vor allem mit einer Analyse des Horizonts um das Spielfeld herum. Die Roboter-
Roboter-Kommunikation im Zusammenhang mit der Ger¨auschquellenlokalisation
er¨oﬀnet hier noch einen anderen Verfahrensansatz: Der orientierungslose Roboter
gibt einen Hilferuf ab, auf den beispielsweise der Torwart im eigenen Team reagiert.
Durch die Lokalisation des Sounds zusammen mit der Veriﬁkation des Torwarts
durch die Sprachanalyse kann so leicht festgestellt werden, in welchem Tor der
eigene Torwart steht.

Diese Arbeit soll die Grundlage f¨ur eine kontext¨ubergreifende Forschung im
Bereich Roboter-Roboter-Kommunikation bilden, so dass – wie bereits in Kapitel 1
dargelegt – auch weitere Forschungsans¨atze ¨uber das Fußballspiel hinaus entstehen,
beispielsweise im Bereich der mobilen Serviceroboter.

42

Literaturverzeichnis

[1] eSpeak.

http://espeak.sourceforge.net/.
GNU General Public License Version 3, Last Access 07.06.2013 23:51.

[2] Was versteht man unter Prosodie?

http://www.uni-bielefeld.de/Universitaet/Einrichtungen/
Zentrale%20Institute/IWT/FWG/Sprache/Prosodie.html.
Last Access 08.06.2013 22:35.

[3] Hans-Dieter Burkhard and Hans-Arthur Marsiske. Endspiel 2050: Wie Robo-

ter Fußball spielen lernen. Heise, 2003. ISBN 9783936931020.

[4] Kai-Uwe Carstensen, Christian Ebert, Susanne Jekat, Cornelia Ebert, Hagen
Langer, and Ralf Klabunde. Computerlinguistik und Sprachtechnologie: Ei-
ne Einf¨uhrung. Spektrum Lehrbuch. Spektrum Akademischer Verlag GmbH,
2010. ISBN 9783827422248.

[5] Antoine Deleforge and Radu Horaud. The cocktail party robot: Sound source
separation and localisation with an active binaural head. IEEE/ACM Inter-
national Conference on Human Robot Interaction, 2012.

[6] Masrur Doostdar, Stefan Schiﬀer, and Gerhard Lakemeyer. RoboCup 2008:
Robot Soccer World Cup XII. chapter A Robust Speech Recognition System
for Service-Robotics Applications, pages 1–12. Springer-Verlag, Berlin, Heidel-
berg, 2009.

[7] Michael D¨urr and Peter Schlobinski. Deskriptive Linguistik. Studienb¨ucher
zur Linguistik. Vandenhoeck + Ruprecht Gm, 2006. ISBN 9783525265185.

[8] L. Dybkjaer, H. Hemsen, and W. Minker. Evaluation of text and speech sys-
tems. Text, speech, and language technology. Springer London, Limited, 2007.
ISBN 9781402058172.

[9] Kristiina Jokinen and Michael McTear. Spoken Dialogue Systems. Synthesis
Lectures on Human Language Technologies Series. Morgan & Claypool, 2010.
ISBN 9781598295993.

[10] Hartmut K¨onig. Protocol Engineering. Springer, 2012. ISBN 9783642291449.

43

Literaturverzeichnis

[11] Angelika Linke, Markus Nussbaumer, and Paul R. Portmann. Studienbuch
Linguistik. Reihe Germanistische Linguistik, 121. Niemeyer Max Verlag
GmbH, 2004.

[12] Beth Logan. Mel frequency cepstral coeﬃcients for music modeling. Interna-

tional Symposium on Music Information Retrieval, 2000.

[13] Dominic Mazzoni and Roger Dannenberg. Audacity.

http://audacity.sourceforge.net/?lang=de.
GNU General Public License Version 2, Last Access 07.06.2013 23:54.

[14] Karl J. Muecke and Dennis W. Hong. Darwin’s evolution: development of a
humanoid robot. IEEE/RSJ International Conference on Intelligent Robots
and Systems, pages 2574–2575, 2007.

[15] Hiroshi G. Okuno, Tetsuya Ogata, and Kazunori Komatani. Computatio-
nal auditory scene analysis and its application to robot audition: Five years
experience. In Second International Conference on Informatics Research for
Development of Knowledge Society Infrastructure, pages 69–76. 2007.

[16] Beate Pﬁster and Tobias Kaufmann. Sprachverarbeitung: Grundlagen und
Methoden Der Sprachsynthese und Spracherkennung. Springer, 2008. ISBN
9783540759102.

[17] Lawrence R. Rabiner. A tutorial on hidden markov models and selected ap-

plications in speech recognition. Proceedings of the IEEE, 1989.

[18] Christian Rentrop. Roboter-Angst im europ¨aischen Kulturkreis.

http://www.netzwelt.de/news/73191 3-verkehrte-netzwelt-honda-asimo-
terminator-alpha-version.html, 12/2005.
Last Access 07.06.2013 23:34.

[19] Robotis. DARwIn-OP Subcontroler.

http://sourceforge.net/projects/darwinop/ﬁles/Hardware/Electronics/
Sub%20Controller/.
Last Access 07.06.2013 23:58.

[20] S. Salvadore and P. Chan. FastDTW: Toward accurate dynamic time warping
in linear time and space. In 3rd Workshop on Mining Temporal and Sequential
Data, 2004.

[21] Klaus Seyerlehner. Mel Frequency Cepstrum.

SVN http://mirlastfm.googlecode.com/svn/trunk/ mirlastfm-read-only.
GNU General Public License Version 3, Last Access 07.06.2013 23:53.

[22] Klaus Seyerlehner. Content-Based Music Recommender Systems: Beyond sim-

ple Frame-Level Audio Similarity. 2010.

44

Literaturverzeichnis

[23] Mark Tatham and Katherine Morton. Developments in speech synthesis. John

Wiley, 2005. ISBN 9780470855386.

[24] Jean-Marc Valin, Seiichi Yamamoto, Jean Rouat, Fran¸cois Michaud, Kazuhiro
Nakadai, and Hiroshi G. Okuno. Robust recognition of simultaneous speech
by a mobile robot. IEEE Transactions on Robotics (4), pages 742–752.

[25] Jutta Weber. Der Roboter als Menschenfreund. c’t, (Heft 2):144 – 149, 2006.

45

Literaturverzeichnis

46

Abbildungsverzeichnis

2.1 Versuchsaufbau Leistungstest der Lautsprecher des DARwIn-OP . .
2.2 Messreihe der Lautsprecherleistung f¨ur den DARwIn-OP und einen
Referenzlautsprecher, links bei 0,5 V Spannung, rechts bei 1,0 V
Spannung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Distance“ . . .

2.3 Frequenzanalyse des synthetisch erzeugten Wortes
2.4 Schaltplan des Microphone Ampliﬁer auf dem CM-730-Board [19,

”

S. 22].

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.1 Gegen¨uberstellung von graphenbasiertem und framebasiertem Dia-
logkontrollsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.2 Links das globale Dialogmodell als Peer-to-Peer-Struktur, rechts
der einzelne Dialog als Client-Server-Modell. DARwIn-OP Graﬁk von
http://darwinop.sourceforge.net/ . . . . . . . . . . . . . . . . . . . . . .

4.1 Algorithmus der Transformation eines Sprachsignals in das Mel-

Cepstrum von [12]

. . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Zustands¨uberg¨ange bei der Detektion von relevanten Sprachsignalen
. . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . .

4.3 Spracherkenner nach Rabiner [4]

in Anlehnung an [16]

5

6
6

7

12

13

19

21
23

5.1 Struktur der erzeugten XML-Dateien. . . . . . . . . . . . . . . . . .

30

Point“ steht
”

Distance“, M f¨ur
”

Meter“ und P f¨ur
”

6.1 Distanzen der Referenzdatens¨atze zueinander, wobei D f¨ur das Wort
. . . . . . . . .
. . . . . .
. . . . .
Distance“ . . . . . . . . . . . .
”
Seven“ . . . . . . . . . . . . . . .

6.2 Kennzeichnung der Einzelworte in einem Idealdatensatz
6.3 Kennzeichnung der Einzelworte in einer Originalaufnahme
6.4 Distanzberechnungen f¨ur das Wort
6.5 Distanzberechnung f¨ur das Wort
6.6 Mittlerer Wortabstand bei einer Samplingrate von 44 kHz und va-
riabler Fenstergr¨oße . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.7 Mittlerer Wortabstand bei einer Fenstergr¨oße von 1024 Samples und
variabler Samplingrate . . . . . . . . . . . . . . . . . . . . . . . . .
6.8 Versuchsaufbau bei der Aufnahme der Originaldatens¨atze und Re-
ferenzdaten. DARwIn-OP Graﬁk von http://www.robotis.com/img/img ko/
sub/DARwIn img 05.jpg

. . . . . . . . . . . . . . . . . . . . . . . . . .

”

32
32
33
34
34

35

36

37

47

Abbildungsverzeichnis

48

Anhang

Programmbeispiele ausf¨uhren

Der Quelltext als Maven-Projekt kann unter
https://github.com/MaikePaetzel/RobotToRobotCommunication
heruntergeladen werden und steht unter der CC BY-NC-SA 3.0 DE Lizenz.

Konsolenbenutzung (unter Linux und Mac)

Voraussetzung: Eine Installation von Java JDK 1.7 und Maven 3 ist Voraus-
setzung f¨ur die Ausf¨uhrung des Programms.

Kompilierung: Unter Linux und Mac kann der Quelltext ¨uber die Konsole
durch die Eingabe der Zeile
mvn clean install“ im Git-Verzeichnis kompiliert
”
werden.

Ausf¨uhrung:
Im Hauptordner liegt nach der erfolgreichen Kompilierung ein
zus¨atzlicher Ordner target. Die Ausf¨uhrung des Programms geschieht im Haupt-
ordner des Git-Verzeichnisses, in dem die Datei BA.jar liegt, durch Eingabe der
Zeile
java -jar BA.jar -s #nummer“, wobei #nummer durch eine nat¨urliche Zahl
”
zwischen Null und Sieben ersetzt werden muss. Die Bedeutung der einzelnen Sze-
nariennummern ist im Abschnitt

Ausf¨uhrbare Klassen“ erkl¨art.
”

Einbindung in eine IDE am Beispiel Eclipse
(f¨ur alle Betriebssysteme)

Voraussetzung: Es wird vorausgesetzt, dass die Maven Integration f¨ur Eclipse
installiert ist. Diese kann jederzeit ¨uber den Eclipse-Marketplace kostenlos hinzu-
gef¨ugt werden.

Import:

1. Unter Eclipse das Import-Fenster ¨oﬀnen.

2. Import-Quelle ist ein existierendes Maven-Projekt aus dem ¨ubergeordneten

Ordner Maven.

49

Anhang

3. Das Wurzelverzeichnis ist der Ordner, in dem die Datei pom.xml liegt. Diese

muss auch als Projekt ausgew¨ahlt werden.

Ausf¨uhrbare Klassen

StartUp:
In der Klasse StartUp k¨onnen alle in der Bachelorarbeit beschriebenen
statistischen Auswertungen gestartet werden. Dazu sind folgende Parameter bei
der Eingabe erlaubt:

• -s 0 analysiert eine einzelne Originalaufnahme auf den Sprachinhalt. Welche
Datei verwendet wird, kann in der entsprechenden Klasse manuell ge¨andert
werden. Beim initialen auschecken des Repositories wird stets eine Datei mit
dem Inhalt

Distance. 3. Point. 7. 3. Meter.“ gew¨ahlt.

”

• -s 1 analysiert den Ordner Micro/Microphondaten mit 100 Originalaufnah-

men auf den Sprachinhalt.

• -s 2 analysiert eine einzelne eSpeak-Idealdatei auf den Sprachinhalt. Welche
Datei verwendet wird, kann in der entsprechenden Klasse manuell ge¨andert
werden. Beim initialen auschecken des Repositories wird stets eine Datei mit
dem Inhalt

Distance. 3. Point. 7. 3. Meter.“ gew¨ahlt.

”

• -s 3 analysiert den Ordner eSpeak/eSpeakdaten mit 600 Idealdaten auf den

Sprachinhalt.

• -s 4 analysiert den Ordner Pitch/RoboterErkennungsdaten mit 600 Idealda-
ten verschiedner Pitches darauf, mit welchem Pitch die Aufnahme erzeugt
wurde.

• -s 5 gibt eine Matrix mit den Distanzwerten zur¨uck, die jede Datei im Refe-
renzdatensatz auf Idealdaten im Vergleich zu jedem anderen Referenzdaten-
satz hat.

• -s 6 gibt eine Matrix mit den Distanzwerten zur¨uck, die jede Datei im Refe-
renzdatensatz auf Originaldaten im Vergleich zu jedem anderen Referenzda-
tensatz hat.

• -s 7 gibt eine Matrix mit den Distanzwerten zur¨uck, die jede Datei im Refe-
renzdatensatz auf Idealdaten im Vergleich zu jedem anderen Referenzdaten-
satz auf Originaldaten hat.

Bei den Szenarien 1, 3 und 4 werden am Ende der Analyse die Testergebnisse in die
Datei Testergebnis/ausgabe.txt geschrieben. Alle Pfade zu Sound- oder Textdateien
liegen immer im Ordner resources.

CreateXMLFile: Diese Klasse nimmt als Parameter den Pfad zu einem Ordner
mit Referenzdaten und den Namen f¨ur die zu erzeugende XML-Datei inklusive
relativ zum Projektverzeichnis liegender Pfadangabe entgegen und erzeugt eine
XML-Datei aus dem Referenzdatenordner.

50

Erkl¨arung der Urheberschaft

Ich versichere, dass ich die Bachelorarbeit im Studiengang Informatik selbstst¨andig
verfasst und keine anderen als die angegebenen Hilfsmittel – insbesondere keine
im Quellenverzeichnis nicht benannten Internet-Quellen – benutzt habe. Alle Stel-
len, die w¨ortlich oder sinngem¨aß aus Ver¨oﬀentlichungen entnommen wurden, sind
als solche kenntlich gemacht. Ich versichere weiterhin, dass ich die Arbeit vorher
nicht in einem anderen Pr¨ufungsverfahren eingereicht habe und die eingereichte
schriftliche Fassung der auf dem elektronischen Speichermedium entspricht.

Ort, Datum

Unterschrift

51

