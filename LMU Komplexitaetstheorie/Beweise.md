# Kapitel 2

## $P \subset E$

## $E \subset EXP$

## $EXP \subset 2E$

## $NP \subseteq EXP$

## $NE \subseteq 2E$

## $P = co-P$, $E = co-E$

## $NP \neq co-NP \Rightarrow P \neq NP$

## $P=NP \Rightarrow E=NE$

# Kapitel 3

## VERTEX COVER ist NP-vollständig

## Ist $L \triangle L'$ endlich, so ist $L \in P$ gdw. $L' \in P$

## Es gibt Orakel $A$ mit $P^A = NP^A$

## Es gibt Orakel $B$ mit $P^B \neq NP^B$

## Es gibt Orakel $C$ mit $NP^C = co-NP^C$ und $P^C \neq co-NP^C$

## Es gibt Orakel $D$ mit $NP^D \neq co-NP^D$ und $P^D = NP^D \cap co-NP^D$

## Es gibt Orakel $E$ mit $NP^E \neq co-NP^E$ und $P^E \neq NP^E \cap co-NP^E$

# Kapitel 4

## $NL \subseteq P$, $NPSPACE \subseteq EXP$

## $NP \subseteq PSPACE$

## Reihenfolge von $EXP, NL, NPSPACE, NP, P, PSPACE, L$

## Satz von Savitch

## NPSPACE = PSPACE

## FL ist unter Komposition abgeschlossen

## REACH ist NL-vollständig

## 2-SATZ ist NL-vollständig

## HORN $\in$ P

## HORN ist P-vollständig

## QBF ist PSPACE-vollständig

## co-NL = NL / notREACH $\in$ NL

# Kapitel 5

## $\Sigma^P_{i+1} = NP^A$, falls $A$ vollständig für $\Sigma^P_i$

## Polynomielle Hierarchie Verhältnisse beweisen

## $\Sigma^P_{i+1} = NP^{\Pi^P_i}$

## PH $\subseteq$ PSPACE

## Proposition 2

## Falls $\Sigma_k^P = \Pi_k^P$, so kollabiert die PH auf Stufe $k$

## AP = PSPACE

## AL = P

## Für $1\leq \alpha \lt \beta$ ist $NTIME(n^\alpha) \subset NTIME(n^\beta)$

## $DTiSp(n^\alpha, n^\beta) \subseteq \Sigma_2\text{-TIME}(n^{\frac{\alpha+\beta}{2}})$

## $NLIN \not\subseteq DTiSp(n, n^\epsilon)$ für jedes $\epsilon < 1$

## $NLIN \not\subseteq DTiSp(n^\alpha, (\log n)^k)$ für alle $k \geq 1$ und $\alpha \lt \sqrt 2$

# Kapitel 6

## PSIZE = P/poly

## Falls SAT $\in$ P/poly, dann ist $\Sigma^P_2 = \Pi^P_2$

## Jeder monotone Schaltkreis, der $\Delta$ berechnet hat die Größe $\Omega(\frac{n^3}{\log^4 n})$

## Für $k$-Approximator $A$ mit $A \not\equiv 0$ ist die Zahl der $\vec{x} \in T_{-}$ mit $A(\vec{x}) = 1$ mindestens $2^{n-2}$

## Sei $S$ ein Stern mit $k$ Kanten. Dann ist die Anzahl der $x \in T_-$, die disjunkt zu $S$ sind, $2^{n-k-1}$.

## Sei $M$ ein Matching mit $k$ Kanten. Dann ist die Anzahl der $x \in T_-$, die diskunkt zu $M$ sind, $2^{n-k-1}$.

## Jeder Graph mit $m$ Kanten enthält entweder einen Stern oder ein Matching mit $\sqrt{m/2}$ Kanten

## Sei G=(V,E) mit |E|=m beliebig. Dann ist die zahl der $x \in T_-$ disjunkt zu G höchstens $2^{n-\sqrt{m/2}-1$

## Die Anzahl der $x \in T_-$ mit $A_1(x) \lor A_2(x) = 0$ und $A_1 \cup A_2(\vec{x}) = 1$ ist höchstens $2^{n-\sqrt{k/2}-1}$

## Die Anzahl der $x \in T_+$ mit $A_1(x) \land A_2(x) = 1$ und $A_1 \cap A_2(\vec{x}) = 0$ ist höchstens $k^2$

## parity kann nicht von Schaltkreisen der Größe $p(n)$ und Tiefe $d$ berechnet werden für konstante $d$ und Polynom $p(n)$, i.e. parity $\not\in AC^0$.

## Ist $\bigvee(x_1, ..., x_n) = 1$, dann ist $Pr[p(x_1,...,x_n) = 0] \leq 0.5$

## Es gibt kein Polynom $q(y_1, ..., y_n)$ vom Grad höchstens $\frac{\sqrt{n}}{2}$ mit $q(y_1, ..., y_n) = \Pi^n_{i=1} y_i$ für $0.9 \cdot 2^n$ der möglichen $\vec{y} \in \{-1, +1\}^n$

# Kapitel 7

## Für alle $f: X \times Y \rightarrow Z$ ist $cc(f) \leq \log |X| + log |Z|$

## $cc(MED) \leq \mathcal{O}(\log n)$

## $cc(f) \geq \log |ran f|$

## Für Knoten $v$ in $P$ ist $R_v$ ein Rechteck

## Falls jede Partition von $X \times Y$ in $f$-einfarbige Rechtecke mindestens $t$ Rechtecke enthält, dann ist $cc(f) \geq \log t$

## Falls $f$ ein Fooling Set der Größe $t$ hat, ist $cc(f) \geq \log t$
