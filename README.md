# AML_2019 Coursework, Part 1, Group 7
## Experiments with Gradient Descent
---
## Introduction

Loss function is a measure of the accuracy of our models, through quantifying the difference of the actual values and the predictions. The gradient descent is an iterative machine learning algorithm used to select the parameters which minimises the loss function. The algorithm is important as it provides a computatively efficient way to solve the optimisation problem through parallelising computing, which is particularly advantageous for large multivariate functions. This report will introduce how the plain vanilla algorithm and two of its modifications, using the Six-Hump Camel Function as an example. Please read <a href="url">http://www.sfu.ca/~ssurjano/camel3.html</a> for more detail. 

## Plain vanilla

The algorithm works in a similar way to the following analogy. Imagining a person half-way to the top of a mountain, trying to get to the bottom of the valley. This can be acheived by carrying out the following steps. Firstly, from where the person is standing, measure the slope of the mountain in all directions. Secondly, choose the direction with the steepest downwards slope. Walk for a short distance (fixed step size) in this direction and repeat the process. Iteratively, this process will allow the person to get to a point where he can no longer find any downward sloping directions to continue walking -- at the valley bottom !

### Step sizes (learning rate)

The table below summarises, for different step sizes, the number of steps needed to convergence. Click <a href="url">https://github.com/Emanon0041/aml_2019_G7/blob/master/images/step_size.png</a> to see a graphical representation of the results. 

| Step size       | Number of step| 
|----------------|-------------|
|0.0005           | 2726        |
|0.001            | 1362         |
|0.002            | 681           |
|0.004           | 340            |
|0.008            | 170         |
|0.016            | 20           |
|0.128           | did not converge in 10000 steps       |
|0.256            | did not converge in 10000 steps      |

Initially, as the step size doubles, the number of iterations would be reduced by approximately 50%. However, for larger step sizes, e.g. 0.128 the path will not converge. The above experiment shows that the gradient path
 -	takes more steps to convergence if the step size is too small
 -	will not converge if the step size is too big
 
### One example 

The graph below shows the function surface and the gradient path using the parameters 
- x_init = [2.0,-1.0]
- n_iter = 3000 
- eta = 0.001 
- tol = 1e-3 

<p align="center">
  <img width="800" height="360" src="https://github.com/Emanon0041/aml_2019_G7/blob/master/images/gd_01_pv.png">
</p>

The algorithm took 426 steps to converge and the loss function was -0.21546. From the gradient path, the algorithm stopped at a local minimum, which, in this case, is not the global minimum. To cope with this problem, we investigate two further modifications to the plain vanilla algorithm. 

## Momentum

Momentum improves upon the plain vanilla algorithm to take into account the previous step. The step size is positively correlated with that of the previous step. The step size will be non-zero even if the gradient is zero. This deals with the problem of saddle points so that the algorithm will no longer stop when reaching such a point. From the graph below, it can be seen that the global minimum is acheived using the same parameters as the plain vanilla algorithm. 

<p align="center">
  <img width="800" height="360" src="https://github.com/Emanon0041/aml_2019_G7/blob/master/images/gd_02_mm.png">
</p>

## Nesterov's Accelarated Gradient (NAG)

NAG is another improvement over the plain vanilla algorithm. Instead of looking at the current slope, the algorithm looks ahead instead for the gradient of the slope in the front. It reduces the step size when the slope ahead is getting flatter or in reversing direction. Using the same parameters, this algorithm took significantly fewer steps than Momentum to acheive convergence. The graphs below shows the function and gradient path for this algorithm.

<p align="center">
  <img width="800" height="360" src="https://github.com/Emanon0041/aml_2019_G7/blob/master/images/gd_03_nag.png">
</p>



## Experiments with Gradient Descent

Pyhton code can be found in the link <a href="url">https://github.com/Emanon0041/aml_2019_G7/blob/master/Group7_Part1_GD.ipynb</a>

| Method               |No. of steps to converge  | Loss function (6 dp)|Description|
|---------------------|--------------|--------------|------------------|
|Plain vanilla        |426           |-0.215463| stops at a local minimum|
|Momentum             |1460          |-1.031628| takes a large number of steps to converge
|NAG                  |607           |-1.031627| performs the best|

The results are summarised in the table above. It can be seen that the NAG is the best algorithm, as it found the global minumum and did it in fewer steps than Momentum.

---

