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
- L2 Loss
- L1 Loss
- Xent softmax loss
- Hinge loss

### What is the difference between softmax loss and hinge loss?
- Softmax loss always wants to improve
- Hinge loss saturates

### What are the disadvantages of the sigmoid activation function?
- Strong gradient only around 0 -> active region for gradient descent
- Saturated neurons kill the gradient flow
- Output is always positive -> gradient in next layer will either be positive or negative for all weights -> inefficient updates

### What is the advantage and the disadvantage of the tanh activation function?

### What are the advantages and the disadvantage of the ReLU activation function?

### What are the advantages and the disadvantage of the Leaky ReLU activation function?

### What are the advantages and the disadvantage of the Parametric ReLU activation function?

### What are the advantages and the disadvantage of Maxout units?

### Give a quick guide to activation functions?
- Sigmoid is not really used
- ReLU is the standard choice
- Second choice are the variants of ReLU and Maxout
- RNNs require tanh or similar

### Name a method used in data preprocessing
For images, subtract the mean image.

# 8 - Training NNs 2

### Why shouldn't you just initialize the weights with zero?

### Why shouldn't you just randomly initialize the weights with a small standard deviationß

### Derive the Xavier init.

### When does Xavier fail? What can you do?

### Where in the architecture should the BN layer be applied?

### Why do you need gamma and beta for BN?

### How does BN work at test time?

### What are the benefits of Batch Normalization?

### What are the benefits of weight decay?

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

# 9 - CNNs

### What are the two assumptions of CNNs?

### What are the important parameters of a conv layer?

### What are the important parameters of a pooling layer?

### Give the equation for the number of neurons in a conv layer

### Give the equation for the number of parameters in a conv layer

### Give the equation for the number of operations needed for a forward pass of a conv layer

### Why do you need padding?
Otherwise:
- Sizes get small too quickly
- Corner pixel is only used once

### What is the difference between valid and same padding?

### How can you backprop through CNN layers?

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

### Give the equations for a basic RNN

### How can you backprop through a RNN?

### What is the problem of the basic RNN?
- Small weights / eigenvalues < 1 -> vanishing gradient
- Large weights / eigenvalues > 1 -> exploding gradient

### Draw / compare RNN to LSTM cell

### What are the gates in the LSTM for?

### Why does the LSTM work better than the RNN?

### Give the LSTM equations












