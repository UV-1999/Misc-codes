# -*- coding: UTF-8 -*-
import inspect
from sympy import *

def error_propagation(func, values, errors):
  variables = list(inspect.signature(func).parameters.keys())
  uncertainties, err = [], []
  for var in variables:
      uncertainties.append(f'd{var}**2')
      err.append(f'd{var}')
  symbol = symbols(list(variables))
  sym_lambda = (func(*symbol))
  sq_jacobian = Matrix([[diff(sym_lambda, sym)*diff(sym_lambda, sym) for sym in symbol]])
  variance = Matrix(uncertainties)
  error = Matrix(err)
  unf = lambdify(list(variables + err), ((sq_jacobian * variance))**(0.5))
  fff = lambdify(list(variables), sym_lambda)
  print(f"{(fff(*values)):.2f} ± {(unf(*values, *errors)[0][0]):.2f}")

# Example usage
error_propagation(lambda x, y: x + sin(y), (1,2), (0.1,0.2))

# Example Output
#1.91 ± 0.13
