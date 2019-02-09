# Outlier Detection
One person's noise could be another person's signal.

**Outlier:** Beobachtung, die sich von den anderen so deutlich unterscheidet, dass man denken könnte, sie sei von einem anderen Mechanismus generiert worden.

### Szenarien
- supervised -> Trainingsdaten mit normalen und ungewöhnlichen Fällen
- semi-supervised -> Trainingdaten von einem von beiden
- unsupervised -> keine Trainingsdaten

## 1 - Statistical Modeling
- Fit a probability distribution on all data
- Outliers are unlikely points

### Different features
- Type of distribution
- Univariate / Multivariate
- Number of distributions
- Parametric / Non-parametric

### Example: Gaussian
- Effectively cuts off based on the Mahalanobis distance
- $Mdist(x, \mu) = (x - \mu)^T \Sigma^{-1}(x - \mu)$
- Problem 1: Distances become increasingly similar with increasing dimensionality. The expected squared distance from the center is $\mathbb{E}(x_1^2 + ... + x_d^2) = d \mathbb{E}(x_1^2) = d \sigma^2$!!!! (for center = origin)
- Problem 2: Mean and variance are sensitive to outliers, but are computed on all data
- Problem 3: Low flexibility - Fitting one Gaussian on two actual Gaussians will result in a mean between those two

## 2 - Depth-based Outliers
1. Construct a convex hull
2. Remove the convex hull points
3. Repeat
4. Assign each point its convex hull layer index

Dangerous assumption: Outliers are at the border of the data space and normal points in the center

### Problems
- Similar to Gaussian
- Convex Hull computation is inefficient in 4+ dimensions

## 2 - Distance-based Outliers

Assumption:
- Normal points have dense neighborhood, outliers not
- Judge point based on distance to its neighbors

### $DB(\epsilon, \pi)$-Outlier
At most $\pi$ percent of all points are in the $\epsilon$-neighborhood of $p$.

### kNN-Outlier
Aggregate the 1-, 2-, ..., k-distance of a point to an outlier score (or just take the k-distance).

### Problems
- Choosing k -> Is a small cluster is a cluster or just some outliers next to each other?
- Clusters of different densities - an outlier close to a really dense cluster vs. a rather sparse cluster

## 3 - Density-based Outliers / Local Outliers
- Compare the density around a point with the density around its neighbors
- Relative density is small for outliers

### Local Outlier Factor
- $\text{reach-dist}_k(p, o) = max(\text{k-distance}(o), dist(p, o)$
- Local reachability density = Inverse of average reach-dists from the k-NNs to p
- LOF(p) = Average lrd(o) / lrd(p)

Interpretation:
- LOF around 1 -> homogenous density
- LOF >> 1 -> outlier

**Variants**
- Only output the top-n local outliers
- Connectivity-based outlier factor $(\cdot )$
- Influended Outlierness for not clearly separated clusters of different densities

## 4 - Winkelbasiertes
- Bestimme die Winkel zwischen Outliern und (allen) anderen Punkten
- Outlier-Winkel haben geringere Varianz

## Klassifikation von Outlier Detection

### Global vs. lokal (Metrik bezüglich allen Punkten oder nur Nachbarn)
- Problem mit global: Outlier sind teil der Referenzmenge
- Problem mit lokal: Wie bestimmt man die Nachbarschaft?

### Labeling vs. Scoring
- Problem mit Labeling: keine top-n Ausgabe möglich

### Zugrundeliegendes Modell
- Statistisches Modell
  - Annahme: Daten folgen der Wahrscheinlichkeitsverteilung des bestimmten Modells 
  - Beispiele: Gaussian, Tiefenbasiertes modell
- Räumliche Nähe
  - Die Nachbarschaft von Outliern weist eine andere Struktur auf (geringere Dichte / anderes Dichteverhältnis)
  - Beispiele: Distanz-basierte und Dichte-basierte Ansätze
- Winkelspektrum
