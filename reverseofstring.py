def reverse(string):
    string = string[::-1]
    return string
string = "python is a case sensitive language"

print("The original string  is : ", end="")
print(string)

print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(string))

