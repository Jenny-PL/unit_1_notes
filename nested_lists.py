alphabet = [['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h'],['i', 'j', 'k', 'l', 'm', 'n'],['o', 'p', 'q', 'r', 's', 't'],['u', 'v', 'w', 'x', 'y', 'z']]

for list in alphabet:
    for element in list:
        print(element, end="")

for i in range(len(alphabet)):
    for j in range(len(alphabet[i])):
        print(alphabet[i][j])

i = 0
while i < len(alphabet):
    j= 0
    while j < len(alphabet[i]):
        print(alphabet[i][j])
        j+= 1
    i += 1
