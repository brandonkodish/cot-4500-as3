# Question 1

# Define the function f(t, y)
def f(t, y):
    return t - y**2

# Initial conditions
t0 = 0
y0 = 1

# Range and iterations
t_end = 2
n_steps = 10
h = (t_end - t0) / n_steps  # Step size

# Lists to store t and y values
t_values = [t0]
y_values = [y0]

# Euler method
t = t0
y = y0
print(f"Step\t t\t y")
print(f"{0:2d}\t {t:.4f}\t {y:.4f}")
for step in range(1, n_steps + 1):
    y = y + h * f(t, y)
    t = t + h
    t_values.append(t)
    y_values.append(y)
    print(f"{step:2d}\t {t:.4f}\t {y:f}")
print("\n")
print("Question 1: 1.244638 \n")

#Question 2
# Define the function f(t, y) = dy/dt
def f(t, y):
    return t - y ** 2


# Initial conditions
t01 = 0.0  # initial time
y01 = 1.0  # initial value of y at t0
t_end1 = 2.0  # end time
n1 = 10  # number of steps

# Step size
h1 = (t_end1 - t01) / n1

# Lists to store the values of t and y
t_values1 = [t01]
y_values1 = [y01]

# Implement the RK4 method
for i in range(n1):
    t_n1 = t_values1[-1]
    y_n1 = y_values1[-1]

    # Compute the slopes
    k1 = h1 * f(t_n1, y_n1)
    k2 = h1 * f(t_n1 + h1 / 2, y_n1 + k1 / 2)
    k3 = h1 * f(t_n1 + h1 / 2, y_n1 + k2 / 2)
    k4 = h1 * f(t_n1 + h1, y_n1 + k3)

    # Update the next value of y
    y_n11 = y_n1 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    # Update the next value of t
    t_n11 = t_n1 + h1

    # Store the results
    t_values1.append(t_n11)
    y_values1.append(y_n11)

    # Print the current step's results
    print(f"Step {i + 1}: t = {t_n11:.4f}, y = {y_n11:.4f}")
print("\n")
print("Question 2: 1.2513")
