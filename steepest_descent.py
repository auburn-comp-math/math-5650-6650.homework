import numpy as np
from numpy.linalg import norm
from backtracking import backtracking
from scipy.optimize import minimize_scalar

"""
@description: exact line search steepest decent method 
@parameters : 
@objFunc    : objective function  
@gradObjFunc: gradient of objective function
@x0         : starting point 
@tol        : tolerance for stopping criteria 
@maxIter    : maximum iteration for stopping criteria
@returns    : minimizer, number of iterations, path of iterates
"""
def exact_steepest_descent_method(objFunc, gradObjFunc, x0, tol, maxIter):
    path      = [x0]
    k         = 0
    xk        = x0
    pk        = -gradObjFunc(x0)
    while norm(pk) > tol and k <= maxIter:
        def subproblem1D(alpha):
            return objFunc(xk + alpha * pk)
        res = minimize_scalar(subproblem1D) 
        xk  = xk + res.x * pk 
        pk  = -gradObjFunc(xk)
        k   = k + 1
        path.append(xk)

    path = np.array(path) # convert to array
        
    if norm(pk) <= tol:
        print("Found the minimizer at {x} with {iter} iterations successfully, gradient's norm is {nrm}.".format(x=xk,iter=k,nrm=norm(pk)))
    else:
        print("Unable to locate minimizer within maximum iterations, last position is at {x}, gradient's norm is {nrm}".format(x=xk,nrm=norm(pk)))
        
    return xk, k, path

"""
@description: fixed step length steepest decent method 
@parameters : 
@objFunc    : objective function  
@gradObjFunc: gradient of objective function
@alpha      : the fixed step length, it is also referred as learning rate in neutral network.
@x0         : starting point 
@tol        : tolerance for stopping criteria 
@maxIter    : maximum iteration for stopping criteria
@returns    : minimizer, number of iterations, path of iterates
"""
def fixed_step_steepest_descent_method(objFunc, gradObjFunc, alpha,  x0, tol, maxIter):
    pass


"""
@description: Backtracking steepest decent method 
@parameters : 
@objFunc    : objective function  
@gradObjFunc: gradient of objective function
@x0         : starting point 
@tol        : tolerance for stopping criteria 
@maxIter    : maximum iteration for stopping criteria
"""
def backtracking_steepest_descent_method(objFunc, gradObjFunc, x0, tol, maxIter):
    pass