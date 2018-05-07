# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:20:36 2018

@author: 其明
"""

'''样本均值法'''

from numpy import *

n=10000
u=random.rand(n)
y=exp(u)
Theta_hat=sum(y)/n
print('Theta_hat=',Theta_hat)