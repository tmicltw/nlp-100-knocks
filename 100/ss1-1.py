string = "パタトクカシーー"

def slice_and_connect(s):
    string = ""
    for i in range(len(s)):
        if i % 2 == 0:
            string += s[i]   
    return string

print(slice_and_connect(string))