# Misc-codes

## uncertainty-propagation.py
Propagation of error: Let us have a property we want to measure, say f and according to some theory, it depends on some a priori independent variables x, y, z, etc. 

Δf = ∑ over; i { ∂_xi f × Δ_xi }

Propagation of uncertainty: Let us have a property we want to measure, say f and according to some theory, it depends on some a priori independent variables x, y, z, etc.

σ_f = square root of { ∑ over i;(∂_xi f × σ_xi )2 }

uncertainty-propagation.py is a python code to use the above formula over a given function f.

### Example usage
error_propagation(lambda x, y: x + sin(y), (1,2), (0.1,0.2))

### Example Output
#1.91 ± 0.13

But if there are unexpected covariances in the variables x, y, z, etc. the above rule (addition in quadrature) may not work. Correlation is a statistical measure of how two things are related.

## sand.py
https://github.com/UV-1999/Misc-codes/assets/80977229/71a5cf25-ab04-48c7-bfbb-46c8f711947b
https://github.com/UV-1999/Misc-codes/assets/80977229/0aab2e09-1dbf-4d49-8f44-d859ce571f55
