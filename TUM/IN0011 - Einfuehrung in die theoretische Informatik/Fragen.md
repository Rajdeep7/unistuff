# Grundbegriffe

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




