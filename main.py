import numpy as np
import matplotlib.pyplot as plt


class FuzzyTriangle:
    def __init__(self, left, center, right):
        """
        Initializes a triangular fuzzy number.

        :param left: The left endpoint of the fuzzy number (a)
        :param center: The peak value (center) of the fuzzy number (b)
        :param right: The right endpoint of the fuzzy number (c)
        """
        if left >= center or center >= right:
            raise ValueError("Invalid fuzzy number triplet. Must satisfy: left < center < right.")

        self.left = left
        self.center = center
        self.right = right

        # Calculate the left and right spreads
        self.left_spread = center - left
        self.right_spread = right - center

    def derivative(self):
        """
        Computes the derivative of f(x) = x^2 at this fuzzy point.

        The result is a new fuzzy triangular number representing the derivative at the fuzzy point.

        :return: FuzzyTriangle representing the derivative, with center 2 * b and spreads 2 * (b - a), 2 * (c - b)
        """
        new_center = 2 * self.center
        new_left_spread = 2 * self.left_spread
        new_right_spread = 2 * self.right_spread

        return FuzzyTriangle(new_center - new_left_spread, new_center, new_center + new_right_spread)

    def __repr__(self):
        """
        String representation of the fuzzy triangular number.
        """
        return f"FuzzyTriangle(left={self.left}, center={self.center}, right={self.right})"

    def plot(self, color='blue', label='Fuzzy Number'):
        """
        Plots the triangular fuzzy number.
        """
        x_vals = [self.left, self.center, self.right]
        y_vals = [0, 1, 0]
        plt.plot(x_vals, y_vals, color=color, label=label)
        plt.fill_between(x_vals, y_vals, color=color, alpha=0.3)


# Get user input for the (a, b, c) triplet
try:
    a = float(input("Enter the left endpoint (a): "))
    b = float(input("Enter the center value (b): "))
    c = float(input("Enter the right endpoint (c): "))

    # Validate and create the fuzzy triangle
    fuzzy_point = FuzzyTriangle(left=a, center=b, right=c)
    print("Created fuzzy triangular number:", fuzzy_point)

    # Compute the derivative of f(x) = x^2 at this fuzzy point
    fuzzy_derivative = fuzzy_point.derivative()
    print("Fuzzy derivative at the fuzzy point:", fuzzy_derivative)

    # Plot settings
    x_range = np.linspace(a - 2, c + 2, 400)  # x range for function plots

    # Plot the fuzzy number
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 2, 1)
    fuzzy_point.plot(color='blue', label='Fuzzy Number')
    plt.title('Fuzzy Number Representation')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.xticks(np.arange(a - 2, c + 2, 0.5))  # More detailed x-ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Plot the function f(x) = x^2
    plt.subplot(2, 2, 2)
    f_x = x_range ** 2
    plt.plot(x_range, f_x, label='$f(x) = x^2$', color='green')
    plt.title('Function $f(x) = x^2$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xticks(np.arange(a - 2, c + 2, 0.5))  # More detailed x-ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Plot the derivative f'(x) = 2x
    plt.subplot(2, 2, 3)
    f_prime_x = 2 * x_range
    plt.plot(x_range, f_prime_x, label="$f'(x) = 2x$", color='red')
    plt.title('Derivative $f\'(x) = 2x$')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.xticks(np.arange(a - 2, c + 2, 0.5))  # More detailed x-ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Highlight the part of the derivative for the fuzzy number
    plt.subplot(2, 2, 4)
    plt.plot(x_range, f_prime_x, label="$f'(x) = 2x$", color='red')
    x_fuzzy_range = np.linspace(fuzzy_point.left, fuzzy_point.right, 200)
    f_prime_fuzzy = 2 * x_fuzzy_range
    plt.plot(x_fuzzy_range, f_prime_fuzzy, color='orange', linewidth=2, label='Derivative on Fuzzy Range')
    plt.fill_between(x_fuzzy_range, f_prime_fuzzy, color='orange', alpha=0.3)
    plt.title('Derivative $f\'(x)$ for Fuzzy Number Range')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.xticks(np.arange(a - 2, c + 2, 0.5))  # More detailed x-ticks
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Show plots
    plt.tight_layout()
    plt.show()

except ValueError as e:
    print("Error:", e)
