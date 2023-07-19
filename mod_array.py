a = list(map(int,input("Enter the array elements: ").split()))
b = int(input("Enter B: "))
def mod_arr(a,b):
    string_= ""
    n = len(a)
    for i in range(n):
        string_+=str(a[i])
    return int(string_)%b
print(mod_arr(a,b))