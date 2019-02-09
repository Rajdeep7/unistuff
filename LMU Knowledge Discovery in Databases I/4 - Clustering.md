# Clustering
- Partitioning Algorithms (k partitions, minimize some objective function)
- Probabilistic Model-Based Clustering (EM)
- Density-based (connectivity function)
- Hierarchical algorithms

## Partitioning Methods
1. Choose k representative samples
2. Assign all samples to their cluster
3. Compute new representatives -> goto 2

**Clusters =** collections of points with low variation

**Strengths**
- Easy implementation

**Weaknesses**
- k must be specified in advance
- Clusters are forced to be Voronoi Cells (convex partitions)
- Result and runtime strongly depend on the initial partition, local optima!

### k-means (LLoyd's Algorithm)
- Center is the representative
- Minimizes within-cluster variation by minimizing SSE

**Strengths**
- Relatively efficient: O(tkn)
- Easy implementation

**Weaknesses**
- Mean must be defined
- k must be specified in advance
- Sensitive to noise -> creates 1-element clusters and therefore reduces the effective k
- Sensitive to outliers (use L1 norm!)
- Clusters are forced to be Voronoi Cells (convex partitions)
- Depends on init and often terminates at non-global optima

### k-means (MacQueen's)
- Aktualisiere die centroids nach jedem Assignment und nach jeder Epoche
- Reihenfolgeabhängig!

### k-medoid (PAM Algorithm, Kaufman)
- Representative must be a sample
- Metric data, because it depends on distance function
- When centroid can't be defined (graphs)
- When centroid is not representative (images)

**Calculation of the medoid**:

$x_\text{medoid} = \text{argmin}_x \sum_i d(x, x_i)$

1. Select random init samples
2. Assign each sample to its medoid and compute the TD on the whole dataset
3. Calculate the new total distance for each of all possible swaps between medoid and non-medoid
4. If there is a better total distance, do the best single swap
5. Goto 3, Until nothing changes

Problem:
- O(tk(n-k)^2)

### Solution: CLARANS Algorithm
- Trading accuracy for speed
- Only consider `maxneighbor` pairs of medoid and candidate in each iteration
- Best first: take the first pair that reduces the TD value
- Terminate after `numlocal` iterations

### k-Median 
- For non-numerical, but ordered data
- Proceed like the k-Means algorithm (same time complexity), but with TD

### k-Mode (Huang 1997)
- Use Hamming Distance to determine the mode of the dataset / cluster -> choose most frequent value in **each** attribute
- Proceed like the k-Means algorithm (same time complexity), but with TD

### Choice of Parameters
Initial Representatives
- Choose m different sets of k initial representatives
- Then, cluster all sampled points with each of the sampled sets as initial partitioning
- Choose the best centroids as init for clustering the whole dataset

Choice of k
- Test k=2 until n-1
- Problem: SSE and TD monotonously decrease with increasing k
- Solution: Silhoutte-Coefficient

### Silhoutte-Coefficient (only for k-means and k-medoid)
- a(o) = average distance between object o and the objects in its cluster
- b(o) = smallest average distance between o and the objects in another cluster 
- s(o) = 0 if a(o) = 0, i.e. the cluster is a single object
- s(o) = (b(o) - a(o)) / max(a(o), b(o)) -> in [-1, 1]
- silh(C) = average s(o) of objects in cluster / all objects

Reading the silhoutte coefficient:
- 1 -> good assignment of o
- 0 -> o ist in between A and B
- -1 -> bad, on average o is closer to members of B

## Expectation Maximization
MLE of parameters (for example Gaussians)

**Cluster =** collection of points drawn from a mixture probability distribution

$\mathcal{N}(x|\mu, \Sigma) = \frac{1}{\sqrt{(2\pi)^d} |\Sigma |} \exp(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu))$

mit 

$|((a, b), (c, d))| = ad - cb$

1. Define clusters as Gaussians
2. Iteratively improve the Gaussian parameters to maximize the likelihood of the data  
  Parameters are Mean, Covariance Matrix and weight of the Gaussian in the Mixture Model
3. Maximize the probability of each sample, which is given directly by the Mixture Model

### Problem: 
- Non-linear mutual dependencies between parameters and probabilities of samples
- Optimizing one cluster's Gaussian depends on all other Gaussians

### Solution:
1. Initialize parameters (randomly) and evaluate their log-likelihood
2. E: Evaluate the probability of each sample using the current parameters
3. M: Re-estimate the parameters using the current probabilites
4. Re-evaluate the log-likelihood and check for convergence

### Strengths:
- Better than k-Means for clusters of varying size
- O(tnk) (but high t in many cases)

### Weaknesses:
- Strong dependence on initial parameters -> Init with k-Means
- Strong dependence on k

### Choosing k:
- MLE is nondecreasing in k :(
- Define a prior on k penalizing higher values of k
- Or discretize the assignments of the GMM and calculate the Silhouette Coefficient

## DBSCAN
ACHTUNG: Punkt ist ab sofort selbst auch ein Teil seiner Nachbarschaft

**Clusters =** dense regions separated by regions of lower point density

Density = Points / Area -> Given by MinPts and radius epsilon

- Every core point in a cluster must have at least MinPts points in its direct neighborhood (given by radius epsilon)
- Point with MinPts is a **core object**, otherwise border object, if reached by core object
- Directly density-reachable = neighbors, source must be a core object
- Density-reachable = transitive closure, is not symmetric!!!
- Density-connected = there is a point that density-reaches both r and q (is symmetric!!!)

Cluster:
- Formed by applying density-reachability
- All points in the cluster are density-connected

### Algorithm
For each unclassified o:
1. If o is a core object, form a new cluster by density-reachability (put all neighboring unclassified points into a **seed list**)
2. Else, o is Noise

Not always the same solution! 
- Border objects might first be noise but will become assigned to a cluster later, so this is determined.
- Two clusters might share the same border object

### Parameter Tuning
- Fix `MinPts` to be for example `2 * dimen - 1`
- Plot the `MinPts`-distance for each object in the dataset
- The first kink in the plot will often come from border objects
- Set epsilon to >= the distance value at the kink

### Strengths
- Clusters are not restricted to convex shapes, can have any
- No Problem with clusters of different size
- Number of clusters is determined automatically / dynamically
- Separates clusters and noise
- Complexity: 
  - Neighborhood Query for an object: O(n)
  - DBSCAN: O(n^2)

### Weaknesses
- Problem bei Clustern unterschiedlicher Dichte
- Input parameters difficult to determine
- Sometimes sensitive to input parameter setting

## Shared Nearest Neighbor Clustering (Jarvis)
- Zwei Objekte sind ähnlich, wenn sie nahe zu einer Referenzmenge R sind
- SNN-Similarity = Anzahl an geteilten k-NNs von zwei Punkten
- Verbinde alle Objekte mit Kanten mit deren Ähnlichkeit als Wert (keine Kanten für 0)
- Lösche alle Kanten unterhalb eines Grenzwerts

Problem:
- Variatonen des Grenzwerts führen zu stark unterschiedlichen Ergebnissen

### Lösung: SNN-Dichte von p mit epsilon (Ertöz)
- Dichte = Anzahl der Kanten eines Punktes / Anzahl der Punkte q mit snn-sim(p,q) >= epsilon
- MinPts spezifiziert den Dichte-Treshold

Algorithmus (k, epsilon, minPts)
1. Berechne Ähnlichkeitsmatrix und -graph über einfaches SNN Clustering
2. Berechne SNN-Dichte für jeden Punkt mit epsilon
3. Bestimme Kernpunkte mit minPts
4. Vereinige Kernpunkte, wenn SNN-sim >= epsilon
5. Ordne Nicht-Kernpunkte einem Cluster zu, wenn es einen Kernpunkt gibt, der sie über sim(p,q) >= epsilon erreicht
6. Alle anderen Nicht-Kernpunkte sind Rauschen

Unterschied zu DBSCAN
- DBSCAN mit Euklidischer Distanz hat fixen Dichte-Grenzwert
- SNN-Dichte ist durch die kNN-Bedingung unabhängig von der eigentlichen Dichte, daher adaptiver
- Wahl von k ist kritisch

## Hierarchical Methods
- Bottom-up (agglomerative) or top-down (divisive)
- Result is a tree where the leafs are clusters with a single object

### Agglomerative HC
1. Each object is a cluster
2. Calculate all pairwise distances between the clusters
3. Merge the closest tuple (can be multiple clusters)
4. Goto 2

Distance functions for clusters:
- Single Link -> distance of clostest objects
- Complete Link -> distance of furthest objects
- Average Link -> average distance of all edges in bipartite graph

### Divisive HC
1. One cluster in the beginning
2. Split (2^n - 1 possibilities in the first step :( )
3. Needs a second flat clustering algorithm for the splitting step

## OPTICS
- Dense Clusters are completely contained by less dense clusters
- -> Density-Based Hierarchical Clustering
- Goal: one run yields clusters of **different** density thresholds

**Parameters**: maximaler Radius $\epsilon$ und fixer `MinPts`

$\text{core-distance}_{\epsilon, MinPts}(o)$ = MinPts-distance or ? if larger than $\epsilon$

$\text{reachability-distance}_{\epsilon, MinPts}(o)$
- if p is within o's core-distance then the core-distance
- if p is without o's core-distance then the dist(p,o) or infinity, if that distance exceeds $\epsilon$

**Idea**
- Remember shorted reachability distances seen so far
- Make always a shortest jump

**Output**
- Order of points
- Core-distance of points
- Reachability-distance of points

## Evaluation of Clustering Results
- Expert's opinion
- Internal measures (without additional information)
- External measures (with ground truth)

### Internal Measures
- Sum of Squared Distances
- Cohesion (similarity of objects in cluster)
- Separation (dissimilarity of clusters)
- Silhouette Coefficient (combining cohesion and separation, only good for globular clusters :/ )

### External Measures
Given: 
- our clustering C
- ground truth / actual clustering G

Measures:
- Recall(C_i, G_j)
- Precision(C_i, G_j)
- F-Measure(C_i, G_j)
- Purity(C, G) = weighted sum of purities (weighted by cluster size percentage)
- pur(C_i, G) = max Precision over clusters in G
- Rand Index = Normalized Number of Agreements
- Jaccard Coefficient

### Rand Index
Gehe durch alle Paare an Punkten und zähle, ob Cluster gleich <=> Ground Truth Cluster gleich 
-> Prozentualer Anteil an Übereinstimmungen

### Jaccard Coefficient
Wie Rand, nur dass (Cluster verschieden, Ground Truth Cluster verschieden) weder in Zähler noch in Nenner mitgezählt werden

### Hopkins statistics

1. Sample random data points (by index), W
2. Sample random data points uniformly by position, U
3. Calculate the distance to the nearest neighbor for all data points
4. H = sum(U) / (sum(U) + sum(W))


- Misst die Cluster Tendency von Daten
- H = 0 -> Daten sind regulär, z.B. auf einem Grid
- H = 0.5 -> Daten sind uniform verteilt
- H = 1 -> Strong Clusters

### Similarity Matrix
Sortiere die beiden Achsen nach Clusterzugehörigkeit

## Ensemble Clustering
- Improved quality
- Improved robustness across wide range of generating probability distributions
- Unification Methods for Distributed Clustering for distributed data

**Approach:** 
- Out of multiple Clusterings, find the clustering with the highest average similarity with the other clusterings 
- Use external evaluation measures

### DBSCAN can be seen as a Join operation ($\epsilon$-similarity join)
