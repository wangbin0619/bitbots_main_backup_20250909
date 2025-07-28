Universität Hamburg
Fakultät für Mathematik,

Informatik und Naturwissenschaften

Bachelorarbeit

Konzeption und Implementierung eines

Verfahrens zur Messung von

Verschiebungsvektoren in

Multispektralbildern

Oliver Bestmann

7bestman@informatik.uni-hamburg.de

Studiengang Informatik

Matr.-Nr. 5945392

Fachsemester 6

Erstbetreuer:

Prof. Dr. rer. nat. Leonie Dreschler-Fischer

Zweitbetreuer:

Dr. Werner Hansmann

Inhaltsverzeichnis

Inhaltsverzeichnis

1 Einleitung

1.1 Zielsetzung dieser Arbeit . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1.2 Gliederung und Vorgehen . . . . . . . . . . . . . . . . . . . . . . . . . . .

2 Optischer Fluss

2.1 Kreuzkorrelation .

.

.

2.2 Differentieller Ansatz .

.

.

. . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.3 Lucas-Kanade Verfahren . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.3.1 Verbesserungen des Verfahrens . . . . . . . . . . . . . . . . . . . .

2.3.2 Eigenschaften des Verfahrens . . . . . . . . . . . . . . . . . . . . .

2.4 Horn-Schunck Verfahren .

. . . . . . . . . . . . . . . . . . . . . . . . . . .

2.4.1 Eigenschaften des Verfahrens . . . . . . . . . . . . . . . . . . . . .

3 Multispektralbilder

3.1 Einführung .

.

.

.

.

.

.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.2 Multispektrales Lucas-Kanade Verfahren . . . . . . . . . . . . . . . . . .

3.3 Multispektrales Horn-Schunck Verfahren . . . . . . . . . . . . . . . . . .

4 Vergleich der Verfahren

4.1 Testdaten .

.

.

.

.

.

.

.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.2

Implementierung und Testumgebung . . . . . . . . . . . . . . . . . . . .

4.3 Vergleichsmethodik .

4.4 Ergebnisse .

.

.

.

.

.

.

.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5 Fazit und Ausblick

Literaturverzeichnis

Eidesstattliche Erklärung

I

1

2

2

4

5

6

8

10

11

11

13

14

14

16

18

22

22

23

24

26

29

31

33

1 Einleitung

1

1 Einleitung

Die Schätzung von Bewegungs- und Verschiebungsvektoren aus Bildfolgen ist ein Prob-

lem, das sich in vielen Bereichen wiederﬁnden lässt. So spielt die Schätzung beispiel-

sweise bei der automatischen Navigation von Robotern und Fahrzeugen eine wichtige

Rolle. Auch in Alltagsanwendungen wie bei optischen Computermäusen oder bei der

Videokompression werden diese Verschiebungsvektoren benötigt. Weiterhin bilden sie

eine Ausgangsbasis für die Erkennung dreidimensionaler Strukturen in Szenen und

zur Schätzung von Bewegungen im Raum, sowie für die Erkennung und Unterschei-

dung von verschiedenen bewegten Objekten. Diese Verschiebungsvektoren sind nach

derzeitigen Erkenntnissen auch in der visuellen Informationsverarbeitung von Men-

schen und anderen Lebewesen von Bedeutung [5, 18, 19, 4].

Diese Vektoren, im Folgenden auch als optischer Fluss bezeichnet, sind eine Größe,

die nicht direkt berechnet werden kann. Darum ist es nun notwendig, geeignete Ver-

fahren zu ﬁnden, um diese Verschiebungsvektoren zu schätzen. Diese können sich

nur auf die messbaren Helligkeitsmuster im Bild stützen. Zur Berechnung benötigte

Größen wie die Gradientenbeträge lassen sich ebenfalls nur aus diesen diskreten Ab-

tastwerten abschätzen. Weiterhin lässt sich aufgrund des Blendenproblems ohne weit-

ere Informationen oder Annahmen über die Bewegung für jeden Bildpunkt grundsät-

zlich nur die Bewegung in Gradientenrichtung schätzen [17, 4].

When only a featureless straight contour of a moving object is visible, one cannot

tell its true velocity and the object seems to be moving perpendicularly to its orien-

tation. [12]

Da man jedoch an der Berechnung der Vektoren unabhängig von der Gradienten-

richtung interessiert ist, bedient man sich geeigneter Modellvorstellungen über die

zu schätzenden Vektorfelder. Beispielsweise wird häuﬁg angenommen, dass das Ver-

schiebungsfeld in einer kleinen Umgebung um jeden Bildpunkt konstant ist. Treten in

dieser Umgebung dann unterschiedliche Gradientenrichtungen auf, so kann damit das

Blendenproblem gelöst werden und somit die Verschiebung korrekt geschätzt werden.

Auch können Annahmen bezüglich der Glattheit des resultierenden Feldes getroffen

werden [7, 4, 17].

1.1 Zielsetzung dieser Arbeit

2

1.1 Zielsetzung dieser Arbeit

Ziel dieser Arbeit ist es, ein Verfahren zu entwickeln, welches zusätzliche Informatio-

nen aus Mehrkanalaufnahmen nutzt, um die Verschiebungsvektoren zwischen zwei

Bildern zu schätzen. Dabei soll auf bereits bekannten Verfahren zur Messung von Ver-

schiebungsvektoren aufgebaut und diese entsprechend erweitert werden. Durch die

direkte Verwendung von Mehrkanalbildern ist dann eine bessere Schätzung der Ver-

schiebung zu erhoffen. Die so hergeleiteten Verfahren sollen in der Sprache C++ mithil-

fe der Graﬁkbibliotek VIGRA implementiert werden.

VIGRA stands for Vision with Generic Algorithms. It’s a novel computer vision

library that puts its main emphasize on customizable algorithms and data struc-

tures. [1]

und sowohl an synthetischen Testbildern als auch an echten Mehrkanalaufnahmen

getestet werden. Da für die synthetischen Testbilder die korrekten Verschiebungsvek-

toren für jeden Bildpunkt vorliegen, ist auch ein quantitativer Vergleich der entwickel-

ten Verfahren untereinander und zu anderen bekannten, auf Grauwertbildern arbeiten-

den Verfahren möglich. Für die Mehrkanalaufnahmen stehen einige von einem Satel-

liten aufgezeichnete Fernerkundungsbilder der Ostsee zur Verfügung. Diese zeigen

eine Algenblütenpopulation in der Ostsee, welche sich mit der Meeresströmung be-

wegt. Durch die Verschiebung der Algen kann direkt auf die Meeresströmungen geschlossen

werden. Des weiteren stehen öffentlich zugängliche Mehrkanalbilder von Wettersatel-

liten zur Verfügung [6].

1.2 Gliederung und Vorgehen

Das erste Kapitel dieser Arbeit beschreibt die Wichtigkeit der Berechnung von Ver-

schiebungsvektoren in Bildfolgen. Weiterhin werden Probleme aufgezeigt, die bei der

Schätzung eben dieser auftreten, sowie kurze Hinweise auf Lösungsansätze beschrieben.

Im zweiten Kapitel werden die theoretischen Grundlagen erläutert. Es wird der Be-

griff des optischen Flusses eingeführt. Neben dem Schätzungsansatz über die Korre-

lation wird der differentielle Berechnungsansatz beschrieben. In diesem Zusammen-

hang wird die wichtige motion-constraint equation beschrieben. Darauf aufbauend wer-

den zwei bedeutsame und bekannte Verfahren zur Schätzung des optischen Flusses auf

Grauwertbildern hergeleitet und kommentiert.

1.2 Gliederung und Vorgehen

3

Das dritte Kapitel diskutiert das Konzept von Mehrkanal, bzw. Multispektralbildern

und dem zusätzlichen Nutzen, der sich durch die Verwendung mehrerer Kanäle bei

der Schätzung von Verschiebungsvektoren erhoffen lässt. Hierbei werden die im zweit-

en Kapitel beschriebenen Grauwertverfahren als Grundlagen genutzt um Verfahren zu

entwickeln, welche die Informationen aus Mehrkanalbildern zur Schätzung von Ver-

schiebungsvektoren nutzen. Daraus motiviert sich dann die Implementierung der erar-

beiteten Verfahren in C++.

In Kapitel vier wird kurz die Implementierung beschrieben. Um die entwickelten

Algorithmen quantiativ vergleichen zu können, werden noch einige Bildsequenzen

erzeugt und beschrieben. Weiter werden exemplarisch einige Vergleichsmaße erklärt.

Zum Schluss werden die Testsequenzen dann mit den unterschiedlichen Verfahren aus-

gewertet und die Ergebnisse miteinander verglichen.

Abschließen wird diese Bachelorarbeit mit einem kurzen Fazit und einem Ausblick,

wie die hier entwickelten Verfahren als Grundlage für weitere Forschung genutzt wer-

den können.

2 Optischer Fluss

4

2 Optischer Fluss

Es existieren verschiedene, zum Teil sich widersprechende Deﬁnitionen für den optis-

chen Fluss. Es seien hier zwei aufgeführt:

Optical ﬂow is the distribution of apparent velocities of movement of brightness

patterns in an image. [4]

The velocity ﬁeld that represents the motion of object points across an image is called

the optical ﬂow ﬁeld. [8]

Als optischer Fluss wird ein 2-dimensionales Vektorfeld bezeichnet, welches ein Geschwindigkeits-

feld, und somit ein Verschiebungsfeld in einem gegebenen Zeitraum, darstellt. Un-

einig sind die beiden Deﬁnitionen jedoch darin, welche Verschiebungen dargestellt

werden. Im Folgenden soll der optische Fluss die durch Veränderungen von Grauwert-
oder Farbmustern wahrgenommene Bewegung in einem Bild I bezeichnen. Jedem Bild-
punkt I(x, y, t) wird dann durch den optischen Fluss ein Verschiebungsvektor (cid:126)u =
(u, v)T zugeordnet. Diese Verschiebungsvektoren entsprechen, entgegen dem zweiten
Zitat, nicht unbedingt der Projektion der echten 3-dimensionalen Verschiebungsvek-

toren auf die Bildebene. Als Beispiel wird häuﬁg eine Kugel mit gleichmäßiger mat-

ter Oberﬂäche herangezogen, die von einer Punktlichtquelle beleuchtet wird (Abbil-

dung 2.1). Dreht sich diese Kugel, so ändert sich die Helligkeitsverteilung nicht – es

können also keine Verschiebungen von Helligkeiten wahrgenommen werden und somit

sind alle Verschiebungsvektoren des optischen Flusses genau null. Bewegt sich jedoch

die Lampe um die nun feste Kugel, so ist eine Änderung der Helligkeitsverteilung

wahrnehmbar. Dadurch ergibt sich eine wahrgenommene Bewegung und es resultieren

hieraus somit von null verschiedene Verschiebungsvektoren. [4, 2, 17, 3]

2.1 Kreuzkorrelation

5

(a)

(b)

Abbildung 2.1: (a) rotierende Kugel ohne Änderung der Grauwerte, (b) Veränderung

der Grauwerte durch bewegte Lichtquelle

Aus diesem Grund wird angenommen, dass die Beleuchtung auf den zu untersuchen-

den Bildern konstant ist und jegliche Änderung der Helligkeitsverteilung ausschließlich

durch die gesuchte Bewegung entsteht. [17]

2.1 Kreuzkorrelation

Ein einfacher Ansatz zur Schätzung von Verschiebungsvektoren zwischen zwei Bild-

funktionen geht über die Kreuzkorrelations-Funktion. Mit Hilfe der Kreuzkorrelation

ist die Lokalisierung eines kleinen Bildausschnittes in einem größeren Bild möglich.

Der Kreuzkorrelations-Term (2.1) beschreibt die Ähnlichkeit zwischen einer Schablone
f an der Stelle u, v und einem Bild g

c(u, v) =

(cid:88)

x,y

f (x, y) · g(x − u, y − v)

(2.1)

Eine Schätzung des optischen Flusses kann nun erfolgen, indem für jeden Bildpunkt

im ersten von zwei aufeinanderfolgenden Bildern sein verschobenes Pendant gefun-

den wird. Dafür kann eine kleine Umgebung um den betrachteten Punkt als Schablone

gewählt werden. Für diese wird dann in einer etwas größeren Umgebung, innerhalb

einer gewählten Maximalverschiebung, für jede mögliche Verschiebung die Kreuzko-

rrelation im zweiten Bild ausgewertet. Der Punkt, an dem die Korrelation am größten

ist, beschreibt die geschätzte Verschiebung.

Der Kreuzkorrelations-Koefﬁzient ist jedoch durch eine Reihe verschiedener Gründe

fehleranfällig.

2.2 Differentieller Ansatz

6

• Wenn sich die Helligkeit des Bildes stark mit der Position ändert, so kann die

Korrelation zwischen der Schablone und der korrekten Zielregion geringer sein,

als zwischen der Schablone und einer sehr hellen Zielregion.

• Der Wertebereich von c(u, v) ist abhängig von der Größe der betrachteten Region.

• Das Verfahren ist nicht invariant gegenüber Helligkeitsänderungen wie sie durch

unterschiedliche Beleuchtung der Schablone und der Zielregion entstehen kön-

nen.

Diesen Mängeln kann man durch die Verwendung des normierten Korrelations-Koefﬁzienten

gerecht werden. Dabei wird der Mittelwert des Bildes bzw. der Schablone vom betra-

chteten Wert abgezogen und das Ergebnis der Kreuzkorrelation durch das Produkt der
Standardabweichungen von f und g dividiert.

cn(u, v) =

(cid:80)

x,y(f (x, y) − ¯f ) · (g(x − u, y − v) − ¯g)

(cid:80)
x,y(f (x, y) − ¯f )2 · (cid:80)

x,y(g(x − u, y − v) − ¯g)2

(2.2)

Es ist jedoch nicht zu übersehen, dass der normierte Korrelations-Koefﬁzient immer

noch einige Mängel hat. So ist das Verfahren nicht rotations- und skalierungsinvariant.

Außerdem ist das Verfahren generell sehr rechenintensiv. Diese Probleme kann man

jedoch vernachlässigen, wenn das Ausgangsmaterial in einer relativ hohen zeitlichen

Auﬂösung vorliegt und somit zwischen zwei Bildern einer Sequenz nur minimale Verän-

derungen stattgefunden haben. Außerdem gibt es Verfahren, die die Kreuzkorrelation

sehr effektiv über die Fourier-Transformation berechnen. Weiterhin ist jedoch auss-
chließlich die Schätzung von Bewegungsvektoren (u, v)T mit ganzzahligen u und v
möglich. [10, 6]

Aus diesen Gründen bedient man sich häuﬁg eines differentiellen Ansatzes zur Schätzung

von Verschiebungsvektoren.

2.2 Differentieller Ansatz

Für die Schätzung des optischen Flusses mit differentiellen Methoden wird angenom-

men, dass die Bildintensität der verschobenen Bildpunke zwischen zwei aufeinander
folgenden Bildern gleich bleibt [17]. Sei I(x, y, t) die Intensität eines Bildpunktes an x, y
zum Zeitpunkt t der sich um ∆x, ∆y im Zeitraum ∆t bewegt.

I(x, y, t) = I(x + ∆x, y + ∆y, t + ∆t)

(2.3)

2.2 Differentieller Ansatz

7

Es wird angenommen, dass die Bewegung klein ist. Unter dieser Annahme kann die

Bildfunktion I mittels einer Taylor-Reihe erster Ordnung angenähert werden.

I(x + ∆x, y + ∆y, t + ∆t) = I(x, y, t) +

∂I
∂x

∆x +

∂I
∂y

∆y +

∂I
∂t

∆t

Aus (2.3) und (2.4) folgt dann direkt

∆x +

∆y +

∆t = 0

∂I
∂x

∂I
∂x

∆x
∆t

+

∂I
∂y
∂I
∂y

∂I
∂t
∂I
∂t

∆t
∆t
∂I
∂y

+

∆y
∆t
∂I
∂x

u +

v = −

∂I
∂y

= 0

(2.4)

(2.5)

(2.6)

(2.7)

wobei u und v die Komponenten des Verschiebungsvektors (cid:126)u im optischen Flussfeld
an x, y, t bezeichnen.

Es wird nun eine vereinfachende Schreibweise für partielle Ableitungen eingeführt.
Die partielle Ableitung einer Funktion F nach der Variablen g wird im folgendes mit
Fg, soweit dies sinnvoll ist, bezeichnet.

Fg :=

∂F
∂g

Mithilfe dieser Vereinfachung kann die oben hergeleitete Gleichung als

Ixu + Iyv = −It

(2.8)

(2.9)

geschrieben werden. Diese Gleichung (2.9) wird als motion constraint equation oder

auch gradient-constraint equation bezeichnet [17, 6]. Die Schätzung des Verschiebungsvek-

tors ist durch die motion-constraint equation jedoch allein nicht möglich, da sie zwei un-

bekannte Variablen besitzt und die Gleichung somit unterbestimmt ist. Sie bezeichnet
eine Gerade im u, v-Raum, auf der die möglichen Lösungen für den Verschiebungsvek-
tor (u, v)T liegen müssen (Abbildung 2.2a) [17].

2.3 Lucas-Kanade Verfahren

8

(a)

(b)

Abbildung 2.2: (a) Gerade im u, v-Raum, auf dem mögliche Verschiebungsvektoren
liegen, (b) Unter der rechten Blende kann die Bewegung des grauen
Rechtecks eindeutig ermittelt werden, unter der linken gibt es un-
endlich viele mögliche Bewegungen

Durch das Blendenproblem ist es nur möglich die Bewegung für einen Bildpunkt in
Richtung seines Gradienten zu bestimmen. Für die Verschiebung u⊥ in Gradientenrich-
tung kann nun die folgende Formel hergeleitet werden [4]

u⊥ =

(cid:113)

−It
x + I 2
I 2
y

(2.10)

Gefragt bei der Schätzung von Verschiebungsvektoren ist jedoch nicht nur der Betrag

in Richtung des Gradienten. Es ist außerdem von Interesse die Richtung der Bewegung

sowie den Betrag in diese zu schätzen. Um das Blendenproblem zu überwinden, wer-

den weitere Informationen zur Schätzung der Verschiebung benötigt. Dies kann jedoch

nur durch das Treffen weiterer Annahmen an die Bewegungen oder über Modellwissen

geschehen. Eine einfache Möglichkeit ist die Annahme einer lokalen Konstanz des op-

tischen Flusses um jeden Bildpunkt. Betrachtet man so in einer kleinen Nachbarschaft

um einen Punkt andere Punkte, die einen anderen Gradienten aufweisen, sich jedoch

in die selbe Richtung bewegen, so entkommt man dem Blendenproblem [17, 7].

2.3 Lucas-Kanade Verfahren

Das Lucas-Kanade Verfahren ist eine relativ einfache Methode zur Schätzung des op-

tischen Flusses in einer Sequenz aus zwei Bildern. Unter der Annahme, dass die Be-

wegung in einer kleinen Umgebung um einen Bildpunkt konstant ist, kann die Ver-

uv2.3 Lucas-Kanade Verfahren

9

Abbildung 2.3: Viele sich im u, v-Raum kreuzende Linien und eine Schätzung für (cid:126)u, die

den Abstand zu allen Linien minimiert.

schiebung in diesem Bildpunkt geschätzt werden. Wichtig um dem Blendenproblem

zu entkommen ist jedoch, dass innerhalb der betrachteten Umgebung mindestens zwei

Punkte mit unterschiedlicher Gradientenrichtung vorkommen [?].

Wird nun für eine kleine m × m Umgebung mit m > 0 um den Bildpunkt x, y der
optische Fluss als konstant angenommen, so muss die motion-constraint equation für je-
den Punkt zugleich gelten. Die Bildpunkte werden mit n = 1, 2, . . . , m2 durchnum-
meriert und ein Gleichungssystem aus m2 Gleichungen wird aufgestellt. In diesem
Gleichungssystem bezeichnet Ij die Intensität des Pixels mit der Nummer j und Ij k
den Gradienten des j-ten Pixels in k-Richtung.

I1xu + I1yv = −I1t

I2xu + I2yv = −I2t

...

Inxu + Inyv = −Int

(2.11)

Das entstandene Gleichungssystem ist nun überbestimmt und es gibt meistens keine

eindeutige Lösung. Jede Gleichung des Gleichungssystems beschreibt eine Gerade im
u, v-Raum, auf der die Lösung für den entsprechenden Punkt liegen muss (Abbildung 2.3).

Der Schnittpunkt dieser Geraden beschreibt den zu schätzenden Verschiebungsvektor.

Gibt es mehr als zwei Geraden, so gibt es häuﬁg nicht nur einen Schnittpunkt. Es wird

nun ein Vektor gesucht, der möglichst nahe an allen constraint-lines liegt und somit

die motion-constraint equations für alle Bildpunkte am Besten erfüllt. Dafür werden die

Quadrate der Abstände des gesuchten Vektors zu den Linien minimiert.

Die Summe der quadratischen Fehler kann nun, in Abhängigkeit von u und v, als

uv2.3 Lucas-Kanade Verfahren

Fehlerfunktion E geschrieben werden.

E(u, v) =

m2
(cid:88)

(cid:16)

j=1

Ij xu + Ij yv + Ij t

(cid:17)2

10

(2.12)

Um das Minimum unter Einﬂuss von u und v zu ermitteln, werden die partiellen
Ableitungen der Fehlerfunktion nach u und v gebildet.

∂E
∂u

∂E
∂v

= 2

= 2

m2
(cid:88)

(cid:16)

j=1

m2
(cid:88)

(cid:16)

j=1

Ij xu + Ij yv + Ij t

Ij xu + Ij yv + Ij t

(cid:17)

(cid:17)

Ij x

Ij y

(2.13)

Die partiellen Ableitungen werden nun in einem linearen Gleichungssystem mit Null
gleichgesetzt. Durch Umformen können die Koefﬁzientenmatrix A und der Lösungsvek-
tor b des linearen Gleichungssystem A(cid:126)u = b bestimmt werden.

A =








m2
(cid:80)
j=1
m2
(cid:80)
j=1

Ij

2
x

Ij xIj y








Ij xIj y

Ij

2
y

m2
(cid:80)
j
m2
(cid:80)
j

b =








−

−








Ij tIj x

Ij tIj y

m2
(cid:80)
j=1
m2
(cid:80)
j=1

(2.14)

Durch Auﬂösen des Gleichungssystems nach dem Verschiebungsvektor (cid:126)u = A−1 · b

kann dieser nun geschätzt werden.

2.3.1 Verbesserungen des Verfahrens

[7] Die Wahrscheinlichkeit, dass die Uniformität der Bewegung mit wachsender Ent-
fernung zum betrachteten Punkt x, y abnimmt, ist in realen Anwendungen meist hoch.

Eine Verbesserung des beschriebenen Verfahrens lässt sich durch die Gewichtung der

einzelnen Quadrate während der Minimierung der Fehlerfunktion erreichen. Eine Gauß’sche
Gewichtungsfunktion eignet sich gut, um die constraint-lines der Bildpunkte nahe x, y
stärker zu gewichten, als die von weiter entfernten. Sei gj das Gewicht für den j-ten
Bildpunktes, so lässt sich die Fehlerfunktion wie folgt erweitern [7]

E(v, v) =

(cid:16)

gj

m2
(cid:88)

j=1

Ij xu + Ij yv + Ij t

(cid:17)2

(2.15)

2.4 Horn-Schunck Verfahren

11

Nach der Minimierung wie oben beschrieben ergibt sich dann für die Koefﬁzienten-

matrix A und für den Vektor b

A =








m2
(cid:80)
j=1
m2
(cid:80)
j=1

gjIj

2
x

gjIj xIj y








gjIj xIj y

gjIj

2
y

m2
(cid:80)
j
m2
(cid:80)
j

b =








−

−








gjIj tIj x

gjIj tIj y

m2
(cid:80)
j=1
m2
(cid:80)
j=1

(2.16)

2.3.2 Eigenschaften des Verfahrens

Der Lucas-Kanade-Schätzer für das optische Flussfeld ist ein einfaches und leicht zu

implementierendes Verfahren, welches auch heute noch eines der meist eingesetzten

Verfahren ist. Auch die Annahme eines konstanten Flusses in einer kleinen Umgebung

ist häuﬁg gerechtfertigt. Da es sich jedoch um eine lokale Methode zur Schätzung der

Verschiebung handelt, wird kein dichtes Vektorfeld geliefert. Die guten Flussinforma-

tionen, die an Objekträndern ermittelt werden können, verschwinden schnell mit wach-

sendem Abstand von diesen [2, 17].

2.4 Horn-Schunck Verfahren

Berthold Horn und Brian Schunck verwenden einen anderen Ansatz zur Lösung des

Blendenproblems.

In this case neighboring points on the objects have similar velocities and the velocity

ﬁeld of the brightness patterns in the image varies smoothly almost everywhere. [4]

Wenn sich jeder Punkt unabhängig von den umgebenen Punkten bewegen würde,

gäbe es keine richtige Möglichkeit, eine Bewegung zu schätzen. Deswegen nehmen

Horn und Schunck an, dass sich das Vektorfeld über das Bild nur gleichmäßig ändert,

woraus ein glattes Feld folgt. Um dieser Modellvorstellung gerecht zu werden, schla-

gen Horn und Schunck eine Glattheitsbedingung vor. Als Kriterium empfehlen sie, die

Quadrate der Gradientenbeträge der Verschiebungsvektoren zu minimieren [4]:

(cid:19)2

(cid:18) ∂u
∂x

(cid:19)2

+

(cid:18) ∂u
∂y

und

(cid:19)2

(cid:18) ∂v
∂x

(cid:19)2

+

(cid:18) ∂v
∂x

(2.17)

2.4 Horn-Schunck Verfahren

12

Neben diesem Glattheitsterm muss auch die motion-constraint equation minimiert wer-
den. Daraus ergibt sich dann das global über alle Pixel Ω zu minimierende Funktional

E(u, v) =

(cid:90) (cid:90)

Ω

(cid:16)

(Ixu + Iyv + It)2 + α2 (cid:0)|∇u|2 + |∇v|2(cid:1)(cid:17)

dxdy

(2.18)

Der Faktor α2 bestimmt, wie stark der Glättungsterm bei der Minimierung gewichtet
wird. Größere Werte für α2 führen zu einer stärkeren Glättung des Vektorfeldes. Horn
und Schunck schlagen für α2 einen Wert vor, der etwa dem Rauschen der Summe der
Gradientenquadrate E2

y entspricht.

x + E2

E kann durch lösen der zugehörigen Euler-Lagrange Gleichungen minimiert werden

(dazu in Kapitel drei mehr) [15]. Es ergeben sich zwei Gleichungen

Ix(Ixu + Iyv + It) − α2∆vx = 0
Iy(Ixu + Iyv + It) − α2∆vx = 0

(2.19)

Der Laplace-Operator ∆ lässt sich nun numerisch approximieren und als ∆s(x, y) =
¯s(x, y) − s(x, y) ausdrücken, wobei ¯s die gewichtete Summe der Intensitätswerte in
einer Nachbarschaft um x, y bezeichnet [4, 17]. Die Gleichungen (2.19) lassen sich nun

umformen zu

(cid:0)I 2
IxIyu + (cid:0)I 2

x + α2(cid:1) u + IxIyv = α2 ¯u − IxIt
y + α2(cid:1) v = α2¯v − IyIt

(2.20)

Ein iteratives Lösungsverfahren bietet sich aufgrund der sehr hohen Zahl unbekan-

nter Variablen und Gleichungen an. Mithilfe des Gauss-Seidel Verfahrens kann ein
neuer Geschwindigkeitsvektor (un+1, vn+1)T für jeden Bildpunkt aus den vorher er-
mittelten Schätzungen (un, vn)T berechnet werden [4, 17].

un+1 = un −

vn+1 = vn −

Ix (Ixun + Iyvn + It)

α2 + I 2

x + I 2
y

(cid:0)Ixun + Iyvnn + It

(cid:1)

Iy

α2 + I 2

x + I 2
y

(2.21)

(2.22)

2.4 Horn-Schunck Verfahren

13

2.4.1 Eigenschaften des Verfahrens

Durch den iterativen Charakter ist das Horn-Schunck Verfahren sehr rechenaufwendig,

da häuﬁg dutzende oder gar hunderte Iterationen benötigt werden, um ein genügend

dichtes Vektorfeld zu bekommen. Durch den Glattheitsterm werden dann jedoch die

Verschiebungsvektoren von Stellen mit höheren Gradientenbeträgen in die Bereiche

mit schwachen Gradienten propagiert. Dadurch ergibt sich auch ein dichtes Vektorfeld

in Bereichen, in denen lokale Verfahren keine Verschiebungen registrieren (siehe Abbil-

dung 2.4) [17, 2].

Barron und Fleet haben in ihrem Artikel verschiedene Verfahren zur Schätzung des

optischen Flusses verglichen und dabei experimentell herausgefunden, dass die An-

fälligkeit für Rauschen beim Horn-Schunck Verfahren größer ist, als für lokale Opera-

toren, wie dem Lucas-Kanade Verfahren [2].

(a) Lucas-Kanade

(b) Horn-Schunck, er-

ste Iteration

(c) Horn-Schunck,
100. Iteration

(d) Horn-Schunck,
500. Iteration

Abbildung 2.4: (a) lokaler Lucas-Kanade Operator, (b, c, d) Horn-Schunck mit unter-
schiedlicher Zahl Iterationen. Es ist gut zu erkennen, wie die Flussin-
formationen in die Flächen hineinpropagiert werden.

3 Multispektralbilder

14

3 Multispektralbilder

3.1 Einführung

Ein Multispektralbild enthält im Gegensatz zu Grauwertbildern nicht nur einen Kanal.

Es werden nun pro Bild mehrere Grauwertbilder gespeichert, welche die selbe Szene in

der selben Auﬂösung zeigen, jedoch Strahlungsintensität in unterschiedlichen Wellen-

längenbereichen bezeichnen. Abhängig davon, wie gut ein Objekt elektromagnetische

Strahlung in einem bestimmten Wellenlängenbereich reﬂektiert, ist es auf den einzelnen

Kanälen des Multispektralbildes auszumachen. Ein bekanntes Beispiel für Multispek-

tralbilder sind Farbbilder, die aus den drei Kanälen Rot, Grün und Blau bestehen. Die

Wellenlängenbereiche müssen jedoch nicht zwingend im sichtbaren Bereich des Licht-

es liegen, sondern es können beispielsweise Radarwellen oder Wellen im Bereich des

Infrarots für einen Kanal in einem Multispektralbild genutzt werden [11].

(a)

(b)

(c)

(d)

(e)

(f)

Abbildung 3.1: Einzelne Kanäle einer Multispektralaufname von Sylt. (a), (b) und (c)
sind Aufnahmen aus dem sichtbaren Bereich, (d) und (e) nahes Infrarot
und (f) mittleres Infrarot.

3.1 Einführung

15

In Abbildung 3.1 sind einzelne Kanäle einer multispektralen Aufname von Sylt ange-
führt. (a), (b) und (c) zeigen die Intensitätsbilder im sichtbaren Bereich, wobei (a) blau,
(b) grün und (c) rotes Licht zeigt. Dabei kann gut der Meeresboden im ﬂachen Wasser

zwischen der Insel und dem Festland erkannt werden. Er hebt sich jedoch trotz des
Wassers kaum von den Landmassen ab. Die Kanäle (d) und (e) sind im Bereich des

nahen Infrarots aufgenommen. Hier wird mit steigender Wellenlänge der Unterschied

zwischen Wasser, welches die Strahlung absorbiert, und dem Land, das die Infrarot-
strahlung von der Sonne besonders gut reﬂektiert, sehr deutlich. Der letzte Kanal (f )

ist aus dem Bereich des mittleren Infrarots [20]. Wie gut zu erkennen ist, erhält man

durch das gleichzeitige Betrachten mehrerer Kanäle häuﬁg mehr Informationen über

die aufgenommenen Bereiche. Unter der Annahme, dass eine aufgenommene Bewe-

gung in mehreren oder allen Kanälen einer Multispektralaufname erkennbar ist, sollte

es nun möglich sein, das Blendenproblem bei der Berechnung von Verschiebungsvek-

toren durch die zusätzlichen Informationen aus anderen Kanälen zu lösen. Dabei müssen

auf den unterschiedlichen Kanälen natürlich unterschiedliche Bildstrukturen zu sehen

sein, was jedoch später noch näher erläutert werden soll.

Es gibt nun unterschiedliche Ansätze Verschiebungsvektoren in Multispektralbildern

zu berechnen. Zwei einfache Verfahren seien hier kurz angerissen [17]:

1. Es bietet sich an, die Kanäle der Multispektralaufnahme in eine Grauwertauf-

name zu kombinieren und auf diese die bereits bekannten Verfahren zur Schätzung

der Flussvektoren anzuwenden. Zur Kombination eignet sich beispielsweise das

arithmetische Mittel der Kanäle. Dies verbessert normalerweise das Signal-Rausch-

Verhältnis des Ausgangsbildes, verwendet jedoch die eigentlichen zusätzlichen

Informationen aus den Kanälen kaum.

2. Eine weitere Möglichkeit ist das Anwenden der bereits bekannten Verfahren auf

jeden Kanal einzeln. Die daraus gewonnen Vektorfelder können dann geeignet

miteinander verrechnet werden. So kann beispielsweise der Mittelwert berechnet

werden oder es können nur die Verschiebungsvektoren übernommen werden, die

in den meisten Kanälen mit einer gewissen Toleranz gefunden wurden.

Beide Verfahren lassen sich ohne großen Aufwand umsetzen, da bereits bekannte Al-

gorithmen unverändert weiter genutzt werden können. Es werden jedoch die Mehrin-

formationen aus den Multispektralbildern kaum in den Schätzungsprozess einbezogen.

In diesem Kapitel sollen deshalb Verfahren entwickelt werden, welche die Infor-

mationen der Multispektralbilder besser nutzen. Als Grundlage zur Konzeption eines

3.2 Multispektrales Lucas-Kanade Verfahren

16

lokalen Verfahrens wird die Lucas-Kanade Methode benutzt und entsprechend erweit-

ert, um einen Schätzer zu ﬁnden, der den Fehler der motion-constraint equation im Kon-

text aller Kanäle gemeinsam minimiert. Als Zweites soll ein globales Verfahren hergeleit-

et werden. Dieses optimiert einerseits die Bewegungsgleichung und anderseits eine

weitere Bedingung an das Vektorfeld und baut damit auf dem Horn-Schunck-Verfahren

auf.

3.2 Multispektrales Lucas-Kanade Verfahren

Das bereits für Grauwertbilder vorgestellte Lucas-Kanade Verfahren lässt sich sehr ein-

fach auf Multispektralbilder erweitern. Es müssen im Voraus jedoch drei Annahmen an

die Quellbilder und das Flussfeld gestellt werden.

1. Der Fluss soll für jeden Kanal durch das selbe Verschiebungsfeld bezeichnet wer-

den. Dies bedeutet also, dass auf jedem Kanal Bewegung in die selbe Richtung zu

erkennen ist.

2. Die Gradientenrichtung sollte in jedem Punkt für eine gute Schätzung möglichst

unterschiedlich in den Kanälen sein.

3. Der optische Fluss um einen beliebigen Punkt x, y kann als konstant angenom-

men werden, wie bereits für das Lucas-Kanade Verfahren für Grauwertbilder.

Ausgehend von der ersten Annahme muss die motion-constraint equation für den sel-
ben Verschiebungsvektor (u, v)T auf allen Kanälen erfüllt werden. Da dies bei mehr als
zwei Kanälen durch Rauschen und Quantisierung nicht zwingend möglich ist, wird
wieder eine Ballungsanalyse durchgeführt, bei der ein Vektor (u, v)T gesucht wird, der
die Verschiebung angibt und zu dem kleinsten quadratischen Fehler beim Erfüllen der
Bedingungsgleichungen führt. Dies erlaubt das Aufstellen einer Fehlerfunktion E(u, v).
Sei K = {I1, I2, ...} die Menge der Bildfunktionen der zu betrachtenden Kanäle des
Bildes

E(u, v) =

(cid:88)

k∈K

(kxu + kyv + kt)2

(3.1)

Die Minimierung dieser Fehlerfunktion allein reicht bei mehr als einem Kanal bere-

its zur Schätzung einer Verschiebung aus. Das Ergebnis würde jedoch durch Rauschen

3.2 Multispektrales Lucas-Kanade Verfahren

17

im Ausgangsmaterial häuﬁg stark von der erwarteten Verschiebung abweichen. Weit-

erhin muss dann für jeden Pixel die oben genannte zweite Bedingung, unterschiedliche

Gradienten für jeden Kanal, in allen Punkten gelten. Aus diesen Gründen wird wie

im Graustufen-Fall die lokale Konstanz der Verschiebung gefordet. Es wird angenom-
men, der Fluss sei in einer kleinen m × m, m > 0 Umgebung um den Punkt x, y kon-

stant. Dann kann ein Gleichungssystem mit einer Bedingungsgleichung für jeden Pixel
j ∈ {1, 2, . . . , m2} innerhalb der Umgebung für jeden Kanal k ∈ K aufgestellt werden.
Dabei bezeichnet ki den i-ten Pixel in der Umgebung um x, y in der Bildfunktion k und
kij den Gradienten an dem Pixel in j-Richtung.

k1xu + k1yv + k1t = 0

k2xu + k2yv + k2t = 0

...

km2 xu + km2 yv + km2 t = 0

(3.2)

Dieses Gleichungssystem ist überbestimmt und eine eindeutige Lösung nicht möglich,
weswegen sich eine Schätzung für u, v mithilfe der Kleinste-Quadrate-Mehode anbi-
etet. Wie bereits für den Grauwert-Fall beschrieben wird eine Gewichtungsfunktion gj
verwendet, damit Pixel, die weiter von x, y entfernt sind, weniger stark in die Schätzung

einbezogen werden. Die zu minimierende Funktion lautet nun

E(u, v) =



(cid:88)

(cid:88)



k∈K

j

gj (kxu + kyv + kt)2





(3.3)

Zur Berechnung des Minimums müssen die partiellen Ableitungen bestimmt und dann

gemeinsam gleich Null gesetzt werden.

0 = 2

0 = 2



(cid:88)

(cid:88)



k∈K

j



(cid:88)

(cid:88)



k∈K

j



gjkx (kxu + kyv + kt)





gjky (kxu + kyv + kt)



(3.4)

3.3 Multispektrales Horn-Schunck Verfahren

Durch Umformen erhält man ein lineares Gleichungssystem der Form A(cid:126)u = b mit

gj (kx)2

gjkxky

gjkxky

gj (ky)2

m2
(cid:80)
j
m2
(cid:80)
j








m2
(cid:80)
j
m2
(cid:80)
j















A =

(cid:88)

k∈K

b =

(cid:88)

k∈K








gjktkx

gjktky

m2
(cid:80)
j
m2
(cid:80)
j

18

(3.5)

(3.6)

Die Lösung dieses Gleichungssystem kann dann mit (cid:126)u = A−1b bestimmt werden.

3.3 Multispektrales Horn-Schunck Verfahren

Das auf dem Lucas-Kanade aufbauende Verfahren aus dem vorigen Abschnitt ist ein

lokales Verfahren und liefert deswegen nur an Stellen eine zuverlässige Schätzung von

Verschiebungsvektoren, die bestimmten Forderungen genügen. In diesem Abschnitt

soll ein globales Verfahren zur Schätzung des optischen Flusses anhand des Horn-

Schunck Verfahren hergeleitet werden, welches die zusätzlichen Informationen aus

Mehrkanalbildern verwendet. Dabei soll neben der Bedingung, die die motion-constraint

equation für jeden Punkt in jedem Kanal stellt, noch eine weitere Bedingung an die

Glattheit des resultierenden Vektorfeldes gestellt werden.

Das von Horn-Schunck vorgeschlagene Verfahren optimiert einerseits die motion-
constraint equation Ixu + Iyv + It, die quadratisch für jeden Bildpunkt in der Punkt-
menge Ω in das zu minimierende Fehlerfunktional E einﬂießt. Ω bezeichnet dabei alle

Bildpunkte des betrachteten Bildes. Es bietet sich nun an, diesen Term für jeden Kanal
aus der Menge K quadratisch in E einﬂießen zu lassen. Der von der Bewegungsgle-
ichung ausgehende zu minimierende Fehler ξm lautet dann

ξm =

(cid:88)

k∈K

(kxu + kyv + kt)2

(3.7)

Zum Anderen ﬂießt ein mit einem Gewichungsfaktor α2 multiplizierter Glattheit-
sterm in das Fehlerfunktional ein. Dieser wird zusätzlich mit der Anzahl der betra-

chteten Kanäle gewichtet, damit seine Relevanz auch bei einer erhöhten Kanalzahl

bestehen bleibt. Es wird die selbe Glattheitsbedingung an das resultierende Vektorfeld

3.3 Multispektrales Horn-Schunck Verfahren

19

gestellt, wie Horn und Schunk sie vorgeschlagen haben. Als ξc bezeichnet ergibt sich
dafür das Fehlerfunktional

ξc = α2|K| (cid:0)u2

x + u2

y + v2

x + v2
y

(cid:1)

(3.8)

Aus ξm und ξc ergibt sich dann das über alle Bildpunkte Ω zu minimierende Fehler-
funktional E, also

(cid:90) (cid:90)

Ω
(cid:90) (cid:90)

E =

=

ξm + ξc dxdy

(cid:88)

(kxu + kyv + kt)2 + α2|K| (cid:0)u2

x + u2

y + v2

x + v2
y

(3.9)

(3.10)

(cid:1) dxdy

k∈K

Ω

Über die Variationsrechnung und mit Hilfe des Euler-Lagrange Formalismus kann für
E die Lagrangefunktion L aufgestellt werden, aus welcher dann direkt ein Gleichungssys-
tem abgeleitet werden kann, welches L und somit auch E minimiert [4, 15].

L(x, y, u, v, ux, uy, vx, vy) = ξm + ξc

(3.11)

Das Gleichungssystem, welches L minimiert, lautet

∂L
∂u
∂L
∂v

−

−

d
du
d
dv

∂L
∂ux
∂L
∂vx

−

−

d
du
d
dv

∂L
∂uy
∂L
∂vy

= 0

= 0

(3.12)

Einsetzen von L in die Gleichungen und das anschließende partielle Ableiten ergibt

das zu lösende Gleichungssystem

2kx (kxu + kyv + kt) − 2α2|K|uxx − 2α2|K|uyy = 0

2ky (kxu + kyv + kt) − 2α2|K|vxx − 2α2|K|vyy = 0

(3.13)

(cid:88)

k∈K
(cid:88)

k∈K

Mit dem Laplace-Operator ∆s = ∇2s = sxx + syy können die partiellen zweifachen

3.3 Multispektrales Horn-Schunck Verfahren

20

Ableitungen von u und v in x- und y-Richtung zusammengefasst werden.

kx (kxu + kyv + kt) − α2|K|∇2u = 0

ky (kxu + kyv + kt) − α2|K|∇2v = 0

(3.14)

(cid:88)

k∈K
(cid:88)

k∈K

Der Laplace-Operator kann mittels einer Approximation direkt berechnet werden, so
dass die partiellen Ableitungen wegfallen. Es gilt in einer guten Näherung ∇2 = ¯s − s,
wobei ¯s den gewichteten Mittelwert von s in einer kleinen Nachbarschaft bezeichnet

[4, 17]. Mit dieser Vereinfachung lässt sich die Gleichung schreiben als

kx (kxu + kyv + kt) − α2|K|(¯u − u) = 0

ky (kxu + kyv + kt) − α2|K|(¯v − v) = 0

(3.15)

(cid:88)

k∈K
(cid:88)

k∈K

Die Klammer im rechten Summanden kann nun ausmultipliziert werden und α2K ¯u
bzw. ¯v in die Summe auf der linken Seite gezogen werden. Aufteilen der Summe und
Ausklammern von u und v führen zu einem linearen Gleichungssystem mit den Un-
bekannten u und v. Es ist zu beachten, dass dieses Gleichungssystem für jeden Bild-
punkt in Ω aufgestellt werden muss.

(cid:34)

(cid:88)

k∈K

(cid:34)

(cid:88)

k∈K

(cid:0)α2 + k2
x

(cid:1)

(cid:35)

kxky

u +

(cid:35)

u +

(cid:34)

(cid:88)

k∈K

(cid:35)

(cid:35)

(cid:34)

(cid:88)

k∈K

kxky

(cid:0)α2 + k2
y

(cid:1)

v = α2|K|¯u −

(cid:88)

ktkx

v = α2|K|¯v −

(cid:88)

ktky

(3.16)

Die Koefﬁzientenmatrix A des Gleichungssystems und ihre Determinante können

nun berechnet werden.

A =








(cid:80)
k∈K
(cid:80)
k∈K

(cid:0)α2 + k2
x

kxky

(cid:1) (cid:80)
k∈K
(cid:80)
k∈K

kxky

(cid:0)α2 + k2
y

(cid:1)








det(A) =

(cid:34)

(cid:88)

k∈K

(cid:0)α2 + k2
x

(cid:1)

(cid:35) (cid:34)

(cid:88)

(cid:0)α2 + k2
y

(cid:1)

(cid:35)

(cid:34)

−

k∈K

(cid:35)2

(cid:88)

k∈K

kxky

(3.17)

(3.18)

3.3 Multispektrales Horn-Schunck Verfahren

21

Mit der Determinante von A lässt sich eine iterative Lösung für u(n+1) und v(n+1)

angeben, die von dem gemittelten Wert u(n) und v(n) der letzten Iteration abhängt.

(cid:20)

(cid:20)

u(n+1) =

v(n+1) =

α2Kv(n) − (cid:80)
k∈K

ktky

(cid:21) (cid:20)

(cid:80)
k∈K

(cid:21)

(cid:20)

kxky

+

(cid:80)
k∈K

ktkx − α2|K|u(n)

(cid:21) (cid:20)

(cid:80)
k∈K

(cid:21)

(cid:0)α2 + k2
y

(cid:1)

− det(A)

α2Ku(n) − (cid:80)
k∈K

ktkx

(cid:21) (cid:20)

(cid:80)
k∈K

(cid:21)

kxky

(3.19)

ktky − α2|K|v(n)

(cid:21) (cid:20)

(cid:80)
k∈K

(cid:21)

(cid:0)α2 + k2
x

(cid:1)

(3.20)

(cid:20)

+

(cid:80)
k∈K
det(A)

4 Vergleich der Verfahren

22

4 Vergleich der Verfahren

In diesem Kapitel werden die in dieser Arbeit hergeleiteten Verfahren für Mehrkanal-

bilder mit den bekannten, grauwertbasierten Verfahren verglichen. Dazu werden zuerst

die verwendeten synthetischen und realen Testbilder beschrieben. Weiterhin wird auf

die Testumgebung und auf die Implementierung der Verfahren im Rahmen dieser Ar-

beit eingegangen, sowie auf die verwendeten Testmethoden und Vergleichsmaße. Ab-

schließend werden die berechneten Ergebnisse vorgestellt und interpretiert.

4.1 Testdaten

Es existieren für Grauwertverfahren viele bekannte Testsequenzen wie die Yosemite-

Sequenz, die NASA-Sequenz oder das Hamburg Taxi. Zu einigen dieser Bildfolgen ex-

istieren Ground Truth-Werte. Dabei handelt es sich um Vektorfelder mit den tatsäch-

lichen Verschiebungsvektoren zwischen den Bildern. Diese können dann mit den geschätzten

Daten unterschiedlicher Verfahren verglichen werden [2]. Zum Testen von Multispek-

tralverfahren existieren jedoch nur einige Farbsequenzen. Auf die Verwendung dieser

Farbsequenzen wird hier verzichtet, da es sich um synthetische Sequenzen handelt, die

nicht ausreichend unterschiedliche Struktur und verschiedene Gradienten in den drei

Kanälen aufweisen.

Um die entwickelten Verfahren dennoch testen zu können, wird ein eigenes Testbild

entwickelt. Dabei wird darauf geachtet, dass die Gradientenrichtungen in den Kanälen

(a)

(b)

(c)

(d)

Abbildung 4.1: Generierte Testbilder. (a) unscharfes Rechteck, (b) Kombination aus sin-
und cos-Funktion, (c) extrem hochskaliertes Rauschen, (d) Mittelwert
der Bilder (a), (b) und (c)

4.2 Implementierung und Testumgebung

23

möglichst verschieden sind. Das Testbild besteht dafür aus drei Kanälen, die in Abbil-

dung 4.1 dargestellt sind. Es werden zwei Kopien angefertigt, wobei die zweite Kopie

um einen Pixel nach unten und einen Pixel nach rechts verschoben ist. Auf beiden

Bildern wird in jedem Kanal unabhängiges Gauß’sches Rauschen hinzugefügt, um eine

realitätsnähere Testsituation zu erzeugen. Für die Analyse der grauwertbasierten Ver-

fahren werden die drei Kanäle jeweils zu gleichen Teilen in ein gemitteltes Grauwert-

bild gespeichert (ebenfalls Abbildung 4.1).

Neben dieser generierten Sequenz werden die Verfahren an einem Ausschnitt eines

Satellitenbildes vom 30.07.1999, aufgezeichnet mit einem WiFS-Sensor, getestet. Der
Ausschnitt ist im zweiten Bild der Sequenz um 1° im Uhrzeigersinn um den Mittelpunkt

des Bildes gedreht. Es handelt sich um eine Aufnahme mit zwei Kanälen. Für den Ver-

gleich mit einem Grauwertverfahren wird wieder der Mittelwert der beiden Kanäle in

ein Graustufen-Bild gespeichert (Abbildung ??).

Weiterhin wird das Verfahren noch qualitativ an einer Zweikanal-Sequenz des selben

Satelliten getestet (Abbildung ??). Diese variiert jedoch von der ersten zur zweiten Auf-

nahme stark in der Helligkeit, wodurch der zeitliche Gradient nicht brauchbar ist. Aus

diesem Grund wird der Hintergrund der einzelnen Bilder mittels eines Medianﬁlters

mit geeignet großem Filterradius herausgerechnet.

Eine weitere Quelle für multispektrale Satellitenbilder sind geostationäre Wetter-

satelliten, deren Bildmaterial im Internet häuﬁg kostenlos verfügbar ist. Ein Ausschnitt

vom 10. April 2010, der einen Windstrom über dem Nordpaziﬁk zeigt, wird für einen

weiteren qualitativen Vergleich gewählt. Die Daten stammen von dem japanischen

Satelliten MTSat-1R [9] und bestehen aus drei unterschiedlichen Kanälen. Ein Kanal
zeigt kurzwelliges Infrarot (um 3.75µm), ein weiterer zeigt Wasserdampf (aufgezeich-
net um 6.75µm) und der letzte Kanal wurde im Bereich des fernen Infrarots um 10.8µm

aufgezeichnet [16].

4.2 Implementierung und Testumgebung

Die beiden hergeleiteten Algorithmen wurden im Rahmen dieser Bachelorarbeit in der

Sprache C++ unter Verwendung der VIGRA-Bibliotek implementiert. Die entsprechen-

den Funktionen nehmen als Parameter jeweils die im Voraus berechneten Gradienten

der Bildfunktion in den beiden Ortsrichtungen sowie in zeitlicher Richtung entgegen.

Die Berechnung dieser kann nach verschiedenen Verfahren geschehen und wurde de-

shalb aus der eigentlichen Funktion ausgegliedert. Weiterhin werden zusätzliche Pa-

4.3 Vergleichsmethodik

24

rameter wie die Gewichtungskonstante α oder die Größe der Umgebung im Lucas-

Kanade Algorithmus übergeben. Das resultierende Flussfeld wird dann pixelweise in

eine Zweikanalgraﬁk geschrieben. Diese kann dann beispielsweise als SVG-Graﬁk aus-

gegeben werden oder anderweitig weiterverarbeitet werden.

Bei beiden Verfahren geschieht die Berechnung eines Punktes im Flussfeld unab-

hängig von der Berechnung der umgebenen Punkte. Im Lucas-Kanade Verfahren ist

dies offensichtlich, da es sich um ein lokales Verfahren handelt. Im Horn-Schunck Algo-

rithmus hängt die Berechnung zwar von den Werten in einer Nachbarschaft ab, jedoch

beziehen sich diese Werte auf eine vorige Iteration. Daraus folgt, dass die beiden einge-

setzen Verfahren auf moderner Hardware sehr gut parallelisierbar sind. In C und C++
kann dies durch die Verwendung von OpenMP, welches ausschließlich die #pragma-
Präprozessordirektive nutzt, sehr einfach und portabel erreicht werden [14]. Die Per-

formance der Algorithmen steigt durch die Verwendung von OpenMP in eigenen Tests

etwa linear mit der Anzahl der CPU-Kerne. Denkbar ist auch die Implementierung

der Verfahren auf einer modernen GPU, wie unter anderem von Onera – The French

Aerospace Lab durchgeführt [13].

Die folgenden Tests wurden mit dem GNU C++-Compiler in der Version 4.4.4 und der

Version 1.6.0 der VIGRA-Bibliotek auf einer Pentium 4 CPU durchgeführt.

4.3 Vergleichsmethodik

Da für die synthetischen Testsequenzen die genauen Verschiebungsvektoren bekan-

nt sind, lassen sich quantitative Verfahren für die Güte der Schätzung deﬁnieren. Es

gibt jedoch verschiedene Möglichkeiten, die Ground-Truth-Daten mit den berechneten

Vektorfeldern zu vergleichen. Dabei sollen einige Maße exemplarisch herausgegriffen

werden.

Im Folgenden wird unter anderem das von Barron, Fleet und Beauchemin vorgeschla-

gene Maß zur Messung des Fehlers der Geschwindigkeitsvektoren benutzt. Die Geschwindigkeit
wird dabei als ein Raum-Zeit-Vektor der Form (cid:126)v = (u, v, 1)T in Einheiten von (Pix-
el, Pixel, Zeit) geschrieben. Um die Abweichungen im Vektorfeld zu messen empﬁelt

es sich nun den Fehler als Winkelabweichung vom korrekten Geschwindigkeitsvek-
tor zu messen. Der 2-dimensionale Verschiebungsvektor (cid:126)u = (u, v)T kann dann als
3-dimensionaler Geschwindigkeitsvektor (cid:126)v geschrieben werden und der Winkelfehler

4.3 Vergleichsmethodik

φE zur wahren Geschwindigkeit (cid:126)vc berechnet werden [2].

(cid:114)

(cid:126)v =

1
u2 + v2 + 1

φE = arccos ((cid:126)v · (cid:126)vc)

· (u, v, 1)T

25

(4.1)

(4.2)

Es ist wichtig zu erwähnen, dass dieser Winkelfehler nicht mit dem Fehler der Rich-

tungen der Verschiebungsvektoren im Ergebnis gleichzusetzen ist. Dieses Maß hängt

sowohl von der Richtung der Vektoren als auch von deren Länge ab. Dadurch führen

Richtungsabweichungen bei einer kleinen Geschwindigkeit zu einem nicht so großen

Fehler, wie Abweichungen bei höheren Geschwindigkeiten. Insbesondere bewirken

auch Vektoren, die zwar in die richtige Richtung zeigen, jedoch einen fehlerhaften Be-

trag haben, einen Fehler [2].

Auch kann eine Aussage zum Betrag der Verschiebungsvektoren gemacht werden.

Zur Bestimmung der Güte kann hier ein einfaches Fehlermaß angewendet werden, wie
der Mittelwert der quadratischen Fehler. Es gilt also für den Fehler |(cid:126)v|E des einzelnen
Geschwindigkeitsvektors

|(cid:126)v|E = (|(cid:126)v| − |(cid:126)vc|)2

(4.3)

Für den lokalen Lucas-Kanade Schätzer kann zusätzlich noch eine Angabe über die
Dichte ρ des resultierenden Vektorfeldes gemacht werden. Mit der Dichte des Feldes

wird in dieser Arbeit der Prozentsatz der Vektoren bezeichnet, der innerhalb einer Tol-
eranz τ von Null verschieden ist. Je größer die Dichte ρ ist, desto dichter ist das beze-
ichnete Vektorfeld. Aus allen Vektoren (cid:126)vn in dem Vektorfeld F folgt dann

ρ =

1
|F |

(cid:88)

v∈F

f ((cid:126)v) mit f ((cid:126)v) =




0 falls |(cid:126)v| < τ



1 sonst

(4.4)

Es wird jeweils die Verschiebung zwischen zwei Mehrkanalbildern mit den entwick-

elten Verfahren geschätzt (Lucas-Kanade MS und Horn-Schunck MS). Weiterhin wer-

den als Vergleich die Mittelwerte der Kanäle gebildet und auf den resultierenden Grauw-

ertbildern mithilfe der bereits bekannten Verfahren ebenfalls die Verschiebung geschätzt

(Lucas-Kanade GW und Horn-Schunck GW). Die resultierenden Vektorfelder werden

dann qualitativ und quantitativ ausgewertet, soweit es möglich ist.

4.4 Ergebnisse

4.4 Ergebnisse

26

Für die synthetisch generierte Bildfolge liefern alle Verfahren relativ gute Ergebnisse
(siehe Tabelle 4.1). Der Winkelfehler φE ist bei den Mehrkanal-Verfahren minimal. Die
Ursache dafür sind die zusätzlichen Informationen aus den multispektralen Bildern,

die besser ausgewertet werden können. Erwähnenswert ist auch, dass das Lucas-Kanade

Verfahren mit mehreren Kanälen in diesem Test einen geringeren Winkelfehler pro-

duzierte als das Horn-Schunck Verfahren auf Grauwertbildern. Dies ist offentsichtlich

auf die Kombination des Sinus/Cosinus-Kanals und des Rausch-Kanals zurückzuführen.

Diese beiden Kanäle sorgen dafür, dass in fast jedem Punkt in den Kanälen ein starker

Unterschied in den Gradientenrichtungen zu ﬁnden ist. Die relativ hohen Winkelfehler

für das Horn-Schunck Verfahren sind auf die Randregionen zurückzuführen, in denen

das sonst sehr glatte Vektorfeld einige Ausreißer aufweist.

Die zweite Testsequenz, der rotierte Ausschnitt aus einem Satellitenbild, bringt das

Lucas-Kanade-Verfahren bereits an seine Grenzen. Das geschätzte Flussfeld ist in Ab-

bildung ??, die Messwerte in Tabelle 4.2 zu sehen. Das Vektorfeld für das Graustufen-
bild ist sehr schwach besetzt. Nur für etwa 20 % der Bildpunkte konnten Verschiebungsvek-

toren geschätzt werden. Dies liegt an den großen, nahezu gradientenfreien Flächen.

Die Mehrkanalversion des Algorithmus kann hier teilweise noch unterschiedliche Gra-

dientenrichtungen in den verschiedenen Kanälen ausmachen, wodurch weitere Ver-

schiebungsvektoren geschätzt werden. Das Vektorfeld ist nun etwa doppelt so dicht

besetzt. Das vom Horn-Schunck Verfahren für diese Testsequenz geschätzte Vektorfeld

ist für beide Felder mit einem Winkelfehler von etwa zehn Prozent sehr gut (Abbil-

dung ??). Auf beiden Bildern haben die Verfahren die Verschiebungsvektoren von den

gut ausmachbaren Algenfronten in die strukturloseren Bereiche propagiert. Durch die

Verwendung von Multispektralbildern konnte der Winkelfehler der Geschwindigkeitsvek-

Methode φE [°]

|(cid:126)v|E [px2]

ρ [ %]

Lucas-Kanade, GW 14.79

Lucas-Kanade, MS

7.85

Horn-Schunck, GW 9.17

Horn-Schunck, MS

7.74

0.47

0.07

0.06

0.10

99.9

100.0

100.0

100.0

Tabelle 4.1: Quantitative Ergebnisse für die synthetische Bildsequenz

4.4 Ergebnisse

27

Methode φE [°]

|(cid:126)v|E [px2]

ρ [ %]

Lucas-Kanade, GW 17.26

Lucas-Kanade, MS

14.87

Horn-Schunck, GW 11.13

Horn-Schunck, MS

9.26

1.45

1.10

1.82

1.47

20.6

41.1

100.0

100.0

Tabelle 4.2: Quantitative Ergebnisse für das rotierende Satellitenbild

toren im Verhältnis zum Grauwertverfahren um etwa 15 Prozent gedrückt werden. Aus

den Flussfeldern ist ersichtlich, dass dieser Unterschied gering ist, da die Verfahren sehr

ähnliche Ergebnisse erbringen.

Im dritten Test wurde die Strömung einer Algenpopulation in einem Satellitenbild

geschätzt. Die Ergebnisse entsprechen denen des vorigen Tests: Auch hier hat der mul-

tispektrale Lucas-Kanade Schätzer ein besseres Ergebnis erbracht als das grauwert-

basierte Verfahren. Da keine Ground-Truth-Werte vorliegen, bedeutet besser in diesem

Kontext, dass das Vektorfeld dichter besetzt ist. Die Richtung des Vektorfeldes stimmt

gut mit der wahrgenommenen Bewegung überein. Das Horn-Schunck Verfahren ist

hier wieder die bessere Wahl. Das geschätzte Vektorfeld auf beiden Bildern ist dicht

besetzt und beschreibt sehr glatt die vermeintliche Verschiebung der Algenblüte.

4.4 Ergebnisse

28

(a) Grauwertbild, Lucas-Kanade Schätzer

(b) Multispektralbild,

Lucas-Kanade

Schätzer

(c) Grauwertbild, Horn-Schunk Schätzer

(d) Multispektralbild,

Horn-Schunk

Schätzer

Abbildung 4.2: Ergebnisse für die Sequenz des geostationären Wettersatelliten

Das für das Satellitenbild des japanischen MTSat-Satelliten geschätzte Verschiebungs-

feld ist in beiden Ausführungen des Lucas-Kanade Schätzers dicht besetzt. Auch ist

jeweils die Bewegungsrichtung des hellen Wolkenstreifens, von links nach rechts, erkennbar.

Das Graustufenverfahren weist jedoch starke Schwankungen in den bestimmten Rich-

tungsvektoren auf, wohingegen der Schätzer auf dem Mehrkanalbild ein deutlich glat-

teres Feld berechnen konnte. Der Horn-Schunck Schätzer produziert ebenfalls in beiden

Varianten ein gutes Feld. Auch hier ist das für die Mehrkanalaufnahme geschätzte Feld

etwas glatter und zeichnet sich durch weniger Variationen in den Richtungen der Ver-

schiebungsvektoren aus. Es fällt jedoch auf, dass die Bewegungen des schnellen Wind-

stromes in die eigentlich recht ruhige, dunklere Region südlich des Windes propagiert

wurden. Es beﬁnden sich jedoch einige kleine Wolkenfragmente in dieser Region, die

andeuten, dass dort kaum Strömung herrscht. Dies kann auch in dem vom Lucas-

Kanade Schätzer geschätzten Vektorfeld nachvollzogen werden.

5 Fazit und Ausblick

29

5 Fazit und Ausblick

Es wurden zwei Verfahren entwickelt, um bei der Schätzung des optischen Flusses

die in Multispektralbildern vorhandenen Informationen besser nutzen zu können als

die bekannten Grauwertverfahren es tun. Dabei wurde auf den bereits bestätigten Ver-

fahren aufgebaut und die den Verfahren zugrundeliegenden Ideen auf die Verwendung

mit Mehrkanalbildern erweitert.

Die Auswertung von Testdaten und der abschließende Vergleich ergaben, dass die

hergleiteten Verfahren, wenn die geforderten Bedingungen erfüllt werden, durchaus

bessere Ergebnisse erbringen können.

Der aus dem Lucas-Kanade Verfahren abgeleitete Schätzer produzierte in den Ver-

gleichen signiﬁkant dichtere und genauere Vektorfelder als das normale Lucas-Kanade

Verfahren und ist somit deﬁnitv als eine Verbesserung anzusehen. Dies ist auch der Fall

gewesen, wenn die Gradientenrichtungen in den verschiedenen Kanälen des Bildes in

einem Punkt ähnlich sind. Es ist denkbar, dass das Verfahren auf Mehrkanalbildern

auch gute Ergebnisse liefert, wenn die Größe der Umgebung, in der die Bewegung

als konstant angenommen wird, verringert wird. Dies setzt natürlich voraus, dass die

Gradientenrichtungen in den Kanälen nicht korrelieren. Das Verfahren ist im Gegen-

satz zum Horn-Schunck Verfahren performant, wodurch es auch für die Verwendung

in Echtzeitanwendungen denkbar ist. So ist beispielsweise eine Verwendung in Com-

puterprogrammen zur Gestenerkennung mittels einer Webcam, die Farbbilder aufze-

ichnet, möglich. Auch die in der Einleitung erwähnte automatische Navigation von

Robotern kann durch die Verwendung von Mehrkanalbildern proﬁtieren. So kann der

Roboter neben den Informationen, die er im sichtbaren Bereich aufzeichnet, noch Daten

aus dem Infrarot- oder UV-Bereich verwenden.

Bei dem vom Horn-Schunck Verfahren abgeleiteten Schätzer wurde in den betra-
chteten Testsequenzen jedoch nur eine geringe Verbesserung von etwa 10 % bis 20 %

erzielt. In den resultierenden Vektorfeldern lässt sich über das reine Augenmaß hin-

aus somit kaum ein Unterschied ausmachen. Dies ist jedoch auch zum Teil auf die bei
der Berechnung verwendeten Werte für die Gewichtungskonstante α, sowie für den
Radius der Nachbarschaft, in der ¯u und ¯v bestimmt werden, zurückzuführen. Diese

Konstanten wurden in den Vergleichen für beide Bildarten gleich gewählt. Es ist je-
doch denkbar, dass durch einen geringeren Wert für α das Feld weniger geglättet wird

5 Fazit und Ausblick

30

und dadurch der Vorteil bei der Verwendung von Multispektralbildern stärker her-

vortritt. Die Auswahl der synthetischen Testsequenzen spielt möglicherweise ebenfalls

eine Rolle. Beide Sequenzen, für die eine quantitative Analyse möglich war, wurden

nur durch einfache globale Transformationen wie Verschiebung und Rotation verän-

dert. Für Vergleiche mit mehr Aussagekraft müssten Sequenzen mit verschiedenen

lokalen Veränderungen erzeugt werden. Dazu könnte man nach einem bekannten Ver-

schiebungsfeld ein Ausgabebild verzerren und diese bekannte Verschiebung danach

erneut schätzen.

Die beiden in dieser Bachelorarbeit hergeleiteten Verfahren sollen als Grundlage für

weitere Entwicklungen dienen. Eine Idee, die in einer anderen Arbeit weiter verfol-

gt werden kann, ist die unterschiedliche Gewichtung der betrachteten Kanäle bei der

Schätzung der Verschiebungsvektoren. So könnten Kanäle, in denen die gesuchte Be-

wegung besonders deutlich wird, stärker in die Berechnung aufgenommen werden als

Kanäle, in denen die Bewegung nicht zu registrieren ist. Dies könnte durch ein lokales

Verfahren abhängig von der Struktur der betrachteten Region in den unterschiedlichen

Kanälen geschehen. In der Fernerkundung ist auch eine Gewichtung der Kanäle an-

hand des Reﬂektionsspektrums des gesuchten Objektes oder Stoffes denkbar.

Literaturverzeichnis

31

Literaturverzeichnis

[1] VIGRA Homepage.

http://hci.iwr.uni-heidelberg.de/vigra/,

abgerufen am 16.07.2010.

[2] J. L. Barron, D. J. Fleet, and S. S. Beauchemin. Performance of optical ﬂow tech-

niques. International Journal of Computer Vision, 12:43–77, 1994.

[3] J. L. Barron and N. A. Thacker. Tutorial: Computing 2d and 3d optical ﬂow. Tina-

Vision, 2005.

[4] Berthold K. P. Horn und Brian G. Schunck. Determining optical ﬂow. Artiﬁcal

Intelligence, 17:185–203, 1981.

[5] Miguel Tavares Coimbra. Approximating Optical Flow Within the MPEG-2 Com-

pressed Domain. IEEE Transactions on Circuits and Systems for Video Technology, 15,

2005.

[6] Gerald Fiedler. Untersuchungen zur Bestimmung zweidimensionaler Strömungsfelder

an der Meeresoberﬂäche mit Hilfe von multispektralen Satellitenbildern. PhD thesis,

Universität Hamburg, Dezember 2003.

[7] Lorenz Gerstmayr. An Improvement of the Lucas-Kanade Optical-Flow Algo-
rithm for every Circumstance, 2008. http://www.ti.uni-bielefeld.de/
downloads/lgerstmayr/lk_improvements.pdf, abgerufen am 21.07.2010.

[8] J. K. Kearney, W. B. Thompson, and D. L. Boley. Optical ﬂow estimation: an error

analysis of gradient-based methods with local optimization. IEEE Trans. Pattern

Anal. Mach. Intell., 9(2):229–244, 1987.

[9] Gunter Dirk Krebs. MTSat 1, 1R (Himawari 6). http://www.skyrocket.de/

space/doc_sdat/mtsat-1.htm, abgerufen am 24.07.2010.

[10] J. P. Lewis. Fast Normalized Cross-Correlation, 1995.

[11] David Malin. Multispectral imaging. http://encyclopedia.jrank.org/
abgerufen am

articles/pages/1163/Multispectral-Imaging.html,
12.07.2010.

Literaturverzeichnis

32

[12] Ikuya Murakami. The aperture problem in egocentric motion. Trends in Neuro-

sciences, 27, 2004.

[13] Onera - The French Aerospace Lab. GPU for Image: GPU-FOLKI.

http:
//www.onera.fr/dtim-en/gpu-for-image/folkigpu.php, abgerufen am
20.07.2010.

[14] OpenMP Architecture Review Board. The OpeMP API speciﬁcation for parallel

programming. http://openmp.org/wp/, abgerufen 22.07.2010.

[15] Benjamin Seppke. Herleitung der Euler-Lagrange Gleichungen für Optical Flow

Constraints, 2010.

[16] Space Science and Engineering Center. Geostationary Image Browser. http:

//www.ssec.wisc.edu/data/geo/index.php.

[17] Rainer Sprengel. Untersuchung differentieller Ansätze zur Schätzung des optischen

Flusses in Grauwert- und Farbbildfolgen. PhD thesis, Universität Hamburg, Mai 1988.

[18] Selim Temizer. Optical Flow Based Robot Navigation.

http://people.
csail.mit.edu/lpk/mars/temizer_2001/Optical_Flow/, abgerufen am
15.07.2010.

[19] Sarita Thakoor und John Morookian.

Insect-inspired optical-ﬂow navigation
http://www.techbriefs.com/content/view/216/32/,

sensors.

2005.

abgerufen am 15.07.2010.

[20] U.S. Geological Survey. LE71970222002196EDC00. Aufname des Landsat 7 ETM+

Satelliten.

Eidesstattliche Erklärung

33

Eidesstattliche Erklärung

Ich versichere, dass ich die vorliegende Arbeit selbstständig und ohne fremde Hilfe

angefertigt und mich anderer als der im beigefügten Verzeichnis angegebenen Hilfsmit-

tel nicht bedient habe. Alle Stellen, die wörtlich oder sinngemäß aus Veröffentlichungen

entnommen wurden, sind als solche kenntlich gemacht.

Ich bin mit der Einstellung in den Bestand der Bibliothek des Fachbereichs einver-

standen.

Oliver Bestmann

Hamburg, den 12. Februar 2012

