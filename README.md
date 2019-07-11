# AML_2019 Coursework, Part 1, Group 7
## Experiments with Gradient Descent
---
## Introduction

In machine learning, the loss function measures the accuracy of our models, by taking the difference of the actual values and the predictions. The gradient descent is an iterative machine learning algorithm used to select the parameters which minimises the loss function. The algorithm is important because it provides a computatively efficient way to solve the optimisation problem, allowing us to improve the accuracy of the predictions. 

The algorithm work in a similar way as the following analogy. Imagine walking half-way on a mountain and trying to get to the valley. Firstly, from where the person is standing, measure the slope of the mountain in all directions. Then, pick the direction that has the steepest slope downwards. Walk for a short distance (fixed step size) in this direction and then repeat the process again. Since the direction of movement is always downwards, this process will eventually allow the person to get to the valley of the mountain. 

However, the algorithm stops at local minimum or saddle point, which may not be the global minimum.

## Plain vanilla

<p align="center">
  <img width="800" height="360" src="https://github.com/Emanon0041/aml_2019_G7/blob/master/images/gd_01_pv.png">
</p>

## Momentum


---
## Nesterov's Accelarated Gradient (NAG)

## Experiments with Gradient Descent
I might include some tables here and references to my code.

| Method              | Convergence ?  |Step size   |
|---------------------|----------------|------------|
|Plain vanilla        | Yes            |426         |
|Momentum             | Yes            |1460        |
|NAG                  | Yes            |607         |

---

