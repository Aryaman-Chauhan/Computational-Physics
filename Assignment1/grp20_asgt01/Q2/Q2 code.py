def fn(x):                                              
 return x**3 - x-3

def dfn(x):                                            
 return 3*x**2 - 1

x0=float(input("Enter initial guess : "))
tolerance=float(input("Enter tolerance : ")) 
iterations=int(input("Number of iterations  : ")) 



for i in range(iterations):                             
   xnew=x0-fn(x0)/dfn(x0)# formula of Newton Raphson method
   if abs(xnew-x0)<tolerance: break                     
   x0=xnew                                              
  
print("The root of the equation by Newton raphson method is: ",x0)
