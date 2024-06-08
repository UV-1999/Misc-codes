# -*- coding: UTF-8 -*-
import inspect # For extracting function parameters
from sympy import * # For symbolic mathematics

def error_propagation(func, values, errors):
  
  # Get the list of parameter names for the provided function
  variables = list(inspect.signature(func).parameters.keys())
  
  # Initialize lists for uncertainties and error terms
  uncertainties, err = [], []

  # Create symbolic representations for uncertainties and error terms
  for var in variables:
      uncertainties.append(f'd{var}**2') # Variance term (squared error)
      err.append(f'd{var}') # Error term
  
  # Create symbolic variables for each parameter
  symbol = symbols(list(variables))

  # Create symbolic variables for each parameter
  sym_lambda = (func(*symbol))

  # Calculate the square of the Jacobian matrix of the function
  # This matrix contains partial derivatives squared
  sq_jacobian = Matrix([[diff(sym_lambda, sym)*diff(sym_lambda, sym) for sym in symbol]])
  
  # Create symbolic matrices for variances and errors
  variance = Matrix(uncertainties)
  error = Matrix(err)
  
  # Create a lambda function to compute the propagated error
  # This function takes the original variables and their errors
  unf = lambdify(list(variables + err), ((sq_jacobian * variance))**(0.5))

  # Create a lambda function for the original function
  fff = lambdify(list(variables), sym_lambda)

  # Evaluate the function and its propagated error with given values and errors
  result = fff(*values)
  propagated_error = unf(*values, *errors)[0][0]
    
  # Print the result with propagated error
  print(f"{result:.2f} ± {propagated_error:.2f}")

# Example usage
error_propagation(lambda x, y: x + sin(y), (1,2), (0.1,0.2))

# Example Output
#1.91 ± 0.13
