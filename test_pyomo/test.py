#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

print(np.tile(np.array([-1, 0, 1, 2]), (4,2)))

xi=[1,2,3,4,5]
x=4.5
i = np.searchsorted(xi, x) - 1
print(i)
print(3--3)