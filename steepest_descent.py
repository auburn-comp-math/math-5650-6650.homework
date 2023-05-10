import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

"""
@params f: function to minimize
@params grad_f: gradient of f
@params x: initial point
@params tol: tolerance
@params max_iter: maximum number of iterations
@returns: minimizer, number of iterations
"""
def steepest_descent_exact(f, grad_f, x, tol, max_iter):
    pass

"""
@params f: function to minimize
@params grad_f: gradient of f
@params x: initial point
@params tol: tolerance
@params max_iter: maximum number of iterations
@params alpha: fixed step size
@returns: minimizer, number of iterations
"""
def steepest_descent_fixed_step(f, grad_f, x, tol, max_iter, alpha):
    pass


"""
@params f: function to minimize
@params grad_f: gradient of f
@params x: initial point
@params tol: tolerance
@params max_iter: maximum number of iterations
@return: minimizer, number of iterations
"""
def steepest_descent_backtracking(f, grad_f, x, tol, max_iter):
    pass