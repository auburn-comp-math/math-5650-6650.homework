import numpy as np
from steepest_descent import exact_steepest_descent_method, fixed_step_steepest_descent_method, backtracking_steepest_descent_method


def test_quadratic_function():
    def QObjFunc(x):
        return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2

    def QGradObjFunc(x):
        return np.array([(x[0] + 2 * x[1] - 7) * 2 + (2 * x[0] + x[1] - 5) * 4, 
                        (x[0] + 2 * x[1] - 7) * 4 + (2 * x[0] + x[1] - 5) * 2])
    
    # some settings to run the algorithms
    x0      = np.array([0., 0.])
    tol     = 1e-9 
    maxIter = 1e6 

    # Run the exact line search steepest descent
    x, iter, path = exact_steepest_descent_method(QObjFunc, QGradObjFunc, x0, tol, maxIter)
    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 3.0) < 1e-6)


    # Run the Fixed step length steepest descent
    alpha = 0.01
    x, iter, path = fixed_step_steepest_descent_method(QObjFunc, QGradObjFunc, alpha,  x0, tol, maxIter)
    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 3.0) < 1e-6)

    # Run the backtracking line search steepest descent
    x, iter, path = backtracking_steepest_descent_method(QObjFunc, QGradObjFunc, x0, tol, maxIter)
    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 3.0) < 1e-6)

def test_rosenbrock_function():
    def RObjFunc(x):
        return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2

    def RGradObjFunc(x):
        return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0]), 200 * (x[1] - x[0] ** 2)])

    # some settings to run the algorithms
    x0      = np.array([-1.2, 1.0])
    tol     = 1e-9
    maxIter = 1e6

    # Run the exact line search steepest descent
    x, iter, path = exact_steepest_descent_method(RObjFunc, RGradObjFunc, x0, tol, maxIter)

    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 1.0) < 1e-6)

    # Run the Fixed step length steepest descent
    alpha = 0.01

    x, iter, path = fixed_step_steepest_descent_method(RObjFunc, RGradObjFunc, alpha,  x0, tol, maxIter)

    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 3.0) < 1e-6)

    # Run the backtracking line search steepest descent
    x, iter, path = backtracking_steepest_descent_method(RObjFunc, RGradObjFunc, x0, tol, maxIter)

    assert(abs(x[0] - 1.0) < 1e-6 and abs(x[1] - 3.0) < 1e-6)




