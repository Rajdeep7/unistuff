# Datenrepräsentation

## Datentypen
### Atomare Datentypen
- Kategorisch (Nominal)
  - Nur gleich / ungleich 
  - Kein besser oder schlechter / irgendeine Richtung
- Ordinal z.B. low, medium and high
  - Kein einheitlicher Abstand, aber totale Ordnung
- Metrisch / Interval
  - Differenzen und Verhältnisse sind aussagekräftig
  - Können diskret oder stetig sein
  
Totale Ordnung
- transitiv
- antisymmetrisch
- abgeschlossen
  
Metrische Distanzfunktion:
- reflexiv (d(x, x) = 0)
- symmetrisch
- strikt (d(x, y) = 0 => x = y)
- Dreiecksungleichung
  
## Multivariate Deskription
Zusammenhang von Merkmalen

### Mean, Varianz, Kovarianz
- $\mu_X = \mathbb{E}[X]$
- $Var(X) = \mathbb{E}[(X - \mu)^2]$
- $\sigma_X = \sqrt{Var(X)}$
- $Cov(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)]$

### Sample Varianz und Sample Standardabweichung
- $\mu_X = \frac{1}{n} \sum_i x_i$
- $Var(X) = \frac{n}{n-1} \frac{1}{n} \sum_i (x_i - \mu)^2$
- $\sigma_X = \sqrt{Var(X)}$

### Korrelationskoeffizient
$\rho_{X,Y} = \frac{cov(X, Y)}{\sigma_X \sigma_Y}$

### $\chi^2$ - Koeffizient
Differenz zwischen der bei Unabhängigkeit erwarteten und der tatsächlich beobachteten Häufigkeit

$\chi^2 = \sum_{i \in X} \sum_{j \in Y} \frac{(o_ij - e_ij)^2}{e_ij}$
- $o_ij$ = beobachtete Häufigkeit
- $e_ij$ = erwartete Häufigkeit = $n \cdot P_i \cdot P_j$

## Normalisierung

### z-score 
$v' = \frac{v - \mu}{\sigma}$

## Zusammengesetzte Datentypen
### Mengen
- Symmetrische Differenz $A \triangle B = A \cup B - A \cap B$
- Jaccard Distanz $d(A, B) = \frac{A \triangle B}{A \cup B}$
- Hamming Distanz mit Basismenge C - Zähle binär die Matches in (A, C) und (B, C) und berechne die Summe der unterschiedlichen Einträge

### Sequenzen / Vektoren
- p-Norm auf $a - b$: $d_p(a, b) = \sqrt[p]{\sum_i |a_i - b_i|^p}$

## Ähnlichkeitsanfragen
- Range query (gibt alle Nachbarn in bestimmtem Radius aus)
- (k) Nearest neighbor query
- Ranking query (gibt Nachbarn in Reihenfolge aus)

## Features für Bilder
- Farbhistogramme
- Textur 
- Formen (Sektorenmodell)

### Farbhistogramme
- Farbraum festlegen
- Menge von Repräsentanten (Bins) im Farbraum auswählen (unterschiedliche Farben)
- Distanz:
  - Euklidische Distanz
  - Multipliziert mit Ähnlichkeitmatrix $A$ zwischen den einzelnen Bins
  - $d(P, Q) = \sqrt{(h_P - h_Q) A (h_P - h_Q)^T}$

### Farbräume
- RGB
- CMY
- HSV (Hue, Saturation, Value) - Rechteck
- HLS (Hue, Luminance, Saturation) - Dreieck

## Texte
### Probleme
1. Nutzlose Wörter
2. Wörter mit gleichem Wortstamm
3. Hochdimensionale Featureräume
4. Unterschiedliche wichtige Terme
5. Sparse feature space

### Lösungen
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
    
## Datenvisualisierung d-dimensionaler Datensätze
- Scatter plots von allen Feature-Paaren
- Parallel Coordinates 
  - Jede Achse ist eine Dimension, jedes Sample ist eine horizontale Linie
  - Sortierung wichtig (Clustererkennung vs. Korrelationserkennung)
- Spiderweb 
  - Wie Parallel Coordinates, aber Features sind Spinnennetz
  
## Data Reduction
- Numerosity reduction 
  - Sampling
  - Aggregation (Mean, Variance, STD etc.)
- Dimensionality reduction
  - t-SNE, PCA, MDS, Random Projections etc.
- Discretization 
  - Binning / Histogram

### Distributive Aggregationsfunktionen
- Das Resultat der Funktion für n aggregierte Werte ist identisch mit dem angewendet auf alle Daten
- sum, min, max, count

### Algebraische Aggregationsfunktionen
- Algebra auf distributiven AF: avg = sum / count etc.

### Holistische Aggregatsfunktionen
- Median, Modus, Rang / Quantile

### Central Tendency Maße
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

### Boxplot
- Enthält 0, 25, 50, 75 und 100 % Quantil

### Aggregations / Generalisierungstechniken
- Binning / Histogramme
  - Equiwidth - einfach, aber Outlier dominieren
  - Equiheight 
    - Skaliert auch für sehr große Mengen
    - Ähnlich wie Boxplot (4 Bins)
    - Wenn ein Wert häufiger als die Bin Height vorkommt, müssen Intervalle vereinigt werden
- Generalisierungshierarche basierend auf Konzept
- Clustering basierend auf Objektähnlichkeit

## OLAP (Online Analytical Processing)

### Data Cube
- Kanten des Cubes sind Dimensionen
- Zellen sind Werte / Kennzahlen: F(Produkt, Zeitraum, Region) = Umsatz

### 1NF
Jedes Attribut hat einen atomaren Wertebereich -> keine komplexen Datentypen / mehrere Attribute in einem etc.

### 2NF
Jedes nicht-primäre Attribut ist von **allen** Schlüsseln abhängig + 1NF

### 3NF
Alle Attribute hängen direkt vom Schlüssel ab und nicht transitiv (CD_ID -> Interpret -> Gründungsjahr). Um Verletzungen zu lösen, können neue Tabellen mit ID-Attributen erzeugt werden (Interpred_ID).

### Star Schema
- Eine Faktentabelle in der Mitte enhält eine Spalte pro Dimension (ArtikelID) und eine pro Kennzahl
- Für jede Dimension gibt es eine Klassifikationstabelle, die z.B. Attribute zu Artikeln speichert
- Nicht normalisiert, redundant, dadurch effizienter

### Snowflake Schema 
- Wie Start, nur in 3NF -> redundanzfrei

### OLAP Operationen
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

### Vorteile
- Verschiedene Aggregate als Kennzahlen möglich (count, sum, etc.)
- Generalisierung und Spezialisierung durch roll-up und drill-down

### Nachteile
- Nur simple nonnumeric data oder simple aggregated numeric values
- Keine intelligente Analyse
