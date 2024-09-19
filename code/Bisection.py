import numpy as np

#Bisection Method to find the root of a function given an interval

def Bisection_Method(func, a, b,tol):
    c_val = lambda x,y: (x+y)/2 #midpoint
    if func(a) * func(b) >  0 : #no root in interval
        print('Invalid Points')
    else :
        c =c_val(a,b) 
        while abs(func(c)) > tol: #takes half the interval
            if func(a) * func(c) < 0:
                b = c
            else:
                a = c 
            c = c_val(a,b)
        return c


func = lambda x: np.cos(x) #any function
a=np.pi; b=2*np.pi #interval
print('The root of the function in ',a,' and b ',b, ' is ',Bisection_Method(func, a,b,10**-6))
