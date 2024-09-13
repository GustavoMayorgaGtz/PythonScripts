# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example
# N = 4
# append 1
# append 2
# insert 3 1
# print
# : Append 1 to the list, arr = [1] .
# : Append  to the list, arr = [1,2].
# : Insert  at index , arr = [1,3,2].
# : Print the array.
# Output:
# [1, 3, 2]
if __name__ == '__main__':
    N = int(input())
    arr = []
    output = ''
    
    for k in range(N):
        inp = str(input().strip())
        option = inp.split()
        if option[0] == 'append':
            arr.append(int(option[1]))
        elif option[0] == 'insert':
            arr.insert(int(option[1]), int(option[2]))
        elif option[0] == 'print':
            if k == N-1:
                output += str(arr)
            else:
                output += str(arr)+'\n'
        elif option[0] == 'pop':
            arr.pop()
        elif option[0] == 'reverse':
            arr.reverse()
        elif option[0] == 'remove':
            arr.remove(int(option[1]))
        elif option[0] == 'sort': 
            arr.sort()
        
    print(output)
    