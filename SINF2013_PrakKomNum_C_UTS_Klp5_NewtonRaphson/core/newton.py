from sympy import symbols, sympify, diff, lambdify

def newton_raphson(expr_str, x0, n_iter=10, tol=1e-6):
  x = symbols('x')
  f_sym = sympify(expr_str)
  df_sym = diff(f_sym, x)
  f = lambdify(x, f_sym, 'numpy')
  df = lambdify(x, df_sym, 'numpy')
  
