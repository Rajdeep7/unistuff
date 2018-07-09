# Introduction

### What were factors of the 2012 breakthrough?
- large data
- faster processing (GPU)
- better optimization and regularization techniques

### What are important requirements for an DL solution in Robotics?
- data efficiency
- robustness and uncertainty information
- autonomous learning
- interpretability

# Bayesian View of ML

### What does the No free lunch theorem state? Give two interpretations
- For each assumptions there are tasks which are not meeting them
- -> For every learning algorithm there is a distribution P on which it generalizes poorly
- -> No learning algorithm is better than any other when averaging over all possible distributions

### Give an example for the No free lunch theorem
- Density Estimation
- Without assumptions: sample a lot of times and count in M bins
  - Problem: number of bins needed increases exponentially with the number of dimensions
  - Problem: number of samples needed grows proportionally with M
- With Isotropic Gaussian assumption, just compute the mean and variance
  - much more efficient
  - strong assumption

### Is learning solved?
In theory yes with probabilistic ML -> tells us how to optimally generalize from given data and prior assumptions
In practice, we need 
- good prior assumptions for a given problem
- efficient algorithms for approximate inference

### 1 Write down the univariate normal distribution's pdf

### 2 Write down the multivariate normal distribution's pdf

### 3 Write down the expectation of f(x) under p(x)

### 4 Write down the variance of f(x) under p(x)

### 5  Write down the E_x[f|y]

### 6 Write down cov[x,y]

### 7 Write down the entropy

### 8 Write down the cross-entropy

### 9 Write down the KL divergence

### 10 Write down the predictive distribution for Bayesian Inference. What is the posterior?

### 11 How is prediction of p(y|D) made for MAP?

### 12 How is prediction of p(y|D) made for MLE?

### 13 Figure comparing Bayesian Inference, MLE and MAP

### 14 Given you have p(t|x,w) and p(w). What are these called? How do you do Bayesian Inference, MLE and MAP?

### 15 Write down the expected loss

### 16 Do a bias variance decomposition of the squared loss

### 17 Give the terms for the bias variance noise decomposition

### What is the meaning of the bias?
How far away is your prediction from the actual value on average

### What is the meaning of the variance?
how far^2 away is you prediction on average from your average prediction

### What is the decomposition of test error, training error, generalization gap and generalization error?
- test error = bias^2 + variance + noise
- train error = bias^2 + noise
- generalization gap = variance
- generation error = bias^2 + variance

### What do you do when train / test error high / low?
- Training error high -> Bias high -> Increase capacity
- Test error high, train error low -> Variance high but bias low -> Increase number of training samples or decrease model capacity
- Training error and test error high -> Bias and variance high -> Increase number of training samples and model capacity

### What are the benefits of Full Bayesian Inference?
- Notion of uncertainty of prediction
- No overfitting
- Known variance
- Smaller variance than for MAP
- Test error = training error -> No need for separate test set
- Either high bias or high but known variance

### How does Model Comparison work in Bayesian ML? Give the predictive distribution (18).
- Define model as a parameter that can be varied
- Prior becomes p(M, w)
- Probabilistic model becomes p(y|M, w)

# Advanced Network Architectures

### Why can't we just add features like for XOR?
- Would need many more features -> suffers from curse of dimensionality
- Would need many more training data to cover whole space, otherwise just local interpolation aroung training points

### Why is DL so much better?
- Hierarchy of parameterized non-linear processing units are fundamentally better probabilistic model / prior for real-world data -> better generalization
- Automatic feature extraction
- End-to-end learning in homogenous architecture

### Why use Batch Normalization?
- Avoid vanishing / exploding gradients / saturating neurons by normalizing **before** the activation function
- Works with almost arbitrary weight init and many saturating activation functions
- Reduce internal covariate shift

### Give the formula for BN (19)

### What are the two assumptions of CNNs?
1. Compositionally: hierarchy of local features
   - Nearby pixels are correlated -> Sparsity
   - Combination of local to global features
2. Translational invariance -> Weight sharing, Max Pooling

### What is the layer size with "same" zero padding?
N_L+1 = ceil(N_l / S)

### How many parameters does a CNN layer have?
- weights M^2 K' K
- biases N^2 -> untied biases
- operations N^2 M^2 K' K

### What networks came after AlexNet?
- VGG
- GoogleNet
- ResNet
- ResNext
- DenseNet

### What are the improvements of VGGNet?
- Smaller filters but more layers (19)
- Replace larger filters with stack of smaller ones
  - more non-linearities
  - less parameters
  - same receptive field

### How does Resnet solve the degradation problem?
- Degradation: more layers give larger training and test error
- Capacity is not the problem! Effective capacity is the problem
- Problem: learning to reproduce a simple linear mapping get harder with depth / a lot of non-linearities
- Solution: 
  - learn only deviation from a linear mapping per layer
  - input to each residual block gets added to output of residual block

### What is the ResNet architecture? What do you need for deeper layers?
- Every residual block has two 3x3 conv layers: BN, ReLU, weight, BN, ReLU, weight
- Regularly double # of filters and downsample spatially using stride 2
- No FC layers except for FC 1000, no dropout
- Original adds before nonlinearity, proposed / better method is to keep the shortcut path completely linear
- For deeper layers (50+)
  - Bottleneck layer reduces parameters
  - Instead of 256 x (3x3x256) use
    1. 64 x (1x1x256)
    2. 64 x (3x3x64)
    3. 256 x (1x1x64)
    
### What does a 1x1 Convolution do?
- Only makes sense when the number of feature maps is different from the input 
- Combines feature maps for each pixel individually
- Kind of selecting features to be processed before an expensive convolution

### What are the improvements of GoogLeNet?
- Goes Multi-Path
- Multiple Inception Modules
- Each Inception Module applys parallel filter operations on the input
- Process parts of features separately
- Feature maps of parallel layers are concatenated at the end -> more and more feature maps
- Drastically reduces the number of parameters

### What are the improvements of ResNext?
- Multi-path residual blocks
- Blocks are like inception modules but with homogenous parallel paths (32 in parallel)
- Parallel paths get added, not concatenated
- Increasing capacity by
  - cardinality (> 32) is best
  - depth is worst
  - width (number of feature maps) is middle

### What is the architecture of DenseNet?
- Every layer is connected to every upstream layer
- Channel-wise concatenation of inputs
- k computed channels per layer = growth rate
- Each layer has BN - ReLU - weights
- Optionally with bottleneck (BN - ReLu - 1x1 convolution) in front
- Whole net has 3 Dense Blocks
  - separated by max pooling to reduce feature map size
  - concatenated features are transferred from block to block

### What are the benefits of DenseNet?
- Strong gradient flow through direct connections between all layers
- Parameter and computational efficiency through diversified features instead of correlated features
- Maintains low complexity features / classifier uses features of all complexity levels
- Combines deeper, wider and multi-path

### What are three questions to a new architecture?
- How well does it generalize?
- How easy to optimize?
- Computational effort?

# Advanced Network Architectures II

### How does Image Segmentation with Pixelwise Scanning work? Is it good?
- Classify one pixel at a time
- Move network pixelwise over larger images
- Problem:
  - Very inefficient at test time
  - Network reduces spatial resolution -> precise segmentation borders hard

### How can you convolutionalize a fully connected layer?
- Number of "feature maps" = number of neurons
- Kernel size is full input
- Stride 1, padding 0

### What is a fully convolutional network?
- All layers are convolutional
- Uses transposed convolution for upsampling
- The less downsampling layers before the upsampling the better (FCN-8s > FCN-32s)

### What are methods to get a small feature map to a big feature map again?
- Basic upsampling -> Just add padding in between the cells
- Transposed Convolution / Deconvolution / Upconvolution 
  - Upsample input so that after the convolutional layer, it has the expected shape
  - -> Linear upsampling
  - Kernel parameters learned
- Unpooling

### How can you upsample max pooling layers?
- Remember indices from max pooling layer
- Put zeros at other cells

### Name three methods for Image Segmentation
- FCNs
- SegNet
- FC-DenseNet

### How does SegNet work?
- 13 convolutional layers from VGG followed by their transposed counterparts
- Pixelwise softmax

### How does SegNet compare to FCN?
- FCN only learns the final transposed convolution parameters followed directly by the softmax
- SegNet applies hierarchy of convolutional layers after unpooling
- SegNet is more precise

### How does FC-DenseNet work?
- U-net architecture with bottleneck
- Skip connections for high resolution maps
- Very deep, very few parameters
- Way better than the other methods

# Adversarial Training

### How can you enhance network performance?
Work on 
- Probabilistic model -> prior via weight decay
- Optimization in point estimate methods -> early stopping, BN...
- Towards Bayesian Inference
  - Ensemble methods
  - Dropout

### General equation for finding an adversarial example (20)

### Specific equation for finding an adversarial example (21)

### Why does FGSM use the sign?
- Guarantees that maximum pixel change is limited by epsilon
- Also take the most out of the other pixels while satisfying this constraint

### Why is overfitting not the problem causing adversarial examples?
Trained with different data and different initial weights, got almost the same adversarial examples

### What causes adversarial examples?
- Excessive linearity
- Activity before the softmax is only non-linear for small epsilon
- Quickly becomes linear -> False classes with high confidence

### Why does data augmentation with noise not help against adversarial attacks?
Number of additional samples needed grows exponentially with input dimensionality

### What is the FGSM? (22)
- Fast Gradient Sign Method

### What is the error function for adversarial training? (23)

### What are the benefits of adversarial training?
- Improves generalization as a regularization method
- Robust against attacks with the same kind of adversarials
- Low computational overhead
- Makes NNs have the best empirical success rate on advserarial examples of any ML model!

### What are drawback of adversarial training?
- Still vulnerable to adversarial attacks
- High confidence for false classification

### Why does adversarial training work despite of the excessive linearity problem?
- Neural networks can represent almost any function
- Adversarial training forces the network to represent a more robust solution

### Name three methods against adversarial attacks?
- Adversarial training with FGSM
- Virtual Adversarial Training
- Bayesian learning 

### 





