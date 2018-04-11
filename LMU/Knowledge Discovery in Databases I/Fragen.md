## 1 - Einleitung

### Was sind die 5 Schritte im Knowledge Discovery Prozess? Nenne jeweils die involvierten Schritte
1. Data Cleaning und -Integration
   - Rauschen
   - Inkonsistenzen
   - Fehlende Werte
2. Transformation, Selection, Projection
   - Normalisieren
   - Diskretisieren
3. Data Mining
   - Frequent Pattern Mining
   - Clustering
   - Classification / Regression
   - Generalization Levels (Aggregation)
   - Outlier Detection
   - Trends Analysis
4. Evaluation
5. Wisssensrepräsentation

### Nenne 7 Data Mining Kategorien
1. Frequent Pattern Mining
2. Clustering
3. Classification
4. Regression
5. Generalization Levels (Aggregation)
6. Outlier Detection
7. Trends Analysis

### Wie unterscheidet man unsupervised und supervised Learning?
Bei supervised sind die Target Values (Klassen etc.) a priori bekannt und es existieren Trainingsdaten.

## 2 - Datenrepräsentation

### Nenne drei Arten von atomaren Datentypen. Wie genau sind sie definiert?
1. Kategorisch / Nominal
   - Nur gleich / ungleich
   - Kein besser oder schlechter
2. Ordinal
   - Kein einheitlicher Abstand, aber totale Ordnung
3. Metrisch / Interval
   - Differenzen und Verhältnisse sind aussagekräftig
   - Kann diskret oder stetig sein

### Welche drei Eigenschaften hat eine Totale Ordnung?
- transitiv
- antisymmetrisch
- abgeschlossen

### Welche vier Eigenschaften hat eine Metrische Distanzfunktion?
- reflexiv (x,x = 0)
- symmetrisch
- strikt (0 => x = y)
- Dreiecksungleichung

### Wie ist die Covarianz definiert?
$Cov(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)]$

### Wie ist der Korrelationskoeffizient definiert?
$\rho_{X,Y} = \frac{cov(X, Y)}{\sigma_X \sigma_Y}$

### Was gibt der $\chi^2$ - Koeffizient an?
Differenz zwischen der bei Unabhängigkeit erwarteten und der tatsächlich beobachteten Häufigkeit

### Wie ist der $\chi^2$ - Koeffizient definiert?
$\chi^2 = \sum_{i \in X} \sum_{j \in Y} \frac{(o_ij - e_ij)^2}{e_ij}$
- $o_ij$ = beobachtete Häufigkeit
- $e_ij$ = erwartete Häufigkeit = $n \cdot P_i \cdot P_j$

### Wie berechnet man die z-score Normalisierung?
$v' = \frac{v - \mu}{\sigma}$

### Erkläre drei Distanzfunktionen für Mengen
- Symmetrische Differenz $A \triangle B = A \cup B - A \cap B$
- Jaccard Distanz $d(A, B) = \frac{A \triangle B}{A \cup B}$
- Hamming Distanz mit Basismenge C - Zähle binär die Matches in (A, C) und (B, C) und berechne die Summe der unterschiedlichen Einträge

### Nenne eine Distanzfunktion für Vektoren
p-Norm auf $a - b$: $d_p(a, b) = \sqrt[p]{\sum_i |a_i - b_i|^p}$

### Nenne drei Features für Bilder
- Farbhistogramme
- Textur 
- Formen (Sektorenmodell)

### Wie berechnet man das Sektorenmodell? Wie das Schalenmodell?
- Sekoren -> Anzahl der Punkte im Sektor
- Schalen -> Schalen um den Mittelpunkt -> Anzahl der Punkte pro Schale

### Nenne zwei Distanzen für Farbhistogramme
1. Euklidische Distanz
2. Euklidische Distanz multipliziert mit Ähnlichkeitmatrix $A$ zwischen den einzelnen Bins  
   $d(P, Q) = \sqrt{(h_P - h_Q) A (h_P - h_Q)^T}$

### Nenne vier Farbräume
- RGB
- CMY
- HSV (Hue, Saturation, Value) - Rechteck
- HLS (Hue, Luminance, Saturation) - Dreieck

### Nenne 5 Probleme und jeweils eine Lösung bei Text Mining
Probleme
1. Nutzlose Wörter
2. Wörter mit gleichem Wortstamm
3. Hochdimensionale Featureräume
4. Unterschiedliche wichtige Terme
5. Sparse feature space

Lösungen
1. Stopwords
2. Stemming / Lemmatization
3. Auswahl der wichtigsten Terme / Features:  
  - Sehr häufige und sehr seltene Terme sind keine guten Discriminators
  - Sortiere Terme absteigend nach Dokumentenhäufigkeit DF, um Rang zu ermitteln
  - Sortiere dann absteigend nach Rang $\cdot$ DF
4. Gewichte Terme mit TF-IDF:
  - Gewichte häufige Terme in einem Dokument
  - Gewichte seltene Terme
  - $TF(t, d) = $ relative Häufigkeit von $t$ in $d$
  - $IDF(t) = \frac{|D|} {\\{d | d \in D \land t \in d \\}}$
  - $TF_IDF(t, d) = TF(t, d) \cdot IDF (t)$
  - Feature Vektor für Dokument besteht aus Tf-idfs für jeden Term des Corpus
5. Nicht Euklidische Distanz verwenden
  - Jaccard Coefficient: $d(D_1, D_2) = \frac{|D_1 \triangle D_2|}{|D_1 \cup D_2|}$
  - Cosinus Ähnlichkeit: 
    - Ähnlichkeit für Wortvektoren (z.B. von Tf-idf)
    - $\cos(\theta) = \frac{a \cdot b}{||a|| ||b||}$

### Nenne drei Möglichkeiten, d-dimensionale Datensätze zu visualisieren
- Scatter plots von allen Feature-Paaren
- Parallel Coordinates 
  - Jede Achse ist eine Dimension, jedes Sample ist eine horizontale Linie
  - Sortierung wichtig (Clustererkennung vs. Korrelationserkennung)
- Spiderweb 
  - Wie Parallel Coordinates, aber Features sind Spinnennetz
  
### Nenne drei Formen der Daten Reduzierung und jeweils die verwendeten Methoden
- Numerosity reduction 
  - Sampling
  - Aggregation (Mean, Variance, STD etc.)
- Dimensionality reduction
  - t-SNE, PCA, MDS, Random Projections etc.
- Discretization 
  - Binning / Histogram
  
### Erkläre drei verschiedene Formen von Aggregatsfunktionen
1. Distributive Aggregationsfunktionen
   - Das Resultat der Funktion für n aggregierte Werte ist identisch mit dem angewendet auf alle Daten
   - sum, min, max, count
2. Algebraische Aggregationsfunktionen
   - Algebra auf distributiven AF: avg = sum / count etc.
3. Holistische Aggregatsfunktionen
   - Median, Modus, Rang / Quantile
   
### Erkläre 5 Central Tendency Maße
- Mid-range = (max + min) / 2 
  - nur für numerisch
- Mean 
  - nur für numerisch
- Median 
  - auch für ordinal
  - less sensitive to outliers
- Medoid
  - metric data, because it depends on distance function
  - when centroid can't be defined (graphs)
  - when centroid is not representative (images)
- Modus

### Wie berechnet man das p-Quantil?
- Falls $np$ ganzzahlig: Mittelwert von x an Stelle np und x an Stelle np+1
- Falls nicht: x an Stelle `floor(np+1)`

### Was ist der Nachteil von Equiwidth und was der von Equiheight Histogrammen?
- Equiwidth: Outlier dominieren
- Equiheight: Häufige Werte verursachen unterschiedliche Höhe, nicht so intuitiv wie Equiwidth

### Was ist ein Data Cube?
- Wird bei Online Analytical Processing verwendet
- Kanten des Cubes sind Dimensionen
- Zellen sind Werte / Kennzahlen: F(Produkt, Zeitraum, Region) = Umsatz

### Wie ist 1NF definiert?
Jedes Attribut hat einen atomaren Wertebereich -> keine komplexen Datentypen / mehrere Attribute in einem etc.

### Wie ist 2NF definiert?
Jedes nicht-primäre Attribut ist von **allen** Schlüsseln abhängig + 1NF

### Wie ist 3NF definiert?
Alle Attribute hängen direkt vom Schlüssel ab und nicht transitiv (CD_ID -> Interpret -> Gründungsjahr). Um Verletzungen zu lösen, können neue Tabellen mit ID-Attributen erzeugt werden (Interpred_ID). + 2NF

### Was ist der Unterschied zwischen Star und Snowflake Schema?
Star Schema
- Eine Faktentabelle in der Mitte enhält eine Spalte pro Dimension (ArtikelID) und eine pro Kennzahl
- Für jede Dimension gibt es eine Klassifikationstabelle, die z.B. Attribute zu Artikeln speichert
- Nicht normalisiert, redundant, dadurch effizienter

Snowflake Schema 
- Wie Start, nur in 3NF -> redundanzfrei

### Erkläre 4 OLAP Operationen
- Roll up 
  - Summarize Data
  - By climbing up hierarchy or by dimension reduction
- Drill down
  - Reverse of roll-up
  - Detailed data or introducing new dimensions
- Slice and dice
  - Selection of one or more dimensions
- Pivot
  - Reorient the cube (3D to series of 2D planes, or different ordering of features in table etc.)
  
### Nenne zwei Vorteile von OLAP
- Verschiedene Aggregate als Kennzahlen möglich (count, sum, etc.)
- Generalisierung und Spezialisierung durch roll-up und drill-down

### Nenne zwei Nachteile von OLAP
- Nur simple nonnumeric data oder simple aggregated numeric values
- Keine intelligente Analyse

## 3 - Frequent Itemset Mining

### Was ist der Unterschied zwischen Frequent Itemset Mining und Association Rule Mining?
- FIM -> Itemsets, die häufig zusammen vorkommen (mindestens x Support)
- ARM -> Regeln / Korrelationen zwischen Itemsets

### Welche zwei Eigenschaften von Frequent Itemsets nutzt der Apriori Algorithmus?
1. Subsets von frequent sind auch frequent -> rechtfertigt Join Step auf frequent k-itemsets
2. Supersets von non-frequent sind auch non-frequent -> rechtfertigt Prune Step

### Beschreibe den Apriori Algorithmus
- Scan, Filter, Join, Prune, Repeat
- Starte mit 1-itemsets (Kandidaten sind offensichtlich)
- Joine nur die k-itemsets, die die gleichen ersten k-1 Elemente haben
- Prune die k-itemsets, die ein non-frequent k-1-itemset beinhalten

### Beschreibe zwei Performance Probleme des Apriori Algorithmus und ggf. eine Lösung
1. Beim Scan Step müssen viele Kandidaten gescannt werden. Zudem haben Transaktionen ebenfalls viele Items. Lösung: Hash-Tree
2. Beim Join Step entstehen viele Kandidaten. Lösung: FP Tree

### Beschreibe die Konstruktion eines FP tree
1. Scanne nach frequent 1-Itemsets / Items -> Werden die Knoten des Baums sein (Wurzel ist leere Menge)
2. Sortiere die frequent Items absteigend nach Frequenz
3. Extrahiere die sortierten frequent Items aus jeder Transaktion  
  Für jede Reihenfolge von sortierten Items:
    - Wenn es einen Pfad im Baum gibt, der mit denselben Knoten beginnt, erhöhe den Count von allen Knoten
    - Füge einen neuen Pfad hinzu, sobald es kein überschneidendes Präfix mehr gibt
4. Speichere eine Header Table, die Referenzen zu allen Frequent Items im Baum hält (Item, Frequency, Head of Linked List)

### Nenne vier Vorteile eines FP Tree
- Vollständig
- Enthält keine Infrequent Items
- Frequency descending ordering -> Höhere Wahrscheinlichkeit, das Pfade im Baum geteilt werden
- Experimente: Compression Ratios über 100

### Beschreibe den Frequent Pattern Growth Algorithmus
Gegeben sei der FP Tree

Für jedes Item:
1. Conditional Pattern Base (Präfixe im Baum) definieren, Wert für Präfix direkt vom Knoten nehmen
2. Conditional FP-Tree bauen
  1. Base in Items unterteilen und Frequency jedes Items zählen, falls < minSup ignorieren
  2. Dieser Schritt ist wie der Initialisierungschritt, aber läuft nur auf den Transaktionen in der Pattern base
3. Bis alle FP-Trees leer oder Listen sind -> Dann Potenzmenge der Liste als frequent patterns aufzählen (geordnet)

### Warum ist der FP Growth Algorithmus bis zu 10 mal schneller als der Apriori Algorithmus?
- Keine Candidate Generation
- Kein Candidate Test
- Kompakte Datenstruktur
- Kein wiederholter DB-Scan

### Wie ist ein Closed Frequent Itemset definiert?
Es gibt kein echtes super-itemset, das denselben Support hat.

### Wie ist ein Maximal Frequent Itemset definiert?
- Es gibt kein echtes super-itemset, das einen Support >= minSup hat
- Kann also nicht von einem super-itemset hergeleitet werden

### Wie ist eine Association Rule auf einem Datensatz definiert?
X => Y ist nur gültig, falls support (X => Y) > 0

### Wie ist der Support einer Association Rule X => Y definiert?
support(X u Y) / |D|

### Wie ist die Confidence einer Association Rule X => Y definiert?
support(X u Y) / support(X)

### Wie findet man Association Rules mit minSup und minConf gegeben?
1. Finde frequent Itemset mit minSup
2. Teile alle Itemsets in zwei nicht-leere Teile auf -> Rule Candidates
3. Berechne für jeden Kandidat A => B die Confidence = support(A u B) / support(A)

### Nenne ein Beispiel, das die Probleme von Support und Confidence aufzeigt. Was ist die Lösung?
5000 students
- 3000 play basketball
- 3750 eat cereal
- 2000 play basketball and eat cereal

### Wie ist die Correlation von zwei Itemsets A und B definiert?
= P(A u B) / (P(A) P(B))
= support(A u B) / (support(A) support(B)) (jeder support ist relativ zum Datensatz!!)

### Wozu dienen Hiearchical Association Rules?
- Reduzieren die Anzahl der Association Rules, indem sie Taxonomien nutzen
- Support von Generalisierungen ist immer höher als der von Nachfolgern (jeans => boots < clothes => boots)

### Beschreibe einen Ansatz, um Multi-Level Associations zu minen
- Top Down, Progressive Deepening
- Starte mit hohen, starken Regeln (Milch => Brot)
- Finde von dort aus tiefere, schwächere Regeln (1.5 Milch => Baguette)
- Optional: Support Threshold für tiefere Ebenen reduzieren

### Wie kann ein kontinuierliches Attribut für das Association Rule Mining diskretisiert werden?
- Statisch (bevor das Mining beginnt)
- Dynamisch (während des Minings, Confidence maximierend)
- Gar nicht und Distanz-basierte Rules minen

### Nenne zwei Anwendungen von Frequent Itemset Mining
1. Kunden kauften auch
2. Suchmaschinen

### Was ist eine starke Association Rule?
support >= minSup und confidence >= minConf

## 4 - Clustering

### Nenne vier Clustering Methoden
- Partitioning Algorithms (k partitions, minimize some objective function)
- Probabilistic Model-Based Clustering (EM)
- Density-based (connectivity function)
- Hierarchical algorithms

### Wie definieren Partitioning Methods ein Cluster?
- Cluster = Menge an Punkten mit geringer Abweichung vom Repräsentant
- Cluster = Convexe Partition

### Nenne allgemeine Stärken von Partitioning Methods
- Einfache Implementierung

### Nenne allgemeine Schwächen von Partitioning Methods
- k muss im Voraus spezifiziert werden
- Clusters sind immer Voronoi Cells / Convexe Partitionen
- Ergebnis und Laufzeit hängen stark von initialer Partitionierung ab
- Lokale Optima

### Wie funktioniert k-means (Lloyd)?
- Repräsentant = Mean
- Minimiert SSE

### Nenne Stärken von k-means
- Effizient: O(tkn)
- Einfache Implementierung

### Nenne Schwächen von k-means
- Mean muss definiert sein
- Empfindlich gegenüber Rauschen und Outliern -> Erstellt 1-Element Cluster und reduziert das effektive k

### Wie funktioniert k-means (MacQueen)?
- Centroids werden nach jedem Assignemnt und nach jeder Epoche aktualisiert
- Reihenfolgeabhängig!

### Wie funktioniert k-medoid (PAM, Kaufman)?
- Repräsentant = Punkt in Datensatz
- Medoid = x, das die minimale TD zu allen Punkten hat

Schritte:
1. Zufällige Inits
2. Jeden Punkt assignen und TD berechnen
3. Für alle Swaps zwischen Medoid und Nicht-Medoid neue TD berechnen
4. Falls besserer Swap gefunden wurde, swappen
5. Goto 3

### Wann wird k-medoid verwendet?
Wenn centroid nicht definiert ist (Graphen) oder nicht aussagekräftig (Bilder)

### Was ist die zentrale Schwäche von k-Medoid mit PAM-Kaufman Algorithmus?
Laufzeit = O(tk(n-k)^2)

###  Wie kann die Laufzeit von k-medoid verbessert werden?
CLARANS Algorithm
- Nur `maxneighbor` Swaps pro Iteration testen
- Ersten Swap, der TD verbessert, nehmen
- Nach `numlocal` Iterationen aufhören

### Wie funktioniert k-Median?
Wie k-Means, aber mit TD -> gleiche Komplexität

### Wie funktioniert k-Mode (Huang)?
- Hamming Distanz, um Modus zu bestimmen -> häufigsten Wert jedes Attributs nehmen
- Wie k-Means, aber mit TD -> gleiche Komplexität

### Wie kann die Wahl der initialen Belegung bei Partitioning Methods verbessert werden?
- m verschiedene initiale Belegungen (k Punkte) auswählen
- Alle gewählten Punkte mit allen Belegungen testen -> konvergiert zu bestimmter SSE / TD
- Beste Belegung als Init für gesamten Datensatz nehmen

### Wie kann k für Partitioning Methods getuned werden?
- k=2 bis n-1 testen
- Problem: SSE und TD fallen monoton mit k
- Lösung: Silhouette Koeffizient berechnen

### Wie wird der Silhouette Koeffizient berechnet?
- a(o) = average distance between object o and the objects in its cluster
- b(o) = smallest average distance between o and the objects in another cluster 
- s(o) = 0 if a(o) = 0, i.e. the cluster is a single object
- s(o) = (b(o) - a(o)) / max(a(o), b(o)) -> in [-1, 1]
- silh(C) = average s(o) of objects in cluster / all objects

### Wie wird der Silhouette Koeffizient interpretiert?
- 1 -> gutes Assignment des Punktes
- 0 -> Punkt ist zwischen zwei Clustern
- -1 -> Schlechtes Assignment des Punktes, ist eigentlich näher an einem anderen Cluster

### Was berechnet der EM Algorithmus?
Die Parameter mit Maximum Likelihood

### Wie definiert der EM Algorithmus ein Cluster?
Cluster = Ansammlung an Punkten, die von einer Verteilung aus einer Mixture Probability Distribution erzeugt wurden

### Wie ist die mehrdimensionale Normalverteilung definiert?
$\mathcal{N}(x|\mu, \Sigma) = \frac{1}{\sqrt{(2\pi)^d} |\Sigma |} \exp(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu))$

### Wie berechnet man die Determinante einer 2D Matrix?
$|((a, b), (c, d))| = ad - cb$

### Wie bestimmt man die Wahrscheinlichkeitsdichte eines Punktes beim Gaussian EM Algorithmus?
$p(x) = \sum_k \pi_k \mathcal{N}(x|\mu_k, \Sigma_k)$

### Warum muss Gaussian EM iterativ gelöst werden?
- Nicht-lineare gegenseitige Abhängigkeiten zwischen Parametern und Wahrscheinlichkeitsdichte der Punkte
- Optimierung eines Clusters hängt von der Optimierung aller anderen Cluster ab

### Beschreibe den EM Algorithmus
1. Initialize parameters (randomly) and evaluate their log-likelihood
2. E: Evaluate the probability of each sample using the current parameters
3. M: Re-estimate the parameters using the current probabilites
4. Re-evaluate the log-likelihood and check for convergence

### Was sind die Stärken von EM?
- Besser als k-Means für Cluster verschiedener Größe
- O(tnk) (t ist oft hoch)

### Was sind die Schwächen von EM? Nenne gegebenfalls lösungen
- Abhängig von initialen Parameterschätzungen -> mit k-Means initialisieren
- Abhängig von k
- Lokale Optima

### Wie kann k bei GMM gewählt werden?
- Problem: NLL monoton fallend mit k
- Lösung 1: Prior auf k, der hohe k bestraft
- Lösung 2: Assignments diskretisieren und Silhouette Coefficient berechnen

### Wie definiert DBSCAN ein Cluster?
Cluster = Dichte Region, getrennt von anderen Clustern durch Regionen mit niedriegerer Dichte

### Wie definiert DBSCAN einen dichten Punkt?
MinPts Punkte im epsilon-Radius

### Wie definiert DBSCAN einen core point?
Dichter Punkt / MinPts Punkte im epsilon Radius

### Wie definiert DBSCAN einen border point?
Liegt im Radius eines core points

### Was ist der Unterschied zwischen density-reachable und density-connected?
- Density-reachable = Transitive Hülle von direkt density reachable (= im Radius eines Core Points) -> Nicht symmetrisch
- Density-connected = beide sind density reachable von einem Core Point -> Symmetrisch

### Wie funktioniert der DBSCAN Algorithmus?
For each unclassified o:
1. If o is a core object, form a new cluster by density-reachability
2. Else, o is Noise

### Liefert der DBSCAN Algorithmus immer dieselbe Lösung?
- Border Objects, die zuerst Noise waren, werden später einem Cluster zugeordnet -> kein Problem
- Aber: Border Objects können zwei verschiedenen Clustern zugeordnet sein -> Reihenfolgeabhängig

### Beschreibe einen Ansatz für Parameter Tuning von DBSCAN
- MinPts fixen auf z.B. 2*dimen - 1
- MinPts-distance plotten für jeden Punkt im Datensatz
- Erster Knick wird oft von border punkten kommen
- epsilon >= Distanz an erstem Knick setzen

### Nenne 5 Vorteile von DBSCAN
- Cluster müssen nicht konvex sein
- Cluster können unterschiedliche Größe haben
- Anzahl der Cluster wird automatisch ermittelt
- Cluster und Noise werden getrennt (vgl. Partitioning Methods)
- Komplexität: 
  - Nachbarschaftsanfrage = O(n)
  - DBSCAN = O(n^2)
  
### Welche Komplexität hat DBSCAN?
- Nachbarschaftsanfrage = O(n)
- DBSCAN = O(n^2)

### Nenne zwei Schwächen von DBSCAN
- Problem bei Clustern unterschiedlicher Dichte
- Input Parameter schwer zu bestimmen / Teilweise empfindlich gegenüber Parameter Setting

### Wie definiert SNN ein Cluster?
Zwei Objekte sind ähnlich, wenn sie nahe zu einer Referenzmenge R sind

### Wie ist SNN-Similarity definiert?
Anzahl an geteilten k-NNs von zwei Punkten (k gegeben)

### Wie funktioniert SNN Clustering (Jarvis)?
- Verbinde alle Objekte mit Kanten mit deren Ähnlichkeit als Wert (keine Kanten für 0)
- Lösche alle Kanten unterhalb eines Grenzwerts

### Was ist das Problem von SNN Clustering?
Variatonen des Grenzwerts führen zu stark unterschiedlichen Ergebnissen

### Wie funktioniert SNN-Dichte Clustering (Ertöz)??
SNN-Dichte = Anzahl der Nachbarn mit mindestens epsilon gemeinsamen kNN
- epsilon definiert inversen Radius 
- minPts definiert SNN-Dichte

Algorithmus (k, epsilon, minPts)
1. Berechne Ähnlichkeitsmatrix und -graph über einfaches SNN Clustering
2. Berechne SNN-Dichte für jeden Punkt mit epsilon
3. Bestimme Kernpunkte mit minPts
4. Vereinige Kernpunkte, wenn SNN-sim >= epsilon
5. Ordne Nicht-Kernpunkte einem Cluster zu, wenn es einen Kernpunkt gibt, der sie über sim(p,q) >= epsilon erreicht
6. Alle anderen Nicht-Kernpunkte sind Rauschen

### Wie unterscheidet sich SNN-Dichte Clustering vom DBSCAN
- DBSCAN mit Euklidischer Distanz hat fixen Dichte-Grenzwert
- SNN-Dichte ist durch die kNN-Bedingung unabhängig von der eigentlichen Dichte, daher adaptiver
- Wahl von k ist kritisch

### Welche zwei grundlegenden Ansätze gibt es für Hierarchisches Clustering? Was ist das Ergebnis davon?
- Bottom-up (agglomerative) und top-down (divisive)
- Ergebnis ist ein Baum, wo die Blätter alle Cluster mit einem einzigen Objekt sind

### Wie funktioniert Agglomerative HC?
1. Each object is a cluster
2. Calculate all pairwise distances between the clusters
3. Merge the closest tuple (can be multiple clusters)
4. Goto 2

### Nenne drei Distanzfunktionen für Cluster
- Single Link -> distance of clostest objects
- Complete Link -> distance of furthest objects
- Average Link -> average distance of all edges in bipartite graph

### Wie funktioniert Divisive HC? Was sind die Nachteile?
1. One cluster in the beginning
2. Split (2^(n-1) - 1 possibilities in the first step :( )
3. Needs a second flat clustering algorithm for the splitting step

### Was ist die Motivation von OPTICS?
- Dichte Cluster sind komplett in weniger dichten Clustern enthalten
- Ziel: ein Durchlauf berechnet Clusterings für verschiedene Dichte Thresholds -> Maximaler Radius ist vorgegeben

### Wie ist die core-distance(o) bei OPTICS definiert?
Minimale Distanz, sodass o zum Core Object wird (undefiniert falls über dem maximalen e)

### Wie ist die reachability-distance(p, o) bei OPTICS definiert?
- Minimale Distanz, sodass o direkt p erreicht (mindestens core-distance von o)
- Unendlich, falls p und o mehr als e entfernt sind

### Was ist das grobe Vorgehen von OPTICS?
- Merke dir alle kürzesten reachability distances bis jetzt (sortiert in einer seed list)
- Mache immer einen kürzesten Sprung 
  - Inserte die Reachability Distance des Sprungs
  - Update die Seed List
- Reachbility Distance zum ersten Punkt ist unendlich

### Was ist der Output von OPTICS?
- Sortierung der Punkte
- Core-Distance der Punkte
- Reachability-Distance der Punkte

### Wie wird der Output von OPTICS interpretiert?
- Die Täler sind Cluster
- Beginn des Clusters liegt bei einem Objekt mit Core Distanz <= e* und Reachability Distanz > e*
- Alle dazugehörigen Punkte folgen, solange Reachability Distanz <= e*

### Was sind Stärken von OPTICS?
- Einfach zu analysieren, unabhängig von der Dimension
- k muss nicht spezifiziert werden
- Robuste / oder gar keine Parameter
- Berechnet Hierarchie von Clustern

### Was sind Schwächen von OPTICS?
- Skalierungsprobleme
- Nutzer muss finales Clustering bestimmen

### Was ist die Laufzeit OPTICS?
- O(n * e-neighborhood-query)
- e-neighborhood normalerweise O(n^2), geht aber auch in O(n log n)

### Welche Variante eliminiert das e bei OPTICS?
DeLiClu-Variante

### Welche Möglichkeiten gibt es zur Evaluation von Clustering Ergebnissen?
- Expertenmeinung
- Internal Measures 
- External Measures (nutzen Ground Truth)

### Was für Internal Measures gibt es zur Evaluation von Clusterings?
- Sum of Squared Distances
- Cohesion (Ähnlichkeit innerhalb des Clusters)
- Separation (Unterschiedlichkeit von Clustern)
- Silhouette Coefficient (Cohesion + Separation) - nur gut für "globular clusters" (runde)

### Was für Externe Measures gibt es zur Evaluation von Clusterings?
- Recall(C_i, G_j)
- Recall(C_i, G_j)
- Precision(C_i, G_j)
- F-Measure(C_i, G_j)
- Purity(C, G)
- Rand Index = Normalized Number of Agreements
- Jaccard Coefficient
- Similarity Matrix

### Wie wird die Purity eines Clusterings C und der Ground Truth G bestimmt?
- weighted sum of purs (weighted by cluster size percentage)
- pur(C_i, G) = max Precision over clusters in G

### Wie wird der Rand Index bestimmt?
Gehe durch alle Paare an Punkten und zähle, ob Cluster gleich <=> Ground Truth Cluster gleich 
-> Prozentualer Anteil an Übereinstimmungen

### Wie wird der Jaccard Coefficient bestimmt?
Wie Rand, nur dass (Cluster verschieden, Ground Truth Cluster verschieden) weder in Zähler noch in Nenner mitgezählt werden

### Wie wird die Similarity Matrix bestimmt?
Sortiere die beiden Achsen nach Clusterzugehörigkeit

### Was ist die Hopkins statistic? Wie wird sie interpretiert?
- Misst die Cluster Tendency von Daten
- H = 0 -> Daten sind regulär, z.B. auf einem Grid
- H = 0.5 -> Daten sind uniform verteilt
- H = 1 -> Strong Clusters

1. Sample random data points (by index), W
2. Sample random data points uniformly by position, U
3. Calculate the distance to the nearest neighbor for all data points
4. H = sum(U) / (sum(U) + sum(W))

## 5 - Outlier Detection

### Was ist ein Outlier?
Beobachtung, die sich von den anderen so deutlich unterscheidet, dass man denken könnte, sie sei von einem anderen Mechanismus generiert worden.

### Nenne 5 Methoden, um Outlier zu erkennen
1. Statistische Modellierung
2. Tiefen-basierte Outlier
3. Distanz-basierte Outlier
4. Dichte-basierte Outlier
5. Winkelbasierte Outlier

### Wie funktioniert Statistische Modellierung zur Outlier-Erkennung?
- Fitte ne Probability Distribution auf die Daten
- Outlier sind unwahrscheinliche Punkte

### Welche Arten von Features gibt es bei Statistischer Modellierung zur Outlier-Erkennung?
- Type of distribution
- Univariate / Multivariate
- Number of distributions
- Parametric / Non-parametric

### Was sind Probleme von Gaussians zur Outlier-Erkennung?
- Problem 1: Distances become increasingly similar with increasing dimensionality. The expected squared distance from the center is $\mathbb{E}(x_1^2 + ... + x_d^2) = d \mathbb{E}(x_1^2) = d \sigma^2$!!!! (for center = origin)
- Problem 2: Mean and variance are sensitive to outliers, but are computed on all data
- Problem 3: Low flexibility - Fitting one Gaussian on two actual Gaussians will result in a mean between those two

### Wie funktionieren Depth-Based Outliers?
1. Construct a convex hull
2. Remove the convex hull points
3. Repeat
4. Assign each point its convex hull layer index

### Was sind Probleme von Depth-Based Outlier Erkennung?
- Similar to Gaussian
- Convex Hull computation is inefficient in 4+ dimensions
- Dangerous assumption: Outliers are at the border of the data space and normal points in the center

### Wie funktionieren Distanz-basierte Outlier?
- Nehmen an, dass Outliers weit entfernte Nachbarn haben
- DB(e,pi) Outlier -> <= p % von allen Punkten sind in der e-Nachbarschaft des Punktes
- kNN Outlier -> Aggregiere 1-, 2-, ..., k-distance eines Punktes zu einem Outlier Score (oder nur k-Distanz)

### Welche Schwächen haben Distanz-basierte Outlier?
- Wahl der Hyperparameter -> k etc. -> Ist es ein Cluster oder nur ein paar Outlier nebeneinander?
- Funktioniert nicht gut bei Clustern verschiedener Dichte

### Nenne drei Anwendungen von Outlier Detection
1. Betrugserkennung
2. Medizin
3. Entdeckung von Messfehlern

### Wie funktionieren Dichte-basierte Outlier / LOF?
- Vergleichen die Dichte um einen Punkt herum mit der Dichte seiner Nachbarn
- Relative Dichte ist bei Outliern klein -> LOF >> 1

Reach-dist(p, o) = max(k-distance(o), dist(p, o) 
(o erreicht p)
Local reachability density of p = inverse average reachdist from kNNs of p
LOF = average ratio of LRDs of neighbors and LRD of the p

### Wie funktioniert die Winkelbasierte Outliererkennung?
Outlier-Winkel (zu allen anderen Datenpunkten) haben geringe Varianz

### Was ist jeweils das Problem von globaler und lokaler Outliererkennung?
- Problem mit global: Outlier sind teil der Referenzmenge
- Problem mit lokal: Wie bestimmt man die Nachbarschaft?

## 6 - Classification

### Erkläre vier Formen der Model Evaluation
1. Cross Validation
2. Leave-one-out (Jackknife)
   - Cross Validation with |test set| = 1
   - Well applicable to kNN
3. Stratified CV
   - Verhältnis der Klassen bleibt erhalten
4. Bootstrap

### Wie funktioniert Bootstrap zur Model Evaluation?
- N Datenpunkte für jedes Sample (mit Zurücklegen)
- 63.2% werden enthalten sein
- Bestimme Error auf ganzem Trainingsset
- Error estimation unterschätzt

Leave-one-out Bootstrap
- Evaluiere jeden Punkt nur auf den Models, die ohne ihn trainiert wurden
- Error estimation überschätzt, da Samples mehrere Punkte enthalten -> kack Trainingsdaten

0.632 Estimator
$Err_{0.632} = 0.368 \cdot \text{Training Error} + 0.632 \cdot \text{Leave-one-out Bootstrap}$

### Nenne zwei Methoden, um Overfitting zu vermeiden
- Falsche / Noisy Trainingsdaten entfernen
- Trainingsdaten vergrößern

### Was ist der Resubstitution Error?
Trainings Error

### Wie berechnet man Precision und Recall bei mehreren Klassen?
Es muss die Klasse gegeben sein, die als positive Klasse zählt, alle anderen sind negativ

### Nenne drei Möglichkeiten p(x|y) bei Bayes zu modellieren
1. Parametric Model (Gaussian)
2. Non-parametric Model (Kernel methods)
3. GMM für jede Klasse

### Was ist die Grundannahme von Naive Bayes?
Features are conditionally independent for any class

### Wie wird der Naive Bayes berechnet?
- p(y) über Häufigkeiten
- p(x|y) über rel. Häufigkeiten bei kategorischen Attributen bzw. Gaussian bei kontinuierlichen Attributen

### Nenne zwei Stärken von Bayes
- Incremental computation (can easily be updated when new training data are available)
- Expert knowledge can be incorporated into the priors

### Nenne zwei Stärken von Naive Bayes insbesondere
- Fast
- Interpretable even in high dimensions, because the dimensions are split up

### Nenne zwei Schwächen von Bayes
- Conditional probabilities often not available / not applicable
- Either naive or inefficient computation for high number of attributes

### Wie ist die Hyperebene einer SVM definiert? Welche Eigenschaft haben alle Punkte auf der Hyperebene?
- Hyperebene: $f(x) = w^Tx + b$
- Gemeinsame Eigenschaft aller Punkte: Wenn sie auf $w$ projiziert werden ergeben sie alle denselben Vektor $-\frac{b}{||w||_2}$

### Wie berechnet man die Distanz zur Hyperebene einer SVM?
$d(x) = \frac{f(x)}{||w||_2}$

### Wie lautet das Primäre Optimierungsproblem einer SVM?
Min $w^T w$

S.t. $y_i f(x_i) \geq 1$

### Wie lautet das Primäre Optimierungsproblem einer Soft Margin SVM?

Min $w^T w + C \sum_i \xi_i$

S.t. $y_i f(x_i) + \xi_i \geq 1$
und $\xi_i \geq 0$

### Wie lautet das Duale Problem einer Soft Margin SVM?

Max $\sum_i \alpha_i - \frac{1}{2} \sum_i \sum_j \alpha_i \alpha_j y_i y_j x_i^T x_j

S.t. $\sum_i \alpha_i y_i = 0$
und $0 \leq \alpha_i \leq C$

(für hard margin ohne $C$)

### Wie hängen Kernel mit phi zusammen?
$K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$

### Nenne 3 Kernel einer SVM
- linear: $a^Tb$
- polynomiell: $(a^Tb + c)^d$
- rbf: $exp(- \gamma||a - b||^2)$

### Vergleiche zwei Trainingsmethoden von Multi-Class SVMs
- 1 vs. all
  - Gewinner ist die SVM mit dem größten Abstand
  - Tendenziell schlechter aber effizienter ab 4 Klassen
- 1 vs. 1
  - Gewinner ist die SVM mit den meisten Votes
  - Quadratische Anzahl an SVMs

### Nenne 3 Stärken von SVMs
- Hohe Genauigkeit
- Maximaler Abstand zu den Datenpunkten / Schwache Tendenz zu Overfitting
- Effiziente Klassifikation

### Nenne 4 Schwächen von SVMs
- Gefittetes Model schwer zu interpretieren / prüfen
- Gibt keine Scores
- Teilweise lange Trainingszeiten
- Aufwendige Implementierung

### Wie geht der ID3 Algorithmus?
ID3(examples, targets, attributes)
1. If all examples have the same class or the attributes are empty return leaf node
2. Select best attribute $a$
3. Partition the examples
4. For each partition: add ID3(partition, attributes - $a$) as child

### Was ist die generelle Split Strategy bei Decision Trees?
Calculate a metric on the current node vs average on the possible child nodes (weighted by percentage of examples)

### Erkläre drei Split Strategies bei Decision Trees
1. Entropy (Information Gain)  
   $-\sum_c p_c \log_2 p_c$ ($c$ iterates the classes)
2. Gini index   
   $1 - \sum_c p_c^2$
3. Misclassification error   
   $1 - max_c(p_c)$
   
### Gini Impurity oder Entropy / Information Gain?
Gini Impurity performs similar to Entropy in 98% of the cases, but is more efficient to compute

### Wie splittet man die Attribute bei Decision Trees?
- Categorical -> many possible partitions
- Numerical -> many possible split points or discretize by binning first
- Choose with Gini for example (duh, good luck with 10 different categories -> number of partitions = 10th bell number)

### Erkläre drei Strategien für Decision Tree Pruning
- Post Pruning 
  - Remove nodes using a validation set (remove until no node removal makes it better!!)
  - Higher classification quality
- Prepruning 
  - Halt tree construction early by specifying minimum support and minimum confidence
  - Faster tree construction
- Minimal Cost Complexity Pruning
  - Cost function = classification error + weighted tree size
  
### Erkläre drei Missing value strategies für Decision Trees
- Assign most common value to missing attribute
- Assign most common value among same-class-examples to missing attribute
- Assign example to all descendants of the node with the same probability 

### Nenne vier Stärken von Decision Trees
- Good interpretability
- Intuitive to most users
- Fast classification with if-then rules
- Comparable classification accuracy

### Nenne zwei Schwächen von Decision Trees
- Not stable
- x_1 > x_2

### Muss die Laufzeit von kNN wirklich so schlecht sein?
Nein, kann mit Index erheblich beschleunigt werden

### Nenne vier Varianten von NN
- NN
- kNN
- Weighted k-NN (classes have weights)
  - Weights are relative frequencies of classes
  - Weights are reciprocal squared distance of neighbor to query object
- Nearest Mean (of class examples)

### Nenne vier Stärken von kNN
- Applicability: good for non-numerical data (even graphs etc.), only needs a distance function
- No training required
- Incremental adaption to new training objects
- Simple

### Nenne drei Schwächen von kNN
- Slow prediction / inefficient
- No output of explicit class knowledge
- Distance can be dominated by irrelevant attributes

### Wie werden Perceptrons mit Step Function trainiert?
Für jeden falsch klassifizierten Punkt wird die Hyperebene ein Stück in dessen Richtung verschoben
