Ger¨auschquellenlokalisierung mit einem
humanoidem Roboter

Bachelorarbeit
im Arbeitsbereich Knowledge Technology, WTM
Prof. Dr. Stefan Wermter

Department Informatik
MIN-Fakult¨at
Universit¨at Hamburg

vorgelegt von
Robert Keßler
am
31. Januar 2012

Gutachter: Prof. Dr. Stefan Wermter

Dr. Cornelius Weber

Robert Keßler
Matrikelnummer: 6053843
Wurmsweg 1
20535 Hamburg

Zusammenfassung

Um eine solide Interaktion mit einem menschlichen Benutzer m¨oglich zu machen,
muss jeder Roboter in Zukunft ein umfangreiches auditorisches System bereitstel-
len. Neben der Spracherkennung ist dabei auch die Ger¨auschquellenlokalisation
ein notwendiger Bestandteil. Diese Arbeit zeigt die Realisierung eines Lokalisie-
rungsverfahrens in der horizontalen Ebene, mit einem humanoidem Roboter unter
Nutzung von Cross Correlation und K¨unstlichen Neuronalen Netzen.
Der Roboter soll 24 verschiedene Richtungen am vollen 360◦ Kreis, mit einem je-
weiligen Abstand von 15◦, unterscheiden. Dies gelingt dem vorgestellten Verfahren
mit einer Genauigkeit von bis zu 92%. Dabei treten die fehlerhaften Klassiﬁkatio-
nen haupts¨achlich zwischen benachbarten Richtungen auf.

Zusammenfassung

IV

Inhaltsverzeichnis

1 Einleitung

2 Grundlagen

2.1 Nao Roboter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Fourier Transformation . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Audiodaten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 Korrelationsanalyse . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.5 K¨unstliche Neuronale Netze . . . . . . . . . . . . . . . . . . . . . .
”How we localize Sound” . . . . . . . . . . . . . . . . . . . . . . . .
2.6

3 Problemstellung und verwandte Arbeiten

3.1 Fragestellung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Verwandte Arbeiten . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Methodik . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4 Eigenes Verfahren

4.1 Theoretische ¨Uberlegungen . . . . . . . . . . . . . . . . . . . . . . .
4.2 Eigenes Verfahren . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . .
4.3 Aufnahme und Transfer
4.4 Vorverarbeitung . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5 General Cross Correlation . . . . . . . . . . . . . . . . . . . . . . .
4.6 K¨unstliches Neuronales Netz . . . . . . . . . . . . . . . . . . . . . .
4.7 Eﬀektoren . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5 Experiment

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1 Erster Test
5.2 Versuch mit einfachen Wortensequenzen . . . . . . . . . . . . . . .
5.3 Vorverarbeitung mit Rauschreduzierung
. . . . . . . . . . . . . . .
5.4 Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6 Fazit

Literaturverzeichnis

Abbildungsverzeichnis

V

1

3
3
5
6
7
8
9

11
11
12
15

21
21
21
22
23
24
25
27

29
30
33
34
36

37

44

45

Inhaltsverzeichnis

VI

Kapitel 1

Einleitung

Aus vielen Bereichen des heutigen Lebens sind technische Ger¨atschaften nicht mehr
wegzudenken. Sei es die Waschmaschine, die Mikrowelle oder der K¨uhlschrank. Die-
se Systeme sollen vor allem eines erreichen - dem Menschen Arbeit abnehmen bzw.
diese erleichtern.
Dieser Trend ist auch bei der Entwicklung von Servicerobotern zu beobachten. Ein
solides Beispiel daf¨ur ﬁndet sich im PERSES Projekt [6]. Dieses Robotersystem
hat explizit die Aufgabe, in einem einfachen Einkaufsladen dem Kunden f¨ur Fra-
gen zu Verf¨ugung zu stehen. Auch als unterst¨utzende Einheit in der Chirurgie [17]
k¨onnen Roboter ihren Einsatzort ﬁnden.
Von einem gew¨ohnlichen Anwender kann jedoch nicht erwartet werden, dass die-
ser sich mit speziellen Eingabemethoden eines Serviceroboters auskennt. Es ist
beispielsweise bei Servicerobotern zur Unterst¨utzung von alten Menschen auch
schlichtweg unrealistisch, dass diese zuerst ein 400-seitiges Handbuch mit allen
Kommandos lesen und vor allem verstehen sollen. Es ist allgemein unpraktisch,
wenn zur Interaktion mit dem System Vorwissen oder umfangreiche Einarbeitung
notwendig sind.
Da bei zwischenmenschlicher Kommunikation Sprache als Hauptmedium genutzt
wird, liegt es auch bei der Mensch-Roboter-Interaktion (MRI) nahe, nat¨urliche
Sprache als Medium zu nutzen. Die Verarbeitung von nat¨urlichsprachlichen Einga-
ben w¨urde es jedem Nutzer erm¨oglichen, einfach mit dem Roboter zu interagieren.
Gerade wenn es zum Beispiel um die Rettung von Menschen in gef¨ahrlichen Ge-
bieten geht, muss der Roboter auch in der Lage sein, sofort mit den Verletzten
zu kommunizieren. Neben der zuverl¨assigen Spracherkennung muss der Roboter
jedoch auch eine M¨oglichkeit besitzen, zu bestimmen woher ein Ger¨ausch oder ein
Hilferuf kommt. Ein Beispiel f¨ur die Notwendigkeit eines solches Systems w¨are ein
verrauchter Raum, eines brennenden Geb¨audes, in dem der Roboter mit einfachen
Kamerabildern kaum weiterf¨uhrende Informationen bekommen kann.
Eine einfache Aufgabenstellung f¨ur einen Serviceroboter im Haushalt ist in Ab-
bildung 1.1 dargestellt. Der Besitzer des Serviceroboters ruft diesem zu, dass er
herkommen soll. Die Aufgabe des Roboters ist nun herauszuﬁnden, wo dieses hier
¨uberhaupt liegt. Ein anderer Anwendungsfall w¨are ein Robotersystem als Tou-
ristenf¨uhrer. Sobald eine Frage gestellt wird, z.B. ”Was ist das dort?”, muss der

1

Kapitel 1. Einleitung

Roboter zuerst einmal feststellen, woher die Frage kommt, da er aus der Semantik
der Frage schließen sollte, dass eine Person der Reisegruppe gerade auf irgendetwas
zeigt. Nachdem er die Person gefunden hat, kann er wom¨oglich ein Bild analysieren
oder anderweitig Informationen sammeln und auswerten. Der Roboter muss somit
ein solide gestaltetes auditorisches System besitzen, um den normalen Umgang
mit dem Anwender zu gew¨ahrleisten.

Abbildung 1.1: Aufgabenstellung eines Serviceroboters

Durch welche Methoden eine Ger¨auschquelle im Raum lokalisiert werden kann,

ist hierbei die Hauptfragestellung, die bearbeitet werden soll.
Es gibt zwar Ans¨atze, die schon in den neunziger Jahren entwickelt wurden, es
fehlte den Robotern jedoch an der notwendigen Rechenleistung [7]. Heutzutage ist
die Technik soweit, dass auch autonome Roboter in der Lage sind, die relativ inten-
siven Berechnungen durchzuf¨uhren. Dies spannt ein attraktives Anwendungsgebiet
auf.

Leitfaden

Die Arbeit ist nun wie folgt gegliedert. Im n¨achsten Kapitel ﬁnden sich einige
Grundlagen, die zur Aneignung von eventuell fehlendem Vorwissen dienen sollen.
Im Kapitel 3 wird die Fragestellung aufgef¨uhrt und verwandte Arbeiten herange-
zogen. Darauf folgend wird die Zielstellung und Umsetzung meines eigenen Ver-
fahrens beschrieben. Im Abschnitt 5 sind zwei Versuche dargestellt, mit denen
mein Verfahren getestet wurde. Abschließend ﬁndet sich eine Zusammenfassung
der Ergebnisse und ein Ausblick auf weitere denkbare Arbeitsans¨atze.

2

Kapitel 2

Grundlagen

Im folgenden Abschnitt wird auf einige Grundlagen eingegangen, die zum Verst¨and-
nis der sp¨ater vorgestellten Arbeiten beitragen sollen. Weiterhin wird der huma-
noide Roboter beschrieben, mit dem mein sp¨ateres Verfahren realisiert wird.

2.1 Nao Roboter

Abbildung 2.1: Nao Roboter

Mein gesamtes Verfahren wird mithilfe eines humanoidem Roboters realisiert [4].
Der Nao Roboter ist 53 Zentimeter groß und besitzt komplexe Bewegungsm¨oglich-
keiten mit 5 Freiheitsgraden pro Arm und Bein, sowie 2 Freiheitsgraden f¨ur den
Kopf und jede Hand. Er bewegt sich auf zwei Beinen fort und besitzt 4 Mikro-
phone an seinem Kopf. Dabei beﬁnden sich das linke und das rechte Mikrophon

3

Kapitel 2. Grundlagen

in der gleichen X-Z Ebene und sind an der Y Achse gespiegelt. Das vordere und
das hintere Mikrophon beﬁnden sich beide auf der Y-Achse, unterscheiden sich
jedoch in H¨ohe und Entfernung zum Mittelpunkt. Die Positionen der Mikrophone
am Roboter sind in Abbildung 2.2 zu erkennen. Die Mikrophone besitzen eine ma-
ximale Sampling Rate von 48 kHz und einem Frequenzbereich f¨ur die Aufnahme
von 20 Hz - 20 kHz.

Abbildung 2.2: Mikrophonpositionen

Der Kopf des Roboters l¨asst sich dabei aus der Ausgangslage (0◦) um jeweils
119.5◦ nach links bzw. nach rechts in der horizontalen Ebene drehen. Daraus ergibt
sich ein Bereich von 239◦, der ohne Bewegung des Roboters zug¨anglich ist. Um die
verbleibenden 121◦ zu erreichen, ist eine Drehung des ganzen Roboters notwendig.
Wie in Abbildung 2.3 erkennbar ist, l¨asst sich der Kopf auch nach vorne bzw. nach
hinten neigen. In meinem Verfahren m¨ochte ich jedoch die Neigung des Kopfes
stets auf 0 Grad belassen und mich nur auf die horizontale Ebene konzentrieren.

Abbildung 2.3: Bewegungsfreiheit des Kopfes

4

2.2. Fourier Transformation

2.2 Fourier Transformation

Die Fourier Transformation ist eine grundlegende Methodik der Mathematik [23].
Sie dient dazu, ein Signal, welches ¨uber den zeitlichen Verlauf abgebildet ist, im
Verlauf ¨uber den Frequenzraum darzustellen. Da in dieser Arbeit nur diskretisierte
Signalfolgen auftauchen, wird auch nur die Diskrete Fourier Transformation (DFT)
erl¨autert.
Angenommen es liegt ein zeitlich diskretisiertes Signal x (n) mit 0 ≤ n ≤ N
endlicher L¨ange vor. Gleichung 2.1 zeigt dabei die Abbildungsvorschrift der Fou-
riertransformation, wobei ejΩ eine komplexe Zahl und Ω selbst den Winkel der
komplexen Zahl in der Polarkoordinatendarstellung beschreiben.
Die Frequenzdom¨ane, in die wir das Signal transformieren wollen, wird nun in
N gleiche Teile aufgeteilt. Da eine komplette Kreisfrequenz 2π sind, werden die
Punkte also gleichm¨aßig im Intervall von 0 bis 2π verteilt. Ω kann nun durch Ωk
(Gleichung 2.2) ersetzt werden. Es ergibt sich daraus die Gleichung 2.3, die einen
Wert f¨ur die Fouriertransformation f¨ur den Parameter k beschreibt

X(ejΩ) =

N
(cid:88)

n=0

x(n) · e−jnΩ

Ω → Ωk =

2π
N

· k

X(ejΩk) =

N
(cid:88)

n=0

x(n) · e−jnΩk

(2.1)

(2.2)

(2.3)

In der Literatur ist es typischerweise so, dass Ωk durch den Frequenzindex k ersetzt
wird. Die Gleichung ¨andert sich demzufolge in der Schreibweise zu:

X(k) =

N
(cid:88)

n=0

x(n) · e−jn kn

N , k = 0, 1, 2, · · · , N − 1

(2.4)

Das Ergebnis der Diskreten Fourier Transformation ist eine Abbildung in den
Raum der Komplexen Zahlen. Die Komplexen Zahlen sind dabei als Polarkoor-
dinaten dargestellt, wobei der Winkel im Bereich von 360◦ gleichm¨aßig verteilt ist.
Der Betrag der Komplexen Zahl gibt dabei an, wie h¨auﬁg die zugrunde liegende
Frequenz auftritt.

Abbildung 2.4 veranschaulicht, wie die Fourier Transformation arbeitet. Ange-
nommen wir haben einen Sinuston mit 2 Hertz (Hz) und ein Mikrophon, was diesen
Ton (rote Linie) eine Sekunde lang mit einer Samplingrate von 32 Hz abgetastet
hat (blaue Punkte). Das Spektrum wird mit der gr¨unen Linie gekennzeichnet. Dort
ist auch der H¨ochstwert f¨ur 2 Hz zu erkennen.

5

Kapitel 2. Grundlagen

Abbildung 2.4: Beispiel einer Fouriertransformation

2.3 Audiodaten

Abtastung

Wenn Audiodaten aus der realen Welt mittels Mikrophonen aufgenommen werden,
m¨ussen diese diskretisiert werden. Diesen Vorgang nennt man Abtastung (engl.
Sampling). Ein Sample ist dabei der diskretisierte Wert der Amplitude eines ana-
logen Audiosignals zu einem bestimmten (diskreten) Zeitpunkt. Die Abtastrate
beschreibt, wie oft in einer Sekunde eine Abtastung des analogen Signals vorge-
nommen wird.

Eigenschaften des aufgenommen Soundﬁles

Alle in dieser Arbeit verwendeten Audiodaten werden mit einer Abtastrate von
48 kHz aufgenommen. Mithilfe dieser Abtastrate f l¨asst sich bestimmen, wie viel
Zeit zwischen zwei Samples vergangen ist.
Unter Zuhilfenahme der Gleichung 2.5 l¨asst sich die vergangene Zeit zwischen zwei
Abtastungen mit 22.83 µs (Gleichung 2.6) bestimmen [21].

∆t =

∆t =

1
f

1
48000 s−1

6

(2.5)

(2.6)

2.4. Korrelationsanalyse

2.4 Korrelationsanalyse

Unter Korrelationsanalyse (engl. Correlation Analysis) versteht man eine Abbil-
dung von zwei Signalen ¨uber Zeit, f(t) und g(t), auf einen Wert im Intervall [-1,1].
Diese Abbildung beschreibt, wie sehr die beiden ¨uber die Zeit verlaufenden Signale
sich ¨ahneln.

Cross Correlation

Um den Zeitversatz zwischen zwei aufgenommenen Audiosignalen zu bestimmen,
eignet sich ein Verfahren namens Cross Correlation (CC) [15]. Damit ist es m¨oglich
den Zeitunterschied (engl. Time Delay of Arrival, TDOA) zwischen zwei Mikro-
phonen zu bestimmen. Bei dem Verfahren wird eines der diskretisierten Signale
jeweils um einen Schritt in der Zeit (also um ein Sample) verschoben und der Ge-
samtfehler zwischen den Amplitudenverl¨aufen bestimmt. Ziel des Verfahrens ist
es, den Wert f¨ur die Verschiebung zu bestimmen, an dem die Fehler minimal und
damit die Correlation maximal wird.

Nehmen wir an, dass die Signale f(n) und g(n), mit der L¨ange N, diskretisiert
vorliegen. Dabei ist N gleich der Dimension der beiden Vektoren. Zun¨achst werden
beide Vektoren mittels 2.7 normiert. Darauf folgend wird die Correlation ¨uber den
Zeitversatz T mittels 2.8 bestimmt.

fnorm(n) =

f (n)
n=0 f (n)2

(cid:80)N

Corr(f, g)T =

N
(cid:88)

n=0

f (n) · g(n + T )

(2.7)

(2.8)

Der Verlauf der Correlation ¨uber den Zeitversatz T ist in Abbildung 2.5 dargestellt.
Man erkennt dort auch den maximalen Punkt der Correlation bei T = -1.

Generalized Cross Correlation

Das Problem in der Zeitdom¨ane ist jedoch, dass der optimale Zeitunterschied zwi-
schen zwei Sample liegen k¨onnte. Um dies mittels Cross Correlation zu l¨osen, ist
dann eine Interpolation zwischen den Samples n¨otig, welche die Algorithmen we-
sentlich komplexer werden lassen.
Um dies zu bew¨altigen, l¨asst sich Generalized Cross Correlation (GCC) verwenden.
Dieses Verfahren nimmt f¨ur die Signale eine Gewichtungsfunktion hinzu. Je nach-
dem, wie diese Funktion gew¨ahlt ist, sind enorme Verbesserungen im Bestimmen
des TDOAs m¨oglich.

7

Kapitel 2. Grundlagen

(a) Signalverlauf f(t) und g(t)

(b) Verlauf der Correlation

Abbildung 2.5: Cross Correlation

2.5 K¨unstliche Neuronale Netze

Um ein System zu entwerfen, was f¨ur eine gewisse Eingabe eine Klassiﬁkation (Ein-
ordnung in eine Kategorie) triﬀt, eignen sich K¨unstliche Neuronale Netze (KNN)
besonders gut [20]. K¨unstliche Neuronale Netze bilden dabei, wie auch ihr bio-
logisches Vorbild, ein Modell, welches auf der Verkn¨upfung von vielen kleinen,
sehr simpel gehaltenen Einheiten basiert. Die k¨unstlichen Neuronen k¨onnen da-
bei in verschiedensten Strukturen angeordnet werden. Oft genutzte Strukturen
sind Feed-Forward-Strukturen, die die Neuronen in einfachen Schichten anordnen
und somit eine Eingabe auf eine Ausgabe abbilden. Rekurrente Neuronale Netze
(RNN) haben r¨uckf¨uhrende Strukturen, die manche Ausgaben von Neuronen wie-
der als Eingabe an vorhergehende Neuronen zur¨uckgeben. Diese Strukturen sind
besonders daf¨ur geeignet, wenn Neuronale Netze einen vorherigen Zustand bei der
n¨achsten Berechnung mit in Betracht ziehen sollen.

8

2.6. ”How we localize Sound”

2.6 ”How we localize Sound”

Wie der Mensch ¨uberhaupt in der Lage ist, die Richtung einer Soundquelle zu
bestimmen, liefert oftmals die Grundlage f¨ur die verschieden technischen L¨osungs-
ans¨atze. William M. Hartman beschreibt dabei 1999 zwei grundlegende Prinzipien,
die es dem Menschen erm¨oglichen, eine Ger¨auschquelle zu lokalisieren [7]. Diese bei-
den Grundlagen sind die Interaural Level Diﬀerence (ILD) und die Interaural Time
Diﬀerence (ITD). Die ILD beschreibt dabei den Intensit¨atsunterschied in der Am-
plitude am linken bzw. am rechten Ohr. Sie wird in Dezibel angegeben und h¨angt
stark von der Frequenz des Ger¨ausches ab. Bei hochfrequenten T¨onen nimmt die
Amplitude im Vergleich vom linken zum rechten Ohr aufgrund der Streuung und
Tr¨ubung am menschlichen Kopf und K¨orper st¨arker ab. Niederfrequente T¨one un-
terliegen jedoch am menschlichen Kopf einer Beugung und erreichen daher beide
Ohren mit fast gleicher Intensit¨at. Nun ist der Mensch jedoch auch problemlos in
der Lage, T¨one im niederfrequenten Bereich zu lokalisieren. Dies ist mithilfe des
ITD m¨oglich. Die Interaural Time Diﬀerence beschreibt dabei den Zeitunterschied,
mit dem ein Ger¨ausch an beiden Ohren des Menschen ankommt. Der Unterschied
in der Zeit und der Unterschied in der Phase eines Signals sind dabei proportional
zueinander. Die Zeitunterschiede liegen dabei im Mikrosekundenbereich. Zurecht
mag also hier die Frage aufkommen, wie dieser Sachverhalt bei einem Nervensys-
tem mit Verz¨ogerungen im Bereich von Millisekunden ¨uberhaupt m¨oglich ist.
Inzwischen gibt es Beweise daf¨ur, dass ein Verarbeitungssystem, die ’superior oli-
ve’ im Mittelhirn, in der Lage ist, eine Art Cross Correlation zu bewerkstelligen.
Zugrunde liegend ist daf¨ur das Modell von L. A. Jeﬀress, welches in Abbildung 2.6
ein grobe Vorstellung von dem Sachverhalt zeigt [9].

Abbildung 2.6: Delay Line Modell

9

Kapitel 2. Grundlagen

10

Kapitel 3

Problemstellung und verwandte
Arbeiten

Im folgenden Kapitel wird die Problemstellung dargestellt und verwandte Arbeiten
herangezogen, welche bisherige L¨osungsans¨atze beschreiben.

3.1 Fragestellung

Die Fragestellung dieser Arbeit ist nun, wie ein Roboter ¨uberhaupt ein Ger¨ausch im
Raum zu ﬁnden vermag. Um ein Ger¨ausch aufzunehmen, muss er die akustischen
Sensoren benutzen und das analoge Signal in ein digitales Signal umsetzen. Dieses
kann dann mithilfe von verschiedenen Verfahren einen R¨uckschluss auf die Posi-
tion der Ger¨auschquelle im Raum liefern. Die Ger¨auschquellenlokalisation sollte
m¨oglichst genau und robust erfolgen. In meiner Arbeit m¨ochte ich dabei bioinspi-
riert mittels Korrelationsanalyse und K¨unstlichen Neuronalen Netzen vorgehen. In
der Literatur verwendete Verfahren beinhalten verschiedene Grundelemente, die
die Einteilung in drei unterschiedliche Rubriken m¨oglich machen.

11

Kapitel 3. Problemstellung und verwandte Arbeiten

3.2 Verwandte Arbeiten

3.2.1 Lokalisierung mittels Korrelationsanalyse

Mithilfe der Korrelationsanalyse wird in der Regel die Interaural Time Diﬀerence
und die Interaural Level Diﬀerence bestimmt.

So beschreiben Lee et. al. (2008) wie mithilfe des TDOA und 4 Mikrophonen,
die vertikale Position einer Ger¨auschquelle bestimmt werden kann [11]. Es wird da-
bei ein k¨unstliches Ohr verwendet. Mit einer Ohrmuschel ausgestattet, erm¨oglicht
es die Vermeidung von Vieldeutigkeit in der Positionsbestimmung. Dabei zeigt
das Verfahren im allgemeinen gute Erfolgsquoten f¨ur die korrekte Bestimmung des
Winkels. Es treten jedoch signiﬁkante Fehler auf, sobald sich die Ger¨auschquelle
¨uber dem Roboterkopf beﬁndet.

Im Verfahren von Murray et. al. 2009 wird eine physikalisch motivierte Heran-
gehensweise gew¨ahlt [16]. Zun¨achst werden zur Vorverarbeitung des Signals ver-
schiedene Verfahren genutzt: Zur Unterscheidung, ob ein Signal relevant ist, wird
der Energiegehalt der Aufnahme ermittelt. Dieser ist bei menschlicher Sprache, im
Gegensatz zum einfachen Rauschen, signiﬁkanten unterschiedlich. Weiterhin wird
zur Anpassung an die Umgebung die Lautst¨arke der Aufnahme moduliert. Wenn
das Signal relevant ist, wird darauf folgend die Interaural Time Diﬀerence, mittels
General Cross Correlation bestimmt. Auf Grundlage der Ausbreitungsgeschwin-
digkeit des Schalls wird der Winkel bestimmt, an dem sich die Ger¨auschquelle
beﬁndet. Das Verfahren erreicht f¨ur Objekte, die vor dem Roboter liegen und
sich demnach im Bereich von 0◦ aufhalten, sehr hohe Genauigkeiten. Eine Abwei-
chung von maximal ±1.5◦ wird angegeben. Mit einer Abweichung von ±7.5◦ gibt
es jedoch im Bereich von 90◦ signiﬁkante Ungenauigkeiten beim Lokalisieren der
Ger¨auschquellen. Auch wurde erw¨ahnt, dass das Verfahren, aufgrund der zeitin-
tensiven Berechnung der Correlation, nicht Echtzeitf¨ahig war.

Liu und Shen (2010) nutzen eine erweiterte Form der GCC: GCC-PHAT [12].
Die Correlation wird mithilfe einer Phasentransferfunktion, also im Frequenzraum,
durchgef¨uhrt. Das Hauptaugenmerk liegt dabei auf einem Modell um Echoeﬀekte
auszuschließen und somit eine genauere Lokalisierung zu erm¨oglichen. Das Verfah-
ren verwendet 4 Mikrophone zu Berechnung der Correlation. Es werden weiterhin
Entfernungen unterschieden. So werden Aufnahmen mit einer Entfernung von 1 m,
2 m und 3 m verwendet. Gr¨oßere Genauigkeit der Lokalisation ﬁndet sich dabei
vor allem im nahen Bereich. Mit zunehmender Entfernung nimmt auch die Genau-
igkeit, besonders f¨ur die Bereiche von 0◦ und 180◦, ab. Durch Hinzunahme eines
weiteren Mikrophonpaars k¨onnen diese Fehler auch f¨ur weitere Entfernungen dras-
tisch reduziert werden.

12

3.2. Verwandte Arbeiten

3.2.2 Lokalisierung mittels Neuronalen Netzen

Ein weiterer Ansatz ist der Einsatz von Neuronalen Netzen, da diese allein mithil-
fe von vorhandenen Trainingsdaten ein komplexes mathematisches Modell durch
geeignete Lernverfahren abstrahieren k¨onnen.

Im Verfahren von Czyzewski (2003) wird gezeigt, wie aus aufgenommenen
Ger¨auschen mithilfe von Beamforming [8] verschiedenste Features extrahiert wer-
den [3]. Diese werden unter drei verschiedenen Trainingsalgorithmen einem Neu-
ronalen Netz pr¨asentiert. Bei dem eingesetzten Neuronalen Netz handelt es sich
um ein Feedforwardnetz, welches in der Lage ist eine Abbildungsvorschrift zu er-
lernen. Die Erfolgsquote der Erkennung schwankt dabei abh¨angig vom gew¨ahlten
Lernverfahren und den genutzten extrahierten Features. Die Erfolgsrate der Neuro-
nalen Netze beﬁndet sich dabei zwischen 78% und 92% bei pr¨asentierten Testdaten.

Ein weitaus n¨aher an die Biologie angelehntes Verfahren ﬁndet sich bei J. Liu et.
al. (2010), dessen Modell sich am auditorischen System im menschlichen Gehirn
orientiert [13]. Es werden spezielle K¨unstliche Neuronale Netze (KNN) genutzt,
um die Struktur im Gehirn nachzustellen. Dabei wird die Funktionsweise der Me-
dial superior olive (MSO) und der Lateral superior olive (LSO) zur Bestimmung
des ITD (MSO) und des ILD (LSO) herangezogen. Die Genauigkeit des Systems
ist jedoch ¨uber den gesamten Winkelbereich beim Nutzen nur einer Komponente,
entweder MSO oder LSO, relativ n¨uchtern. Es werden gerade mal 25% erreicht.
Bemerkenswert ist jedoch die Zunahme der Genauigkeit im gesamten System, wenn
die gewonnenen Daten aus MSO und LSO im Inferior Colliculus (IC) kombiniert
werden. Es werden damit Genauigkeiten von 80%, im Bereich von -45◦ bis 45◦
sogar 90%, erreicht. Es treten auch hier, trotz hoher Genauigkeit im Bereich von
0◦, erneut Schw¨achen im Bereich von 90◦ auf. Weiterhin ist das System aufgrund
der rechenintensiven Verfahren nicht Echtzeitf¨ahig.

Eine weitere M¨oglichkeit, Neuronale Netze einzusetzen, ist das Voraussagen
der Position der Ger¨auschquelle [16]. Einerseits kann es Rechenzeit sparen und
andererseits dem System einen gewissen Vorsprung verschaﬀen. Murray, Erwin
und Wermter setzten 2009 auf das oben erw¨ahnte Verfahren mithilfe von Cross
Correlation ein weiteres System auf, welches eine Vorherbestimmung der Position
mithilfe von Rekurrenten Neuronalen Netzen (RNN) erm¨oglicht. Dem Netz werden
dabei die Positionen der Ger¨auschquelle zum Zeitpuntk t0 und danach t1 vorge-
geben und das RNN bestimmt daraus die Position, an der die Soundquelle zum
Zeitpunkt t2 voraussichtlich sein m¨usste. Das RNN liefert dabei recht zuverl¨assige
Daten und bildet damit eine solide Grundlage zur Approximation der Position der
sich bewegenden Ger¨auschquellen.

13

Kapitel 3. Problemstellung und verwandte Arbeiten

3.2.3 Lokalisierung mittels Lookup Tables

Eine weitere Herangehensweise, die in dieser Arbeit betrachtet wird, beinhaltet
das Erstellen einer Lookup Table. Diese Verfahren erzeugen, bevor das System
tats¨achlich zum Einsatz kommt, eine Datenstruktur in der einfache und schnell
zu berechnende Features auf ein Ergebnis (meist die Position) abgebildet werden.
Um solch eine Datenstruktur herzustellen, m¨ussen jedoch eine Menge an Trai-
ningsdaten vorhanden sein und das System ben¨otigt eine gewisse Vorlaufzeit um
einsatzbereit zu sein.

Im Verfahren von Cho et. al. (2009) wird dabei der Raum um den Roboter
herum in kleine Bereiche aufgeteilt [2]. Nach dem Aufnehmen des Signals und der
Bestimmung des Time Delay of Arrival (TDOA) kann f¨ur jeden Bereich ein be-
stimmter Wert mithilfe SRP-PHAT bestimmt werden. Der Bereich, an dem der
Wert maximal ist, kann als Position der Ger¨auschquelle ausgegeben werden. Da
jedoch bei sehr starker Aufteilung des Raumes in kleine Bereiche unglaublich viele
Punkte entstehen, die durchsucht werden m¨ussten, beschreiben die Autoren ein
Verfahren, welches Punkte im Raum mit dem gleichen ITD zusammenfasst. Die
somit erzeugte Datenstruktur ist wesentlich schlanker und erm¨oglicht so die Echt-
zeitf¨ahigkeit. Das Verfahren bietet zudem einen hohen Grad der Genauigkeit. Es
werden in der horizontalen Ebene 93.9% und in der vertikalen Ebene bis zu 92.8%
Genauigkeit erreicht.

In einem weiteren Verfahren von Czyzewski (2003) wird mithilfe von verschiede-
nen Vorverarbeitungsmethoden ein regelbasiertes System erstellt [3]. Er beschreibt,
wie zun¨achst mithilfe von Subbandﬁltern einzelne Frequenzb¨ander extrahiert wer-
den. Diese werden mithilfe von Korrelationsanalysen bewertet und es wird mit den
gewonnenen Daten eine Regelbasis konstruiert. Die Ergebnisse zeigen bei einer gro-
ben Bestimmung der Richtung sehr hohe Genauigkeiten. Jedoch wird beim Vor-
handensein von St¨orger¨auschen die Genauigkeit selbst beim groben Bestimmen der
Richtung drastisch reduziert. Das System erreicht bei einer Signal-to-Noise-Ratio
(SNR) von 0 nur 52% bei -20 SNR nur ca. 70% Erfolg. Dies ist bei der groben
Unterteilung der Herkunft in 4 Bereiche ein schlechtes Ergebnis. Bei gr¨oßerer Dif-
ferenzierung der Richtung erreicht das System von 0◦ bis 20◦ in 5◦-Schritten jedoch
einen durchschnittliche Genauigkeit von 90%. Jedoch w¨are, f¨ur vergleichbare Da-
ten, ein Test am kompletten 360◦ Kreis notwendig.

Das Verfahren von Guentchev und Weng (1998) bildet ein klassisches Such-
verfahren [5]. Es werden aus einem mit 4 Mikrophonen aufgenommenen Ger¨ausch
sowohl die 6 Werte f¨ur ITD als auch f¨ur ILD extrahiert. So kommen 12 Werte zu-
sammen, die auf die bekannte Positionen im Raum abgebildet werden. Dabei wird
f¨ur die Positionsdarstellung, aufgrund der Empﬁndlichkeit der Entfernung, die Po-
larkoordinatendarstellung gew¨ahlt. Aus vielen solchen Beispielen wird mithilfe des
SHOSLIF-RPT Algorithmus ein Baum aufgebaut, der bei der Verwendung des Sys-

14

3.3. Methodik

tems genutzt wird. Es wird dabei sichergestellt, das die k ¨ahnlichsten Punkte zur
Eingabe, jeweils in einer Laufzeit von O(log(n)) bei n Eintr¨agen im Baum gefunden
werden. Das Verfahren liefert dabei gute Erfolge und weicht in der horizontalen
Ebene nur ca. ±2.2◦, in der vertikalen Ebene um ±2.8◦ ab. Nur die Entfernungs-
bestimmung liefert Fehler von durchschnittlich ±19%.

Da f¨ur die Roboter beim Bewegen zu einem Ort auch die Entfernung eine große
Rolle spielt, m¨ochte ich noch ein Verfahren vorstellen, welches sich haupts¨achlich
diesem Problem annimmt. Das Verfahren von Rodemann 2010 beschreibt dabei
das Extrahieren von sogenannten Audio Proto Objects [19]. Es handelt sich da-
bei um eine Zusammenstellung charakteristischer Features eines Ger¨ausches. So
werden z.B. ITD, ILD, das Spektrum, sowie die Amplitude mit einbezogen. Auch
die Kategorie, in die ein Audiosignal f¨allt, zeigt extreme Auswirkungen auf die
Genauigkeit der Entfernungsbestimmung. Das Verfahren ist dabei mit der Kom-
bination der eben aufgef¨uhrten Eigenschaften in der Lage, eine Genauigkeit von
77% bei der Entfernungsbestimmung zu erreichen. Das Verwechseln von nahen und
entfernten Ger¨auschen f¨allt dabei nur zu einem kleinen Teil des Gesamtfehlers ins
Gewicht. Die Verwechselung von nahen und fernen Ger¨auschen besitzt nur einen
Fehler von 0.12%. In einem normalen Raum sind bei Entfernungen bis zu 6 Metern
also realistische Entfernungsbestimmungen m¨oglich.

3.2.4 Ergebnisse

Die dargestellten Verfahren beschreiben verschiedenste Verarbeitungen der gesam-
melten Audiodaten. Alle Verfahren basieren in ihrer Grundidee jedoch auf dem
von Hartmann beschriebenen Zeit- bzw. Amplitudenunterschied. Einige Verfahren
extrahieren noch weitere Eigenschaften aus den gewonnenen Audiodaten, um die
Qualit¨at noch weiter zu steigern. Es sollte jedoch ¨uberlegt werden, wie weit die
Genauigkeit einer Lokalisation, f¨ur bestimmte Anwendungen bereits ausreicht und
wo noch explizite Verbesserungen n¨otig sind.

3.3 Methodik

Um im sp¨ateren Teil meiner Arbeit eine objektive Auswertung meiner Testergeb-
nisse zu erreichen, m¨ochte ich nun zun¨achst die Methoden vorstellen, die ich dazu
verwenden m¨ochte. Im Speziellen beschreibe ich, wie einerseits mein Verfahren zur
Korrelationsanalyse ¨uberpr¨uft und zum anderen die Ergebnisse der Neuronalen
Netze sinnvoll dargestellt werden k¨onnen.

3.3.1

¨Uberpr¨ufung der Korrelationsanalyse

F¨ur die ¨Uberpr¨ufung der Korrelationsanalyse ziehe ich zun¨achst eine Theorie aus
einem anderen Verfahren heran [16]. Dort wird der Winkel abh¨angig vom Oﬀ-
set der Korrelationsanalyse durch ein physikalisches Modell mit der Formel 3.1

15

Kapitel 3. Problemstellung und verwandte Arbeiten

bestimmt. Der Parameter cair beschreibt dabei die Schallgeschwindigkeit und be-
tr¨agt f¨ur 20 ◦C, 343 m
s . Θ beschreibt den Winkel der Ger¨auschquelle und ∆t den
Zeitunterschied zwischen zwei Abtastungen (Gleichung 2.6).

σ =

SinΘ · c
cair · ∆t

(3.1)

Die angegebene Formel bezieht sich jedoch auf Mikrophone, die durch keine weite-
ren Hindernisse, zwischen ihnen, gest¨ort werden. Es wird also angenommen, dass
der Schall sich ungehindert zwischen den beiden Mikrophonen ausbreiten kann.
Dies ist bei dem Nao jedoch aufgrund der Kopﬀorm nicht gegeben. Die Mikro-
phone (links und rechts) des Nao sind laut den technischen Daten 12 Zentimeter
voneinander entfernt. Der Schall muss jedoch noch den Kopf umrunden, was die
Strecke um einige Zentimeter verl¨angert.
In der Abbildung 3.1 ﬁndet sich daher der modellbeschriebene Verlauf des Oﬀsets
bei gegebenem Winkel und verschiedenen Abst¨anden der Mikrophone voneinan-
der. Die rote Linie markiert dabei den Abstand von 12 Zentimeter, die der Schall
aufgrund der technischen Daten mindestens zur¨ucklegen muss. Die blaue Linie
markiert einen Abstand von 22 Zentimetern, die als empirische Obergrenze dieser
Analyse festgelegt wurde. Die Farbe der Quadrate markiert den entsprechenden
Winkel.
Die Graﬁk zeigt weiterhin einen Verlauf von Datenpunkten und deren Mittel-
werten, die durch eine Korrelationsanalyse des linken und rechten Mikrophons
gewonnen wurden. Durch die Graﬁk l¨asst sich erkennen, das der Kurvenverlauf
des physikalischen Modells und der Korrelationsanalyse ¨ahnlich sind. Um diese
¨Ahnlichkeit auch statistisch zu st¨utzen, m¨ochte ich den mittleren quadratischen
Fehler und die Standardabweichung der Daten in Abh¨angigkeit vom simulierten
Mikrophonabstand betrachten. Dazu wurden der mittlere quadratische Fehler aller
Datenpunkte eines bestimmten Winkels, bez¨uglich zum Datenpunkt der entspre-
chenden Mikrophonentfernung, bestimmt. Die Ergebnisse dieser Analyse sind in
Abbildung 3.2 dargestellt. Dort ist auch die Standardabweichung vom mittleren
Fehler notiert. In dieser Graﬁk ist zu erkennen, das bei einem simulierten Abstand
der Mikrophone, mit c = 16 cm ein mittlerer Fehler von 1.8 auftritt. Im Mittel
weicht meine Korrelationsanalyse bei dem angenommenen Abstand der Mikropho-
ne nur 2 Sample ab. Allgemein ist der mittlere Fehler f¨ur die simulierten Werte
von ca. 12-19 cm gering und die genutzte Korrelationsanalyse liefert Ergebnisse,
die dem physikalischen Modell hinreichend nahe sind.

16

3.3. Methodik

Abbildung 3.1: Verlauf der Simulation und der Korrelationsanalyse

Abbildung 3.2: Mittlerer Fehler in Abh¨angigkeit des simulierten Mikrophonabstan-
des

17

Kapitel 3. Problemstellung und verwandte Arbeiten

3.3.2 Confusion Matrix

Die Qualit¨at des K¨unstlichen Neuronalen Netzes m¨ochte ich mithilfe einer Con-
fusion Matrix bestimmen [22]. Eine Confusion Matrix gibt bei einem gegebenem
Klassiﬁzierungsverfahren seine Qualit¨at an. Es handelt sich bei der Confusion Ma-
trix um eine 2-dimensionale Matrix, in der jeweils die Zeilen die tats¨achliche Klasse
eines Testdatums angeben und die Spalten die Klasse, in die es vom Klassiﬁzie-
rungsverfahren eingeordnet wurde. Da im Beispiel des Neuronalen Netzes jeder
Eingabewinkel vom System auch als Ausgabewinkel erkannt werden soll, eignet
sich die Confusion Matrix perfekt zum Analysieren dieser Aufgabe. Ein Beispiel
f¨ur solch eine Matrix ist in Abbildung 3.3 zu sehen.
Die Abbildung zeigt dabei ein m¨ogliches Ergebnis einer Confusion Matrix. Die

Abbildung 3.3: Beispielhafte Confusion Matrix

schwarzen Eintr¨age auf der Hauptdiagonalen sind richtige Klassiﬁzierungen. Dort
hat das Klassiﬁzierungsverfahren den korrekten Winkel ermittelt. Ein Beispiel f¨ur
eine extreme Fehlklassiﬁkation ist bei 180◦ zu erkennen. Dort wurde der Winkel
f¨alschlicherweise in die Klasse 60◦ eingeordnet.

Die Berechnung der G¨ute der Klassiﬁkation l¨asst sich anhand des Verh¨altnisses von
richtiger Klassiﬁkationen zur gesamten Datenmenge beschreiben. Alle Eintr¨age auf
der Hauptdiagonalen der Confusion Matrix sind korrekte Klassiﬁkationen. Alle an-
deren Eintr¨age sind fehlerhafte Klassiﬁkationen. Es wird also der Quotient aus den
Elementen auf der Hauptdiagonalen und allen Elemente in der gesamten Matrix
als G¨ute der Klassiﬁkation angegeben.
Weiterhin ließe sich in meinem speziellen Anwendungsfall auch noch eine weitere
Metrik f¨ur die G¨ute der Klassiﬁkationen einf¨uhren, da die Klassen direkte physika-

18

3.3. Methodik

lische Nachbarn am 360 Grad Kreis sind. Sollten sich zum Beispiel nur Elemente
auf der Haupt- und den beiden Nebendiagonalen der Matrix ﬁnden, so l¨asst sich
daraus ableiten, dass kein Datum weiter als eine Klasse zu weit links bzw. rechts
eingeordnet wurde.

19

Kapitel 3. Problemstellung und verwandte Arbeiten

20

Kapitel 4

Eigenes Verfahren

4.1 Theoretische ¨Uberlegungen

Bei der Betrachtung der bisherigen Verfahren sind an manchen Stellen einige Pro-
bleme aufgetreten. So ﬁnden sich an den Seitenbereichen, wo die Soundquelle
jeweils einen Winkel von ca. 90 Grad einnimmt, weitaus gr¨oßere Fehler, als um
0 Grad herum [16]. Weiterhin sind zwei Mikrophone in der horizontalen Ebene
nicht in der Lage, eine genaue Bestimmung der Position der Ger¨auschquelle zu
gew¨ahrleisten. Aufgrund der Front-Back-Konfusion sind stets zwei Punkte m¨oglich,
an denen sich eine Ger¨auschquelle beﬁnden kann.

Unter Hinzunahme eines zweiten Mikrophonpaars kann einerseits die Front-Back-
Confusion aufgel¨ost werden. Andererseits kann bei geeigneter Positionierung der
Mikrophonpaare zueinander eine h¨ohere Genauigkeit an den Seitenbereichen er-
reicht werden. Im Idealfall w¨are ein Mikrophonpaar zu verwenden, welches ortho-
gonal zu dem bisherigen Mikrophonpaar liegt. So w¨are der ungenaue Bereich des
einen Paares gleichzeitig der genaue Bereich des zweiten Paares.

4.2 Eigenes Verfahren

Meine Zielstellung ist es, mit dem Nao Roboter und 3 seiner 4 Mikro-
phone eine Ger¨auschquellenlokalisierung am vollen 360 Grad Kreis zu
realisieren. Das Verfahren besteht dabei aus mehreren Teilschritten:

1. Das Signal wird von den Mikrophonen des Naos aufgenommen und ¨uber

WLAN/LAN an einen leistungsst¨arkeren Rechner ¨ubertragen.

2. Dieser Rechner verarbeitet das Signal in mehreren Schritten.

3. Zun¨achst wird mithilfe eines Energiewertverfahrens entschieden, ob das Si-

gnal zur Weiterverarbeitung geeignet erscheint.

21

Kapitel 4. Eigenes Verfahren

4. Anschließend wird optional das Rauschen mit einem einfachen Verfahren

reduziert.

5. Darauf folgend wird die Cross Correlation von zwei Mikrophonpaaren be-

stimmt und in ein trainiertes Neuronales Netz gegeben.

6. Dieses ermittelt dann den Winkel, an dem sich die Ger¨auschquelle beﬁndet.

7. Die Eﬀektoren des Roboters drehen dann den Kopf in die entsprechenden
Richtung bzw. der Roboter teilt auf andere Weise den bestimmten Winkel
mit.

4.3 Aufnahme und Transfer

Die Berechnungen werden aufgrund der schwachen Leistung, nicht direkt auf dem
Roboter durchgef¨uhrt. Die Aufnahme eines Audiosamples erfolgt jedoch auf dem
Roboter mithilfe eines einfachen Python-Skriptes (Quellcode 4.1). Die vom Her-
steller zu Verf¨ugung gestellte Basissoftware erlaubt das Aufnehmen einer 4 Kanal-
Wavedatei mit einer Abtastrate von bis zu 48 kHz. Dabei unterliegt der Kanal 4
jedoch stets dem Einﬂuss des L¨ufters, der ein starkes St¨orrauschen verursacht. In
Abbildung 2.2 l¨asst sich dicht neben dem hinteren Mikrophon die L¨ufter¨oﬀnung
erkennen. Dadurch ist der Kanal 4 in der Regel nicht f¨ur eine Analyse geeignet.
Die aufgenommene Datei wird im /tmp Verzeichnis des Roboters abgelegt. Mithilfe
einer ssh-Verbindung kann dann mittels scp die aufgenommene Datei auf einen leis-
tungsst¨arkeren Rechner ¨ubertragen werden, auf dem die eigentliche Berechnungen
ausgef¨uhrt werden (Quellcode 4.2).

d e f

1
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

i n t e r v a l ) :

r e c o r d S a m p l e ( s e l f , naopath ,
”””
T h i s method t e l l s
put
”””
#T e l l
s e l f . m i c r o p h o n e P r o x y . s t a r t M i c r o p h o n e s R e c o r d i n g ( naopath + ’ s a m p l e ’ + s t r ( s e l f . ID CODE)

t o r e c o r d a sound s a m p l e o f a g i v e n l e n g t h and

i n t o t h e /tmp d i r e c t o r y on t h e r o b o t ’ s

t h e m i c r o p h o n e s t o b e g i n t h e r e c o r d i n g

t h e r o b o t

s y s t e m

f i l e

i t

+ ’ . wav ’ )

t h e s o u n d s a m p l e i s b e e i n g r e c o r d e d

l o n g a s

#S l e e p t h e t h r e a d a s
t i m e . s l e e p ( i n t e r v a l )
#Stop t h e r e c o r d i n g on t h e r o b o t
s e l f . m i c r o p h o n e P r o x y . s t o p M i c r o p h o n e s R e c o r d i n g ( )
#Return t h e ID CODE o f
r e t u r n s e l f . b o u n d C y c l i n g P a r a m e t e r s ( )

t h e r e c o r d e d s a m p l e and go one ID CODE f u r t h e r

Quellcode 4.1: Aufnahme

22

1
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
23

4.4. Vorverarbeitung

d e f

i n i t

( s e l f , NAO IP , USER, PASSWD) :

””” T h i s method s e t s up t h e s c p t r a n s f e r o b j e c t s ”””

#C r e a t e t h e s s h c o n n e c t i o n t o t h e r o b o t
t r a n s p o r t = paramiko . T r a n s p o r t ( ( NAO IP , 2 2 ) )

#Connect t o i t w i t h a username and p a s s w o r d
t r a n s p o r t . c o n n e c t ( username=USER, p a s s w o r d=PASSWD)

#B u i l d t h e SFTP O b j e c t
s e l f . s f t p = paramiko . SFTPClient . f r o m t r a n s p o r t ( t r a n s p o r t )

from t h e r o b o t

t o g e t

f i l e s

d e f

t r a n s f e r S a m p l e ( s e l f ,
””” T h i s method t r a n s p o r t s

i d c o d e , naopath ,

l o c a l p a t h ) :

t h e r e c o r d e d f i l e

t o t h e l o c a l

f i l e

s y s t e m ”””

#D e t e r m i n e t h e f i l e n a m e on t h e nao f i l e
f i l e n a m e = ’ s a m p l e ’ + s t r ( i d c o d e ) + ’ . wav ’

s y s t e m a s w e l l a s on t h e t a r g e t

f i l e n a m e

#T r a n s p o r t
t h e f i l e n a m e
s e l f . s f t p . g e t ( naopath + f i l e n a m e ,

l o c a l p a t h + f i l e n a m e )

#P r i n t i n g a Message o f
p r i n t ” T r a n s p o r t e d : nao : ” + naopath + f i l e n a m e + ” > l o c a l : ” + l o c a l p a t h + f i l e n a m e

t h e T r a n s p o r t a t i o n on t h e C o n s o l e

Quellcode 4.2: Transfer

4.4 Vorverarbeitung

4.4.1 Energiewertbestimmung

Um eine gute Unterscheidung zwischen gew¨unschten und unerw¨unschten Signa-
len zu erreichen wird in meinem Verfahren eine Energiefunktion genutzt [16]. Der
Energiegehalt (cid:15) wird bei jeder Aufnahme bestimmt und gibt dabei ein Maß f¨ur den
Anteil von menschlicher Stimme in der Aufnahme an. Die Quadrate der Ampli-
tudenwerte des Signals werden ¨uber die Zeit aufsummiert. Anschließend wird der
aufsummierte Wert durch die Anzahl der Samples geteilt, um einen von der L¨ange
der Aufnahme unabh¨angigen Wert zu erhalten (Gleichung 4.1).

(cid:15) =

(cid:80)n

i=0 [yi]2
n

(4.1)

Im Beispielsample aus Kennedys Rede (Abbildung 5.2) erkennt man ein gewisses
Grundrauschen. Aufgrund des Energiegehalts dieses Grundrauschens l¨asst sich ei-
ne Entscheidungsgrenze f¨ur das Verwenden des Signals bestimmen. Da in jeder
Umgebung gewisse St¨orquellen (Computerl¨ufter, Summen von Aggregaten, usw.)
zu ﬁnden sind, wird bei meinem Verfahren zu Beginn eine Kalibrierung vorgenom-
men, indem der Roboter eine bestimmte Zeit lang die Stille aufnimmt, um daraus
eine Grundlinie zu berechnen. Die Berechnung der Energie in der Software l¨asst
sich im Quellcode 4.3 einsehen.

23

Kapitel 4. Eigenes Verfahren

d e f

1 c l a s s Energy ( ) :
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
23
24
25
26
27
28
29

d e f

””” T h i s C l a s s

i s a b l e t o e s t i m a t e t h e Energy o f a Sample ”””

t h r e s h o l d ) :

i n i t

frame ,
( s e l f ,
# Save t h e f r a m e d a t a
s e l f . f r a m e = f r a m e
# Save t h e g i v e n t h r e s h o l d
s e l f . t h r e a s h o l d = t h r e s h o l d
# S e t
s e l f . a c t i v a t i o n = F a l s e
# S e t
s e l f . e n e r g y = 0
# C a l l
s e l f .

t h e Energy t o z e r o

t h e a c t i v a t i o n t o f a l s e

t h e method t o c a l c u l a t e Energy
c a l c u l a t e E n e r g y ( )

t h e Sample ”””
t h e s a m p l e

c a l c u l a t e E n e r g y ( s e l f ) :
””” T h i s Method c a l c u l a t e s
t h e Energy o f
# E s t i m a t e minimum and maximum v a l u e s o f
s e l f . minimum = min ( s e l f . f r a m e )
s e l f . maximum = max ( s e l f . f r a m e )
# C a l c u l a t e t h e s q u a r e d sum o v e r a l l
f o r

i n r a n g e ( l e n ( s e l f . f r a m e ) ) :

i
s e l f . e n e r g y += ( s e l f . f r a m e [ i ] ∗ s e l f . f r a m e [ i ] )

s a m p l e s

# N o r m a l i z e i t by d i v i d i n g i t
s e l f . e n e r g y = s e l f . e n e r g y / l e n ( s e l f . f r a m e )
# Check i f
i f

t h e e n e r g y i s above t h e t h r e s h o l d

( s e l f . e n e r g y > s e l f . t h r e a s h o l d ) :
# I f
s e l f . a c t i v a t i o n = True

t h e a c t i v a t i o n t o t r u e

s o s e t

t h r o u g h t h e l e n g t h o f

t h e s a m p l e

Quellcode 4.3: Energieberechnung

4.4.2 Rauschreduzierung

Nachdem die Energieanalyse eines Ger¨auschs entschieden hat, dass dieses weiter
genutzt werden soll, kann das Rauschen mithilfe von Spectral Substraction redu-
ziert werden. Diese Vorverarbeitung wurde bei meinen Versuchen jedoch als starke
Fehlerquelle identiﬁziert. Bei dem Verfahren handelt es sich im Wesentlichen um
eine Implementierung des von S. Boll beschriebenen Ansatzes [1]. Eine Aufnah-
me, die lediglich Rauschen enth¨alt, wird in einzelne Bl¨ocke unterteilt. Von jedem
Block wird das Spektrum mithilfe der Fouriertransformation bestimmt und ein
Mittelwert ¨uber alle Bl¨ocke gebildet. Anschließend wird das so gebildete Spektrum
vom Spektrum jedes anschließend aufgenommenen Ger¨ausches subtrahiert. Durch
die inverse Fouriertransformation wird das so gebildete Spektrum wieder in den
Amplitudenverlauf ¨uber die Zeit umgewandelt.

4.5 General Cross Correlation

Sobald die Vorverarbeitung erfolgt und die Aufnahme zur Weiterverarbeitung ge-
eignet ist, wird mit der Korrelationsanalyse begonnen (Quellcode 4.4). Dazu muss
jedoch noch ein Interval festgelegt werden, in dem der zweite Kanal gegen¨uber dem
ersten verschoben werden soll. Auf Grundlage der Gleichung 2.5 wissen wir, wie
viel Zeit zwischen zwei Samples vergeht. Weiterhin kennen wir die Positionen der
Mikrophone und k¨onnen den Kopf des Roboters als Sph¨are annehmen. Mithilfe
dieser Informationen l¨asst sich die maximale Zeit bestimmen, die die Schallwellen
von einem zum anderen Mikrophon ben¨otigen. Um ein wenig Spielraum zu besit-
zen wurde der Oﬀset um den verschoben werden soll auf 30 Sample festgelegt. Dies
erm¨oglicht einen maximalen bestimmbaren Zeitunterschied von 684.9 µs.

24

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
23
24
25
26
27

28

4.6. K¨unstliches Neuronales Netz

Die Correlation wird dabei zwischen den Mikrophonen Front-Left und Front-Right
bestimmt. Wie oben beschrieben ist aufgrund der Architektur des Naos eine solide
Nutzung des hinteren Mikrophons aufgrund der in der N¨ahe liegenden Bauteile
nicht m¨oglich. Die aus den verbleibenden Mikrophonpaaren gewonnenen Daten
werden in das n¨achste System eingegeben.

””” A C l a s s

1 c l a s s C o r r e l a t i o n A n a l y s i s ( ) :
2
3
4
5
6

s e l f . o f f s e t = abweichung
s e l f . v e c t o r 1 = [ 0 f o r

i n i t

d e f

i

( s e l f , v e c t 1 , v e c t 2 , abweichung ) :

t o c a l c u l a t e t h e C r o s s C o r r e l a t i o n between two V e c t o r s ”””

]

s e l f . v e c t o r 2 = [ 0 f o r

i

i n x r a n g e ( abweic hun g ) ] + v e c t 2 + [ 0 f o r

]

i n x r a n g e ( abweic hun g ) ] + v e c t 1 + [ 0 f o r

i

i

i n x r a n g e ( abweichung )

i n x r a n g e ( abweichung )

s e l f . v e c t o r 1 = s e l f . n o r m a l i z e V e c t o r ( s e l f . v e c t o r 1 )
s e l f . v e c t o r 2 = s e l f . n o r m a l i z e V e c t o r ( s e l f . v e c t o r 2 )

s e l f . c o r r e l a t i o n = s e l f . g e n e r a t e C o r r e l a t i o n V e c t o r ( )

d e f g e n e r a t e C o r r e l a t i o n V e c t o r ( s e l f ) :

””” T h i s Method g e n e r a t e s
r e t u r n s e l f . c o r r e l a t e ( )

d e f c o r r e l a t e ( s e l f ) :

t h e C o r r e l a t i o n V e c t o r b a s e d on a g i v e n method ”””

””” T h i s method u s e s

t h e b u i l d i n S c i P y t o o l s but makes t h e CC o n l y o v e r

t h e

i n t e r e s t i n g e l e m e n t s ”””
s e l f . v e c t o r 2 = deque ( s e l f . v e c t o r 2 )
s e l f . v e c t o r 2 . r o t a t e (− s e l f . o f f s e t −1)
v = [ ]
f o r

i n x r a n g e ( 0 , s e l f . o f f s e t ∗2+1) :

i
s e l f . v e c t o r 2 . r o t a t e ( 1 )
v . append ( l i s t ( S . c o r r e l a t e ( np . a r r a y ( s e l f . v e c t o r 1 ) , np . a r r a y ( s e l f . v e c t o r 2 ) , mode = ’

v a l i d ’ ) ) [ 0 ] )

r e t u r n v

Quellcode 4.4: Cross Correlation

4.6 K¨unstliches Neuronales Netz

Nachdem die Correlationsanalyse die beiden Werte f¨ur die Interaural Time Dif-
ference ermittelt hat, k¨onnen diese dem K¨unstlichen Neuronalen Netz pr¨asentiert
werden. Bei dem zugrunde liegenden Neuronalen Netz handelt es sich um ein Feed-
forward Netz, welches die Eingabe (ITD) auf eine entsprechende Ausgabe (Winkel
in der Horizontalen der Ger¨auschquelle) abbildet. Bei der Wahl der Anzahl der
Eingabeneuronen und der Anzahl der Ausgabeneuronen sind wenig Variationen
m¨oglich. Wir ben¨otigen zwei Eingabeneuronen um jeweils einen ITD Wert in das
Neuronale Netz zu speisen. Weiterhin ben¨otigen wir 24 Ausgabeneuronen, da wir
24 verschiedene Positionen an dem sich die Ger¨auschquelle beﬁnden kann, unter-
scheiden wollen. Interessant wird es bei der Wahl der Anzahl der Neuronen in der
versteckten Schicht. Die dort gew¨ahlte Anzahl an Neuronen kann einen großen
Einﬂuss auf das Verfahren haben (vlg. [20]).
Ich werde daher in meinem Versuch verschiedene Werte f¨ur die Anzahl von ver-
steckten Neuronen verwenden und deren Ergebnisse betrachten. Grundlegend kann
jedoch folgende Argumentation zur Wahl der Anzahl der Neuronen in der versteck-
ten Schicht herangezogen werden:
In Abbildung 4.1 sieht man eine Beispielverteilung der von beiden Mikrophonpaa-
ren ermittelten ITDs im 2-dimensionalem Raum.

25

Kapitel 4. Eigenes Verfahren

Abbildung 4.1: Entscheidungsgrenzen durch versteckte Neuronen

Jede Farbe repr¨asentiert dabei eine andere Position, an der sich die Ger¨ausch-
quelle beﬁndet. Jedes versteckte Neuron ist nun in der Lage, mit einer geraden
Linie den Raum in zwei Klassen einzuteilen. Die beiden Neuronen in der Graﬁk
unterteilen den Raum in 4 verschiedene Bereiche. Wenn man davon ausgeht, dass
die Geraden stets durch den Ursprung verlaufen, lassen sich mithilfe von m ver-
steckten Neuronen genau 2 · m Klassen unterscheiden. Um das Neuronale Netz
beim Lernen ﬂexibler zu halten, wird jedoch ein Biasneuron hinzugef¨ugt, wodurch
die Linien nun nicht mehr durch den Ursprung laufen m¨ussen. Das Neuronale Netz
muss zwischen 24 verschiedenen ITD-Paaren unterscheiden. Eine Abgrenzung zu
allen anderen Klassen erfolgt dabei mit zwei Geraden. Es werden also 48 versteckte
Neuronen als Richtwert genutzt.

Das Training des Neuronalen Netzes erfolgt mit dem einfachen Backpropagation
Trainingsalgorithmus. Die ITD Paare werden jeweils in eine Trainingsmenge und
eine Testmenge aufgeteilt. Das Verh¨altnis zwischen Trainings- und Testmenge wird
dabei ungef¨ahr bei 60:40 liegen [14].

26

4.7. Eﬀektoren

4.7 Eﬀektoren

Sobald das Neuronale Netz bestimmt hat, wo sich die Ger¨auschquelle beﬁndet,
wird die Position der Ger¨auschquelle dem Benutzer zun¨achst sprachlich mitgeteilt.
Eine Bewegung des Kopfes in die entsprechende Richtung ist auch m¨oglich. Dazu
werden die vom Hersteller mitgelieferte Bewegungsfunktionen genutzt.

27

Kapitel 4. Eigenes Verfahren

28

Kapitel 5

Experiment

Um das Verfahren zu testen und seine Richtigkeit zu veriﬁzieren wurden zwei
zeitlich und r¨aumlich unterschiedliche Versuchsreihen betrachtet. Die Versuchs-
durchf¨uhrung bestand dabei aus dem Sammeln von Audiodaten an einem 360◦
Kreis, der im Abstand von 15◦ Markierungen aufwies. Der Roboter wurde in die
Mitte dieses Kreises - mit einem Radius von 1 Meter - aufgestellt. Das vordere
Mikrophon war in Richtung 0◦ ausgerichtet. Der im folgenden verwendete Winkel
bezieht sich immer auf diese 0◦-Position und steigt bei der Draufsicht auf den Ro-
boter mit dem Uhrzeigersinn. In Abbildung 5.1 ﬁndet sich ein Foto des zweiten
experimentellen Aufbaus. Bei dem Raum, in dem beide Experimente durchgef¨uhrt
wurden, handelte es sich um einen simuliertes Wohnzimmer (engl. Homelab) in
dem L¨ufterrauschen und leise Nebenger¨ausche von anderen arbeitenden Studenten
zugegen waren. Aus den aufgenommenen Daten wurden die ITD Paare extrahiert.
Diese wurden anschließend dreimal in je Trainingsdaten- und Testdaten aufgeteilt,
sodass f¨ur jedes Training drei unterschiedlich zuf¨allig gew¨ahlten Teilmengen aus
der gesamten Datenmenge verwendet werden konnten.

Abbildung 5.1: Experimenteller Aufbau

29

Kapitel 5. Experiment

5.1 Erster Test

Der erste Test wird mit dem Vorspielen, einer einfachen Audiodatei umgesetzt. Es
handelt sich bei der Aufnahme um den Anfang der Rede von John F. Kennedy zum
bevorstehenden Raumfahrtprogramm an der Rice University in Houston, Texas
am 12. September 1962 [10]. In Abbildung 5.2 ist dazu der Amplitudenverlauf, der
Aufnahme abgebildet, die verwendet wurde. Die Datei war im MP3 Format mit
64 Kbps. Die markierten Teile der Rede wurden f¨ur die Extraktion der ITD Paare
genutzt.

Abbildung 5.2: Rede: ”We choose to go to the moon.”

Dieser kurze Ausschnitt seiner Rede wurde aus 24 verschiedenen Richtungen im
Abstand von jeweils 15◦ rund um den Roboter herum aufgenommen. Aus diesen
Daten wurden f¨ur die signiﬁkanten Bereiche (siehe 5.2) jeweils die ITD Paare be-
stimmt. Die schattierten Abschnitte 2 und 3 wurden bei der Extraktion aufgrund
ihrer L¨ange jeweils in zwei Bereiche aufgeteilt. Es liegen somit f¨ur jede Richtung
7 ITD Paare vor. Diese wurden anschließend jeweils dreimal in eine Trainings-
und eine Testmenge zerlegt. Die Trainingsmenge umfasste dabei 4 ITD Paare, die
Testmenge 3. In Abbildung 5.3 ist die gesamte Datenmenge vor der Aufteilung in
Trainings- und Testdaten abgebildet. Die Farbe der Datenpunkte gibt dabei den
Winkel an, dem die extrahierten ITD Paare angeh¨oren. Mithilfe der generierten
Trainingsdaten (96 ITD Paare) wurde verschiedene Neuronale Netze trainiert, die
sich durch ihre interne Struktur unterschieden. Zu Beginn lag die verwendete Lern-
rate bei 0.9, um eine schnelle und grobe Anpassung an die Daten zu erm¨oglichen.
Das Netz wurde dann in 20 Zyklen je 1200 mal mit jeweils einem zuf¨allig gew¨ahl-
tem Datum der Trainingsmenge trainiert. Nach jedem Zyklus wurde die Lernrate
um 0.0125 gesenkt, um eine feinere Anpassung des Neuronalen Netzes zu gew¨ahr-
leisten. Die Wahl der Lernrate zu Beginn und der Anzahl der Zyklen wurde aus
empirischen Gr¨unden gew¨ahlt.

Nachdem alle Trainingsdurchl¨aufe abgeschlossen waren, wurde mithilfe der Testda-
ten und einer Confusion Matrix die G¨ute des Neuronalen Netzes bestimmt. Diese
Vorgehensweise erfolgte f¨ur alle drei Teilmengen aus dem gesamten Datensatz. Die
anschließend gewonnenen Ergebnisse wurden gemittelt. In Abbildung 5.4 ﬁndet

30

sich jeweils die Anzahl der Neuronen in der versteckten Schicht, die durchschnitt-
liche Erfolgsquote ¨uber drei Testl¨aufe und die empirische Laufzeit1.

5.1. Erster Test

Abbildung 5.3: Extraktion - Kennedy

(a) Erfolg der Neuronalen Netze

(b) Trainingsdauer der Neuronalen Netze

Abbildung 5.4: Ergebnisse - Datenmenge Kennedy

1Die Empirische Laufzeit wurde durch die Zeit bestimmt, die das Training des Neuronalen
Netzes in Anspruch nahm. Dabei wurde jedes Training auf einem Lenovo K320-i7 durchgef¨uhrt.
Die technischen Daten dazu ﬁnden sich im Anhang.

31

Kapitel 5. Experiment

In Abbildung 5.5 sind die Confusion Matrizen der Neuronalen Netze mit 6, 48
und 78 Neuronen in der versteckten Schicht dargestellt. Es wurden gerade diese
Matrizen gew¨ahlt da sie als Repr¨asentant f¨ur wenig, mittel und viele versteckte
Neuronen in dieser Versuchsreihe auftauchen.

(a) 6 versteckte Neuronen

(b) 48 versteckte Neuronen

(c) 78 versteckte Neuronen

Abbildung 5.5: Confusion Matrizen - Kennedy

32

5.2. Versuch mit einfachen Wortensequenzen

5.2 Versuch mit einfachen Wortensequenzen

In der n¨achsten Versuchsreihe wurde das Neuronale Netz mit wesentlich mehr
Daten trainiert. Es wurden daf¨ur die Worte Hello, Fish, Look Here, Coﬀee und
Tea aufgenommen. Es ergaben sich aus den Aufzeichnungen nach der Extrakti-
on insgesamt 26 Datenpaare (Abbildung 5.6). Diese Daten wurden erneut 3 mal
zuf¨allig in Trainingsdaten (16 Elemente) und Testdaten (10 Elemente) aufgeteilt.
Anschließend wurden erneut verschiedene Neuronale Netze trainiert. Diesmal wur-
den insgesamt 32 Zyklen verwendet - ansonsten unterscheidet sich das Vorgehen
jedoch nicht zum zuvor beschriebenen. Mittels einer Confusion Matrix wurden er-
neut die Neuronalen Netze in ihrer G¨ute eingeordnet. Die Ergebnisse ﬁnden sich
in Abbildung 5.7. In Abbildung 5.8 sind die Confusion Matrizen der jeweiligen
Neuronalen Netze dargestellt.

Abbildung 5.6: Extraktion - Wortsequenzen

33

Kapitel 5. Experiment

(a) Erfolg der Neuronalen Netze

(b) Trainingsdauer der Neuronalen Netze

Abbildung 5.7: Ergebnisse - Datenmenge Wortsequenzen

5.3 Vorverarbeitung mit Rauschreduzierung

Zuletzt wurde mittels einem einfachen Verfahren zur Rauchunterdr¨uckung der Ver-
such unternommen, die Qualit¨at des Verfahrens noch zu verbessern. Das Trainieren
des Neuronalen Netzes wurde jedoch nach der Betrachtung der extrahierten Da-
ten fallen gelassen, da sich die generierten ITD Paare ersichtlicherweise nicht zur
weiteren Nutzung eigneten. Abbildung 5.9 zeigt die dabei extrahierten Daten bei
zuvor erfolgtem reduzieren des Rauschens.

Abbildung 5.9: Noisy Words Extraction

34

(a) 6 versteckte Neuronen

(b) 48 versteckte Neuronen

(c) 78 versteckte Neuronen

Abbildung 5.8: Confusion Matrizen - Wortsequenzen

Kapitel 5. Experiment

5.4 Zusammenfassung

Mein Verfahren wurde zweimal mit verschiedenen Daten getestet. Dabei hat sich
gezeigt, dass die Lokalisation bei wenigen Neuronen in der versteckten Schicht nicht
zuverl¨assig funktioniert. Auﬀallend ist jedoch der Anstieg der Erfolgsquote, sobald
die Anzahl der versteckten Neuronen steigt. Gleichzeitig bedarf es f¨ur das Trai-
ning mit zunehmender Zahl an Neuronen eine l¨angere Trainingszeit. Es muss also
ein gutes Mittelmaß zwischen der Trainingsdauer und der Erfolgsquote gefunden
werden. Die Versuche das Verfahren noch zu verbessern, indem eine Rauschredu-
zierung angewandt wurde hat sich als nicht tragbar erwiesen. Dies liegt daran, dass
die Methode zur Rauschreduktion auch den Informationsgehalt des Sprachsignals
vermindert. Dadurch ist eine stabile Bestimmung der Cross Correlation nicht mehr
m¨oglich.

36

Kapitel 6

Fazit

Die Problemstellung dieser Arbeit bestand darin, zu untersuchen wie ein humanoi-
der Roboter eine Ger¨auschquelle lokalisieren kann. Der vorgestellte Ansatz ermit-
telt dabei zun¨achst die Interaural Time Diﬀerence mithilfe von Cross Correlation.
Anschließend wurde die Ger¨auschquellenposition mit einem trainierten K¨unstli-
chen Neuronalen Netz berechnet.
Die experimentellen Ergebnisse zeigen eine gute Erfolgsquote f¨ur das vorgestell-
te Verfahren. Die zuvor aufgestellten Bedingungen werden durch das Experiment
best¨atigt. Der Roboter ist in der Lage eine Lokalisation der Ger¨auschquellen am
vollen 360 Grad Kreis vorzunehmen und somit auch zuverl¨assig die Front-Back-
Confusion aufzul¨osen. Die Erfolgsquote der Klassiﬁkation ist, wie die Experimente
gezeigt haben, dabei von der Anzahl der Neuronen in der versteckten Schicht des
Netzes abh¨angig.
Probleme traten hingegen besonders bei der Vorverarbeitung - dem Reduzieren
von Rauschen - auf. Auch ist die Qualit¨at der Mikrophone des Roboters eher als
gering einzustufen. Ger¨ausche, die weiter als ca. 1 Meter von den Mikrophonen
entfernt sind, sind nur noch schwach zu vernehmen.

Eine Verbesserungsm¨oglichkeit w¨are es, die Cross Correlation mit einem geeigneten
Verfahren zu beschleunigen. Da eine Reihe von Vektoren auf ¨Ahnlichkeit gepr¨uft
werden, ist eine Parallelisierung der Berechnung ein m¨oglicher Ansatz.
Das Neuronale Netz bietet weiterhin eine schnelle Adaption auf eine neue Umge-
bung. Es werden daf¨ur jedoch erneut Trainingsdaten ben¨otigt. Ein Verfahren, das
neben der Nutzung weitere verl¨assliche Trainingsdaten sammeln w¨urde, w¨are eine
sinnvolle Weiterentwicklung meines Ansatzes. So w¨are der Roboter problemlos in
der Lage, sich auf neue ihm unbekannte Lokalit¨aten einzustellen.
Auch eine Datenbasis von unterschiedlichen Neuronalen Netzen f¨ur unterschiedli-
che Situationen und Orte w¨are eine m¨ogliche Anpassung, um eine h¨ohere Genau-
igkeit, gerade in gr¨oßeren Geb¨audekomplexen zu erreichen.

Letztendlich zeigt die Kombination von Korrelationsanalyse und der anschießenden
Winkelbestimmung mithilfe von Neuronalen Netzen einen sinnvollen und hinrei-
chend guten Ansatz f¨ur den Einsatz auf einem humanoidem Roboter.

37

Kapitel 6. Fazit

38

Anhang A. Technische Daten

Desktop Computer
Lenovo IdeaCentre K320
Serial - ES06527419

Operating System
Linux 2.6.38-12-generic #51-Ubuntu SMP Wed Sep 28 14:27:32 UTC 2011
x86 64 x86 64 x86 64 GNU/Linux

CPU
Intel(R) Core(TM) i7 CPU 870 @ 2.93GHz

Size
Capacity
Width
Clock
Cores
Enabledcores
Threads
L1 Cache
L2 Cache
L3 Cache

1197MHz
2930MHz
64 bits
533MHz
4
4
2
32KiB
256 KiB
8MiB

RAM

Slot 1 - 2GiB DIMM DDR3 Synchronous 1066 MHz (0.9 ns) 64 bits
Slot 2 - 2GiB DIMM DDR3 Synchronous 1066 MHz (0.9 ns) 64 bits
Slot 3 - 2GiB DIMM DDR3 Synchronous 1066 MHz (0.9 ns) 64 bits
Slot 4 - empty

39

Anhang A. Technische Daten

40

 DATASHEETNAOH25 is a trusted platform for education and research in various topics, from robotics and computer science to autism and human-robot interaction. NAOH25 is ALDEBARAN Robotics’ most advanced robot. This fully-featured humanoid robot provides an open platform with full integra-tion of state-of-the-art hardware and softwares. NAOH25 is robust, interactive and easy to use allowing you to focus on your core research.GENERAL FEATURESBODY CARACTERISTICSHEIGHT: ~58 CM - 22.8’’WEIGHT: ~5 KG - 11LBBODY MATERIAL: ABS - PCENERGYCHARGER: AC 90-230 volts / DC 24 voltsBATTERY CAPACITY: ~90 min. autonomyDEGREES OF FREEDOMHEAD: 2 DOFARM: 4 DOF in each armPELVIS: 1 DOFLEG: 5 DOF in each legHAND: 2 DOF in each handMULTIMEDIASPEAKERS: 2 LoudspeakersMICROPHONES: 4 MicrophonesVISION: 2 CMOS Digital CamerasNETWORK ACCESSCONNECTION TYPE:● WI-FI (IEE 802.11 b/g)● Ethernet ConnectionACTUATORSALDEBARAN ROBOTICS TMORIGINAL DESIGN BASED ON:● Hall effect sensors● dsPICS microcontrollersLEDSENSORS● 36 x Hall effect sensors● 2 x gyrometer 1 axis● 1 x accelerometer 3 axis● 2 x bumpers● 2 x sonar channels● 2 x I/R● Tactile sensors (head, hands)● 8 x FSRsTACTILE SENSOR: 12 LEDs 16 Blue levelsEYES: 2 x 8 LEDs RGB FullcolourEARS: 2 x 10 LEDs 16 Blue levelsTORSO: 1 LED RGB FullcolourFEET: 2 X 1 LED RGB FullcolourMOTHERBOARD● x86 AMD GEODE 500MHz CPU● 256MB SDRAM / 2GB Flash MemorySOFTWARE COMPATIBILITIESOS: Embedded Linux (32bit x 86 ELF) using custom OpenEmbedded based distributionPROGRAMMING LANGUAGES:C++, Urbi script, Python, .NetAll specifications are not contractual and are subject to change.www.aldebaran-robotics.comAnhang B. Nao Speziﬁkation

42

Literaturverzeichnis

[1] S. F. Boll. Suppression of acoustic noise in speech using spectral subtraction.
Acoustics, Speech and Signal Processing, IEEE Transactions on, 27(2):113–
120, 1979.

[2] Y. Cho, D. Yook, S. Chang, and H. Kim. Sound source localization for ro-
bot auditory systems. Transactions on Consumer Electronics, IEEE, 55(3),
August 2009.

[3] A. Czyzewski. Automatic identiﬁcation of sound source position employing
neural networks and rough sets. Pattern Recognition Letters, 24(6):921–933,
March 2003.

[4] D. Gouaillier, V. Hugel, P. Blazevic, C. Kilner, J. Monceaux, P. Lafourcade,
B. Marnier, J. Serre, and B. Maisonnier. Mechatronic design of nao humanoid.
Proceedings of the IEEE International Conference on Robotics and Automa-
tion, 2009.

[5] K. Y. Guentchev and J. J. Weng. Learning-based three dimensional sound
In AAAI

localization using a compact non-coplanar array of microphones.
SYMPOSIUM ON INTELLIGENT ENVIRONMENTS, 1998.

[6] J. Key C. Schauer C. Schr¨oter H. Gross T. Hempel H. B¨ohme, T. Wilhelm.
An approach to multi-modal human-machine interaction for intelligent service
robots. Robotics and Autonomous Systems, 44(1):83–96, 2003.

[7] W. M. Hartmann. How we localize sound. Physics Today, 52(11):24–29,

November 1999.

[8] P. Stoica J. Li. Robust Adaptive Beamforming. John Wiley & Sons, Inc., 2005.

[9] L. A. Jeﬀress. A place theory of sound localization. Journal of comparative

and physiological psychology, 41:35–39, 1948.

[10] John F. Kennedy.

jfk 1962 0912 spaceeﬀort 64kb.mp3. Presidential Library, 9 1962.
Access 28.11.2011 12:58.

http://www.archive.org/download/jfks19620912/
Last

43

Literaturverzeichnis

[11] S. Lee, S. Hwang, Y. Park, and Y. Park. Sound source localization in median
plane using artiﬁcial ear. International Conference on Control, Automation
and Systems, 2008.

[12] H. Liu and M. Shen. Continuous sound source localization based on micropho-
ne array for mobile robots. In International Conference on Intelligent Robots
and Systems (IROS), 2010 IEEE/RSJ, 2010.

[13] J. Liu, D. Perez-Gonzalez, A. Rees, H. Erwin, and S. Wermter. A biologically
inspired spiking neural network model of the auditory midbrain for sound
source localisation. Neurocomputing, 74:129–139, December 2010.

[14] S. Marsland. Machine learning: an algorithmic perspective. Chapman & Hall/-
CRC machine learning & pattern recognition series. CRC Press, 2009.

[15] R. Martin, U. Heute, and C. Antweiler. Advances in Digital Speech Transmis-

sion. John Wiley & Sons, Ltd, 2008.

[16] J. C. Murray, H. Erwin, and S. Wermter. Robotic sound-source localisation
architecture using cross-correlation and recurrent neural networks. Neural
Networks, 22(2):173–189, 2009.

[17] M. Obando, L. Liem, W. Madauss, M. Morita, and B. Robinson. Robotic
surgery in pituitary tumors. Operative Techniques in Otolaryngology-Head
and Neck Surgery, 15(2):147–149, 2004.

[18] Aldebaran Robotics. User guide version 1.10.10. Digital Manual.

[19] T. Rodemann. A study on distance estimation in binaural sound localizati-
on. In Intelligent Robots and Systems (IROS), 2010 IEEE/RSJ International
Conference, 2010.

[20] R. Rojas. Neural networks: a systematic introduction. Springer-Verlag New

York, Inc., New York, NY, USA, 1996.

[21] M. Russ. Sound Synthesis and Sampling. Focal Press, 2004.

[22] C. Sammut and G. I. Webb. Encyclopedia of Machine Learning. Springer,

2010.

[23] A. Spanias, T. Painter, and V. Atti. Audio Signal Processing and Coding.

John Wiley & Sons, Inc., 2005.

44

Abbildungsverzeichnis

1.1 Aufgabenstellung eines Serviceroboters (entliehen von [2]) . . . . . .

2.1 Nao Roboter (entliehen von [18])
. . . . . . . . . . . . . . . . . . .
2.2 Mikrophonpositionen (entliehen von [18]) . . . . . . . . . . . . . . .
2.3 Bewegungsfreiheit des Kopfes (entliehen von [18]) . . . . . . . . . .
2.4 Beispiel einer Fouriertransformation . . . . . . . . . . . . . . . . . .
2.5 Cross Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.6 Delay Line Modell (entliehen von [9]) . . . . . . . . . . . . . . . . .

2

3
4
4
6
8
9

3.1 Verlauf der Simulation und der Korrelationsanalyse . . . . . . . . .
17
3.2 Mittlerer Fehler in Abh¨angigkeit des simulierten Mikrophonabstandes 17
18
3.3 Beispielhafte Confusion Matrix . . . . . . . . . . . . . . . . . . . .

4.1 Entscheidungsgrenzen durch versteckte Neuronen . . . . . . . . . .

26

5.1 Experimenteller Aufbau . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Rede Kennedy [10]
. . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Extraktion - Kennedy . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . .
5.4 Ergebnisse - Datenmenge Kennedy
5.5 Confusion Matrizen - Kennedy . . . . . . . . . . . . . . . . . . . . .
5.6 Extraktion - Wortsequenzen . . . . . . . . . . . . . . . . . . . . . .
5.7 Ergebnisse - Datenmenge Wortsequenzen . . . . . . . . . . . . . . .
5.9 Noisy Words Extraction . . . . . . . . . . . . . . . . . . . . . . . .
5.8 Confusion Matrizen - Wortsequenzen . . . . . . . . . . . . . . . . .

29
30
31
31
32
33
34
34
35

45

Abbildungsverzeichnis

46

Erkl¨arung der Urheberschaft

Ich versichere an Eides statt, dass ich die vorliegende Bachelorarbeit selbstst¨andig
und ohne unerlaubte Hilfe Dritter angefertigt habe. Alle Stellen, die inhaltlich oder
w¨ortlich aus anderen Ver¨oﬀentlichungen stammen, sind kenntlich gemacht. Diese
Arbeit lag in gleicher oder ¨ahnlicher Weise noch keiner Pr¨ufungsbeh¨orde vor und
wurde bisher noch nicht ver¨oﬀentlicht.

Ort, Datum

Unterschrift

47

