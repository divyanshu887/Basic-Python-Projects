# Ridge Regression

## &nbsp; Introduction
- Ridge regression also known as Tikhonov regularization uses L2 penalty for regularization.
-
-

## &nbsp; Working of Ridge Regression
-
-
-

## &nbsp; Ridge Regression Cost Function
<p align="center">
  <img src="https://miro.medium.com/max/421/1*XN9hxyk82UySDAvQ_9w76Q.gif">
</p>

## &nbsp; Ridge Regression Constrain
<p align="center">
  <img src="https://miro.medium.com/max/875/1*sC4KLMHU0j_1gR3VmlgGtg.png">
</p>

where,
- c is the upper bound
- n is number of training examples
- D is the number of features 
- λ denotes the amount of shrinkage.

## &nbsp; Different cases for tuning values of lambda.
- λ = 0 implies all features are considered and it is equivalent to the linear regression where only the residual sum of squares is considered to build a predictive model
- λ = ∞ implies no feature is considered i.e, as λ closes to infinity it eliminates more and more features
- 0 < λ < ∞ : We get weights between 0 and that of simple linear regression

## &nbsp; Advantage of Ridge Regression
- It avoids overfitting a model.
- It trades variance for bias 

## &nbsp; Disadvantage of Ridge Regression
- It cannot shrink coefficients to exactly zero, which indicates that there is no feature selection.   
- Its model interpret-ability is low
- It increases bias
