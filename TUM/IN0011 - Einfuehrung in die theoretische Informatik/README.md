# 2 - Grundbegriffe

- Alphabet $\Sigma$ ist eine endliche Menge (= Buchstaben unserer Wörter)
- Wort über $\Sigma$ ist eine endliche Folge von Zeichen aus $\Sigma$, z.B. baba
- $\epsilon$ ist das leere Wort mit Länge 0
- $\Sigma^*$ sind alle Wörter über $\Sigma$
- $L \subseteq \Sigma^*$ ist eine Sprache, auch $\\{\epsilon\\}$
- $\emptyset$ ist die leere Sprache

## Operationen auf Sprachen
$AB = \\{uv | u \in A \land v \in B\\}$
- alle mit allen
- $\emptyset A = \emptyset$
- $\\{\epsilon\\} A = A$

$A^0 = \\{\epsilon\\}$
- selbst $\emptyset^* = \\{\epsilon\\}$

$A^+ = \bigcup_{n \geq 1} A^n$

$A^* = A^+ \cup A^0 = \bigcup_{n \geq 1} A^n \cup \\{\epsilon\\}$
- erklärt $\epsilon \in \Sigma^*$
- aber $\epsilon \not\in \Sigma$

## Rechenregeln
$A(B \cup C) = AB \cup AC$ und $(B \cup C)A = BA \cup CA$

$A(B \cap C) = AB \cap AC$ gilt nicht immer
- Beispiel: $A = \\{a, aa\\}, B = \\{a\\}, C = \\{aa\\}$
- $A(B \cap C) = A \emptyset = \emptyset$
- $AB \cap AC = \\{aa, aaa\\} \cap \\{aaa, aaaa\\} = \\{aaa\\}$

## Grammatiken

$G = (V, \Sigma, P, S)$
- $V$ = Nichtterminale
- $\Sigma$ = Terminale / Alphabet
- $P \subseteq (V \cup \Sigma)^* \times (V \cup \Sigma)^*$ = Produktionen
- $S \in V$ = Start

### Ableitungsrelation

$\alpha \rightarrow_G \alpha'$
- falls der Übergang durch eine Regel $\beta \rightarrow \beta' \in P$ erzeugt werden kann

Ableitung von $\alpha_n$ aus $\alpha_1$:

$\alpha_1 \rightarrow_G \alpha_2 \rightarrow_G ... \rightarrow_G \alpha_n$

Für $\alpha_1 = S$ **erzeugt** $G$ das Wort $\alpha_n$ 
- $L(G)$ = alle erzeugten Wörter

### Reflexive transitive Hülle
- $\alpha \rightarrow_G^0 \alpha$
- $\alpha \rightarrow_G^{n+1} \gamma \iff \exists \beta. \alpha \rightarrow_G^n \beta \rightarrow_G \gamma$

Reflexive transitive Hülle:  
$\alpha \rightarrow_G^* \beta \iff \exists n. \alpha \rightarrow_G^n \beta$

Nicht-reflexive transitive Hülle:  
$\alpha \rightarrow_G^+ \beta \iff \exists n > 0. \alpha \rightarrow_G^n \beta$

Sprache einer Grammatik:  
$L(G) = \\{w \in \Sigma^* | S \rightarrow_G^* w\\}$

## Chomsky Hierarchie
- Typ 0: immer
- Typ 1: falls keine Produktion das Wort verkleinert (außer $S \rightarrow \epsilon$)
  $|\alpha| \leq |\beta|$ für alle $\alpha \rightarrow \beta$
- Typ 2: falls zusätzlich jede Bedingung **ein** Nichtterminal ist  
  $\alpha \in V$
- Typ 3: falls zusätzlich jedes Resultat aus einem Terminal und eventuell noch einem Nichtterminal besteht (außer $S \rightarrow \epsilon$)  
  $\beta \in \Sigma \cup \Sigma V$  
  -> hat immer nur ein Nichtterminal!!!

Namen:
- Typ 0: Phrasenstrukturgrammatik / Rekursiv-aufzählbare Sprache
- Typ 1: Kontextsensitive Grammatik / Kontextsensitive Sprache
- Typ 2: Kontextfreie Grammatik / Kontextfreie Sprache
- Typ 3: Rechtslineare Grammatik / Reguläre Sprache

## Erkennungsproblem
Ist eine gegebene Zeichenkette ein Programm / kann sie von den Regeln erzeugt werden?

### Recognizer
Problem, welches das Erkennungsproblem für eine gegebene Grammatik löst

### Wortproblem
Gegeben ein Wort $w \in \Sigma^*$ und eine Grammatik $G$, ist $w \in L(G)$?

# 3 - Reguläre Sprachen
## Deterministischer Endlicher Automat 
DFA $M = (Q, \Sigma, \delta, q_0, F)$
- $Q$ = Zustände
- $\Sigma$ = Eingabealphabet
- $\delta: Q \times \Sigma \rightarrow Q$ = Übergangsfunktion
- $q_0$ = Startzustand
- $F \subseteq Q$ = Endzustände

$\hat{\delta}: Q \times \Sigma^* \rightarrow Q$
- $\hat{\delta}(q, \epsilon) = q$
- $\hat{\delta}(q, aw) = \hat{\delta}(\delta(q,a), w)$ 
- $\Rightarrow \hat{\delta}(q, wa) = \delta(\hat{\delta}(q,w), a)$ 
- -> Zustand, den man von $q$ mit $w$ erreicht

Akzeptierte Sprahce $L(M) = \\{w \in \Sigma^* | \hat{\delta}(q_0, w) \in F \\}$

## Nichtdeterministischer Endlicher Automat 
NFA $N = (Q, \Sigma, \delta, q_0, F)$
- $Q$ = Zustände
- $\Sigma$ = Eingabealphabet
- $\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$ = Übergangsfunktion
- $q_0$ = Startzustand
- $F \subseteq Q$ = Endzustände

### Von Zuständen zu Zuständen

$\bar{\delta}(S,a): \mathcal{P}(Q) \times \Sigma \rightarrow \mathcal{P}(Q) = \bigcup_{q \in S} \delta(q, a)$

$\hat{\bar{\delta}}: \mathcal{P}(Q) \times \Sigma^* \rightarrow \mathcal{P}(Q)$
- $\hat{\bar{\delta}}(S, \epsilon) = S$
- $\hat{\bar{\delta}}(S, aw) = \hat{\bar{\delta}}(\bar\delta(S,a), w)$ 
- -> Zustände, die man von irgendeinem $q \in S$ mit $w$ erreicht

Akzeptierte Sprache $L(N) = \\{w \in \Sigma^* | \hat{\bar{\delta}}(\\{q_0\\}, w) \cap F \neq \emptyset\\}$  
-> NFA rät richtigen Weg der Zustände

## Rechtslineare Grammatik <-> DFA

### Von DFA $M$ zu rechtslinearer $G$
Gegeben: $M = (Q, \Sigma, \delta, q_0, F)$

Grammatik $G$:
- $V = Q$
- $T = \Sigma$
- $S = q_0$
- $P$ enthält
  - $q_1 \rightarrow aq_2$ für $\delta(q_1, a) = q_2$
  - $q_1 \rightarrow a$ zusätzlich für $\delta(q_1, a) \in F$ -> kann sich entscheiden aufzuhören
  - $q_0 \rightarrow \epsilon$, falls $q_0 \in F$
  
$\hat{\delta}(q_0, a_1 ... a_n) \in F$  
gdw  
$q_0 \rightarrow_G a_1 q_2 \rightarrow_G a_1 a_2 q_3 \rightarrow_G ... \rightarrow_G a_1 ... a_n q_n \rightarrow_G a_1 ... a_n$ eine Ableitung von $G$ ist.

### Von rechtslinearer $G$ zur NFA $M$
Gegeben: $G = (V, \Sigma, P, S)$

NFA $M$:
- $Q = V \cap \\{q_f\\}$ (mit $q_f \not \in V$ of course)
- $\Sigma = \Sigma$
- $q_0 = S$
- Für jede Produktion $X \rightarrow a Y$: $Y \in \delta(X, a)$
- Für jede Produktion $X \rightarrow a$: $q_f \in \delta(X, a)$
- $F = \\{q_f\\}$

$S \rightarrow_G a_1 X_1 \rightarrow_G a_1 a_2 X_2 \rightarrow_G ... \rightarrow_G a_1 ... a_{n-1} X_{n-1} \rightarrow_G a_1 ... a_n$ ist eine Ableitung von $G$  
gdw  
$q_f \in \delta(S, a_1 ... a_n)$

Falls $S \rightarrow \epsilon$: Mach $q_0$ ebenfalls zum Endzustand

### Von NFA $N$ zu DFA $M$ / Potenzmengenkonstruktion
Gegeben: $N = (Q, \Sigma, \delta, q_0, F)$

DFA $M$:
- $\mathcal{P}(Q)$ Zustände
- $\Sigma = \Sigma$
- $\delta_M$
- $\\{q_0 \\}$ Startzustand
- $F_M = \\{S \subseteq Q | S \cap F \neq \emptyset \\}$

$w \in L(N)$  
$\iff \hat{\bar \delta}(\\{q_0\\}, w) \cap F \neq \emptyset$  
$\iff \hat{\delta_M}(\\{q_0\\}, w) \in F_M$  
$\iff w \in L(M)$  

### Worst Case Potenzmengenkonstruktion
Gegeben: $L_k = \\{ w \in \\{0,1\\}^* | \text{das k-letzte Bit von w ist 1} \\}$

TODO: Beweis

**-> Jeder DFA $M$ mit $L(M) = L_k$ hat mindestens $2^k$ Zustände**

## NFAs mit $\epsilon$-Übergängen
-> Für Produktionen der Gestalt $A \rightarrow B$

$\epsilon$-NFA -> $\delta : Q \times (\Sigma \cup \\{\epsilon \\}) \rightarrow \mathcal{P}(Q)$

### Für jeden $\epsilon$-NFA $N$ gibt es einen NFA $N'$
- $\delta' : Q \times \Sigma \rightarrow \mathcal{P}(Q)$  
  $\delta'(q, a) = \bigcup_{i \geq 0, j \geq 0} \hat \delta(\\{ q \\}, \epsilon^i a \epsilon^j)$
  -> Für jeden Zustand, vereinige alle Zustände, die mit a oder eingefügten $\epsilon$ erreicht werden können
- Falls $N$ $\epsilon$ akzeptiert, dann setze $F' = F \cup \\{q_0 \\}$, sonst $F' = F$

## Reguläre Ausdrücke
- $\emptyset$, $\epsilon$ und $a$ für $a \in \Sigma$ sind reguläre Ausdrücke
- Falls $\alpha$ und $\beta$ reguläre Ausdrücke sind, dann auch $\alpha \beta$, $\alpha | \beta$ und $\alpha^*$

### Definierte Sprache
- $L(\emptyset) = \emptyset$, $L(\epsilon) = \epsilon$ und $L(a) = a$
- $L(\alpha \beta) = L(\alpha) L(\beta)$ -> alle Kombinationen konkatenieren
- $L(\alpha | \beta) = L(\alpha) \cup L(\beta)$
- $L(\alpha^*) = L(\alpha)^*$ -> $\\{\epsilon\\}$ + alle Wiederholungen 

### Strukturelle Induktion
Beweis von Eigenschaft $P$ für alle regulären Ausdrücke
- Beweise $P(\emptyset)$, $P(\epsilon)$ und $P(a)$ für alle $a \in \Sigma$
- Beweise $P(\alpha) \land P(\beta) \Rightarrow P(\alpha \beta)$
- Beweise $P(\alpha) \land P(\beta) \Rightarrow P(\alpha | \beta)$
- Beweise $P(\alpha) \Rightarrow P(\alpha^*)$

## Reguläre Sprache $\iff$ Es gibt einen regulären Ausdruck

### Regulärer Ausdruck $\Rightarrow$ Sprache ist regulär
Gegeben: regulärer Audruck $\gamma$  
-> Konstruiere $\epsilon$-NFA $N$ mit $L(N) = L(\gamma)$

Basisfälle:
- $\gamma = \emptyset$ -> NFA akzeptiert nichts / $F = \emptyset$
- $\gamma = \epsilon / a$ -> NFA akzeptiert nur $\epsilon / a$

Falls $\gamma = \alpha \beta$
- Wir haben $N_\alpha$ und $N_\beta$
- $Q_\gamma = Q_\alpha \cup Q_\beta$ mit $Q_\alpha \cap Q_\beta = \emptyset$
- Starte mit $N_\alpha$  
  -> $q_{0 \gamma} = q_{0 \alpha}$
- Ende mit $N_\beta$
  -> $F_\gamma = F\beta$
- Verbinde alle Endzustände von $N_\alpha$ über $\epsilon$-Übergänge mit $q_{0 \beta}$  
  -> $\delta = \delta_\alpha \cup \delta_\beta \cup \\{(f, \epsilon) \rightarrow \\{q_{0 \beta} \\} | f \in F_\alpha \\}$

Falls $\gamma = \alpha | \beta$
- Verbinde $q_{0 \gamma}$ über $\epsilon$-Übergänge mit $q_{0 \alpha}$ und $q_{0 \beta}$
- $F_\gamma = F\alpha \cup F\beta$

Falls $\gamma = \alpha^*$
- Mache $q_{0 \gamma}$ zum Endzustand, um $\epsilon$ zu akzeptieren
- Verbinde $q_{0 \gamma}$ und alle $F_\alpha$ mit $q_{0 \alpha}$ über $\epsilon$-Übergänge

### Reguläre Sprache $\Rightarrow$ Es gibt einen regulären Ausdruck
TODO: Beweis und Komplexität von Konversionen

## Abschlusseigenschaften Regulärer Sprachen
Falls $A$ und $B$ reguläre Sprachen sind, dann auch
- $AB$, $A \cup B$ und $A^*$ (können direkt über Regulären Ausdruck dargestellt werden)
- $\overline{A} = \Sigma^* - A)$ (vertausche die Endzustände des DFAs)
- $A \cap B$ ($= \overline{\overline{A} \cup \overline{B}}$)
- $A - B$ ($= A \cup \overline{B}$)

### Produkt-Konstruktion
Gesucht: DFA, der $L(M_1) \cap L(M_2)$ akzeptiert (beide DFAs)
- $Q = Q_1 \times Q_2$
- $\Sigma = \Sigma$
- $q_0 = (q_{01}, q_{02})$
- $F = F_1 \times F_2$
- $\delta((q_1, q_2), a) = (\delta_1(q_1, a), \delta_2(q_2, a))$
- -> Läuft beide parallel ab

### Aufgabe: Beweise, dass die akzeptierte Sprache gleich $L(M_1) \cap L(M_2)$ ist

## Pumping Lemma
Wie zeigt man, dass eine Sprache nicht regulär ist?

Für jede Reguläre Sprache $R \subseteq \Sigma^*$
- gibt es ein $n > 0$
- sodass jedes Wort $z$ mit $|z| \geq n$ 
- in $z = uvw$ zerlegen lässt, sodass
  1. $v \neq \epsilon$
  2. $|uv| \leq n$
  3. $\forall i \geq 0. uv^iw \in R$
  
### Beweis
Gegeben sei der DFA, der $R$ erkennt
- setze $n = |Q|$

Für jedes akzeptierte Wort $z$ mit $|z| = m \geq n$ werden $m$ Kanten abgelaufen, also $> n$ Zustände.
- Da $n = |Q|$ gibt es mindestens einen Zustand, der doppelt abgelaufen wurde
- Sei $q_0 = p_0 \overset{a_1} \rightarrow p_1 \overset{a_2} \rightarrow p_2 ... \overset{a_m} \rightarrow p_m$
- Dann gibt es also $0 \leq i < j \leq n$ mit $p_i = p_j$

Unterteile $z$ in:
- $u = a_1 ... a_i$
- $v = a_{i+1} ... a_j$ -> Zyklus
- $w = a_{j+1} ... a_m$

Dann gilt:
- $|uv| \leq n$, da $v$ der erste Zyklus ist  
  -> es wurden maximal $|Q| + 1$ Zustände durchlaufen  
  -> es wurden maximal $|Q| = n$ Kanten durchlaufen
- $v \neq \epsilon$, da es einen Zyklus geben muss, da bei $m \geq n$ Kanten $> n$ Zustände abgelaufen werden
- $$\forall i \geq 0. uv^iw \in R$, da $v$ den Zyklus abläuft

### Pumping-Lemma-Zahl für R
-> n, für das das Pumping-Lemma gilt  
-> $|Q_M|$ ist immer eine Pumping-Lemma-Zahl für $L(M) = R$

### $a^ib^i$ ist nicht regulär
Angenommen, es sei regulär
- dann gibt es eine Pumping-Lemma-zahl $n$
- Wähle $z = a^nb^n$
- Zerlege es in $uvw$
- Es gilt $|uv| \leq n$ -> $u$ und $v$ bestehen nur aus $a$s, da die ersten $n$ Zeichen $a$s sind
- Damit muss $uv^0w = uw = a^{n-|v|}b^n \in L$ gelten. Da $v \neq \epsilon$, kann das nicht sein

### $a^{m^2} | m \geq 0$ ist nicht regulär
TODO: Beweis

### Die Sprache der wohlgeklammerten Ausdrücke über $\\{(, ) \\}$ ist nicht regulär
TODO: Beweis

### Die Sprache der arithemtischen Ausdrücke ist nicht regulär
Angenommen, es sei doch regulär
- Dann gibt es einen DFA
- Ersetze alle Transitionen, die nicht mit ( oder ) beschriftet sind durch $\epsilon$-Transitionen
- Dadurch ergibt sich ein $\epsilon$-NFA, der die Sprache der wohlgeklammerten Ausdrücke über $\\{(, ) \\}$ erkennt
- Dadurch ergibt sich ein NFA und dadurch ein DFA, der die Sprache erkennt
- Dadurch ergibt sich eine rechtslineare Grammatik -> die Sprache der wohlgeklammerten Ausdrücke über $\\{(, ) \\}$ ist regulär
- Diese Sprache ist aber nicht regulär

## Entscheidungsverfahren
- Eingabe: Ein oder mehrere Objekte, die reguläre Sprachen beschreiben (DFA, NFA, RE, Typ 3 etc.)
- Frage: Haben diese Objekte eine bestimmte Eigeschaft?

### Probleme mit $D$ gegeben:
- Wortproblem $w \in L(D)$?
- Leerheitsproblem $L(D) = \emptyset$?
- Endlichkeitsproblem $L(D)$ endlich?
- Äquivalenzproblem $L(D_1) = L(D_2)$?

### Wortproblem in $\mathcal{O}(|w| + |M|)$ entscheidbar für DFA $M$
Einfach einlesen und ausführen

### Wortproblem in $\mathcal{O}(|Q|^2|w| + |N|)$ entscheidbar für NFA $N$
- Wort der Reihe nach durchgehen und $S = \bar{\delta}(S, w_i)$ updaten
- Kucken, ob $S$ irgendwann was von $F$ enthält

### Leerheitsproblem in $\mathcal{O}(|Q|^2|\Sigma|)$ entscheidbar für NFA $N$
- Kucken, ob $q_0$ einen Endzustand erreichen kann
- Einfache Breitensuche
- NFA hat $\leq |Q|^2|\Sigma|$ Kanten, DFA hat $\leq |Q||\Sigma|$ Kanten

### Endlichkeitsproblem ist für NFAs / DFAs entscheidbar
- Kucken, ob von $q_0$ aus eine nicht-leere Schleife erreichbar ist, von der aus $F$ erreichbar ist

### Äquivalenzproblem ist für DFAs entscheidbar
- Komplement und Durchschnitt kann mit endlichen Automaten berechnet werden
- $L_1 \subseteq L_2 \iff L_1 \cap \overline L_2 = \emptyset$
- $L_1 = L_2 \iff L_1 \subseteq L_2 \land L_2 \subseteq L_1$

### $\Rightarrow$ Äquivalenzproblem ist für Reguläre Ausdrücke entscheidbar

### Äquivalenzproblem ist für DFAs in Zeit $\mathcal{O}(|Q_1||Q_2||\Sigma|)$ entscheidbar
Leerheitsproblem überprüfen für:
- $L(M_1) \cap \overline{L(M_2)}$
- $L(M_2) \cap \overline{L(M_1)}$
- Jeweils $|Q_1||Q_2|$ Zustände -> jeweils Laufzeit von $\mathcal{O}(|Q_1||Q_2||\Sigma|)$

### Äquivalenzproblem ist für NFAs in Zeit $\mathcal{O}(2^{|Q_1|+|Q_2|})$ entscheidbar, bei fixem $\Sigma$
2 NFAs mit $m$ und $n$ Zuständen ergeben 2 DFAs mit $\mathcal{O}(2^{|m|} 2^{|n|})$ Zuständen

## Rechenregeln für reguläre Ausdrücke
- $\emptyset | \alpha \equiv \alpha | \emptyset \equiv \alpha$
- $\emptyset \alpha \equiv \alpha \emptyset \equiv \emptyset$
- $\epsilon \alpha \equiv \alpha \epsilon \equiv \alpha$
- $\emptyset^* \equiv \epsilon$
- $\epsilon^* \equiv \epsilon$

Assoziativität:
- $(\alpha | \beta) | \gamma \equiv \alpha | (\beta | \gamma)$
- $(\alpha \beta) \gamma \equiv \alpha (\beta \gamma)$

Kommutativität:
$\alpha | \beta \equiv \beta | \alpha$

Distributivität:
- $\alpha(\beta | gamma) \equiv \alpha \beta | \alpha \gamma$
- $(\beta | gamma) \alpha \equiv \beta \alpha | \gamma \alpha$

Stern Lemma:
- $\epsilon | \alpha \alpha^* \equiv  \alpha^*$
- $\alpha^* \alpha \equiv \alpha \alpha^*$
- $(\alpha^*)^* \equiv \alpha^*$

### Satz von Redko
Es gibt keine endliche Menge von gültigen Äquivalenzen aus denen sich alle gültigen Äquivalenzen herleiten lassen!

## Automaten und Gleichungssyteme

### Ardens Lemma
Sind $A, B$ und $X$ Sprachen mit $\epsilon \not \in A$, so gilt  
$X = AX \cup B \Rightarrow X = A^*B$

($\epsilon \not \in A$ muss gelten, da $X = \\{\epsilon \\} X \cup B$ keine eindeutige Lösung hat. Jede Sprache $X \supseteq B$ ist Lösung)

## Minimierung endlicher Automaten



