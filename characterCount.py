a= "python session"

char_count = {}

for char in a: # iterating through each character in the string
    if char != " ":
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

for key, value in char_count.items():
    print(f"{key} = {value}")
        