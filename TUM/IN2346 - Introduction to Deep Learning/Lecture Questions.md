# 1 - Introduction

### What is the formal definition of Machine Learning?
Very common definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E."

### Does a validation / test set still make sense for unsupervised learning?
Yes, in order to find out if the findings (for example clustering) generalize well.

# 2 - Linear Regression

### Give the objective function of linear regression

$J(\theta) = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)^2$

### Derive the closed form solution for linear regression

### For univariate linear regression, show that MLE = Least Squares Estimate given that the mean is modeled by the linear regression and the variance is fixed.

### Given that we optimize the parameters of logistic regression with MLE, derive the loss function

### Why should you use the analytical gradient over the numerical gradient?
Approximate and slow vs. exact and fast

### What is the difference between L1 and L2 regularization?
- Different p-norm
- L1 enforces sparse weights, L2 weights will take "all information into account"
- L2 enforces weights with similar values

### What is regularization?
Any strategy that aims to lower the validation error by increasing the training error

# 3 - Introduction to Neural Networks

### Why activation functions?
W_3 (W_2 (W_1 x)) = W' x 

### Name and give formulas for seven different activation functions
- Sigmoid: sigma(x) = 1 / (1 + e^-x)
- Tanh: tanh(x)
- ReLU: max(0,x)
- Leaky ReLU: max(c x, x)
- Parametric ReLU: max(p x, x)
- Maxout: max(h_1, h_2)
- ELU: alpha * (e^x - 1) if x < 0 else x

### Why organize a neural network into layers?
- Fast to compute with matrix operations
- Enables weight sharing in CNN layers

### Why should you use a computational graph?
- Can easily modularize complex functions

### What happens if there are multiple outputs in a compute node?

### What happens if there are loops in the graph?

### How do you handle large Jacobians (4000 input, 4000 output, batch size 16)

### Why backpropagation and not forward propagation of gradients?

# 4 - Backpropagation

### Derive the gradients for a two-layer neural network with binary cross-entropy loss

### Draw the computational graph for two inputs, no hidden layer, three outputs and squared error

### Why do we only compute the partial derivatives w.r.t. the weights and not the full derivatives?

# 5 - Optimization

### How is a convex function defined?
A line / plane segment between any two points lies above or on the graph

### Give the equation for a single parameter update on a single training example with SGD
theta_k+1 = theta_k - alpha * gradient of loss w.r.t. theta

### What is the difference between iteration and epoch?
- Iteration = One training step / one update of the parameters using the mini-batch
- Epoch = One complete pass through training set
- If dataset is small and fits into the memory, then batch gradient descent would mean 1 iteration = 1 epoch

### What are the problems of SGD?
- Gradient is scaled equally across all dimensions
  - cannot indepenently scale directions
  - need to have conservative min learning rate to avoid divergence
  - slower than necessary
- Finding a good learning rate is an art by itself

### Give the update equation of SGD with Momentum

### What is the advantage of Nesterov's Momentum?

### How does Nesterov's Momentum work?

### Give the update equation of Nesterov's Momentum

### What does RMSProp do? 

### What is the advantage of RMSProp?

### What does Adam do?

### What is the advantage of Adam?

### What does AdaGrad do?

### Why is AdaGrad not used very often?

### Draw a very high learning rate, high learning rate, good learning rate and low learning rate

### What is the difference between a gradient and a derivative?
- Derivative is scalar
- Gradient is multi-variable generalization of the derivative

### True or false: the hessian is the transposed jacobian of the gradient?
So true.

### Explain Newton's method

### Can you apply Newton's method for linear regression? What do you get as a result?

### Why can't you simply use Newton's method for Deep Learning?

# 6 Optimization 2

### Give two ways of decaying the learning rate
- lr = 1 / (1 + rate * epoch) * lr_init
- lr = (1-t) * lr -> every n steps

### What happens if the LR is too high? What if too low?

### What are training, validation and test set for?
Training set:
- For training the neural network
Validation set:
- Hyperparameter optimization
- Check generalization progress
Test set:
- Only for the very end
- Never touch during development or training

### Name hyperparameters
- Network architecture (# layers, # weights)
- # iterations
- Learning rate / solver paramters
- Regularization
- Batch size

### When should you use cross validation?
When data set is extremely small and / or our model has low training times

### How do you do cross validation?
- Partition data into k subsets, train on k-1 and evaluate performance on the remaining subset
- Compute mean and standard deviation of the different performance scores

# 7

# 8

# 9

# 10

# 11
