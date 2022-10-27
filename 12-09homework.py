# #1
a = input()
k_up = 0
words = a.split(' ')

for j in words:
    j_low = 0
    j_up = 0
    for i in j:

        if i.islower():
            j_low += 1
# вот тут нужно поменять  
        elif i.isupper():
             j_up += 1
    if j_up > j_low:
        k_up += 1
x = k_up/len(words)*100
print(x,'%')
