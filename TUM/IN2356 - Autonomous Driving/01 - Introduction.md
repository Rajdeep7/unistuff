# Introduction (Apr 10 and Apr 17 2018)

## Current Research Topics

### RACE 
Since the technology in cars improved over many decades, the electronics are chaotic. RACE aims to provide a simple and structured system.

### Adversarial Examples
Not only small pixel perturbations but also objects in the physical world can make a model trained on ImageNet predict obviously wrong categories. (In the video, they printed a texture onto a turtle).

### Semantic Scenario Inerpretation and Decision Making
Goal was to restrict the learning algorithm by giving it a hard-coded ontology of high-level driving rules

### Digital Testfield
Roads and highways, where german car manufacturers can try out their autonomous vehicles

### Multisensor Data Fusion
Radars and Neural Networks are not always correct - the goal is to reconcile their outputs to produce better estimates (ensemble learning).

### Robinos Model Cars
- Hardware-agnostic software solution for AD
- Modularization with open specification -> companies can exchange modules

### Robinos Model Cars - Situative behavior arbitration block
- Execute algorithms in parallel (result + certainty of result + desire)
- Important definitions (exam!) / properties of functions / behaviors:
  1. **Applicability:** The ability of the function to operate, expressed in percent. A lane change might set this to 100%, if all conditions are met, or 30%, if lane markings are unclear, or 0%, if the lane is occupied.
  2. **Desire:** Desire of the function to operate, in percent. ACC with input 130 km/h mit set this to 100%, if the highway is empty, but 50% if it is behind a slower car.
  3. **Risk:** Risk involved when performing the behavior, in percent. Lane change with optimal conditions might set this to 20%, but if another car is approaching with high spee, to 90%.
  4. **Comfort:** Comfort to the driver when performing the behavior, in percent. High lateral or longitudinal acceleration / deceleration will result in a low comfort level.
  
## Robot architectures
### PCA flow
- Environment -> Perception -> Cognition -> Action -> Environment -> PCA -> ...
- Information flow becomes really important!

### Robotics over time
- Industrial Robotics, Service Robotics and Passenger Cars were almost complete separated
- Now, the become more and more similar
- In the future, the basic technologies will converge
- There won't be a universal robot!

## Notes
- The topics listed on the course website are currently inaccurate 
- High resolution maps will be a main topic in the exam
- Exam preparation lecture will contain hints about what will be in the exam
- The exam won't be easy
- The "desired outcome" part on slide 6, lecture 1 will be a guideline for the exam
- Convoy track (convoy truck) might be a good topic for the exam
- Throughout the lectures, the lecturer will go through old exam questions, explain why these questions were asked etc. -> more hints about the exam!
- The exam will be on August 4 2018, 9:30 - 11:30 (exam time 10:00 - 11:00) in MW 2001 / MW 0001
