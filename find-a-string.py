def count_substring(string, sub_string):
    size = len(sub_string)
    forSize = len(string) - (size-1)
    slist = list(string)
    counter = 0
    for k in range(forSize):
        a = ''.join(slist[k:(size+k)])
        if a == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)