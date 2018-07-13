# IN2349 - Advanced Deep Learning for Robotics

Course page: https://bbaeuml.github.io/ss18-advanced-dl-for-robotics/

`Summary.md` contains the content of all lectures in Q&A format. Most of the content consists of formulas (for example derivation of Monte Carlo Dropout). These are not in the .md file, so it might not be too helpful for studying for the exam.

The exam contained three large exercises:
1. Bayesian Deep Learning
   - Give the Predictive Distribution for Full Bayesian and MLE
   - Given KL(q(w)||p(w|X,T)), derive the ELBO
   - Explain why the ELBO actually is the lower bound for the evidence (because KL >= 0)
   - Explain what the training and test error consist of (test error = bias^2 + variance + noise)
2. Adversarial Training
   - Give the general search criterion
   - Explain FGSM with equations
   - Explain Virtual Adversarial Training and give its search criterion
   - Explain what the main problem enabling adversarial attacks on neural networks is
3. Reinforcement Learning
   - Give the Bellman equation
   - How can discrete and continuous actions be sampled, when a neural network is used to represent the policy?
   - Something about Policy Gradients
   - Something about Q-learning
