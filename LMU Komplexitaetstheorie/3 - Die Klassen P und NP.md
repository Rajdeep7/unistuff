# Probleme in P und NP

## SAT
- Geg.: Aussagenlogische Formel F in KNF
- Frage: Ist F erfüllbar?
- Notiz: Das ganze ist in KNF, da DNF trivial ist. KNF sind die 0 Einträge der Wahrheitstabelle mit allen Variablen verneint. Von KNF zur DNF gehts über das Distributivgesetz. Von DNF zur KNF über die Wahrheitstabelle.

$SAT \in NP$: NTM rät Variablenbelegung

Spezialfälle:
- Horn-SAT: Jede Klausel enthält höchstens ein positives Literal
- $k$-SAT: Jede Klausel enthält höchstens $k$ Literale
- Horn-SAT und 2-SAT sind in P

## k-Färbbarkeit
- Geg.: Graph $G = (V,E)$
- Frage: Gibt es eine Färbung $c: V \rightarrow \\{1,...,k\\}$?
- Färbung: $\\{u, v\\} \in E \Rightarrow c(u) \neq c(v)$

Seite 12 fehlt! (Proposition 1 zeigt, wie man ein Problem NP zuordnet, siehe coPRIM)

## Vertex Cover
- Geg.: Graph $G$, $k \in \mathbb{N}$
- Frage: Gibt es ein Vertex Cover der Größe $k$?
- Vertex Cover: Menge an Knoten, die mindestens einen Knoten jeder Kante enthält
- In $NP$, denn Überprüfen eines Vertex Covers ist in $P$, NTM rät Vertex Cover 

Ende von Seite 12

## co-PRIM
- Gegeben: $n \in \mathbb{N}$
- Frage: Ist $n$ zusammengesetzt?

$n \in co-PRIM \iff \exists k, l: (k > 1 \land l > 1 \land k \cdot l = n)$
- Die Bedingung in der Klammer ist in $P$ überprüfbar
- NTM rät $k$ und $l$

## Graphenisomorphie
- Ist $G_1$ isomorph zu $G_2$? (Knoten umbennen)

# Vollständigkeit
## Reduktion 

$L_1 \leq_p L_2 \iff \exists f \in FP \text{ mit } \forall x: x \in L_1 \iff f(x) \in L_2$

- $L_1$ ist also höchstens so schwierig wie $L_2$, denn ich kann $L_1$ mit $L_2$ lösen.
- $f$ ist die Reduktion
- Reduzierbarkeit ist transitiv
- Das rechte $\iff$ muss sein, da wir für $f(x) \not\in L_2$ auch von $x \in L_1$ ausgehen dürfen wollen.
- Für das Lösen von $L_2$ bringt uns die Reduzierbarkeit nichts, da $f$ nicht-invertierbar sein kann. Falls $f^{-1} \in FP$ gilt $L_2 \leq_p L_1$.

### NP-schwere $L$
- $\forall L' \in NP: L' \leq_p L$
- Obere Schranke für Probleme in NP

### NP-vollständige $L$
- $L$ ist NP-schwer und $L \in NP$
- $L \in P \iff P = NP$
- Beispiele: SAT, 3-SAT, 3-Färbbarkeit, Vertex Cover

## Proposition 2: 3-SAT $\leq_p$ Vertex Cover
$\Rightarrow$ Vertex Cover ist NP-vollständig

Beweis:
- 1er oder 2er Klauseln können in 3er Klauseln umgewandelt werden: $a \lor b \iff a \lor b \lor b$
- $n$ Variablen -> $2n$ Knoten $x - \overline x$
- $m$ Klauseln -> $3m$ Knoten $c_1, c_2, c_3$
  - Jeder dieser Knoten ist mit den anderen beiden verbunden
  - Es müssen also zwei ausgewählt werden -> Joker-Knoten, die repräsentieren, welche Variablen in der Klausel *nicht* belegt werden
  - $c_i$ ist mit dem zugehörigen Variablen-Knoten verbunden
- $k = n + 2m$
- Reduktion ist in $FP$ und $x \in L_1 \iff f(x) \in L_2$ ist offensichtlich (laut VL)

# Landkarte von NP
- NP
  - P
  - L*
  - NP-vollständig (SAT, VC etc.)
  
Wir werden zeigen:
- $P \neq NP \Rightarrow \exists L \in NP \text{\\ } P$, die nicht NP-vollständig sind
- $P \neq NP \Rightarrow$ Es gibt keinen dünnen NP-vollständigen Probleme

### Symmetrische Differenz $A \triangle B$
- Das, was $A$ und $B$ unterscheidet

## Lemma 3:
> Wenn $L \triangle L'$ endlich ist, so gilt $L \in P \iff L' \in P$

Beweis:
- Wir kodieren alle $w \in L \triangle L'$ in den Zuständen einer Maschine
- Überprüfe, ob $w$ durch diese Zustände abgedeckt ist und operiere dann wie die TM für $L$ bzw für $L'$ -> Ist in $P$

## Theorem 4 / Ladner's Theorem
> Falls $P \neq NP$, dann gibt es $L^* \in NP \text{\\ } P$, aber $L^*$ nicht NP-vollständig ($L$ ist NP-intermediate)

Skipped ???
Siehe http://oldblog.computationalcomplexity.org/media/ladner.pdf

# Relativierung

## Orakelturingmaschine
- Extra Anfrageband
- Drei zusätzliche Zustände: ANFRAGE, JA, NEIN
- Verhalten wird durch Orakel $A$ bestimmt mit $A \subseteq \Sigma^*$: Im Zustand ANFRAGE, geht die Maschine in den Zustand
  - JA, falls der Inhalt des Anfragebandes $\in A$ ist
  - NEIN andernfalls
- Orakel enthält Information, die der TM gratis zur Verfügung steht (externer Server, DB etc.)

$L(T^A) = \\{w; T \text{ akzeptiert } w \text{ mit Orakel } A\\}$

## Relativierte Klassen
- $P^A = \\{L; \exists \text{ DTM } T, k \in \mathbb{N} \text{ mit } L(T^A) = L \text{ und } \forall w \in \Sigma^*: TIME_T(w) = \mathcal{O}(|w|^k)\\}$
- ${NP}^A = \\{L; \exists \text{ NTM } T, k \in \mathbb{N} \text{ mit } L(T^A) = L \text{ und } \forall w \in \Sigma^*:  NTIME_T(w) = \mathcal{O}(|w|^k \\}$

Für jedes Orakel $A$ gilt:
- ${P}^\emptyset \subseteq {P}^A$
- ${NP}^\emptyset \subseteq {NP}^A$

Wir werden zeigen:
- Es gibt Orakel $A$ mit $P^A = {NP}^A$
- Es gibt Orakel $B$ mit $P^B \neq {NP}^B$
- Folgerung: Beweistechniken, die sich relativieren lassen (also auch mit Orakel funktionieren) sind ungeeignet, das P vs. NP Problem zu lösen. Dies ist z.B. der Fall für Diagonalisierungen oder Maschinensimulationen.

## Theorem 5: Es gibt $A$, sodass $P^A = {NP}^A$
Wir müssen zeigen, dass ${NP}^A \subseteq P^A$

Beweis:
- Sei $L \in {NP}^A$, dann gibt es eine Orakel NTM $T_N$ mit $L(T_N^A) = L$ und $NTIME_{T_N}(w) = p(|w|)$ mit $p$ als Polynom
- Das Orakel $A = \\{(T, w, \text{#}^{k}); \text{DTM T akzeptiert w und benutzt höchstens k Bandzellen}\\}$
- Wir bauen nun eine DTM $T$, die $L$ akzeptiert und höchstens $q(|w|)$ Bandzellen benötigt. Diese DTM darf sehr lange brauchen - solange sie nur $q(|w|)$ Bandzellen benötigt, kann unser Orakel die Frage direkt lösen, sodass die hohe Anzahl der Schritte, die $T$ eigentlich bräuchte, keine Rolle spielt.
- $T$ ist folgendermaßen konstruiert:
  - $T$ iteriert den Berechnungsbaum von $T_N$. Wenn $T_N$ in $p(|w|)$ Schritten akzeptiert, so akzeptiert $T$ also in $2^{q(|w|)}$ Schritten.
  - $T$ mag zwar wesentlich länger brauchen als $T_N$, doch es wird für seine Simulation nicht mehr Bandzellen als $T_N$ benötigen. Da $T_N$ in $p(|w|)$ Schritten akzeptiert, braucht bis zu dieser Tiefe jeder globale Zustand von $T_N$ maximal $p(|w|)$ Bandzellen. Also braucht $T$ bei seiner Simulation auch nur maximal $p(|w|)$ Bandzellen, bis es den Pfad im Berechnungsbaum gefunden hat.
  - $T_N^A$ kann an beliebigen Stellen des Berechnungsbaums das Orakel befragen. Dazu schreibt es $(T', w', \text{#}^{k'}$ auf sein Anfrageband. $k' \leq p(|w|)$, da $T_N^A$ für diese Anfrage mindestens $k'$ Schritte benötigt. $T$ kann diese Anfrage ohne Orakel selbst berechnen, indem es $T'$ für höchstens $k'$ Schritte simuliert. Da $k' \leq p(|w|)$, benötigt es dafür weiterhin nur polynomiell viele Bandzellen und bleibt eine DTM ohne Orakel. 
  - $T$ kann also $T_N^A$ simulieren und benötigt dafür $\leq q(|w|)$ Bandzellen.
- Frage: wir müssen $q(|w|)$ spezifizieren, da wir eine feste obere Schranke für die Anzahl der Bandzellen haben müssen. Sonst wird uns ein "Nein" des Orakels nicht weiterhelfen (das Wort könnte ja für ein noch höheres $k$ angenommen werden). Wie berechnen wir $q$???

## Theorem 6: Es gibt $B$, sodass $P^B \neq {NP}^B$

Beweis:
- Wir definieren ein Problem $L_B$, das auf einem Orakel $B$ basiert, und die beiden Klassen trennt:  
  $L_B = \\{0^n; \exists b \in B: |b| = n \\}$
- Unabhängig des Orakels $B$ ist $L_B$ klar in NP: Für alle $0^*$ Wörter rät die NTM ein passendes $b$ und fragt das Orakel, ob $b$ enthalten ist

Konstruktion von $B$, sodass $L_B \not\in P^B$ durch Diagonalisierung:
- Wir zählen alle möglichen Orakel-DTMs $T$ auf, für die $T^X \in P^X$
- Ordnung durch Folgendes gegeben: $TIME_{T_k}(x) \leq |x|^k + k$
- Die Sprache des Orakels ist induktiv: $B = \bigcup B_i$
- Jedes $B_i$ hat Schranke $n_i$, das die Länge der Elemente in $B_i$ exklusiv beschränkt
- $B_0 = \emptyset, n_0 = 0$
- $n_{i+1} = min \\{m; m > n_i^i + i \text{ und } 2^m > m^{i+1} + i+1\\}$
- Erste $n$: `[0, 2, 5, 28]`, dann Overflow (größer als 21955 und $2^m > m^4 + 4$)
