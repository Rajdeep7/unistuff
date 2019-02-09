# Classification

## Genereal Quality Measures
- Classification Accuracy
- Model complexity
- Interpretability
- Efficiency (Training time, prediction time)

## Evaluation
### 1 - Cross Validation
### 2 - Leave-one-out (Jackknife)
- Cross Validation with |test set| = 1
- Well applicable to kNN

### 3 - Stratified CV
Proportionality of classes is preserved

### 4 - Bootstrap
Source: https://stats.stackexchange.com/questions/96739/what-is-the-632-rule-in-bootstrapping
- Pick N data points for each bootstrap sample
- Asymptotically 63.2% of all data will be in a bootstrap sample
- Evaluate the whole training set on the models (each trained on one bootstrap sample)
- Error estimation is downward biased, as the models are evaluated on their training data as well

**Leave-one-out Bootstrap**
- Evaluate each sample only on those models trained without it
- Upward biased error estimation due to the non-distinctness of a bootstrap sample

**0.632 Estimator**

$Err_{0.632} = 0.368 \cdot \text{Training Error} + 0.632 \cdot \text{Leave-one-out Bootstrap}$

## Quality Measures
- Resubstitution Error = Training Error
- Recall (TP Rate), Precision (TP / P), Specificity (TN Rate)
- For multiclass problems: Recall etc. only applicable when specifying the positive class

## Avoiding Overfitting
- Remove noisy / false training data
- Choose the size of the training set

## Bayesian Classifiers
### Models for p(x|y)
- Parametric models (single distribution)
- Non-parametric models (Kernel methods)
- GMM (**for each class**), computed by EM algorithm

### Naive Bayes
- Core assumption: conditionally independent attributes for any given class
- Estimation of $p(x_i|y_j)$ for
  - categorical attributes: relative frequencies for each class
  - continuous attributes: fit a Gaussian for each class

### Non-Naive Bayes
- Construct a covariance matrix for modeling $p(x|y_j)$ 
- Effectively a GMM on all classes

### Strengths
- Incremental computation (can easily be updated when new training data are available)
- Expert knowledge can be incorporated into the priors
- Naive Bayes:
  - Fast
  - Interpretable even in high dimensions, because the dimensions are split up

### Weaknesses
- Conditional probabilities often not available / not applicable
- Either naive or inefficient computation for high number of attributes

## SVMs

Hyperebene: $f(x) = w^Tx + b$

Gemeinsame Eigenschaft aller Punkte: Wenn sie auf $w$ projiziert werden ergeben sie alle denselben Vektor $-\frac{b}{||w||_2}$.

Distanz zur Hyperebene:

$d(x) = \frac{f(x)}{||w||_2}$

### Primäres Optimierungsproblem

Min $w^T w$

S.t. $y_i f(x_i) \geq 1$


### Primäres Optimierungsproblem Soft Margin

Min $w^T w + C \sum_i \xi_i$

S.t. $y_i f(x_i) + \xi_i \geq 1$
und $\xi_i \geq 0$

### Duales Problem 

Max $\sum_i \alpha_i - \frac{1}{2} \sum_i \sum_j \alpha_i \alpha_j y_i y_j x_i^T x_j

S.t. $\sum_i \alpha_i y_i = 0$
und $0 \leq \alpha_i \leq C$

(für hard margin ohne $C$)

### Kernel Machines
- Ersetzt implizit jedes $x_i$ mit $\phi(x_i)$. $\phi$ mappt in anderen Raum, z.B. mit $x_1^2$ etc.
- $K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$
- Kernelmatrix ($K(x_i, x_j)$) muss positiv semi-definit sein / darf keine negativen Eigenwerte besitzen

Kernel:
- linear: $a^Tb$
- polynomiell: $(a^Tb + c)^d$
- rbf: $exp(- \gamma||a - b||^2)$

### Multi-Class SVMs
- 1 vs. all
  - Gewinner ist die SVM mit dem größten Abstand
  - Tendenziell schlechter aber effizienter ab 4 Klassen
- 1 vs. 1
  - Gewinner ist die SVM mit den meisten Votes
  - Quadratische Anzahl an SVMs

### Stärken
- Hohe Genauigkeit
- Maximaler Abstand zu den Datenpunkten / Schwache Tendenz zu Overfitting
- Effiziente Klassifikation

### Schwächen
- Gefittetes Model schwer zu interpretieren / prüfen
- Gibt keine Scores
- Teilweise lange Trainingszeiten
- Aufwendige Implementierung

## Decision Trees
ID3(examples, targets, attributes)
1. If all examples have the same class or the attributes are empty return leaf node
2. Select best attribute $a$
3. Partition the examples
4. For each partition: add ID3(partition, attributes - $a$) as child

## Split Strategies
- Generally, calculate a metric on the current node vs average on the possible child nodes (weighted by percentage of examples)
- The following metrics should be as low as possible
- Gini Impurity performs similar to Entropy in 98% of the cases, but is more efficient to compute

### 1. Entropy (Information Gain)
$-\sum_c p_c \log_2 p_c$ ($c$ iterates the classes)

### 2. Gini index
$1 - \sum_c p_c^2$

### 3. Misclassification error
$1 - max_c(p_c)$

### Splitting attributes
- Categorical -> many possible partitions
- Numerical -> many possible split points or discretize by binning first
- Choose with Gini for example (duh, good luck with 10 different categories -> number of partitions = 10th bell number)

### Pruning
- Post Pruning 
  - Remove nodes using a validation set (remove until no node removal makes it better!!)
  - Higher classification quality
- Prepruning 
  - Halt tree construction early by specifying minimum support and minimum confidence
  - Faster tree construction
- Minimal Cost Complexity Pruning
  - Cost function = classification error + weighted tree size
 
### Missing value strategies
- Assign most common value to missing attribute
- Assign most common value among same-class-examples to missing attribute
- Assign example to all descendants of the node with the same probability 

### Strengths
- Good interpretability
- Intuitive to most users
- Fast classification with if-then rules
- Comparable classification accuracy

### Weaknesses
- Not stable
- x_1 > x_2

## Nearest Neighbors
- Instance-based Training (lazy evaluation as opposed to eager evaluation)
- Can be sped up with an index
- Choosing k -> Overfitting vs Generalization (Variance vs. Bias)
  - 1 to 10 is good
  - Or let k grow with sqrt(n)

### Variants
- NN
- kNN
- Weighted k-NN (classes have weights)
  - Weights are relative frequencies of classes
  - Weights are reciprocal squared distance of neighbor to query object
- Nearest Mean (of class examples)

### Strengths
- Applicability: good for non-numerical data (even graphs etc.), only needs a distance function
- No training required
- Incremental adaption to new training objects
- Simple

### Weaknesses
- Slow prediction / inefficient
- No output of explicit class knowledge
- Distance can be dominated by irrelevant attributes

## Neural Networks

Training of perceptron with step function: move hyperplane a little step towards each misclassified point
