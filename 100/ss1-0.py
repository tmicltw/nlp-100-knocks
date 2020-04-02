string = "python"

def reverse(s):
    string = ""
    for c in s:
        string = c + string
    return string

print(reverse(string))