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

### Give the equation for the binary cross-entropy loss
L(t, y) = t log y + (1-t) log (1-y)

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
- Comparable architectures

### Why should you use a computational graph?
- Can easily modularize complex functions
- Language agnostic -> create in python, execute in C

### What happens if there are multiple outputs in a compute node?
Add the incoming gradients up

### What happens if there are loops in the graph?
Either they are infinite, then the forward pass never ends or they are limited by some condition then they can be expressed as a finite series of nodes -> acyclic graph.

### Why backpropagation and not forward propagation of gradients?

# 4 - Backpropagation

### Derive the gradients for a two-layer neural network with cross-entropy loss

### Derive the sigmoid function

### Draw the computational graph for two inputs, no hidden layer, three outputs and squared error

### What does w_a,b,c denote?
- layer a
- neuron b
- weight c

### Draw the computational graph for one hidden layer

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
velocity = beta * velocity + gradient
theta = theta - alpha * velocity

or 

v^k+1 = beta * v^k + Nabla_theta L(theta^k)
theta^k+1 = theta^k - alpha * v^k+1

### Why do we need momentum?
- Exponentially weighted average of gradient
- Averages out oscillating gradients
- Accumulates series of gradients pointing in the same direction
- Functions per direction!

### How does Nesterov's Momentum work?
- Same as momentum, except for the computation of the gradient
- Compute the gradient at theta_k + v_k instead of theta_k

### What does RMSProp do? Give the update equation
- Divides the learning rate by an exponentially-decaying average of squared gradients

Average is s:
s^k+1 = beta * s^k + (1-beta) * squared gradient
theta^k+1 = theta^k - alpha * gradient / (sqrt(s^k+1) + epsilon)

### What is the advantage of RMSProp?
- s can be interpreted as the uncentered variance of gradients -> second momentum
- Dividing by square gradients:
  - Division in directions of low variance will be small
  - Division in directions of high variance will be large
- -> Dampening the oscillations for high-variance directions
- -> less likely to diverge
- -> can increase the learning rate

### What does Adam do? Give the update equations
Combines momentum and RMSProp
m = first momentum (mean of gradients)
v = second momentum (variance of gradients)

m = beta1 * m + (1-beta1) * gradient
v = beta2 * v + (1-beta2) * squared gradient

theta = theta - alpha * m / (sqrt(v) + epsilon)

### What doe bias correction mean for Adam?
m and v are initialized with zero -> bias towards zero
-> bias-corrected moment updates:
m' = m / (1-beta1)
v' = v / (1-beta2)

theta = theta - alpha * m' / (sqrt(v') + epsilon)

### What is the advantage of Adam?
- Combines momentum and RMSprop / first and second order momentum

### What does AdaGrad do? Why is AdaGrad not used very often?
- Adapt the learning rate of all model parameters
- It accumulates gradients from the beginning
- In theory: more progress in regions where the function is more flat
- In practice, this results in excessive decrease in the effective learning rate for most DL models

### Draw a very high learning rate, high learning rate, good learning rate and low learning rate

### What is the difference between a gradient and a derivative?
- Derivative is scalar
- Gradient is multi-variable generalization of the derivative

### True or false: the hessian is the transposed jacobian of the gradient?
So true.

### Explain Newton's method
- Approximates the function by a second-order Taylor series expansion
- Closed form solution for minimum of expansion
- No learning rate required
- Requires computing the Inverse of the Hessian matrix

### Can you apply Newton's method for linear regression? What do you get as a result?
Optimal solution after first iteration

### Why can't you simply use Newton's method for Deep Learning?
- Requires computing the inverse of the Hessian matrix
- Hessian matrix has length(theta)^2 elements
- Computational complexity is O(length(theta)^3) per iteration
- Also, Newton, L-BFGS etc. don't work well for minibatches

# 6 Optimization 2

### Give two ways of decaying the learning rate
- lr = 1 / (1 + rate * epoch) * lr_init
- lr = (1-t) * lr -> every n steps

### What happens if the LR is too high? What if too low?
- too high:
  - training error increases
  - or oscillates around local minimum
- too low:
  - very slow convergence

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
- Number of iterations
- Learning rate / solver paramters
- Regularization
- Batch size

### When should you use cross validation?
When data set is extremely small and / or our model has low training times

### How do you do cross validation?
- Partition data into k subsets, train on k-1 and evaluate performance on the remaining subset
- Compute mean and standard deviation of the different performance scores

# 7 - Training NNs

### Write down the Softmax and its MLE loss function
-log (softmax output for target)

### Compare L1 to L2 loss as output losses
L2 Loss:
- Sum of squared differences
- Prone to outliers
- Compute-efficient
- Optimum is the mean

L1 Loss: 
- Sum of absolute differences
- Robust to outliers
- Costly to compute
- Optimum is the median

### Give the equations for 4 different output losses
- L2 Loss sum_i^n (y_i - f(x_i))^2
- L1 Loss sum_i^n |y_i - f(x_i)|
- Xent softmax loss -log (softmax output for target)
- Hinge loss sum_j != y_i max(0, s_j - s_y_i + 1) -> overall loss is averaged over samples

### What is the difference between softmax loss and hinge loss?
- Softmax loss always wants to improve
- Hinge loss saturates

### What are the disadvantages of the sigmoid activation function?
- Strong gradient only around 0 -> active region for gradient descent
- Saturated neurons kill the gradient flow
- Output is always positive -> gradient in next layer will either be positive or negative for all weights -> inefficient updates

### What is the advantage and the disadvantage of the tanh activation function?
- Advantage: zero centered
- Disadvantage: saturates, strong gradient only around 0

### What are the advantages and the disadvantage of the ReLU activation function?
- Advantages: fast convergence, does not saturate, large and consistent gradients
- Disadvantage: zero input / output kills the gradient

### What are the advantages and the disadvantage of the Leaky ReLU activation function?
- Advantages: does not die, fast convergence, does not saturate, large and consistent gradients
- Disadvantage: slope hyperparameter needs to be tuned

### What are the advantages and the disadvantage of the Parametric ReLU activation function?
- Advantages: does not die, fast convergence, does not saturate, large and consistent gradients
- Disadvantage: slope parameter needs to be trained and bounded

### What are the advantages and the disadvantage of Maxout units?
- Advantages:
  - Generalization of ReLUs
  - Linear regimes
  - Does not die
  - Does not saturate
- Disadvantage: Increase of the number of parameters

### Give a quick guide to activation functions
- Sigmoid is not really used
- ReLU is the standard choice
- Second choice are the variants of ReLU and Maxout
- RNNs require tanh or similar

### Name a method used in data preprocessing
For images, subtract the mean image.

# 8 - Training NNs 2

### Why shouldn't you just initialize the weights with zero?
Hidden units all compute the same function
-> Gradients all the same
-> Need to break symmetry somehow

### Why shouldn't you just randomly initialize the weights with a small standard deviation?
- Activations quickly become zero, even after only 10 layers
- Multiplying independent Gaussians with small stddev with each other pushes the values towards zero
- Gradients vanish because inputs to layers are close to zero

### What does the Xavier init do?
- We want our input to have the same variance as our score (before activation function)
- Var(output) = (n Var(w)) Var(x) 
- -> scales linearly with number of inputs
- -> set Var(w) to 1/n

### When does Xavier fail? What can you do?
- Fails for ReLU, more and more activations become zero with increasing layers
- Set Var(w) to 2/n

### Where in the architecture should the BN layer be applied?
After the weights (fully connected or convolutional) and before the non-linearity

### Why do you need gamma and beta for BN?
- Unit Gaussians everywhere might not be best for the network
- Enable a layer to undo the BN

### How does BN work at test time?
Compute mean and variance by running an exponentially weighted average across training mini-batches 

### What are the benefits of Batch Normalization?
- Very deep nets are much easier to train because of more stable gradients
- Much larger range of hyperparameters works similarly
- Reduces internal covariate shift

### Add weight decay to E
E = E + lambda delta^T delta

### What are the benefits of weight decay?
- Penalizes large weights
- Improves generalization

### Explain methods of data augmentation for images. If necessary, also explain what to do during test time
- (Random) cropping
  During test time, no random cropping but a fixed set of crops!
- Flipping the image
- Random brightness and contrast changes

### Name regularization techniques
- Weight decay
- Data augmentation
- Early stopping
- Bagging (different learning algorithm, different objective function etc.)
- Dropout

### What is a condition for an error decrease caused by ensemble methods?
Uncorrelated errors -> error will decrease linearly with the ensemble size

### What is the intuition behind dropout?
Central: reducing co-adaptation between neurons

Causes redundant representations:
- Randomly removing neurons avoids highly specialized neurons with high outgoing weights
- Forces more distributed representations and more balanced weights
- -> Robust to small changes in the input

Can be considered as an ensemble of networks:
- Efficient bagging method with parameter sharing
- Dropout implcitly creates ensemble of various networks, where each network is only trained on one mini-batch
- Each model in the ensemble makes an error
- When taking the average of the predictions, the errors are also averaged
- For uncorrelated errors, this linearly decreases the variance of the error with the ensemble size
- Errors are not uncorrelated, but also not completely correlated because of weight inits and random mini-batches

### What is the disadvantage of dropout?
Reduces the effective capacity of a model -> larger models need more training time

### What is the weight scaling inference rule?
Scale layer's output with dropout rate at test time to keep the expected total activation level the same

# 9 - CNNs

### What are the two assumptions of CNNs?
TODO

### What are the advantages of Convolutional Layers compared to Fully Connected Layers?
TODO

### What are the important parameters of a conv layer?
- Input size N
- Spatial filter extent F
- Number of filters K
- Padding P
- Stride S

### What are the important parameters of a pooling layer?
- Input size N
- Spatial filter extent F
- Padding P (although padding makes no sense according to the lecture)
- Stride S

### Give the equation for the number of neurons in a conv layer
(N + 2*P - F) / S + 1

### Give the equation for the number of parameters in a conv layer
F * F * D_in * K + K

### Give the equation for the number of operations needed for a forward pass of a conv layer
TODO

### Why do you need padding?
Otherwise:
- Sizes get small too quickly
- Corner pixel is only used once

### What is the difference between valid and same padding?
Same padding keeps the input and output width / height constant, if stride = 1 -> P = (F - 1) / 2
Valid uses no padding

### How can you backprop through CNN layers?
TODO

# 10 - CNNs 2

### What architectures came after AlexNet?
- ZFNet
- VGG
- GoogleNet
- Resnet

### What were the improvements of LeNet? How many parameters did it have?
- Actual use of conv layers
- Reduce spatial filter extent while increasing number of filters
- Use average pooling
- 60K parameters

### What were the improvements of AlexNet? How many parameters did it have?
- Use max pooling
- Use ReLUs
- Use Dropout
- Use same padding
- 60M parameters

### What were the improvements of VGG? How many parameters did it have?
- Striving for simplicity
- Smaller filters but more layers
- Replace larger filters with stack of smaller ones (7x7 -> 3 3x3 filters)
- Number of filters multiplied by 2 after a pooling layer
- Analyzed a lot of architectures
- 138M parameters

### What were the improvements of Resnet?
- Solves the degradation problem (more layers give larger training and test error)
- Makes it easy for the residual block to learn a linear mapping, even with great depth
- Each block only learns a deviation from the linear mapping
- Skip connections: output = f(Wx + b + input)
- Use same padding, because we need same dimensions for the addition

### Draw the concept of a Resnet block

### Why do we need 1x1 convolutions?
- To shrink the number of channels
- Further adds a non-linearity
- Combines feature maps for each pixel individually
- Kind of selecting features to be processed before an expensive convolution

### What were the improvements of GoogleNet? How many parameters did it have?
- Use multiple filter sizes per inception module
- Multipath -> process parts of features separately
- 1x1 convolutions before expensive convolutions and after max pooling to reduce the share of the max pooling layer in the output
- Concatenate the feature maps of each path
- Drastically reduces the number of parameters (5M)

### Draw an Inception module

### What does transfer learning do?
- Use what has been learned for another setting
- For example use Net from large dataset for small dataset

### When does transfer learning make sense? (From P1 to P2)
- When task P1 and P2 have the same input (for example an RGB image)
- When you have more data for task P1 than for task P2
- When the low-level features of P1 could be useful to learn P2

# 11 RNNs

### When do we need RNNs?
- Variable input length
- And / or variable output length

### Give the equations for a basic RNN
A_t = f(theta_c A_t-1 + theta_x x_t)
h_t = g(theta_h A_t)

### How can you backprop through a RNN?
Unroll it as a feedforward net all the way to t=0
-> weights will be the same in each step
-> add the derivatives at different times for each weight

### What is the problem of the basic RNN?
- Small weights / eigenvalues < 1 -> vanishing gradient
- Large weights / eigenvalues > 1 -> exploding gradient

### Draw / compare RNN to LSTM cell

### What are the gates in the LSTM for?

### Why does the LSTM work better than the RNN?

### Give the LSTM equations












