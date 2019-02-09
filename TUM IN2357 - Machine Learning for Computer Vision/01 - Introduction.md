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

### Naming
- Sensor measurement $z$
- Actual state $x$
- Action $u$

### Normalizer $\eta$
$p(Z)^{-1} = \eta$

### Conditional independence
$p(x, y|z) = p(x|z) p(y|z)$

### Causal vs Diagnostic Reasoning
- Diagnostic: $p(\text{in front of door} | \text{sensor says in front of door})$
- Causal: $p(\text{sensor says in front of door} | \text{in front of door})$
- Causal knowledge easier to obtain -> Bayes rule

### Combining Evidence over Time
- Markov Assumption: a prediction (sensor measurement) does not give more information to the next time step, if we know the actual state
  - $p(z\_{t+1} | x\_t, z\_t) = p(z\_{t+1} | x\_t)$
  - So, the prediction errors are independent making the predictions conditionally independent given $x$
  - We can combine them still with the simple Bayes rule and even reuse the result from the time step before -> recursive
  
### State Transitions
- Outcome of an action $u$ is also a random variable (for example "state after closing the door")
  - $P(closed | closed) = 1, P(open | closed) = 0$ (obviously, as it was already closed)
  - $P(closed | open) = 0.9, P(open | open) = 0.1$ (action might fail)
- Next state can be calculated by integrating over all possible previous states and applying the action

### Beliefs
- Combine sensor updates $p(x|z)$ and action updates $p(x|u)$
- Compute belief of current state $x_t$ after sequence of $u_1, z_1, ... , u_t, z_t$
- $\text{Bel}(x_t) = p(x_t | u_1, z_1, ... , u_t, z_t)$

### Dynamic Bayes Network / Graphical Representation
![](https://github.com/batzner/unistuff/blob/master/TUM/IN2357%20-%20Machine%20Learning%20for%20Computer%20Vision/img/01-dynamic-bayes-network.png?raw=true)

Assumptions:
1. Measurement $z_t$ only depends on current state $x_t$
2. State $x_t$ only depends on last state $x_{t-1}$ and action taken $u_t$ -> no memory

### Bayes Filter Algorithm
1. For sensor measurement:
   1. Keep running sum of new Bel's as normalization factor
   2. Calculate new Bel by integrating over $x$ in current Bel and multiplying with $p(z|x)$
2. For action:
   1. Iterate over $x$ in new Bel
   2. For each $x$, integrate over probability of each old $x'$ combined with the action $p(x|u, x')$

### Bayes Filter Applications
1. Kalman filters
2. Particle filters
3. HMM
4. Dynamic Bayesian networks
5. Partially Observable Markov Decision Processes (POMDPs)

## Notes
- Exam will contain more assignments than needed to reach the highest grade
