# Frequent Itemset Mining
### Frequent Itemset Mining
Itemsets, die häufig zusammen vorkommen (mindestens x Support)

### Association Rule Mining
Regeln / Korrelationen zwischen Itemsets

## Apriori Algorithmus
- Subsets von frequent sind auch frequent -> rechtfertigt Join Step auf frequent k-itemsets
- Supersets von non-frequent sind auch non-frequent -> rechtfertigt Prune Step

### Algorithmus: Scan, Filter, Join, Prune, Repeat
- Starte mit 1-itemsets (Kandidaten sind offensichtlich)
- Joine nur die k-itemsets, die die gleichen ersten k-1 Elemente haben
- Prune nur mit den k-1-itemsets
  
### 1.  Performance Probleme mit Filter
- Große Anzahl an Kandidaten
- Große Anzahl an Kandidaten, die in einer Transaktion enthalten sind

Lösung: Hash-Tree

### 2. Performance Problem mit Join!

## Lösung: Frequent-Pattern Tree

1. Scanne nach frequent 1-Itemsets / Items -> Werden die Knoten des Baums sein (Wurzel ist leere Menge)
2. Sortiere die frequent Items absteigend nach Frequenz
3. Extrahiere die sortierten frequent Items aus jeder Transaktion  
  Für jede Reihenfolge von sortierten Items:
    - Wenn es einen Pfad im Baum gibt, der mit denselben Knoten beginnt, erhöhe den Count von allen Knoten
    - Füge einen neuen Pfad hinzu, sobald es kein überschneidendes Präfix mehr gibt
4. Speichere eine Header Table, die Referenzen zu allen Frequent Items im Baum hält (Item, Frequency, Head of Linked List)

Vorteile:
- Vollständig
- Enthält keine Infrequent Items
- Frequency descending ordering -> Höhere Wahrscheinlichkeit, das Pfade im Baum geteilt werden
- Experimente: Compression Ratios über 100

Problem: Enthält immer noch non-frequent itemsets in den Pfaden!

## Frequent Pattern Growth

Für jedes Item:
1. Conditional Pattern Base (Präfixe im Baum) definieren, Wert für Präfix direkt vom Knoten nehmen
2. Conditional FP-Tree bauen
  1. Base in Items unterteilen und Frequency jedes Items zählen, falls < minSup ignorieren
  2. Dieser Schritt ist wie der Initialisierungschritt, aber läuft nur auf den Transaktionen in der Pattern base
3. Bis alle FP-Trees leer oder Listen sind -> Dann Potenzmenge der Liste als frequent patterns aufzählen (geordnet)

Ist 10x schneller weil:
- Keine Candidate Generation
- Kein Candidate Test
- Kompakte Datenstruktur
- Kein wiederholter DB-Scan

### Closed Frequent Itemset
- Es gibt kein echtes super-itemset, das denselben Support hat.

### Maximal Frequent Itemset
- Es gibt kein echtes super-itemset, das einen Support >= minSup hat
- Kann also nicht von einem super-itemset hergeleitet werden

## Association Rules
- Association Rule: X => Y mit X u Y != null in D -> Muss support haben
- Support = support(X u Y) / |D|
- Confidence = support(X u Y) / support(X)

Given: minSup, minConf
1. Finde frequent Itemset mit minSup
2. Teile alle Itemsets in zwei nicht-leere Teile auf -> Rule Candidates
3. Berechne für jeden Kandidat A => B die Confidence = support(A u B) / support(A)

## Problems with Suppport and Confidence
5000 students
- 3000 play basketball
- 3750 eat cereal
- 2000 play basketball and eat cereal

Solution: Correlation
= P(A u B) / (P(A) P(B))
= support(A u B) / (support(A) support(B))

## Hierarchical Association Rules
- Reduce the number of association rules by exploiting taxonomies
- Eliminate trivial association rules X => Y, where any item in Y is an ancestor of any item in X (jackets => clothes)  
  -> Generalized association rules remain
- Support of generalizations is higher than support of descendants  
  If jeans => boots exceeds minsup, so does clothes => boots
  
## Mining Multi-Level Associations

### Top Down, Progressive Deepening 
- Start with high-level strong rules (milk => bread)
- Then find lower-lever weaker rules (1.5 milk => baguette)
- Optionally reduce the support threshold for lower levels

## Multidimensional and Quantitative Association Rules
- Age 19-25 and status is student => buys coke
- With or without repeated dimensions (..., buys popcorn -> buys coke)

Quantitative Attributes (Age):
- Static discretization (before mining)
- Dynamic discretization (during mining, maximizing the confidence)
- Distance-based association rules
