# Einführung

# Turing Maschine
- $T = (Q, \Sigma, I, q_0, F)$
- $I$ enthält 5-tupel $(q, s, s', m, q')$ mit
  - $q, q' \in Q$
  - $s \in \Sigma^k$
  - $s' \in (\Sigma - \text{□})^k$
  - $m \in \\{L,R,S\\}^k$
  
DTM 
- für alle $q, s$ gibt es maximal ein 5-tupel in $I$
NTM
- andernfalls

Globaler Zustand $S = (q,b)$
- $q \in Q$
- $b \in \text{Band}^k$
- $\text{Band} = \Sigma^k \times \mathbb{N}$

Globaler Anfangszustand $S_0 = (q_0, b_0)$
- alle Köpfe ganz links
- alle Bänder leer, außer erstes Band
- erstes Band enthält Eingabe

## Akzeptierende DTM (acceptor)
- $F = \\{\text{ACC, REJ}\\}$
- $T$ akzeptiert $w \in \Sigma^*$, falls Berechnung in Zustand $(\text{ACC}, b$ hält

Sprachen
- Sprache $L$ modelliert ein Entscheidungsproblem

Akzeptierte Sprache
- $L(T) = \\{w; \text{T akzeptiert w}\\}$

# Zeitkomplexität
- $\text{TIME}_T(w) \in \mathbb{N} \cup \\{\infty\\}$

## Komplexitätsklassen
- $P = \\{L \subset \Sigma^* ; \exists \text{DTM }T, k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*: \text{TIME}_T(w) = \mathcal{O}(|w|^k)\\}$
- $E = \\{L \subset \Sigma^* ; \exists \text{DTM }T, k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*: \text{TIME}_T(w) = \mathcal{O}(2^{k|w|})\\}$
- $EXP = \\{L \subset \Sigma^* ; \exists \text{DTM }T, k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*: \text{TIME}_T(w) = \mathcal{O}(2^{|w|^k})\\}$
- $2\cdot E = \\{L \subset \Sigma^* ; \exists \text{DTM }T, k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*: \text{TIME}_T(w) = \mathcal{O}(2^{2^{k|w|}})\\}$

Bemerkungen:
- $w \in \Sigma^*$ - Bedingung gilt auch für Wörter außerhalb von $L$
- Klassen sind robust / ändern sich nicht bei Variation des Maschinenmodells

## Übersetzer DTM (transducer)
- $F = \\{q_f\\}$
- Jede Berechnung endet in $(q_f, b)$
- Alle Köpfe in $b$ stehen ganz links und Ausgabe steht auf dediziertem Ausgabeband

$T$ **berechnet** $f: \Sigma^* \rightarrow \Sigma^*$, falls jede Berechnung für jedes $w \in \Sigma^*$ endet mit korrekter Ausgabe

## Komplexitätsklassen von Funktionen
Analog zu Sprachen:
$FP = \\{f: \Sigma^* \rightarrow \Sigma* \exists \text{DTM }T, k \in \mathbb{N} \text{ mit: T berechnet f und } \forall w \in \Sigma^*: \text{TIME}_T(w) = \mathcal{O}(|w|^k)\\}$

# Halteproblem (Einschub)
Gibt es eine DTM $T_{halt}$, die $\forall T,x$ vorhersagt, ob $T$ für $x$ hält?

Beweis (klassisch):
- Wir konstruieren eine DTM $D$, die hält, wenn $T_{halt}$ rejected, und unendlich lang läuft, wenn $T_{halt}$ akzeptiert
- Wichtig: $D$ und $T_{halt}$ haben nicht denselben Input! $D$ kann irgendwas als Input haben und reicht dann $(D,x)$ an $T_{halt}$ weiter.
  1. Wir bestimmen $D(x)$
  2. Dazu bestimmen wir $T_{halt}(D,x)$
  3. Dazu müsste die Maschine $D(x)$ bestimmen und in eine Endlos-Schleife geraten -> $T_{halt}$ kann nicht halten. Oder die Maschine bestimmt "$D(x)$ hält?" magisch, dann nimmt $D$ das Ergebnis und macht das Gegenteil von $T_{halt}$'s Vorhersage. q.e.d.

Beweis (Diagonalisierung): ???

## Modellagnostische Beweise
- Siehe https://en.wikipedia.org/wiki/Halting_problem#Sketch_of_proof
- Partielle Funktion $f$ von $X$ nach $Y$ ist $f : X' \rightarrow Y$ mit $X' \subset X$.
- Totale Funktion: partielle Funktion mit $X' = X$
- Berechenbare Funktion: es gibt einen Algorithmus, der sie berechnet

Beweis (klassisch):
- Wir nehmen an, dass es eine totale berechenbare binäre Funktion $h$ gibt, die für ein Programm $P$ und Input $x$ sagt, ob es hält oder nicht.
- Sei $g(x)$ definiert als $\cases{0 & if $h(x,x) = 0$,\cr undefined ,&otherwise. \cr}$
- Wenn eine Funktion undefined ist, bewirkt das eine nicht haltende Berechnung bei dementsprechenden Eingaben
- Wenn es ein Programm für $h$ gibt ($h$ ist berechenbar), gibt es auch ein Programm für $g$, genannt $P_g$
- $h(P_g, P_g) = 1 \iff g(P_g) = 0 \iff h(P_g, P_g) = 0$ q.e.d.

Beweis (Diagonalisierung):
- Wir nehmen an, dass es eine totale berechenbare binäre Funktion $h$ gibt, die für ein Programm $P$ und Input $x$ sagt, ob es hält oder nicht. $h$'s Parameter sind der Index von $P$ und der Index von $x$
- Reihen: Alle Programme
- Spalten: Alle Eingaben
- Zellen: $h(i_P, j_x)$
- Wir konstruieren ein neues Programm $g(i_P)$, das für $h(i_P, i_P) = 0$ $0$ ausgibt und andernfalls nicht definiert ist -> Wir invertieren die Einträge der Diagonale
- $g$ muss eine der Reihen sein, gleichzeitig kann $g$ keine der Reihen sein, da die Einträge invertiert wurden. q.e.d.

# Herleitung von P ≠ E

Trennendes Problem: $H_{exp} = \\{(T,w); \text{T akzeptiert w in } 2^{|w|} \text{ Schritten und T ist eine 2-Band DTM} \\}$
- $H_{exp} \in E$ und $H_{exp} \not\in P$

## Lemma 1

> Für jede $k$-Band DTM $T$ gibt es eine 2-Band DTM $T'$ mit $L(T) = L(T')$ und $\text{TIME}\_{T'}(w) = \mathcal{O}(\text{TIME}\_{T}(w)^2)$

Beweis:
- $T'$ hat Alphabet mit Trennzeichen $\Sigma_T \cup \\{\text{#}\\}$
- Auf Band 1 speichert $T'$ alle Bänder mit Trennzeichen
- Auf Band 2 speichert $T'$ die Kopfpositionen in one-hot-encoding -> gleich viele Zellen wie Band 1
- Die Instruktionen pro Band werden nacheinander ausgeführt
- Im Worst-case müssen beide Bänder komplett nach rechts verschoben werden, wenn sich das erste simulierte Band vergrößert
- Im $t$-ten Schritt sind beide Bänder je maximal $k\cdot t+k$ lang
- Pro simuliertem Schritt ($t$) und pro Band ($k$) sind das $kt+k$ Schritte für $T'$
- Da $k$ konstant und unabhängig von $|w|$ ist ergeben sich $\mathcal{O}(t^w)$ Schritte

## Lemma 2: $H_{exp} \in E$

Beweis:
- 5-Band DTM, die $H_{exp}$ akzeptiert
  1. Band enhält Input (Beschreibung von $T$ und $w$), wird nie verändert
  2. Band simuliert Band 1 von $T$
  3. Band simuliert Band 2 von $T$
  4. Band speichert binär kodierten Zustand von $T$
  5. Band enhält Zähler
- Initialisierung:
  - $w$ auf 2. Band kopieren
  - 4. Band mit kodiertem $q_0$ beschreiben
  - 5. Band mit binär-kodierter $2^{|w|}-1$ initialisieren ($|w|$ Einsen)
- Pro Schritt:
  - Passende Instruktion auf 1 suchen
  - 2,3,4 aktualisieren
  - Wenn $T$ hält, in entsprechendem Zustand (ACC, REJ) halten
  - Wenn Zähler abgelaufen ist, verwerfen
  - Zähler dekrementieren
- Laufzeit ($n = |w|$)
  - Initialisierung: $\mathcal{O}(n)$
  - Pro Schritt: $\mathcal{O}(n)$ ???
  - Maximal $2^n$ Schritte
  - $2^n \cdot \mathcal{O}(n) \leq \mathcal{O}(2^{2n})$
  
## Lemma 3: $H_{exp} \not\in P$

Beweis (analog zu Halteproblem):
- Annahme: Es gibt eine TM $T_{halt}$, die erkennt, ob $T$ $w$ in $2^{|w|}$ Schritten akzeptiert
- Aus der Definition von $P$ folgt, dass $TIME_{T_{halt}}((T, w)) = \mathcal{O}((|T|+|w|)^k)$ mit $k \in \mathbb{N}$
- O.b.d.A. können wir annehmen, dass $T_{halt}$ 2 Bänder hat, da die Zeitkomplexität weiterhin polynomiell bleibt.
- Wir konstruieren eine 2-Band TM $D$, die bei Eingabe einer TM $T$ auf das erste Band $(T, T)$ schreibt, $T_{halt}$ simuliert und ACC und REJ vertauscht
- Dadurch gilt: $D$ akzeptiert $T \iff T$ akzeptiert $T$ nicht
- Ersetze $T$ durch $D$ um einen Widerspruch zu erzeugen
- Die Laufzeit von $D$ ist $\mathcal{O}(|D|^k)$ und damit $\lt 2^{|D|}$. Falls die Laufzeit über diesem Limit wäre, kann die widersprüchliche Äquivalenz "$D$ akzeptiert $D \iff D$ akzeptiert $D$ nicht" nicht hergestellt werden, da aus "$D$ akzeptiert $D$" "$T_{halt}$ akzeptiert $D,D$ nicht" und damit wieder "$D$ akzeptiert $D$" folgt, da das Zeitlimit überschritten wurde.

Beweis (eigener):
- Annahme: Es gibt eine TM $T_{halt}$, die erkennt, ob $T$ $w$ in $2^{|w|}$ Schritten akzeptiert
- $D$ übergibt sich und seinen Input $x$ an $T_{halt}$ und macht dann das Gegenteil von $T_{halt}$s Vorhersage
- Aus der Definition von $T_{halt}$ folgt: $D$ akzeptiert $x \Rightarrow T_{halt}$ akzeptiert $(D, x)$ 
  - Diese Implikation ist nur gültig, wenn $D$ und somit $T_{halt}$ unter dem Limit von $2^{|x|}$ Schritten bleiben
- Aus der Definition von $D$ folgt: $T_{halt}$ akzeptiert $(D, T(+x)) \Rightarrow D$ akzeptiert $(T,x)$ **nicht**!

Dieser Beweis 
- funktioniert für alle echt enthaltenen Komplexitätsklassen
- funktioniert nicht für dieselbe Klasse, da $T_{halt}$ $D,D$ bzw. $D,x$ nicht akzeptiert (selbst wenn $D$ es akzeptiert), da es das Zeitlimit überschreitet
- ist gültig, sobald ein Input mit dem Widerspruch erzeugt wurde. Wir können allerdings nicht einen zufälligen kurzen Input wählen, da $D$ absolut von $T_{halt}$ abhängt. Wir können also nicht absichtlich eine kurze Laufzeit kreieren, um unter dem Limit von $2^x$ zu bleiben. 

Generell: **Um zu bestimmen, ob eine DTM in t Schritten hält, braucht man mindestens t Schritte**

## Theorem 4: $P \subset E$

# Nichtdeterministische TM
- Pro $(q, s)$ kann es mehrere 5-Tupel in $I$ geben
- Mehrere Folgezustände pro Globalem Zustand / Berechnungsbaum

## Nichtdeterministisch akzeptierende TM
- $T$ akzeptiert $w$, falls es mindestens einen akzeptierenden Pfad gibt
- Bei mehreren Möglichkeiten rät die TM bestmöglich

$NTIME_T(w) = \cases{\text{Länge des kürzesten akzeptierenden Pfades} & falls $w \in L(T)$,\cr \text{Länge des kürzesten Pfades} & sonst. \cr}$

## Komplexitätsklassen
- $NP = \\{L; \exists \text{ NTM } T \text{ und } \exists k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*:  NTIME_T(w) = \mathcal{O}(|w|^k \\}$
- $NE = \\{L; \exists \text{ NTM } T \text{ und } \exists k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*:  NTIME_T(w) = \mathcal{O}(2^{k|w|} \\}$
- $NEXP = \\{L; \exists \text{ NTM } T \text{ und } \exists k \in \mathbb{N} \text{ mit } L(T) = L \text{ und } \forall w \in \Sigma^*: NTIME_T(w) = \mathcal{O}(2^{|w|^k} \\}$

Aus der Definition folgt:
- $NP \subset NE \subset NEXP$ (Beweis ähnlich zu $P \subset E$, aber komplizierter)
- $* \subseteq N*$

## Theorem 5: $NP \subseteq EXP$
Beweis:
- Aus $L \in NP$ folgt, dass es eine NTM $T_N$ gibt, die $L$ in $\mathcal{O}(|w|^k)$ Schritten akzeptiert
- Verzweigungsgrad $d$: Für alle $(q, s)$ gibt es maximal $d$ Tupel in $I$
- Wir konstruieren eine DTM $T_D$, die $L$ in $\mathcal{O}(2^{|w|^k})$ Schritten entscheidet
- $T_D$ iteriert den Berechnungsbaum von $T_N$ generell in Breitensuche mit größer werdendem $l$, wobei $l$ das Tiefenlimit ist. Pro $l$ wird der Berechnungsbaum mit Tiefensuche iteriert.
- Der Berechnungsbaum bis zu einer Tiefe $l$ hat maximal eine Größe von $d^l$. Das korrekte $l$, das zum kürzesten akzeptierenden Pfad führt, finden wir in $\mathcal{O}(|w|^k)$ Tiefensuchen. Bis (und einschließlich) dahin benötigt jede Tiefensuche $\mathcal{O}(d^l) = \mathcal{O}(d^{|w|^k})$ Schritte.
- Insgesamt ergeben sich $\mathcal{O}(|w|^k) \cdot \mathcal{O}(d^{|w|^k})$ Schritte. Für $d \geq 2$ kann dies zu $\mathcal{O}(d^{|w|^k}) = \mathcal{O}(2^{log_2(d) |w|^k}) = \mathcal{O}(2^{|w|^{k+1}})$ vereinfacht werden. q.e.d.

Analog: $NE \subseteq 2E$

Generell: Nichtdeterministische Zeit $t \subseteq$ Deterministische Zeit $2^t$

# Komplementierung
- $\overline L = \Sigma^* - L$
- $co-\mathcal{C} = \\{\overline L; L \in \mathcal{C}\\}$ für Komplexitätsklasse $\mathcal{C}$
- $\Rightarrow P \subseteq NP \Rightarrow co-P \subseteq co-NP$

$co-P = P$, $co-EXP = EXP$ etc., da es zu jedem $L$ in $co-P$ eine Sprache $\overline L$ in $P$ gibt. Um $L$ zu entscheiden müssen wir nur die finalen Zustande der TM für $\overline L$ vertauschen.

$co-NP = NP$ ist offen, da die Maschine in $NP$ ein Wort akzeptiert, wenn es mindestens **einen** akzeptierenden Pfad gibt. Sie verwirft aber erst, wenn **alle** Pfade verwerfen. Wenn wir also einfach die finalen Zustände an jedem Blatt des Berechnungsbaum vertauschen, dann simulieren wir nicht $\overline L$ korrekt, da wir Wörter vorschnell akzeptieren, die eigentlich in $L$ sind. Also müssen wir den gesamten Baum ablaufen, um sicherzustellen, dass alle Pfade in der komplementären TM / kein Pfad in der TM akzeptiert, bevor wir ein Wort für $\overline L$ akzeptieren.

$P = NP \Rightarrow co-P = co-NP \Rightarrow co-NP = NP$ (mit $co-P = P$).

# Padding
- Technik zum Übertragen von Kollapsresultaten nach oben
- Padding Symbol $\text{#} \not\in \Sigma$
- $pad(w) = w\text{##}...\text{##}$ mit $|pad(w)| = 2^{|w|}$

## Theorem 6: $P=NP \Rightarrow E=NE$
- $L \in NE \Rightarrow$ Es gibt eine NTM $T_{N}$, die $w \in L$ in $\mathcal{O}(2^{k|w|})$ akzeptiert
- Es gibt auch eine NTM $T_{padN}$, die $pad(w)$ in $\mathcal{O}(2^{k|w|})$ Schritten akzeptiert, indem sie annimmt, dass alle Inputs bereits gepaddet sind
- $NTIME_{T_{padN}} = \mathcal{O}(|pad(w)|^k) \Rightarrow T_{padN} \in NP \Rightarrow T_{padN} \in P$
- Es gibt eine DTM $T_{padD}$, die das gepaddete $w$ in $\mathcal{O}(2^{k'|w|})$ Schritten akzeptiert
- Es gibt also auch eine DTM $T_D$, die $w$ in $\mathcal{O}(2^{k'|w|})$ Schritten akzeptiert, indem sie $w$ paddet ($2^{|w|}$ Schritte) und dann $T_{padD}$ simuliert.
- Es folgt $NE \subseteq E$. Mit der Definition von $NE$ folgt $E = NE$. q.e.d

