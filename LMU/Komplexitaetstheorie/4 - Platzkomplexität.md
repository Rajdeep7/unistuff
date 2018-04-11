# Platzkomplexität
- Eingabe und Ausgabe wird nicht mitgezählt
- Eingabeband read-only, Ausgabeband (bei Übersetzern) write-only, Ausgabekopf kann nicht nach links
- Arbeitsbänder = restliche Bänder

### Für Akzeptoren
- $SPACE_T(x) = $ maximale Anzahl der auf allen Arbeitsbändern irgendwann während der Berechnung genutzten Zellen
- $NSPACE_T(x) = $ minimaler Platzbedarf einer akzeptierenden Berechnung oder allgemeines Minimum für $x \not\in L(T)$

Eine $SPACE(S(n))$ Maschine kann für mindestens $2^\Omega(S(n))$ Schritte laufen (z.B. ein binärer Counter).

$DTIME(S(n)) \subseteq SPACE(S(n))$, da zu jedem Schritt nur eine Zelle pro Band beschrieben werden kann.

$SPACE(S(n)) \subseteq DTIME(2^{\mathcal{O}(S(n))})$ und $NSPACE(S(n)) \subseteq DTIME(2^{\mathcal{O}(S(n))})$

## Platzkomplexitätsklassen
- $L = \\{A; \exists \text{ DTM } T: L(T) = A \text{ und } SPACE_T(x) = \mathcal{O}(\log |x|) \\}$
- $PSPACE = \\{A; \exists \text{ DTM } T: L(T) = A \text{ und } SPACE_T(x) = (\log |x|)^{\mathcal{O}(1)} \\}$
- $NL = \\{A; \exists \text{ NTM } T: L(T) = A \text{ und } SPACE_T(x) = \mathcal{O}(\log |x|) \\}$
- $NPSPACE = \\{A; \exists \text{ NTM } T: L(T) = A \text{ und } SPACE_T(x) = (\log |x|)^{\mathcal{O}(1)} \\}$
- $FL = \\{F: \Sigma^\* \times \Sigma^\*; \text{berechenbar mit }SPACE = \mathcal{O}(\log |x|)$

Mindeste sinnvolle Platzkomplexitätsklasse ist $L$, da die Maschine das Input-Tape lesen muss. Um den letzten Index des gelesenen Input-Tapes zu darzustellen, braucht man $\log |x|$ Zellen. Da dieser Index in einer gewöhnlichen Berechnung auch irgendwo vermerkt / gespeichert wird, braucht die Maschine mindestens $\log |x|$ Zellen.

## Erreichbarkeitsproblem / REACH
- Geg: gerichteter $G = (V, E)$, $s, t \in V$
- Frage: Ist $t$ von $s$ aus erreichbar?
- Ist in P, z.B. Tiefensuche

## $NL \subseteq P$
- NTM $T$ erkennt $x \in A?$ mit $NSPACE_T(x) = k\cdot \log |x|$
- $G(x)$ ist der Graph **globaler** Zustände bei Eingabe $x$
- $x \in A \iff (G(x), s_0, t(x)) \in REACH$ (O.b.d.A gehen wir von einem akzeptierenden Zustand für $x$ aus)
- $|G(x)| = \mathcal{O}(|x|^{k+2})$: 
  - Ein globaler Zustand besteht aus den Inhalten aller Bänder, den Kopfpositionen und dem aktuellen Zustand (konstant)
  - Jede der $k\cdot \log |x|$ genutzten Zellen kann eines von $c$ verschiedenen Symbolen enthalten. Es ergeben sich $c^{k\cdot \log |x|} = \mathcal{O}(|x|^k)$ verschiedene Zustände eines Bandes / aller Bänder
- $REACH(G(x), s_0, t(x)) \in P$
  
## $NP \subseteq PSPACE$
- Das Durchsuchen des Berechnungsbaumes von der NTM im Beweis $NP \subset EXP$ benötigt nur polynomiell viel Platz

## Landkarte
$L \subseteq NL \subseteq P \subseteq NP \subseteq PSPACE \subseteq NPSPACE \subseteq EXP$

## Satz von Savitch
> REACH kann von DTM mit Platz $\mathcal{O}(\log^2 n)$ entschieden werden.

Beweis:
- Rekursive Aufrufe von $REACH(u, v, j)$, wobei $j$ die maximale Anzahl von Schritten ist.
- Bei der Rekursion werden alle von $u$ erreichbaren Knoten auf Erreichbarkeit von $v$ geprüft.
- Im Worst-Case ist der Weg von $s$ nach $t$ $|V|-1$ Kanten lang. Dann hätte die Rekursion $\mathcal{O}(n)$ Aufrufe. 
- Der Trick ist hier, einen Pfad $(1,2,3,4,5,6,7,8,9)$ in $(1,5,7,8,9)$ zu unterteilen, indem man die maximale Anzahl von Schritten pro Aufruf halbiert. Dann kommt die $2$ nicht in Frage, weil sie zur $1$ und zur $9$ je nur $8/2 = 4$ Schritte brauchen darf
- `REACH(u, v, j)` berechnet, ob $u\rightarrow v$ in $\leq 2^j$ Schritten möglich ist:

```
REACH(u, v, j):
  if (j == 0):
    return u == v or (u, v) in E
  else:
    for w in V:
      if REACH(u, w, j-1) and REACH(w, v, j-1):
         return true
    return false
```

- `REACH(s, t, ceil(log(|V|))` liefert korrektes Ergebnis, da der direkte Weg $\leq |V| \leq 2^{\lceil \log |V| \rceil}$ Schritte beinhaltet
- Platzkomplexität:
  - TM muss nur den Aufrufstack speichern -> $\leq \lceil\log n \rceil$ Einträge
  - Ein Eintrag beinhaltet $u, v$ und $i$. Jeder Knoten kann mit $\lceil \log n \rceil$ Zellen kodiert werden. Ein Eintrag braucht also $\mathcal{O}(\log n)$ Zellen
  - $\lceil \log n \rceil \cdot \mathcal{O}(\log n) = \mathcal{O}(\log^2 n)$

## NPSPACE = PSPACE

Beweis:
- NTM erkennt mit $SPACE(x) = |x|^k$
- Globaler Zustandsgraph hat Größe $2^{|x|^{k+2}}$
- REACH auf Zustandsgraph benötigt Platz $\mathcal{O}(\log^2 2^{|x|^{k+2}}) = \mathcal{O}(|x|^{2k+4})$

# Vollständige Probleme in NL, P und PSPACE
- $p$-Reduktion macht in $P$ wenig Sinn, da fast jedes Problem $B$ $P$-schwer ist unter $\leq_P$. Die Funktion überprüft einfach, ob $x \in A$ oder nicht und gibt dann ein $b \in B$ oder ein $\overline b \not \in B$ zurück.

### Definition
- $A$ ist logspace-reduzierbar auf $B$ ($A \leq_{\log} B$), falls es eine funktion $f \in FL$ gibt mit $\forall x: x \in A \iff f(x) \in B$
- Für $P$-schwer und $NL$-schwer wird $\leq_{\log}$ verwendet
- Wir müssen beweisen, dass $\leq_{\log}$ transitiv ist!

## $f \in FL, g \in FL \Rightarrow g \circ f \in FL$
- Naiver Ansatz, der zuerst $f(x)$ berechnet funktioniert nicht, da das Ergebnis irgendwo gespeichert werden muss und $\gt \mathcal{O}(\log |x|)$ Zellen benötigen könnte

Beweis:
- Bänder der zusammengesetzten TM:
  - Input x
  - Arbeitsbänder von $T_f$
  - Zähler 
  - Zwischenergebnis y
  - i
  - Arbeitsbänder von $T_g$
  - Output
- Idee: in $y$ wird stets nur ein Symbol von $f(x)$ gespeichert
- Die Maschine simuliert $T_g$. Wenn $T_g$ ein Symbol von $f(x)_i$ anfordert (es kann immer nur eins gleichzeitig lesen):
  - $i$ auf dediziertes Band schreiben
  - Zähler auf 0 setzen und $y$ und Arbeitsbänder von $T_f$ löschen
  - $T_f$ simulieren. Wenn $T_f$ auf sein Output-Band schreiben würde, stattdessen auf y schreiben. Wenn $T_f$ seinen Output-Kopf nach rechts verschiebt, Zähler inkrementieren. Falls Zähler > i, ist $y = f(x)_i$ und $T_g$ kann weiter machen. Ansonsten, muss $y$ auf blank gesetzt werden und $T_f$ macht weiter, bis i irgendwann erreicht ist.
- Platzkomplexität:
  - $SPACE_{T_f}(x)$
  - Zähler und i benötigen jeweils $\log |x|$ Zellen, $y$ benötigt 1. ??? Woher kommt das log x Zellen? Wenn f(x) = x!, dann ist für x=10 f(x) 3.6 mio - in binär brauchen wir dafür 22 zellen, was log 10 ist. Andererseits wäre $T_f$ für eine solche Funktion nicht in $\log |x|$, da es irgendwie seinen Output-Zähler und Zwischenergebnisse speichern muss.
  - $SPACE_{T_g}(f(x))$
  - Insgesamt $\mathcal{O}(log |x|)$ q.e.d
