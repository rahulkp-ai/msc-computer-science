def f(x):
    return x ** 2

def f_derivative(x):
    return 2 * x

def gradient_descent(start_x, learning_rate=0.1, iterations=50):
    x   =   start_x
    for _ in range(iterations):
        grade   =   f_derivative(x)
        x       =   x - learning_rate * grade
        print(f"Minimum found near x    = {x:.4f}")
    return x

result = gradient_descent(start_x=10)

print(f"Minimum found near x    = {result:.4f}")