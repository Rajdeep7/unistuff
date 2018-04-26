# Regression

### Basis functions
- Not just for non-linear dependencies but for mapping our data to $\mathbb{R}$ in general

### Naming
- $E$ is the loss function, for now the sum of squared errors
- $x_i$ is the input for the i-th sample (one-dimensional for now)
- $t_i$ is the target for the i-th sample

### Linear Regression - Analytical Solution
1. $E$ is SSE
2. $\mathbf{w} = (w_0, w_1)^T$ and $\mathbf{x}_i = (1, x_i)^T$ gives us $f(\mathbf{x}_i, \mathbf{w}) = \mathbf{w}^T\mathbf{x}_i$
3. $\nabla E(\mathbf{w}) = \mathbf{0}^T = \sum_i \mathbf{w}^T \mathbf{x}_i \mathbf{x}_i^T - \sum_i t_i \mathbf{x}_i^T$
4. The sums can be evaluated independently from $\mathbf{w}^T$, so this is a simple system of linear equations and stays the same for more features.

### Polynomial Regression
- Simply add more "features" by using $M$ basis functions:  
  $\mathbf{\phi}(x) = (1, \phi_1(x), ..., \phi_{M-1}(x))$
- Still analytical solution, we can simply replace $\mathbf{x}$ with $\mathbf{\phi}(x)$
- $\nabla E(\mathbf{w}) = \mathbf{0} = \mathbf{w}^T \sum_i \mathbf{\phi}(x_i) \mathbf{\phi}(x_i)^T - \sum_i t_i \mathbf{\phi}(x_i)^T$
- $\mathbf{\phi}(x_i) \mathbf{\phi}(x_i)^T$ is an outer product. We sum outer products, which we can substitute with $\Phi^T \Phi$ with $\Phi$ containing one row for each training example and one column for each feature. This yields:
- $\nabla E(\mathbf{w}) = \mathbf{w}^T \Phi^T \Phi - \mathbf{t}^T \Phi$
- Setting the gradient to zero gives us the normal equation $\Phi^T \Phi \mathbf{w} = \Phi^T \mathbf{t}$
- Solving for $w$ directly yields the Pseudoinverse $\Phi^+ = (\Phi^T \Phi)^{-1} \Phi^T$

### Computing the Pseudoinverse
- SVD is a stable approach (probably most of the times at least)
- $\Phi = UDV^T$ yields $\Phi^+ = VD^+U^T$ (pseudo-inverse of a diagonal simply contains the reciprocal of non-zero elements)

### Regularization
- blablabla Overfitting blabla generalization blablabla large parameters lead to oscillation 
- Add $\frac{\lambda}{2}\lVert \mathbf{w} \rVert^2$ to loss -> derivative is $\lambda \mathbf{w}^T$
- Now, $\nabla E(\mathbf{w}) = \mathbf{w}^T \Phi^T \Phi + \lambda \mathbf{w}^T - \mathbf{t}^T \Phi$
- $\Rightarrow \Phi^T \Phi \mathbf{w} + \lambda \mathbf{w} = \Phi^T \mathbf{t}$
- $\Rightarrow \mathbf{w} = (\lambda \mathbf{I} + \Phi^T \Phi)^{-1} \Phi^T \mathbf{t}$
- $\Rightarrow$ complex model for small dataset :)))

## Probabilistic Perspective 

### MLE = MSE
- We assume normally distributed residuals with zero-mean and fixed variance (independent from our weights or the input)
- We also assume equally probable $x$s, i think?
- Maximize the log-likelihood -> terms with variance are constant -> MSE / SSE remains

### Maximum A-Posteriori 
- Posterior $\propto$ Likelihood * Prior
- When maximizing the Posterior, we can just add the regularizer term for the prior to the negative log-likelihood
- $\lambda = (\sigma_1 / \sigma_2)^2$, where $\sigma_1$ is the std dev. of the residuals and $\sigma_2$ the std dev. of $p(w)$

### Posterior Distribution
1. Idea: find distribution over model parameters
2. Idea: use that to estimate prediction uncertainty / predictive distribution
