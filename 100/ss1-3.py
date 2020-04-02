string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"


def tokenized(s):
    tokens = []
    starting_number = 0
    for i in range(len(s)):
        char = s[i]
        if char == " " or char == ",":
            token = s[starting_number:i]
            if len(token) > 0:
                tokens.append(token)
            starting_number = i + 1
    return tokens


tokens = tokenized(string)

def count(l):
    result = []
    for i in range(len(l)):
        token = l[i]
        length = len(token)
        result.append(length)
    return result

print(count(tokens))
    

