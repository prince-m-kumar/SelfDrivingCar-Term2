from math import *

#Maximize Gaussian
def function(mu,sigma2,x):
	return 1/sqrt(2.*pi*sigma2)*exp(-.5*(x-mu)**2/sigma2)

print (function(10.,4.,8.))


# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean =((mean1*var2)+(mean2*var1))/(var1+var2)
    new_var =(var1*var2)/(var1+var2)
    return [new_mean, new_var]



print (update(10.,8.,13., 2.))

# Write a program that will predict your new mean
# and variance given the mean and variance of your 
# prior belief and the mean and variance of your 
# motion. 


def predict(mean1, var1, mean2, var2):
    new_mean =mean1+mean2
    new_var =var1+var2
    return [new_mean, new_var]



print (predict(10., 4., 12., 4.))








