# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# Example
# n = 3
# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4
# Input Format

if __name__ == '__main__':
    n = int(input())
    
    for i in range (n):
        print(i**2)