def swap_case(s):
    s.split()
    output = ""
    for k in s:
        if str(k).upper() == k:
            output += str(k).lower()
        elif str(k).lower() == k:
            output += str(k).upper()
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)