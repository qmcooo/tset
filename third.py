# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:29:07 2018

@author: 其明
"""

'''重要性抽样'''

from numpy import *

n=10000
u=random.rand(n)
x=u
y=exp(x)
#Theta_hat=3*sum(y/(1+x))/(2*n)
Theta_hat=5*sum(y/(1+x+0.5*square(x)))/(3*n)
print('Theta_hat=',Theta_hat)