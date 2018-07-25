# 2 - Grundbegriffe

### Definiere Alphabet
Endliche Menge, die die Zeichen enthält, aus denen Wörter gebildet werden.

### Definiere Wort
Endliche Folge von Zeichen aus $\Sigma$

### Definiere eine formale Sprache
Mit Alphabet (endliche Menge an Zeichen) $\Sigma$ und Wort definiert als endliche Folge von Zeichen aus $\Sigma$, $\Sigma^\*$ ist die Menge aller Wörter über $\Sigma$, inklusive des leeren Wortes $\epsilon$. Eine formale Sprache ist dann eine Teilmenge $L \subseteq \Sigma^*$.

### Definiere die Konkatenation zweier Sprachen A und B
$AB = \\{ uv | u \in A \land v \in B\\}$

### Definiere $A^*$ und $A^+$
- $A^0 = \\{\epsilon\\}$
- $A^n = A ... A (n mal)$
- $A^* = \bigcup_{n \in \mathbb{N}} A^n$
- $A^+ = \bigcup_{n \geq 1} A^n$

### Für welche Operation auf Sprachen gilt das Distributivgesetz?
Für die Vereinigung: 
- $A(B \cup C) = AB \cup AC$
- $(B \cup C)A = BA \cup CA$

### Was ist $\emptyset A$ und $\\{\epsilon\\}A$?
$\emptyset$ und $A$

## Grammatiken

### Definiere eine Grammatik 
- $G = (V, \Sigma, P, S)$
- V = Nichtterminale
- $\Sigma$ = Terminale / Alphabet
- $P \subseteq (V \cup \Sigma)^* \times (V \cup \Sigma)^*$ = Produktionen
- $S \in V$ ist das Startsymbol

### Definiere die Ableitungsrelation
Ableitungsrelation $\rightarrow_G$ 
- auf Wörtern $\alpha \rightarrow_G \alpha'$ über $V \cup \Sigma$
- $\alpha \rightarrow_G \alpha'$
- gdw es eine Regel $\beta \rightarrow \beta'$ in P und Wörter $\alpha_1, \alpha_2$ gibt, so dass
- $\alpha = \alpha_1 \beta \alpha_2$ und $\alpha' = \alpha_1 \beta' \alpha_2$

Ableitung: $\alpha_1 \rightarrow_G \alpha_2 \rightarrow_G ... \rightarrow_G \alpha_n$

### Definiere die Sprache einer Grammatik
- Erzeugung: $\alpha_1 = S$ und $\alpha_n \in \Sigma^*$ -> $G$ erzeugt das Wort $\alpha_n$
- Sprache: Menge aller Wörter, die von G erzeugt werden
- $L(G) = \\{w \in \Sigma^* | S \rightarrow_G^* w\\}$

### Definiere die reflexive transitive Hülle einer Grammatik
- $\alpha \rightarrow_G^0 \alpha$
- $\alpha \rightarrow_G^{n+1} \gamma \iff \exists \beta. \alpha \rightarrow_G^n \beta \rightarrow_G \gamma$
- $\alpha \rightarrow_G^* \beta \iff \exists n. \alpha \rightarrow_G^n \beta$

### Definiere die Typen der Chomsky Hierarchie
G ist vom Typ
- 0 immer
- 1 falls $|\alpha| \leq |\beta|$ für jede Produktion $\alpha \rightarrow \beta$ unterschiedlich von $S \rightarrow \epsilon$
- 2 falls G vom Typ 1 und $\alpha \in V$ für jede Produktion $\alpha \rightarrow \beta$
- 3 falls G vom Typ 2 und $\beta \in \Sigma \cup \Sigma V$ für jede Produktion $\alpha \rightarrow \beta$ unterschiedlich von $S \rightarrow \epsilon$

### Was sind die Namen der Grammatiken und Sprachen der Chomsky Hierarchie?
- 0 -> Phrasenstrukturgrammatik, Rekursiv-aufzählbare Sprache
- 1 -> Kontextsensitive Grammatik, Kontextsensitive Sprache
- 2 -> Kontextfreie Grammatik, Kontextfreie Sprache
- 3 -> Rechtslineare Grammatik, Reguläre Sprache

### Was ist das Wortproblem?
Gegeben eine Grammatik G und ein Wort w, gilt $w \in L(G)$

# 3 - Reguläre Sprachen

## 3.1 - DFAs

### Definiere einen DFA
DFA M = $(Q, \Sigma, \delta, q_0, F)$
- $Q$ = endliche Menge von Zuständen
- $\Sigma$ = Eingabealphabet
- $\delta : Q \times \Sigma \rightarrow Q$ = Übergangsfunktion
- $q_0 \in Q$ = Startzustand
- $F \subseteq Q$ = Menge an Endzuständen

### Definiere die akzeptierte Sprache eines DFAs
$\hat \delta : Q \times \Sigma^* \rightarrow Q$ definiert als:
- $\hat \delta (q, \epsilon) = q$
- $\hat \delta (q, aw) = \hat \delta(\delta(q, a), w)$ für $a \in \Sigma, w \in \Sigma^*$

$L(M) = \\{w \in \Sigma^* | \hat \delta (q_0, w) \in F \\}$

### Zeige, dass es für jeden DFA $M$ eine rechtslineare Grammatik $G$ mit $L(G) = L(M)$ gibt
$M = (Q, \Sigma, \delta, q_0, F)$
- $G = (V, T, P, S)$
- $V = Q, T = \Sigma, S = q_0$
- $(q_1 \rightarrow a q_2) \in P \iff \delta(q_1, a) = q_2$
- $(q_1 \rightarrow a) \in P \iff \delta(q_1, a) \in F$
- $(q_0 \rightarrow \epsilon) \in P \iff q_0 \in F$

Daraus folgt:
- $\hat{\delta}(q_0, a_1 ... a_n) \in F$  
- gdw  
- $q_0 \rightarrow_G a_1 q_2 \rightarrow_G a_1 a_2 q_3 \rightarrow_G ... \rightarrow_G a_1 ... a_n q_n \rightarrow_G a_1 ... a_n$ eine Ableitung von $G$ ist.
- $\Rightarrow L(G) = L(M)$

### Definiere einen NFA
DFA N = $(Q, \Sigma, \delta, q_0, F)$
- $Q$ = endliche Menge von Zuständen
- $\Sigma$ = Eingabealphabet
- $\delta : Q \times \Sigma \rightarrow \mathcal{P}(Q)$ = Übergangsfunktion
- $q_0 \in Q$ = Startzustand
- $F \subseteq Q$ = Menge an Endzuständen

### Definiere die akzeptierte Sprache eines NFAs

### Zeige, dass es für jede rechtslineare Grammatik $G$ einen NFA $N$ mit $L(G) = L(M)$ gibt

### Zeige, dass es für jeden NFA $N$ einen DFA $M$ mit $L(G) = L(M)$ gibt

### Definiere einen $\epsilon$-NFA












