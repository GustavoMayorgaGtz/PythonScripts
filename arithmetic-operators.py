# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# a = 4
# b = 5

# Print the following:

# 8
# -2
# 15

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    addition = a + b
    substraction = a - b
    product = a * b
    print(addition)
    print(substraction)
    print(product)