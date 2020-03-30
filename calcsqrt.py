#! /user/bin/env python3

# Davy Ryan
#calculate sqrt of number

def sqrt(x):
    z = x/2.0
    
    while(abs(x -(z*z)) > 0.01):
        z -= (z*z - x) /(2*z)

    return z

print(sqrt(63.0))
