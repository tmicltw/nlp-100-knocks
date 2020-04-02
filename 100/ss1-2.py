patrol = "パトカー"
taxi = "タクシー"

def coined(str1, str2):
    string = ""
    for i in range(len(str1)):
        string = string + str1[i] + str2[i]
    return string

print(coined(patrol, taxi))