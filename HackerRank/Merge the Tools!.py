def merge_the_tools(string, k):
    # your code goes here
    u_length = k
    for i in range(0, len(string) - u_length + 1, u_length):
        u_string = string[i : i + u_length]
        print(''.join(sorted(set(u_string), key = lambda x: u_string.index(x))))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)