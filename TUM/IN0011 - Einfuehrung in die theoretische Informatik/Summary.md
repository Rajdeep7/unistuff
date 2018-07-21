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
