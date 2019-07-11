# AML_2019 Coursework, Part 1, Group 7
## Experiments with Gradient Descent
---
## Introduction

In machine learning, the loss function measures the accuracy of our models, by taking the difference of the actual values and the predictions. The gradient descent is an iterative machine learning algorithm used to select the parameters which minimises the loss function. The algorithm is important because it provides a computatively efficient way to solve the optimisation problem, allowing us to improve the accuracy of the predictions. This report will introduce how the plain vanilla algorithm and its two modifications work, by using the Three-Hump Camel Function as an example, see <a href="url">http://www.sfu.ca/~ssurjano/camel3.html</a> for more detail. 

_（ Gradient descent is an optimization technique to find the loss function minimum by going in the direction of negative gradient. The advantage of using gradient descent is when dealing with large multivariate functions (a matrix), traditional linear algebra technique might take a long time to compute the matrix inverse, whereas gradient descent can save a lot of computation time through parallelising computing. ）_

## Plain vanilla

The algorithm work in a similar way as the following analogy. Imagine walking half-way on a mountain and trying to get to the valley. Firstly, from where the person is standing, measure the slope of the mountain in all directions. Then, pick the direction that has the steepest slope downwards. Walk for a short distance (fixed step size) in this direction and then repeat the process again. Since the direction of movement is always downwards, this process will eventually allow the person to get to the valley of the mountain. 

### Step sizes (learning rate)

| Step size       | Number of step| 
|----------------|-------------|
|0.0005           | 2726        |
|0.001            | 1362         |
|0.002            | 681           |
|0.004           | 340            |
|0.008            | 170         |
|0.016            | 20           |
|0.128           | did not converge in 10000 steps       |
|0.256            | did not converge in 10000 steps       |

Step size doubled, number of step decreases by half????

However, the path did not converge (within 10000 steps) if eta was 0.128 or above. The above experiment shows the gradient path
 -	takes a long time to convergence if step size is too small
 -	does not converge at all if the step size is too big

<p align="center">
  <img width="800" height="360" src="https://github.com/Emanon0041/aml_2019_G7/blob/master/images/gd_01_pv.png">
</p>

From the above graphs, the algorithm stops at local minimum, which may not be the global minimum.

## Momentum


## Nesterov's Accelarated Gradient (NAG)


## Experiments with Gradient Descent
I might include some tables here and references to my code.

| Method              | Convergence ?  |No. of steps  | loss function|
|---------------------|----------------|--------------|--------------|
|Plain vanilla        | Yes            |426           |-0.21546379471670118|
|Momentum             | Yes            |1460          |-1.0316283918420706|
|NAG                  | Yes            |607           |-1.0316272989132922|

---

