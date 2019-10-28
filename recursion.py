"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return

    do_something(n - 1)
    print(n ** 2)


# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring


def calculate_blocks(n):
    if n <= 0:
        return 0
    return n + calculate_blocks(n - 1)


def build_pyramid():
    rows = int(input("How many rows is your pyramid?"))
    print("For {} rows you will need {} blocks".format(rows, calculate_blocks(rows)))


build_pyramid()
