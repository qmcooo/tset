# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:33:25 2018

@author: 其明
"""

'''随机投点法'''

from numpy import *

n=10000
u=random.rand(n)
v=random.rand(n)
x=u
y=e*v
n0=size(where((exp(x)>=y)==True))
Theta_hat=e*n0/n
print('Theta_hat=',Theta_hat)