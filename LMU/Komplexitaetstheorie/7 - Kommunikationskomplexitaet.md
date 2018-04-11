# Kommunikationskomplexität

### Protokoll
- Wer sendet wann welches bit -> abhängig von berechneter Funktion
- Was ist Output
- Komplexität = Höhe des Baums
- Kommunikationskomplexität = minimales Protokoll

## Obere Schranken
- $\log |X| + \log |Z|$

## Untere Schranken

### Definitionen
- $R_v$ = Inputs, die $v$ erreichen
- $\\{ R_l; l \in \text{Leaves} \\}$ = Partition von $X \times Y$
- Rechteck $R = A \times B$ für $A \subseteq X, B \subseteq Y$
  - Beliebiger Swap von $x$s und $y$s -> immer noch in $R$
- Einfarbiges $R$ = alle haben denselben Wert $z$
- Fooling Set $S$ = einfarbig und Swaps auf den Indizes führen immer zu anderen Farben

### log |ran f|
ran f = mit x, y erreichbare Ausgabewerte z

### $R_v$ ist immer ein Rechteck

### Kleinste Partition
- Hat t einfarbige Rechtecke (bzgl. f)
- $\geq \log t$

### Fooling Sets
- Kein Rechteck enthält zwei Tupel des Fooling Sets
- Also mindestens t Rechtecke, um S zu überdecken
- $\geq \log t$

### Rang
- Rang(f) = Rang der Belegungsmatrix $M_f$
- Für jedes positive Blatt $l$ ist $M_l$ die Matrix mit dem Input-Rechteck als 1 markiert
- $M_l$ ist Rechteck -> Rang 1
- $M_f$ ist Summe aller $M_l$s
- Rang einer Matrix ist nie größer als die Summe der Ränge ihrer Summandenmatrizen
- $Rang(f) \leq |L_1| \leq |L|$
- $\geq \log Rang(f)$

Mit Rang von negative Blätter zeigt man
- $\geq \log (2 Rang(f) - 1)$

## Relationen
- $(x, y, P(x,y)) \in R$
- Menge $M \subseteq X \times Y$ ist für $R$ einfarbig, falls alle Tupel aus M das z in $(x, y, z) \in R$ immer gleich ist

$R_+ = $ Tupel (x, y), die sich in einem Bit unterschieden
- Bit finden
- Suchbereich schrittweise halbieren
- Pro Schritt schauen, ob parity der ersten Hälfte gleich ist 
  - Falls ja, in zweiter Hälfte weitersuchen
  - Falls nein, in erster Hälfte weitersuchen
- log n Runden, Pro Runde 2 bits Kommunikation

## Untere Schranke Hamming Distanz
- Inputs sind Tupel mit Hamming Distanz 1 - zusammengefasst in Menge C
- Output ist Index des verschiedenen Bits
- Jede Partition von $X \times Y$ in einfarbige Rechtecke hat mindestens $\frac{|C|^2}{|X||Y|}$ Rechtecke
