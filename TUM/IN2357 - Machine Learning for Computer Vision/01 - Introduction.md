# Introduction / Probabilistic Reasoning

### Categories of Learning
- Unsupervised
- Supervised
  - Regression
  - Classification
- Reinforcement

## Probabilistic Reasoning

### Sample space $\mathcal{S}$
$\mathcal{S} = $ set of outcomes

### Random Variable X
- assigns real number to each element of $\mathcal{S}$
- discrete or continuous

### Normalizer $\eta$
$p(X)^{-1} = \eta$

### Conditional independence
$p(x, y|z) = p(x|z) p(y|z)$

### Causal vs Diagnostic Reasoning
- Diagnostic: $p(\text{in front of door} | \text{sensor says in front of door})$
- Causal: $p(\text{sensor says in front of door} | \text{in front of door})$
- Causal knowledge easier to obtain -> Bayes rule

### Combining Evidence over Time
- Markov Assumption: a prediction (sensor measurement) does not give more information to the next time step, if we know the actual state
  - $p(\hat{y}\_{t+1} | y\_t, \hat{y}\_t) = p(\hat{y}\_{t+1} | y\_t)$
  - So, the prediction errors are independent making the predictions conditionally independent given $y$
  - We can combine them still with the simple Bayes rule

## Notes
- Exam will contain more assignments than needed to reach the highest grade
