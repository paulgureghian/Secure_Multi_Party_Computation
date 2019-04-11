""" Created in Apr 2019 by Paul A. Gureghian """

""" SMPC can split data and add encrpyted variables to other encrpyted variables """
""" And multiply encrypted variables with plaintext values. """

### Import Numpy
import numpy as np

### Demo of SMPC 
Q = 501337
def encrpyt(x):
    share_a = np.random.randint(0,Q)
    share_b = np.random.randint(0,Q)
    share_c = (x - share_a-share_b) % Q
    return (share_a, share_b, share_c)

def decrpyt(*shares):
    return sum(shares) % Q

def add(x, y):
    z=[]
    assert (len(x) == len(y))
    for i in range(len(x)):
        z.append((x[i] + y[i]) % Q)
    return z
    
def product(x, w): # w is a plaintext value
    z=[]
    for i in range(len(x)):
        z.append((x[i] * w) % Q)
    return z
    
### Encrpyt variables
var1 = encrpyt(2)
var2 = encrpyt(5)        
    
### Get sum
get_sum = add(var1, var2)

### Print results
print(get_sum)
print(decrpyt(*get_sum))
print(decrpyt(*get_sum[0:2]))  



     
    
    
    
    
    







     
    
    